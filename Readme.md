# Comandos para correr el proyecto

.\venv\Scripts\activate o .\venv\Scripts\Activate.ps1

uvicorn app.main:app --reload


# Data Base

Existe un script: *init_db.py* para volver a crear la DB

Comando para hacer querys:

    sqlite3 app_data.db

# Estructura de Archivos

api/
├── app/
│   ├── core/
│   ├── crud/
│   ├── db/
│   │   ├── __init__.py
│   │   ├── database.py
│   │   ├── models.py
│   │   ├── schemas.py
│   ├── routes/
│   ├── services/
│   ├── tests/
├── data/                    
│   └── app_data.db          
├── .env
├── Dockerfile
├── docker-compose.yml
├── README.md
