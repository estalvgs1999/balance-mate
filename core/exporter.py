import pandas as pd


def export_to_excel(dataframe, save_path):
    try:
        # En el futuro aquí estará la lógica real de exportación
        dataframe.to_excel(save_path, index=False)
        return True, "Archivo exportado con éxito."
    except Exception as e:
        return False, f"Error al exportar: {str(e)}"
