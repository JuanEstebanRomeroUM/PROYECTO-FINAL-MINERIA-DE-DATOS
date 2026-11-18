# Proyecto Integrador Final – Minería de Datos

## Clasificación de registros de facturas asociadas a cancelaciones

### 1. Descripción del proyecto

Este proyecto utiliza técnicas de minería de datos y aprendizaje automático para clasificar registros de facturas de acuerdo con su asociación a cancelaciones, utilizando el conjunto de datos Online Retail II.

Se desarrolló un proceso de integración, limpieza, análisis exploratorio, preparación de datos, entrenamiento y evaluación de modelos de clasificación. Finalmente, se implementó una API con FastAPI para consumir el modelo entrenado.

### 2. Tecnologías utilizadas

- Python 3.12.14
- Pandas 3.1.1
- NumPy 2.5.4
- Scikit-learn 1.9.1
- FastAPI
- Pydantic
- Uvicorn
- Pickle
- Jupyter Notebook
- Git y GitHub

### 3. Estructura del proyecto

```text
PROYECTO-FINAL-MINERIA-DE-DATOS/
│
├── api/
│   └── main.py
│
├── Data/
│
├── Model/
│   └── modelo_cancelaciones.pkl
│
├── Notebooks/
│   ├── Proyecto.ipynb
│   └── resumen_proceso_etl.csv
│
├── .gitignore
├── requirements.txt
└── README.md
```

La carpeta Data contiene los datos originales y se mantiene excluida del repositorio para evitar subir archivos pesados.

### 4. Instalación

Clonar el repositorio:

```bash
git clone https://github.com/JuanEstebanRomeroUM/PROYECTO-FINAL-MINERIA-DE-DATOS.git
```

Ingresar a la carpeta:

```bash
cd PROYECTO-FINAL-MINERIA-DE-DATOS
```

Crear un entorno virtual:

```bash
python -m venv .venv
```

Activar el entorno en Windows:

```powershell
.venv\Scripts\Activate.ps1
```

Instalar las dependencias:

```bash
pip install -r requirements.txt
```

### 5. Ejecución de la API

Desde la carpeta principal ejecutar:

```bash
uvicorn api.main:app --reload
```

La API estará disponible localmente en:

`http://127.0.0.1:8000`

Documentación interactiva de Swagger:

`http://127.0.0.1:8000/docs`

### 6. Endpoints disponibles

| Método | Endpoint | Descripción |
|---|---|---|
| GET | `/` | Información general de la API. |
| GET | `/health` | Verifica el estado del servicio y la disponibilidad del modelo. |
| POST | `/predict` | Recibe datos de una factura y devuelve su clasificación. |

### 7. Esquema de entrada para predicciones

El endpoint POST `/predict` recibe un objeto JSON con las siguientes variables:

| Variable | Tipo | Validación |
|---|---|---|
| precio_promedio | float | Mayor que cero |
| numero_productos | int | Mayor o igual a uno |
| numero_registros | int | Mayor o igual a uno |

Ejemplo de solicitud:

```json
{
  "precio_promedio": 95.00,
  "numero_productos": 2,
  "numero_registros": 2
}
```

La respuesta incluye la clase predicha y la probabilidad estimada de cancelación.

### 8. Modelo de Machine Learning

Se compararon dos algoritmos:

- Regresión logística.
- Random Forest.

Se seleccionó Random Forest por obtener el mejor F1-score, con un resultado de 0.5862.

Resultados de evaluación:

- Accuracy: 84.28 %.
- Precision: 46.26 %.
- Recall: 79.97 %.
- F1-score: 58.62 %.
- ROC-AUC: 0.88.

El modelo y su pipeline de procesamiento se serializaron mediante Pickle.

**Archivo generado:** `Model/modelo_cancelaciones.pkl`.

### 9. Limitaciones

El modelo clasifica registros de facturas asociados a cancelaciones utilizando información de la factura ya registrada. Por tanto, no debe interpretarse como un sistema de predicción anticipada de cancelaciones futuras.

La precisión obtenida indica que existen falsos positivos, por lo que sus resultados deben utilizarse como apoyo para el análisis y no como decisiones automáticas definitivas.

Los registros sintéticos empleados en las pruebas de la API permiten verificar su funcionamiento técnico, pero no sustituyen una validación con nuevos datos reales.

### 10. Despliegue y disponibilidad

La API fue ejecutada y probada localmente mediante Uvicorn y Swagger UI. Se verificaron los endpoints principales y se realizaron pruebas de predicción con registros nuevos.

No se realizó un despliegue en un servicio de hosting público. La aplicación puede ejecutarse localmente siguiendo las instrucciones de instalación y ejecución de este documento.

### 11. Repositorio

GitHub:

https://github.com/JuanEstebanRomeroUM/PROYECTO-FINAL-MINERIA-DE-DATOS