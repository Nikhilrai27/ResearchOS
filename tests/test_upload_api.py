from io import BytesIO

from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)

def test_upload_pdf_api():
    """
    Test the PDF upload API endpoint.
    """

    pdf_content = b"%PDF-1.4\nDummy PDF"

    response = client.post(
        "/api/v1/papers/upload",
        files={
            "file": (
                "sample.pdf",
                BytesIO(pdf_content),
                "application/pdf",
            )
        },
    )

    assert response.status_code == 201

    data = response.json()

    assert data["message"] == "PDF uploaded successfully."
    assert "file_path" in data

def test_upload_invalid_file_api():
    """
    Test uploading a non-PDF file.
    """

    txt_content = b"This is not a PDF."

    response = client.post(
        "/api/v1/papers/upload",
        files={
            "file": (
                "notes.txt",
                BytesIO(txt_content),
                "text/plain",
            )
        },
    )

    assert response.status_code == 400

    data = response.json()

    assert data["detail"] == "Only PDF files are allowed."    

def test_upload_large_file_api():
    """
    Test uploading a file larger than the maximum allowed size.
    """

    large_pdf = (
        b"%PDF-1.4\n"
        + b"A" * (50 * 1024 * 1024 + 1)
    )

    response = client.post(
        "/api/v1/papers/upload",
        files={
            "file": (
                "large.pdf",
                BytesIO(large_pdf),
                "application/pdf",
            )
        },
    )

    assert response.status_code == 400

    data = response.json()

    assert data["detail"] == "File exceeds the maximum size of 50 MB."

def test_upload_empty_file_api():
    """
    Test uploading an empty PDF file.
    """

    response = client.post(
        "/api/v1/papers/upload",
        files={
            "file": (
                "empty.pdf",
                BytesIO(b""),
                "application/pdf",
            )
        },
    )

    assert response.status_code == 400

    data = response.json()

    assert data["detail"] == "Uploaded file is empty."    
