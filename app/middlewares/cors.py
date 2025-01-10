from fastapi.middleware.cors import CORSMiddleware

def add_cors_middleware(app):
    """
    Configura el middleware de CORS para la aplicación FastAPI.
    """
    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],  # Cambiar a dominios específicos en producción
        allow_credentials=True,  # Permite enviar cookies y credenciales
        allow_methods=["*"],  # Permite todos los métodos HTTP
        allow_headers=["*"],  # Permite todos los encabezados HTTP
    )
