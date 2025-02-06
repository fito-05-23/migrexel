import os
import sqlite3
import pandas as pd

def create_connection(db_file):
    """Crea una conexión a la base de datos SQLite."""
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        # Habilitar el soporte para UTF-8
        conn.execute('PRAGMA encoding = "UTF-8";')
        print(f"Conexión exitosa a {db_file}")
    except sqlite3.Error as e:
        print(f"Error al conectar a la base de datos: {e}")
    return conn

def execute_sql(conn, sql, params=None):
    """Ejecuta una sentencia SQL."""
    try:
        cursor = conn.cursor()
        if params:
            cursor.execute(sql, params)
        else:
            cursor.execute(sql)
        conn.commit()
    except sqlite3.Error as e:
        print(f"Error al ejecutar la sentencia SQL: {e}")
