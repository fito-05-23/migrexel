import pandas as pd
import sqlite3

def sanitizar_identificador(identificador):
    """Elimina o reemplaza caracteres no válidos en identificadores SQL."""
    return identificador.replace("-", "_").replace(" ", "_")

def generate_create_table_sql(df, table_name):
    """Genera el SQL para crear una tabla con una columna ID autoincremental."""
    table_name = sanitizar_identificador(table_name)

    columns = ['"id" INTEGER PRIMARY KEY AUTOINCREMENT']  # Agregar columna ID

    for col in df.columns:
        col_name = sanitizar_identificador(col)
        
        # Determinar tipo de dato
        if col_name.lower() == "PRECIO":
            col_type = "DECIMAL(10,2)"
        elif col_name.lower() == "id":  
            col_name = "Codigo_Cliente"  # Evitar conflicto con id autoincremental
            col_type = "TEXT"
        else:
            col_type = "TEXT"  # Puedes ajustar esto según el tipo de dato

        columns.append(f'"{col_name}" {col_type}')
    
    # Agregar campos de fecha
    columns.append('"Fecha_Alta" DATETIME DEFAULT CURRENT_TIMESTAMP')
    columns.append('"Fecha_Actualizacion" DATETIME DEFAULT CURRENT_TIMESTAMP')

    columns_sql = ", ".join(columns)
    return f'CREATE TABLE IF NOT EXISTS "{table_name}" ({columns_sql});'

def generate_insert_sql(df, table_name):
    """Genera el SQL para insertar datos en una tabla, sin incluir la columna ID."""
    table_name = sanitizar_identificador(table_name)

    insert_statements = []
    for _, row in df.iterrows():
        columns = [sanitizar_identificador(col) for col in df.columns]
        columns = ['Codigo_Cliente' if col.lower() == 'id' else col for col in columns]  # Cambiar ID

        columns_sql = ", ".join([f'"{col}"' for col in columns])
        
        values = []
        for value in row:
            if isinstance(value, str):
                value = value.replace("'", "''")  # Escapar comillas simples
                values.append(f"'{value}'")
            elif pd.isna(value):
                values.append("NULL")
            else:
                values.append(str(value))
        
        values_sql = ", ".join(values)
        insert_statements.append(f'INSERT INTO "{table_name}" ({columns_sql}) VALUES ({values_sql});')
    
    return insert_statements