
from pathlib import Path
import pickle

import pandas as pd
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field, ConfigDict

# Ubicación del modelo
PROJECT_DIR = Path(__file__).resolve().parent.parent
MODEL_PATH = PROJECT_DIR / "Model" / "modelo_cancelaciones.pkl"

# Cargar el modelo
modelo = None

try:
    with open(MODEL_PATH, "rb") as archivo:
        modelo = pickle.load(archivo)
except Exception:
    modelo = None

# Crear aplicación
app = FastAPI(
    title="API de Clasificación de Cancelaciones",
    description="Servicio para clasificar registros de facturas.",
    version="1.0.0"
)


# Validación de datos de entrada
class DatosFactura(BaseModel):
    model_config = ConfigDict(extra="forbid")

    precio_promedio: float = Field(gt=0)
    numero_productos: int = Field(ge=1)
    numero_registros: int = Field(ge=1)


# Ruta principal
@app.get("/")
def inicio():
    return {
        "mensaje": "API de clasificación de cancelaciones",
        "version": "1.0.0",
        "documentacion": "/docs"
    }


# Verificar servicio y modelo
@app.get("/health")
def health():
    if modelo is None:
        raise HTTPException(
            status_code=503,
            detail="El modelo no está disponible."
        )

    return {
        "status": "ok",
        "model_loaded": True
    }


# Realizar predicción
@app.post("/predict")
def predecir(datos: DatosFactura):
    if modelo is None:
        raise HTTPException(
            status_code=503,
            detail="El modelo no está disponible."
        )

    try:
        entrada = pd.DataFrame([datos.model_dump()])

        prediccion = int(modelo.predict(entrada)[0])
        probabilidades = modelo.predict_proba(entrada)[0]

        return {
            "prediccion": prediccion,
            "clasificacion": (
                "Factura cancelada"
                if prediccion == 1
                else "Factura normal"
            ),
            "probabilidad_cancelacion": round(
                float(probabilidades[1]), 4
            )
        }

    except Exception:
        raise HTTPException(
            status_code=500,
            detail="No fue posible procesar la predicción."
        )
