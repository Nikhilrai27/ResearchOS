# ResearchOS Repository Map

**Project:** ResearchOS
**Repository Owner:** Nikhil Rai
**Repository Type:** AI Research Assistant / SaaS
**Last Updated:** 2026-06-26

---

# Repository Statistics

| Item                | Count |
| ------------------- | ----: |
| Source Directories  |    12 |
| Python Source Files |    18 |
| Documentation Files |     5 |
| Test Files          |     4 |

---

# Repository Structure

```text
ResearchOS/
│
├── app/
│   ├── agents/
│   ├── api/
│   │   └── upload.py
│   ├── core/
│   │   ├── config.py
│   │   └── logging.py
│   ├── models/
│   ├── services/
│   │   ├── embeddings/
│   │   ├── pdf/
│   │   │   └── upload_service.py
│   │   ├── rag/
│   │   └── vectordb/
│   ├── utils/
│   └── main.py
│
├── data/
│   ├── uploads/
│   └── vectordb/
│
├── docker/
├── docs/
├── scripts/
├── tests/
│
├── CURRENT.md
├── CURRENT_STATUS.md
├── PROJECT_SCOPE.md
├── README.md
├── ROADMAP.md
├── requirements.txt
├── .env.example
└── .gitignore
```

---

# Root Directory

## app/

**Purpose**

Contains the complete backend application.

### Submodules

* agents/
* api/
* core/
* models/
* services/
* utils/

---

## data/

Stores application data generated at runtime.

### uploads/

Stores uploaded PDF files.

### vectordb/

Stores vector database files.

---

## docker/

Contains Docker configuration files.

---

## docs/

Contains project documentation.

---

## scripts/

Utility scripts used during development.

---

## tests/

Contains automated tests.

---

# Application Package

---

## app/main.py

**Purpose**

FastAPI application entry point.

**Responsibilities**

* Create FastAPI app
* Register routes
* Configure middleware
* Initialize application

**Current Status**

Completed

---

## app/api/

Contains REST API endpoints.

### upload.py

**Purpose**

Handles PDF upload requests.

**Responsibilities**

* Receive uploaded files
* Call UploadService
* Return API responses

---

## app/core/

Shared application configuration.

### config.py

Configuration management.

### logging.py

Central logging configuration.

---

## app/services/

Contains business logic.

### embeddings/

Future embedding generation.

### pdf/

PDF processing services.

#### upload_service.py

Current upload processing logic.

Future responsibilities:

* File validation
* SHA256 hashing
* Duplicate detection
* Metadata extraction
* Database integration

### rag/

Future Retrieval-Augmented Generation pipeline.

### vectordb/

Future vector database operations.

---

## app/models/

Database models.

(Currently placeholder.)

---

## app/utils/

Utility/helper functions.

(Currently placeholder.)

---

## app/agents/

Future AI agents.

(Currently placeholder.)

---

# Scripts

## test_config.py

Configuration validation.

## test_logger_helper.py

Logging helper tests.

## test_logging.py

Logging tests.

---

# Tests

## test_main.py

FastAPI application tests.

---

# Documentation Files

## README.md

Project overview.

## ROADMAP.md

Long-term development roadmap.

## PROJECT_SCOPE.md

Project objectives and scope.

## CURRENT.md

Daily development checkpoint.

## CURRENT_STATUS.md

Current implementation status.

---

# Runtime Directories

## data/uploads/

Uploaded research papers.

## data/vectordb/

Persistent vector database storage.

---

# Ignored Directories

These directories are intentionally omitted from this document because they are generated automatically:

* venv/
* .git/
* **pycache**/
* .pytest_cache/

