from fastapi import APIRouter

router = APIRouter()

@router.get("/example-mistakes")
def example_route():
    return {"message": "This is an example route"}
