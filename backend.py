from fastapi import FastAPI, Query
from fastapi.middleware.cors import CORSMiddleware
import pandas as pd
from typing import List
import numpy as np

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  
    allow_credentials=True,
    allow_methods=["*"],  
    allow_headers=["*"],  
)

df = pd.read_csv("operadoras.csv", sep=";")


def search_operators(query: str, df: pd.DataFrame) -> List[dict]:
    """Busca textual nas operadoras."""
    results = df[df['Nome_Fantasia'].str.contains(query, case=False, na=False)]
    results = results.replace([np.inf, -np.inf], np.nan).fillna("")  # Substitui valores inválidos
    return results.to_dict(orient='records')


@app.get("/buscar")
def buscar_operadoras(query: str = Query(..., min_length=1)):
    """Endpoint para buscar operadoras pelo nome."""
    return search_operators(query, df);

@app.get("/todas")
def listar_todas():
    """Endpoint para retornar todas as operadoras."""
    return df.replace([np.inf, -np.inf], np.nan).fillna("").to_dict(orient='records')

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
