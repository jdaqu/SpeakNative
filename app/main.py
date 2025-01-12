from fastapi import FastAPI
from app.routes import api_router
from app.middlewares.cors import add_cors_middleware
from app.db.database import Base, engine

# Crea las tablas en la base de datos
Base.metadata.create_all(bind=engine)

# Inicializa la aplicación
app = FastAPI(title="API de Prueba", version="1.0.0")

add_cors_middleware(app)

# Incluye las rutas
app.include_router(api_router)
