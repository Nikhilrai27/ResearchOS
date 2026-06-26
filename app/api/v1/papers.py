from fastapi import (
    APIRouter,
    File,
    HTTPException,
    UploadFile,
    status,
)

from app.models.schemas import UploadResponse
from app.services.pdf.upload_service import UploadService

router = APIRouter(
    prefix="/papers",
    tags=["Papers"],
)


@router.post(
    "/upload",
    response_model=UploadResponse,
    status_code=status.HTTP_201_CREATED,
)
async def upload_paper(file: UploadFile = File(...)):
    """
    Upload a PDF research paper.
    """
    service = UploadService()

    try:
        file_path = await service.save_file(file)

        return UploadResponse(
            message="PDF uploaded successfully.",
            file_path=str(file_path),
        )

    except ValueError as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=str(e),
        )