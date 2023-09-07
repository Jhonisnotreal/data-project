from fastapi import FastAPI
import json
import pandas as pd

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}

df1 = []
with open("data/australian_user_reviews.json", encoding="utf-8-sig") as file:
    for linea in file:
        df1.append(eval(linea))

df = pd.DataFrame(df1)


nulos = df.isnull().sum()

# df = df.drop_duplicates()

# Calcular el IQR para cada columna numérica
Q1 = df.quantile(0.25)
Q3 = df.quantile(0.75)
IQR = Q3 - Q1

# Identificar los outliers utilizando el IQR
outliers = ((df < (Q1 - 1.5 * IQR)) | (df > (Q3 + 1.5 * IQR))).any(axis=1)

# Filtrar el DataFrame para eliminar los outliers
df = df[~outliers]

print(df.head())