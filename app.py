import os
import pandas as pd
from sqlalchemy import create_engine

HOST = os.getenv("MSSQL_HOST", "localhost")
PORT = os.getenv("MSSQL_PORT", "1433")
DB   = os.getenv("MSSQL_DB", "master")
USER = os.getenv("MSSQL_USER", "sa")
PWD  = os.getenv("MSSQL_PASSWORD", "YourStrong!Passw0rd")

# SQLAlchemy-Engine mit pyodbc
connection_string = (
    f"mssql+pyodbc://{USER}:{PWD}@{HOST}:{PORT}/{DB}"
    "?driver=ODBC+Driver+18+for+SQL+Server"
    "&Encrypt=yes&TrustServerCertificate=yes"
)
engine = create_engine(connection_string)

with engine.connect() as conn:
    df = pd.read_sql("SELECT name, database_id, create_date FROM sys.databases", conn)
    print(df.to_string(index=False))