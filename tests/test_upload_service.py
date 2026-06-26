from io import BytesIO

import pytest
from fastapi import UploadFile

from app.services.pdf.upload_service import UploadService


@pytest.mark.asyncio
async def test_valid_pdf_upload(tmp_path):
    """
    Test that a valid PDF is successfully saved.
    """

    service = UploadService(upload_dir=str(tmp_path))

    pdf_content = b"%PDF-1.4\nDummy PDF Content"

    upload_file = UploadFile(
        filename="sample.pdf",
        file=BytesIO(pdf_content),
        headers={"content-type": "application/pdf"},
    )

    saved_path = await service.save_file(upload_file)

    assert saved_path.exists()
    assert saved_path.suffix == ".pdf"

@pytest.mark.asyncio
async def test_invalid_file_type(tmp_path):
    """
    Test that non-PDF files are rejected.
    """

    service = UploadService(upload_dir=str(tmp_path))

    txt_content = b"This is not a PDF."

    upload_file = UploadFile(
        filename="notes.txt",
        file=BytesIO(txt_content),
        headers={"content-type": "text/plain"},
    )

    with pytest.raises(ValueError, match="Only PDF files are allowed."):
        await service.save_file(upload_file)    

@pytest.mark.asyncio
async def test_file_size_limit(tmp_path):
    """
    Test that files larger than the maximum allowed size are rejected.
    """

    service = UploadService(upload_dir=str(tmp_path))

    large_pdf = b"%PDF-1.4\n" + b"A" * (UploadService.MAX_FILE_SIZE + 1)

    upload_file = UploadFile(
        filename="large.pdf",
        file=BytesIO(large_pdf),
        headers={"content-type": "application/pdf"},
    )

    with pytest.raises(
        ValueError,
        match="File exceeds the maximum size of 50 MB.",
    ):
        await service.save_file(upload_file)        
        
@pytest.mark.asyncio
async def test_duplicate_file_handling(tmp_path):
    """
    Test that duplicate uploads receive different filenames.
    """

    service = UploadService(upload_dir=str(tmp_path))

    pdf_content = b"%PDF-1.4\nDummy PDF"

    file1 = UploadFile(
        filename="paper.pdf",
        file=BytesIO(pdf_content),
        headers={"content-type": "application/pdf"},
    )

    file2 = UploadFile(
        filename="paper.pdf",
        file=BytesIO(pdf_content),
        headers={"content-type": "application/pdf"},
    )

    path1 = await service.save_file(file1)
    path2 = await service.save_file(file2)

    assert path1.exists()
    assert path2.exists()
    assert path1 != path2        