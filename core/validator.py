import pandas as pd


def validate_csv_structure(file_path):
    try:
        df = pd.read_csv(file_path, sep=";")
        required_columns = [
            "oficina",
            "fechaMovimiento",
            "numeroDocumento",
            "debito",
            "credito",
            "descripcion",
        ]

        if all(col in df.columns for col in required_columns):
            return True
        else:
            return False
    except Exception:
        return False
