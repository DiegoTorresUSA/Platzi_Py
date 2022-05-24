import pandas as pd


def resumir_arcos_comerciales(arcos_comerciales):
    arcos_comerciales['tr_minimo'] = pd.to_timedelta(arcos_comerciales.tr_minimo)
    arcos_comerciales['tr_maximo'] = pd.to_timedelta(arcos_comerciales.tr_maximo)
    arcos_comerciales['tr_optimo'] = pd.to_timedelta(arcos_comerciales.tr_optimo)

    arcos_comerciales_grupo = ['linea', 'sentido', 'tipodia', 'trayecto']
    arcos_resumen = arcos_comerciales.groupby(arcos_comerciales_grupo).agg(
        {'tr_optimo': 'min', 'tr_minimo': 'min', 'tr_maximo': 'max', 'nodo_1': 'first', 'nodo_2': 'last'}
    )

    arcos_resumen.reset_index(inplace=True)
    arcos_resumen.rename(columns={'nodo_1': 'nodo', 'trayecto': 'sublinea'}, inplace=True)
    return arcos_resumen


def cargar_dataset_resumir_arcos(ruta):
    arcos = pd.read_excel(ruta, 'Arcos Comerciales y T.Recorrido')
    return resumir_arcos_comerciales(arcos)

def _generar_csv_con_arcos_resumen(ruta_data_set):
    arcos_resumidos = cargar_dataset_resumir_arcos(ruta_data_set)
    arcos_resumidos.to_csv('C:\Lenovo\mision TIC2022\Platzi_Py\Prueba_TRANSMILENIO/resultado.csv', index = False)


if __name__ == '__main__':
    _generar_csv_con_arcos_resumen('C:\Lenovo\mision TIC2022\Platzi_Py\Prueba_TRANSMILENIO\PSO20220223.xls')