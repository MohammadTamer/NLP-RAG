from fastapi import APIRouter
from app.services.vector_db_service import delete_collection, create_collection

router = APIRouter()

@router.delete("/reset")
def reset_db():
    delete_collection()
    create_collection()
    return {"message": "database reset"}