# from fastapi import FastAPI, HTTPException
# from pydantic import BaseModel
# import os
# import replicate
# from dotenv import load_dotenv
# import re
# from fastapi.middleware.cors import CORSMiddleware

# # Load environment variables from .env file
# load_dotenv()

# # Initialize FastAPI app
# app = FastAPI()

# # Configura el middleware de CORS
# # Esto es necesario para permitir solicitudes desde diferentes dominios/orígenes, como el de tu extensión de Chrome.
# app.add_middleware(
#     CORSMiddleware,
#     allow_origins=["*"],  # Permite solicitudes desde cualquier origen (útil para desarrollo)
#     # En producción, reemplaza "*" con dominios específicos, por ejemplo:
#     # allow_origins=["https://your-frontend-url.com", "http://localhost:3000"]
#     allow_credentials=True,  # Permite enviar cookies y credenciales si es necesario
#     allow_methods=["*"],  # Permite todos los métodos HTTP, como GET, POST, OPTIONS
#     allow_headers=["*"],  # Permite todos los encabezados HTTP en las solicitudes
# )

# # Retrieve the Replicate API token from environment variables
# REPLICATE_API_TOKEN = os.getenv("REPLICATE_API_TOKEN")

# # Initialize Replicate client
# client = replicate.Client(api_token=REPLICATE_API_TOKEN)

# # Define the data model for text input
# class TextInput(BaseModel):
#     text: str

# @app.get("/")
# def read_root():
#     return {"message": "Hello, world! Welcome to your API!"}

# # POST route to process text with the AI model
# # main.py



# @app.post("/process-text/")
# def process_text(input_data: TextInput):
#     try:
#         prompt_template = (
#             "You are an English language assistant for non-native speakers focusing on professional communication. "
#             "Please help improve the following text by structuring your response in a standardized format:\n\n"
#             "Text:\n"
#             f"{input_data.text}\n\n"
#             "Please answer in the following format:\n\n"
#             "- **Correct form to say**: Provide the corrected and improved version of the text.\n"
#             "- **What error did you have?**: Identify the grammar, vocabulary, or phrasing errors.\n"
#             "- **Topics to study**: Suggest topics or grammatical rules the user could study to avoid these errors.\n"
#             "- **Other ways to express that**: Provide alternative ways to express the same ideas more naturally or professionally.\n\n"
#             "Structured Response:"
#         )

#         model_version = "meta/meta-llama-3-8b-instruct"  # Reemplaza con el ID correcto del modelo
#         raw_response = replicate.run(model_version, input={"prompt": prompt_template})

#         print("Full response from AI model:", raw_response)

#         # Unimos la lista en una sola cadena si es necesario
#         if isinstance(raw_response, list):
#             raw_response = ''.join(raw_response)
#         raw_response = str(raw_response)

#         # Define patrones regex flexibles para capturar cada sección, incluyendo listas en "Topics to study" y "Other ways to express that"
#         patterns = {
#             "Correct form to say": r"\*\*Correct form to say\*\*:\s*(.+?)(?=\n\*\*|\Z)",
#             "What error did you have?": r"\*\*What error did you have\?\*\*:\s*(.+?)(?=\n\*\*|\Z)",
#             "Topics to study": r"\*\*Topics to study\*\*:\s*(.+?)(?=\n\*\*|\Z)",
#             "Other ways to express that": r"\*\*Other ways to express that\*\*:\s*(.+?)(?=\n\*\*|\Z)"
#         }

#         # Extraemos cada parte usando regex, permitiendo listas en algunos campos
#         structured_response = {}
#         for key, pattern in patterns.items():
#             match = re.search(pattern, raw_response, re.DOTALL)
#             structured_response[key] = match.group(1).strip() if match else "No response found"

#         return {"response": structured_response}
#     except Exception as e:
#         raise HTTPException(status_code=500, detail=str(e))
# ========================================================================

# from dotenv import load_dotenv
# from fastapi import FastAPI, HTTPException, Depends
# from pydantic import BaseModel
# from sqlalchemy.orm import Session
# from database import SessionLocal
# from models import Phrase, Mistake, Topic
# import os
# import replicate
# import re
# from fastapi.middleware.cors import CORSMiddleware


# load_dotenv()

# # Initialize FastAPI app
# app = FastAPI()

