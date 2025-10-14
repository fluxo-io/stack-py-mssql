import os
import pandas as pd
import pyodbc

HOST = os.getenv("MSSQL_HOST", "localhost")
PORT = os.getenv("MSSQL_PORT", "1433")
DB   = os.getenv("MSSQL_DB", "master")
USER = os.getenv("MSSQL_USER", "sa")
PWD  = os.getenv("MSSQL_PASSWORD", "YourStrong!Passw0rd")

conn_str = (
    f"DRIVER={{ODBC Driver 18 for SQL Server}};"
    f"SERVER={HOST},{PORT};"
    f"DATABASE={DB};"
    f"UID={USER};PWD={PWD};"
    "Encrypt=yes;TrustServerCertificate=yes;"
)

with pyodbc.connect(conn_str) as conn:
    df = pd.read_sql("SELECT name, database_id, create_date FROM sys.databases", conn)
    print(df.head().to_string(index=False))
