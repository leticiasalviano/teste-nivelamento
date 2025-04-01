import pandas as pd
import mysql.connector
from sqlalchemy import create_engine
from urllib.parse import quote_plus

# Configuração do banco de dados
DB_USER = "root"
DB_PASSWORD = "15012001"
DB_HOST = "localhost"
DB_NAME = "teste_bd"
TABLE_NAME = "demonstracoes_contabeis"

password = quote_plus(DB_PASSWORD)

engine = create_engine(f"mysql+mysqlconnector://{DB_USER}:{password}@{DB_HOST}/{DB_NAME}")


df = pd.read_csv("4T2023.csv", sep=";")

df["VL_SALDO_FINAL"] = df["VL_SALDO_FINAL"].str.replace(",", ".").astype(float)
df["VL_SALDO_INICIAL"] = df["VL_SALDO_INICIAL"].str.replace(",", ".").astype(float)

df.to_sql(TABLE_NAME, con=engine, if_exists="append", index=False, chunksize= 1000)

print("Dados inseridos com sucesso!")