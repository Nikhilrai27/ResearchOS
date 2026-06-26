from pydantic import BaseModel


class UploadResponse(BaseModel):
    message: str
    file_path: str