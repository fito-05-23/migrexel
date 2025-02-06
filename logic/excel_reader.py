import pandas as pd

def read_excel(file_path):
    """Lee un archivo Excel y devuelve un DataFrame."""
    try:
        # Determinar el motor de lectura basado en la extensión del archivo
        if file_path.lower().endswith('.xls'):
            engine = 'xlrd'
        elif file_path.lower().endswith('.xlsx'):
            engine = 'openpyxl'
        else:
            raise ValueError("Formato de archivo no soportado. Solo se admiten archivos .xls y .xlsx.")

        # Leer el archivo Excel usando el motor apropiado
        df = pd.read_excel(file_path, engine=engine, dtype=str)
        return df
    except Exception as e:
        print(f"Error al leer el archivo Excel: {e}")
        return None