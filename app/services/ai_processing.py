import replicate

from app.core.config import settings

def get_replicate_client():
    """Obtiene una instancia del cliente Replicate."""
    if not settings.REPLICATE_API_TOKEN:
        raise ValueError("El token de API de Replicate no está configurado.")
    return replicate.Client(api_token=settings.REPLICATE_API_TOKEN)

def generate_prompt(text: str) -> str:
    """Genera el prompt que será enviado al modelo de IA."""
    return (
        "You are an English language assistant for non-native speakers focusing on professional communication. "
        "Please help improve the following text by structuring your response in a standardized format:\n\n"
        f"Text:\n{text}\n\n"
        "Please answer in the following format:\n\n"
        "- **Correct form to say**: Provide the corrected and improved version of the text.\n"
        "- **What error did you have?**: Identify the grammar, vocabulary, or phrasing errors.\n"
        "- **Topics to study**: Suggest topics or grammatical rules the user could study to avoid these errors.\n"
        "- **Other ways to express that**: Provide alternative ways to express the same ideas more naturally or professionally.\n\n"
        "Structured Response:"
    )

def call_replicate_model(prompt: str) -> str:
    """Llama al modelo de IA con el prompt generado."""
    try:
        client = get_replicate_client()
        response = client.run(settings.MODEL_VERSION, input={"prompt": prompt})
        print(f"Respuesta de IA: {response}")
        if isinstance(response, list):
            response = ''.join(response)
        return response
    except Exception as e:
        print(f"Error al llamar al modelo de IA: {e}")
        raise RuntimeError("Hubo un problema al procesar la solicitud con IA.")


import re

def parse_response(response: list) -> dict:
    """Parsea la respuesta del modelo usando expresiones regulares."""
    try:
        # Une todos los elementos de la lista en un único string
        raw_response = ''.join(response)
        
        # Regex patterns para extraer las secciones clave
        patterns = {
            "Correct form to say": r"\*\*Correct form to say\*\*:\s*(.+?)(?=\n\*\*|\Z)",
            "What error did you have?": r"\*\*What error did you have\?\*\*:\s*(.+?)(?=\n\*\*|\Z)",
            "Topics to study": r"\*\*Topics to study\*\*:\s*(.+?)(?=\n\*\*|\Z)",
            "Other ways to express that": r"\*\*Other ways to express that\*\*:\s*(.+?)(?=\n\*\*|\Z)"
        }

        # Extrae cada sección usando los patrones
        structured_response = {}
        for key, pattern in patterns.items():
            match = re.search(pattern, raw_response, re.DOTALL)
            structured_response[key] = match.group(1).strip() if match else None

            print(f"STRCUTED RESPONSE: {structured_response}")

        return structured_response
    except Exception as e:
        print(f"Error al parsear la respuesta con regex: {e}")
        return {"raw_response": ''.join(response)}  # Devuelve la respuesta cruda en caso de error


# def parse_response(response: str) -> dict:
#     """Parsea la respuesta del modelo en un formato estructurado."""
#     try:
#         sections = {}
#         for line in response.split("\n"):
#             if line.startswith("- **"):
#                 key, value = line.split("**:", 1)
#                 key = key.replace("- **", "").strip()
#                 sections[key] = value.strip()
#         return sections
#     except Exception as e:
#         print(f"Error al parsear la respuesta: {e}")
#         return {"raw_response": response}


def process_with_ai(text: str) -> dict:
    """Procesa un texto utilizando el modelo de IA."""
    prompt = generate_prompt(text)
    raw_response = call_replicate_model(prompt)
    structured_response = parse_response(raw_response)
    return {"response": structured_response}


# def process_with_ai(text: str) -> dict:
#     """
#     Procesa un texto con el modelo de IA y devuelve una respuesta estructurada.
#     """
#     # Define el prompt para el modelo de IA
#     prompt_template = (
#         "You are an English language assistant for non-native speakers focusing on professional communication. "
#         "Please help improve the following text by structuring your response in a standardized format:\n\n"
#         "Text:\n"
#         f"{text}\n\n"
#         "Please answer in the following format:\n\n"
#         "- **Correct form to say**: Provide the corrected and improved version of the text.\n"
#         "- **What error did you have?**: Identify the grammar, vocabulary, or phrasing errors.\n"
#         "- **Topics to study**: Suggest topics or grammatical rules the user could study to avoid these errors.\n"
#         "- **Other ways to express that**: Provide alternative ways to express the same ideas more naturally or professionally.\n\n"
#         "Structured Response:"
#     )

#     # Realiza la llamada al modelo de IA
#     model_version = "meta/meta-llama-3-8b-instruct"  # Asegúrate de usar el ID correcto
#     raw_response = replicate.run(model_version, input={"prompt": prompt_template})

#     # Maneja y devuelve la respuesta
#     if isinstance(raw_response, list):
#         raw_response = ''.join(raw_response)

#     return {"response": raw_response}
