import pandas as pd
import csv


def validate_csv_structure(file_path):
    try:
        # Detect delimiter dynamically
        with open(file_path, "r", encoding="utf-8") as f:
            sample = f.read(1024)
            try:
                delimiter = csv.Sniffer().sniff(sample).delimiter
            except csv.Error:
                delimiter = ";"

        df = pd.read_csv(file_path, sep=delimiter)
        required_columns = [
            "oficina",
            "fechaMovimiento",
            "numeroDocumento",
            "debito",
            "credito",
            "descripcion",
        ]

        missing_cols = [col for col in required_columns if col not in df.columns]
        if missing_cols:
            return False, f"Missing required columns: {', '.join(missing_cols)}"
            
        # Basic check for empty file
        data_rows = df[df["numeroDocumento"] != "TOTAL"]
        if len(data_rows) == 0:
            return False, "The CSV file is empty or contains no data rows."

        return True, "Valid structure."
    except Exception as e:
        return False, f"Error reading the file: {str(e)}"
