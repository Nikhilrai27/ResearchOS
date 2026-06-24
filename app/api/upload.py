from fastapi import APIRouter, UploadFile, File
from app.services.pdf.upload_service import UploadService

router = APIRouter(
    prefix="/upload",
    tags=["Upload"],
)

upload_service = UploadService()


@router.post("/")
async def upload_pdf(file: UploadFile = File(...)):
    saved_path = await upload_service.save_file(file)

    return {
        "message": "File uploaded successfully",
        "filename": file.filename,
        "saved_to": str(saved_path),
    }