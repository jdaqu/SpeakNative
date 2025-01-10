from fastapi import APIRouter
from app.routes.phrases import router as phrases_router
from app.routes.topics import router as topics_router
from app.routes.mistakes import router as mistakes_router
from app.routes.vocabulary import router as vocabulary_router

# Configura el enrutador principal
api_router = APIRouter()

# Incluye las rutas individuales
api_router.include_router(phrases_router, prefix="/phrases", tags=["Phrases"])
api_router.include_router(topics_router, prefix="/topics", tags=["Topics"])
# api_router.include_router(mistakes_router, prefix="/mistakes", tags=["Mistakes"])
# api_router.include_router(vocabulary_router, prefix="/vocabulary", tags=["Vocabulary"])
