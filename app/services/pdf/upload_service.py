from pathlib import Path
from fastapi import UploadFile


class UploadService:
    """Service responsible for handling PDF uploads."""

    def __init__(self, upload_dir: str = "data/uploads"):
        self.upload_dir = Path(upload_dir)
        self.upload_dir.mkdir(parents=True, exist_ok=True)

    async def save_file(self, file: UploadFile) -> Path:
        """
        Save an uploaded file and return its path.
        """
        file_path = self.upload_dir / file.filename

        contents = await file.read()

        with open(file_path, "wb") as f:
            f.write(contents)

        return file_path