import uuid
from pathlib import Path

from fastapi import UploadFile


class UploadService:
    """Service responsible for handling PDF uploads."""

    MAX_FILE_SIZE = 50 * 1024 * 1024  # 50 MB

    def __init__(self, upload_dir: str = "data/uploads"):
        self.upload_dir = Path(upload_dir)
        self.upload_dir.mkdir(parents=True, exist_ok=True)

    async def validate_pdf_file(self, file: UploadFile) -> None:
        """
        Validate the uploaded PDF file.
        """

        # Check filename
        if not file.filename:
            raise ValueError("No filename provided.")

        # Check extension
        extension = Path(file.filename).suffix.lower()
        if extension != ".pdf":
            raise ValueError("Only PDF files are allowed.")

        # Check MIME type
        if file.content_type != "application/pdf":
            raise ValueError("Invalid MIME type. Only PDF files are allowed.")

        # Read uploaded file
        contents = await file.read()
        file_size = len(contents)

        # Empty file check
        if file_size == 0:
            raise ValueError("Uploaded file is empty.")

        # Maximum file size check
        if file_size > self.MAX_FILE_SIZE:
            raise ValueError("File exceeds the maximum size of 50 MB.")

        # Reset file pointer
        await file.seek(0)

    def generate_file_id(self) -> str:
        """
        Generate a unique filename for uploaded PDFs.
        """
        return f"{uuid.uuid4()}.pdf"

    async def save_file(self, file: UploadFile) -> Path:
        """
        Save an uploaded PDF file and return its path.
        """

        # Validate before saving
        await self.validate_pdf_file(file)

        # Generate a unique filename
        while True:
            filename = self.generate_file_id()
            file_path = self.upload_dir / filename

            # Ensure the filename does not already exist
            if not file_path.exists():
                break

        # Read uploaded contents
        contents = await file.read()

        # Save the file
        with open(file_path, "wb") as f:
            f.write(contents)

        return file_path

    def delete_paper_file(self, file_path: Path) -> bool:
        """
        Delete an uploaded PDF file.

        Args:
            file_path: Path to the PDF file.

        Returns:
            True if the file was deleted, False if the file does not exist.
        """

        if file_path.exists():
            file_path.unlink()
            return True

        return False