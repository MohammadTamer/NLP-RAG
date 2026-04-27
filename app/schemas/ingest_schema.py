from pydantic import BaseModel

class IngestResponse(BaseModel):
    message: str
    filename: str
    chunks_count: int