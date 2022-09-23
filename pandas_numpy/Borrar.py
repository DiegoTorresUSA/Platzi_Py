@router.post("/actualizar/")
async def actualizar_tm(tipo_dia: int = Form(...),
                        pso_archivo: UploadFile | None = None,
                        iph_archivo: UploadFile | None = None,
                        # tm_archivo: UploadFile = Form(...)
                        ):  # revisar cuales son obligatorios

    if iph_archivo:
        peticion = PeticionActualizarIph(tipo_dia=tipo_dia, iph_archivo=iph_archivo)
        return actualizar_iph(peticion)
    elif pso_archivo:
        peticion = PeticionActualizarPso(tipo_dia=tipo_dia, pso_archivo=pso_archivo)
        return actualizar_pso(peticion)
    else:
        return {'mensaje': 'error'}

    '''elif tm_archivo:
        peticion = PeticionActualizarTmSrvs(tipo_dia=tipo_dia, tm_archivo=tm_archivo)
        return actualizar_tm_srvs(peticion)'''


# [START. Funcion Actualizar IPH]
def actualizar_iph(peticion: PeticionActualizarIph):
    try:
        # -----------------------------------------------------------------------------------------
        iph_cargado = pd.read_csv(peticion.iph_archivo.file)
        tipo_dia = peticion.tipo_dia
        # -----------------------------------------------------------------------------------------

        # [START validacion iph_archivo, cuando lo cargan]
        with db_utils_instance.crear_conexion_vision().begin() as conn:

            # [Start. Definiendo los archivos, variables que se van a necesitar]
            gestion = _consultar_gestion_activa_por_tipodia(tipo_dia, conn)
            gestion_id = gestion.iloc[0]['id']
            bucket_name = gestion.iloc[0]['bucket']
            arcos_archivo_nombre = gestion.iloc[0]['pso_archivo']
            # [End. Definiendo los archivos, variables que se van a necesitar]

            # [Start Consultar la información necesaria]
            franjas = _consultar_franjas(gestion_id, conn)
            iph_cargado = _formatear_remover_iph(iph_cargado)
            arcos_base = _traer_archivo_excel_bucket(bucket_name, arcos_archivo_nombre, ARCOS_PESTANA)
            arcos_base = _formatear_remover_arcos(arcos_base)
            arcos_base['id_arco'] = arcos_base.apply(
                lambda row: '{}-{}-{}'.format(row.linea, row.trayecto, row.sentido), axis=1)
            srvs = _consultar_srvs(gestion_id, conn)
            matriz = _consultar_matriz_distancia(conn)

            if srvs.empty:
                raise ValueError('No existen servicios para actualizar la TM')

            arcos_con_novedad = pd.DataFrame()

            arcos_con_novedad, arcos = _enriquecer_arcos(arcos_base.copy(deep=False),
                                                         matriz.drop(columns=['sentido', 'linea', 'sublinea', 'ruta']))
            srvs_con_novedad, srvs = _enriquecer_srvs(iph_cargado, franjas, srvs,
                                                      matriz.drop(columns=['sentido', 'parada_id', 'id_arco']),
                                                      arcos)
            archivo_tm_actualizada_nombre = PATRON_ARCHIVO_SALIDA_ACTUALIZADA.format('actualizada')

            _remover_tabla_maestra_detalle(gestion_id, conn)

            gestion_id_actualizada = _persistir_tabla_maestra(gestion_id, srvs, tipo_dia, archivo_tm_actualizada_nombre,
                                                              iph_cargado, arcos_archivo_nombre, conn)
            novedades = {'NOVEDADES EN ARCOS': arcos_con_novedad, 'NOVEDADES EN SERVICIOS': srvs_con_novedad}
            _generar_archivo_actualizado_gestion_tabla_maestra(tipo_dia, gestion_id_actualizada, novedades,
                                                               archivo_tm_actualizada_nombre, bucket_name, conn)

        novedades = {'cantidad_arcos': arcos_con_novedad.shape[0],
                     'cantidad_srvs': srvs_con_novedad.shape[0],
                     'gestion_id': gestion_id,
                     'mensaje': 'Actualización Realizada'}
        return novedades
    except FileNotFoundError:
        msg = 'Los archivos no fueron cargados'
        return {'mensaje': msg}


# [END validacion iph_archivo]


def actualizar_pso(peticion: PeticionActualizarPso):
    try:
        # -----------------------------------------------------------------------------------------
        pso_cargado = pd.read_excel(peticion.pso_archivo.file, ARCOS_PESTANA)
        tipo_dia = peticion.tipo_dia
        # -----------------------------------------------------------------------------------------

        with db_utils_instance.crear_conexion_vision().begin() as conn:

            gestion = _consultar_gestion_activa_por_tipodia(tipo_dia, conn)
            gestion_id = gestion.iloc[0]['id']
            bucket_name = gestion.iloc[0]['bucket']
            iph_archivo_nombre = gestion.iloc[0]['expediciones_archivo']

            franjas = _consultar_franjas(gestion_id, conn)
            iph = _traer_archivo_csv_bucket(bucket_name, iph_archivo_nombre)
            iph = _formatear_remover_iph(iph)
            arcos_base = _formatear_remover_arcos(pso_cargado)

            arcos_base['id_arco'] = arcos_base.apply(
                lambda row: '{}-{}-{}'.format(row.linea, row.trayecto, row.sentido), axis=1)
            srvs = _consultar_srvs(gestion_id, conn)
            matriz = _consultar_matriz_distancia(conn)

            if srvs.empty:
                raise ValueError('No existen servicios para actualizar la TM')

            arcos_con_novedad = pd.DataFrame()
            archivo_tm_actualizada_nombre = PATRON_ARCHIVO_SALIDA.format('actualizada')

            arcos_con_novedad, arcos = _enriquecer_arcos(arcos_base.copy(deep=False),
                                                         matriz.drop(columns=['sentido', 'linea', 'sublinea', 'ruta']))
            srvs_con_novedad, srvs = _enriquecer_srvs(iph, franjas, srvs,
                                                      matriz.drop(columns=['sentido', 'parada_id', 'id_arco']),
                                                      arcos)
            _remover_tabla_maestra_detalle(gestion_id, conn)
            gestion_id_actualizada = _persistir_tabla_maestra(gestion_id, srvs, tipo_dia, archivo_tm_actualizada_nombre,
                                                              iph, pso_cargado, conn)

            novedades = {'NOVEDADES EN ARCOS': arcos_con_novedad, 'NOVEDADES EN SERVICIOS': srvs_con_novedad}
            _generar_archivo_actualizado_gestion_tabla_maestra(tipo_dia, gestion_id_actualizada, novedades,
                                                               archivo_tm_actualizada_nombre, bucket_name, conn)

        novedades = {'cantidad_arcos': arcos_con_novedad.shape[0],
                     'cantidad_srvs': srvs_con_novedad.shape[0],
                     'gestion_id': gestion_id,
                     'mensaje': 'Actualización Realizada'}
        return novedades
    except FileNotFoundError:
        msg = 'No fue posible Actualizar la TM'
        return {'mensaje': msg}
