from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)

def test_upload_pdf():
    pdf_content = b"%PDF-1.4\nDummy PDF Content"

    response = client.post(
        "/upload/",
        files={
            "file": (
                "sample.pdf",
                pdf_content,
                "application/pdf",
            )
        },
    )

    assert response.status_code == 200

    data = response.json()

    assert data["message"] == "File uploaded successfully"
    assert data["filename"] == "sample.pdf"