# # Configura el middleware de CORS
# # Esto es necesario para permitir solicitudes desde diferentes dominios/orígenes, como el de tu extensión de Chrome.
# app.add_middleware(
#     CORSMiddleware,
#     allow_origins=["*"],  # Permite solicitudes desde cualquier origen (útil para desarrollo)
#     # En producción, reemplaza "*" con dominios específicos, por ejemplo:
#     # allow_origins=["https://your-frontend-url.com", "http://localhost:3000"]
#     allow_credentials=True,  # Permite enviar cookies y credenciales si es necesario
#     allow_methods=["*"],  # Permite todos los métodos HTTP, como GET, POST, OPTIONS
#     allow_headers=["*"],  # Permite todos los encabezados HTTP en las solicitudes
# )

# # Retrieve the Replicate API token from environment variables
# REPLICATE_API_TOKEN = os.getenv("REPLICATE_API_TOKEN")

# # Initialize Replicate client
# client = replicate.Client(api_token=REPLICATE_API_TOKEN)

# # Database dependency
# def get_db():
#     db = SessionLocal()
#     try:
#         yield db
#     finally:
#         db.close()

# # Request model
# class TextInput(BaseModel):
#     text: str

# @app.post("/process-text/")
# def process_text(input_data: TextInput, db: Session = Depends(get_db)):
#     try:
#         # Define the prompt for the AI model
#         prompt_template = (
#             "You are an English language assistant for non-native speakers focusing on professional communication. "
#             "Please help improve the following text by structuring your response in a standardized format:\n\n"
#             f"Text:\n{input_data.text}\n\n"
#             "Please answer in the following format:\n\n"
#             "- **Correct form to say**: Provide the corrected and improved version of the text.\n"
#             "- **What error did you have?**: Identify the grammar, vocabulary, or phrasing errors.\n"
#             "- **Topics to study**: Suggest topics or grammatical rules the user could study to avoid these errors.\n\n"
#             "Structured Response:"
#         )

#         # Call the AI model
#         model_version = "meta/meta-llama-3-8b-instruct"  # Replace with the correct version ID
#         raw_response = replicate.run(model_version, input={"prompt": prompt_template})

#         # Combine response if necessary
#         if isinstance(raw_response, list):
#             raw_response = ''.join(raw_response)
#         raw_response = str(raw_response)

#         # Regex patterns to extract AI response
#         patterns = {
#             "Correct form to say": r"\*\*Correct form to say\*\*:\s*(.+?)(?=\n\*\*|\Z)",
#             "What error did you have?": r"\*\*What error did you have\?\*\*:\s*(.+?)(?=\n\*\*|\Z)",
#             "Topics to study": r"\*\*Topics to study\*\*:\s*(.+?)(?=\n\*\*|\Z)"
#         }

#         # Extract structured response
#         structured_response = {}
#         for key, pattern in patterns.items():
#             match = re.search(pattern, raw_response, re.DOTALL)
#             structured_response[key] = match.group(1).strip() if match else None

#         # Extract details
#         correct_text = structured_response.get("Correct form to say")
#         errors = structured_response.get("What error did you have?")
#         topics = structured_response.get("Topics to study")

#         # Insert topics into the database
#         topic_ids = []
#         if topics:
#             for topic_name in topics.split("\n"):
#                 topic_name = topic_name.strip()
#                 existing_topic = db.query(Topic).filter(Topic.name == topic_name).first()
#                 if not existing_topic:
#                     new_topic = Topic(name=topic_name, description="")
#                     db.add(new_topic)
#                     db.commit()
#                     topic_ids.append(new_topic.id)
#                 else:
#                     topic_ids.append(existing_topic.id)

#         # Insert mistakes into the database
#         mistake_ids = []
#         if errors:
#             for error_line in errors.split("\n"):
#                 if "->" in error_line:
#                     mistake, correction = error_line.split("->")
#                     new_mistake = Mistake(mistake=mistake.strip(), correct_text=correction.strip())
#                     db.add(new_mistake)
#                     db.commit()
#                     mistake_ids.append(new_mistake.id)

#         # Insert the phrase into the database
#         new_phrase = Phrase(
#             original_text=input_data.text,
#             correct_text=correct_text,
#             topic_to_study=topic_ids[0] if topic_ids else None
#         )
#         db.add(new_phrase)
#         db.commit()

#         # Return a structured response
#         return {
#             "message": "Data processed successfully.",
#             "structured_response": structured_response,
#             "phrase_id": new_phrase.id,
#             "topic_ids": topic_ids,
#             "mistake_ids": mistake_ids
#         }

#     except Exception as e:
#         raise HTTPException(status_code=500, detail=str(e))

# =====================================================
# ====================================================
# =====================================================

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
