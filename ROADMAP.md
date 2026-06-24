# ROADMAP.md
# ResearchOS — Complete Development Roadmap
Version: 1.0
Total Estimated Tasks: 400+
Each task: 10–30 minutes

---

## PHASE 0 — Project Planning
Goal: Define scope, architecture, and project foundation before writing code.

### Milestone 0.1 — Documentation Foundation
  Task 0.1.1 — Write PROJECT_SCOPE.md
    Subtask 0.1.1.1 — Define problem statement
    Subtask 0.1.1.2 — Define target users
    Subtask 0.1.1.3 — Define core features
    Subtask 0.1.1.4 — Define out-of-scope items
    Subtask 0.1.1.5 — Define success criteria
    Subtask 0.1.1.6 — Define technical constraints

  Task 0.1.2 — Write README.md
    Subtask 0.1.2.1 — Project vision section
    Subtask 0.1.2.2 — Problem statement section
    Subtask 0.1.2.3 — Architecture overview
    Subtask 0.1.2.4 — Technology stack table
    Subtask 0.1.2.5 — Roadmap status table
    Subtask 0.1.2.6 — Installation guide placeholder
    Subtask 0.1.2.7 — Folder structure diagram

  Task 0.1.3 — Write Complete ROADMAP.md
    Subtask 0.1.3.1 — Define all phases
    Subtask 0.1.3.2 — Break phases into milestones
    Subtask 0.1.3.3 — Break milestones into tasks
    Subtask 0.1.3.4 — Break tasks into subtasks
    Subtask 0.1.3.5 — Estimate time per task

  Task 0.1.4 — Create CURRENT_STATUS.md
  Task 0.1.5 — Create DECISIONS.md skeleton
  Task 0.1.6 — Create CHANGELOG.md skeleton
  Task 0.1.7 — Create LEARNING_LOG.md skeleton

STATUS: ✅ COMPLETE

---

## PHASE 1 — Environment Setup
Goal: Create a reproducible, professional Python development environment.

### Milestone 1.1 — Python Environment
  Task 1.1.1 — Verify Python installation
    Subtask 1.1.1.1 — Run python --version (must be 3.11+)
    Subtask 1.1.1.2 — Run pip --version
    Subtask 1.1.1.3 — Understand why Python 3.11+ matters

  Task 1.1.2 — Create virtual environment
    Subtask 1.1.2.1 — Understand what a virtual environment is
    Subtask 1.1.2.2 — Run python -m venv venv
    Subtask 1.1.2.3 — Understand the venv folder structure
    Subtask 1.1.2.4 — Add venv to .gitignore

  Task 1.1.3 — Activate virtual environment
    Subtask 1.1.3.1 — Activate on Windows (venv\Scripts\activate)
    Subtask 1.1.3.2 — Activate on Mac/Linux (source venv/bin/activate)
    Subtask 1.1.3.3 — Verify activation (which python)

  Task 1.1.4 — Install core dependencies
    Subtask 1.1.4.1 — Understand requirements.txt purpose
    Subtask 1.1.4.2 — Create requirements.txt
    Subtask 1.1.4.3 — Install fastapi
    Subtask 1.1.4.4 — Install uvicorn
    Subtask 1.1.4.5 — Install python-dotenv
    Subtask 1.1.4.6 — Install pydantic-settings
    Subtask 1.1.4.7 — Install pytest
    Subtask 1.1.4.8 — Verify all installations

### Milestone 1.2 — Git Setup
  Task 1.2.1 — Initialize Git repository
    Subtask 1.2.1.1 — Run git init
    Subtask 1.2.1.2 — Understand .git folder
    Subtask 1.2.1.3 — Configure git username and email

  Task 1.2.2 — Create .gitignore
    Subtask 1.2.2.1 — Add venv/
    Subtask 1.2.2.2 — Add __pycache__/
    Subtask 1.2.2.3 — Add .env
    Subtask 1.2.2.4 — Add *.pyc
    Subtask 1.2.2.5 — Add data/uploads/
    Subtask 1.2.2.6 — Add data/vectordb/
    Subtask 1.2.2.7 — Add .DS_Store (Mac)

  Task 1.2.3 — First commit
    Subtask 1.2.3.1 — git add .
    Subtask 1.2.3.2 — git commit -m "chore: project planning documents"
    Subtask 1.2.3.3 — Understand conventional commits format

  Task 1.2.4 — Connect to GitHub
    Subtask 1.2.4.1 — Create GitHub repository
    Subtask 1.2.4.2 — Add remote origin
    Subtask 1.2.4.3 — Push first commit

### Milestone 1.3 — Environment Configuration
  Task 1.3.1 — Create .env.example
    Subtask 1.3.1.1 — Understand why .env files matter
    Subtask 1.3.1.2 — Add OPENAI_API_KEY placeholder
    Subtask 1.3.1.3 — Add APP_ENV placeholder
    Subtask 1.3.1.4 — Add DEBUG placeholder
    Subtask 1.3.1.5 — Add DATABASE_URL placeholder

  Task 1.3.2 — Create .env (local, not committed)
    Subtask 1.3.2.1 — Copy .env.example to .env
    Subtask 1.3.2.2 — Fill in real values
    Subtask 1.3.2.3 — Verify .env is in .gitignore

  Task 1.3.3 — Test environment loading
    Subtask 1.3.3.1 — Write tiny test script to load .env
    Subtask 1.3.3.2 — Verify variables are accessible
    Subtask 1.3.3.3 — Delete test script

---

## PHASE 2 — Repository Structure
Goal: Create professional folder structure before writing any logic.

### Milestone 2.1 — Project Skeleton
  Task 2.1.1 — Create top-level folders
    Subtask 2.1.1.1 — Create app/
    Subtask 2.1.1.2 — Create tests/
    Subtask 2.1.1.3 — Create docs/
    Subtask 2.1.1.4 — Create docker/
    Subtask 2.1.1.5 — Create data/uploads/
    Subtask 2.1.1.6 — Create data/vectordb/
    Subtask 2.1.1.7 — Create scripts/

  Task 2.1.2 — Create app/ subfolders
    Subtask 2.1.2.1 — Create app/api/
    Subtask 2.1.2.2 — Create app/agents/
    Subtask 2.1.2.3 — Create app/core/
    Subtask 2.1.2.4 — Create app/models/
    Subtask 2.1.2.5 — Create app/services/
    Subtask 2.1.2.6 — Create app/utils/

  Task 2.1.3 — Create services/ subfolders
    Subtask 2.1.3.1 — Create app/services/pdf/
    Subtask 2.1.3.2 — Create app/services/embeddings/
    Subtask 2.1.3.3 — Create app/services/vectordb/
    Subtask 2.1.3.4 — Create app/services/rag/

  Task 2.1.4 — Create __init__.py files
    Subtask 2.1.4.1 — Understand why __init__.py is needed
    Subtask 2.1.4.2 — Create __init__.py in every package folder
    Subtask 2.1.4.3 — Verify Python can import from packages

### Milestone 2.2 — Core Configuration Module
  Task 2.2.1 — Create app/core/config.py
    Subtask 2.2.1.1 — Understand pydantic-settings
    Subtask 2.2.1.2 — Create Settings class
    Subtask 2.2.1.3 — Add OPENAI_API_KEY field
    Subtask 2.2.1.4 — Add APP_ENV field
    Subtask 2.2.1.5 — Add DEBUG field
    Subtask 2.2.1.6 — Add UPLOAD_DIR field
    Subtask 2.2.1.7 — Add MAX_FILE_SIZE field
    Subtask 2.2.1.8 — Add model_config for .env loading
    Subtask 2.2.1.9 — Create singleton settings instance
    Subtask 2.2.1.10 — Test settings can be imported

  Task 2.2.2 — Create app/core/logging.py
    Subtask 2.2.2.1 — Understand Python logging module
    Subtask 2.2.2.2 — Set up structured logging
    Subtask 2.2.2.3 — Create get_logger() helper function
    Subtask 2.2.2.4 — Test logger works

### Milestone 2.3 — Application Entry Point
  Task 2.3.1 — Create app/main.py (minimal FastAPI app)
    Subtask 2.3.1.1 — Understand FastAPI app creation
    Subtask 2.3.1.2 — Create FastAPI() instance
    Subtask 2.3.1.3 — Add root health check endpoint
    Subtask 2.3.1.4 — Add app title, version, description

  Task 2.3.2 — Run the application
    Subtask 2.3.2.1 — Run uvicorn app.main:app --reload
    Subtask 2.3.2.2 — Visit http://localhost:8000
    Subtask 2.3.2.3 — Visit http://localhost:8000/docs
    Subtask 2.3.2.4 — Understand FastAPI auto-documentation
    Subtask 2.3.2.5 — Understand what --reload does

  Task 2.3.3 — Write first test
    Subtask 2.3.3.1 — Create tests/test_main.py
    Subtask 2.3.3.2 — Write test for health check endpoint
    Subtask 2.3.3.3 — Run pytest and verify pass
    Subtask 2.3.3.4 — Understand TestClient in FastAPI

---

## PHASE 3 — PDF Upload System
Goal: Allow users to upload PDF research papers safely.

### Milestone 3.1 — Upload Models
  Task 3.1.1 — Create Pydantic models for paper metadata
    Subtask 3.1.1.1 — Understand Pydantic models
    Subtask 3.1.1.2 — Create PaperBase model
    Subtask 3.1.1.3 — Create PaperCreate model
    Subtask 3.1.1.4 — Create PaperResponse model
    Subtask 3.1.1.5 — Add fields: id, title, filename, size, created_at
    Subtask 3.1.1.6 — Add field validators for file size

### Milestone 3.2 — Upload Service
  Task 3.2.1 — Create app/services/pdf/upload_service.py
    Subtask 3.2.1.1 — Understand file handling in Python
    Subtask 3.2.1.2 — Write validate_pdf_file() function
    Subtask 3.2.1.3 — Write save_upload_file() function
    Subtask 3.2.1.4 — Write generate_file_id() function
    Subtask 3.2.1.5 — Handle file already exists case
    Subtask 3.2.1.6 — Write delete_paper_file() function

### Milestone 3.3 — Upload API Endpoint
  Task 3.3.1 — Create app/api/v1/papers.py
    Subtask 3.3.1.1 — Create APIRouter for papers
    Subtask 3.3.1.2 — Write POST /papers/upload endpoint
    Subtask 3.3.1.3 — Understand FastAPI UploadFile
    Subtask 3.3.1.4 — Validate file type (PDF only)
    Subtask 3.3.1.5 — Validate file size
    Subtask 3.3.1.6 — Return proper response model
    Subtask 3.3.1.7 — Add proper HTTP status codes
    Subtask 3.3.1.8 — Add error handling

  Task 3.3.2 — Register router in main.py
    Subtask 3.3.2.1 — Import router
    Subtask 3.3.2.2 — Add router with /api/v1 prefix
    Subtask 3.3.2.3 — Test in /docs UI

### Milestone 3.4 — Database for Paper Metadata
  Task 3.4.1 — Understand why we need a database
    Subtask 3.4.1.1 — Difference between SQL and vector DB
    Subtask 3.4.1.2 — When to use which

  Task 3.4.2 — Set up SQLite with SQLAlchemy
    Subtask 3.4.2.1 — Install sqlalchemy
    Subtask 3.4.2.2 — Create app/core/database.py
    Subtask 3.4.2.3 — Create engine and SessionLocal
    Subtask 3.4.2.4 — Create Base for models

  Task 3.4.3 — Create Paper database model
    Subtask 3.4.3.1 — Create app/models/paper.py
    Subtask 3.4.3.2 — Add Paper SQLAlchemy model
    Subtask 3.4.3.3 — Add all required fields
    Subtask 3.4.3.4 — Create tables on startup

  Task 3.4.4 — Create paper repository (CRUD)
    Subtask 3.4.4.1 — Understand repository pattern
    Subtask 3.4.4.2 — Create create_paper() function
    Subtask 3.4.4.3 — Create get_paper_by_id() function
    Subtask 3.4.4.4 — Create get_all_papers() function
    Subtask 3.4.4.5 — Create delete_paper() function

### Milestone 3.5 — Upload Tests
  Task 3.5.1 — Write tests for upload service
    Subtask 3.5.1.1 — Test valid PDF upload
    Subtask 3.5.1.2 — Test invalid file type rejection
    Subtask 3.5.1.3 — Test file size limit
    Subtask 3.5.1.4 — Test duplicate file handling

  Task 3.5.2 — Write API tests for upload endpoint
    Subtask 3.5.2.1 — Test successful upload returns 201
    Subtask 3.5.2.2 — Test non-PDF returns 400
    Subtask 3.5.2.3 — Test missing file returns 422

---

## PHASE 4 — PDF Parsing
Goal: Extract raw text from uploaded PDF files.

### Milestone 4.1 — Parser Foundation
  Task 4.1.1 — Install and understand PyMuPDF
    Subtask 4.1.1.1 — Install pymupdf (pip install pymupdf)
    Subtask 4.1.1.2 — Understand what PyMuPDF does
    Subtask 4.1.1.3 — Understand PDF structure (pages, blocks, spans)

  Task 4.1.2 — Create parser interface
    Subtask 4.1.2.1 — Understand why interfaces matter
    Subtask 4.1.2.2 — Create abstract BaseParser class
    Subtask 4.1.2.3 — Define parse() method signature
    Subtask 4.1.2.4 — Define ParseResult dataclass

### Milestone 4.2 — PyMuPDF Parser Implementation
  Task 4.2.1 — Create app/services/pdf/parser.py
    Subtask 4.2.1.1 — Create PyMuPDFParser class
    Subtask 4.2.1.2 — Implement parse() method
    Subtask 4.2.1.3 — Extract text page by page
    Subtask 4.2.1.4 — Capture page numbers with text
    Subtask 4.2.1.5 — Extract document metadata (title, author)
    Subtask 4.2.1.6 — Handle corrupted PDFs gracefully
    Subtask 4.2.1.7 — Handle password-protected PDFs
    Subtask 4.2.1.8 — Return structured ParseResult

### Milestone 4.3 — Parse API Endpoint
  Task 4.3.1 — Add POST /papers/{paper_id}/parse endpoint
    Subtask 4.3.1.1 — Validate paper exists
    Subtask 4.3.1.2 — Call parser service
    Subtask 4.3.1.3 — Store raw text in database
    Subtask 4.3.1.4 — Update paper status field
    Subtask 4.3.1.5 — Return parse result summary

### Milestone 4.4 — Parser Tests
  Task 4.4.1 — Create test fixtures
    Subtask 4.4.1.1 — Find or create sample test PDF
    Subtask 4.4.1.2 — Create tests/fixtures/ folder
    Subtask 4.4.1.3 — Add sample.pdf to fixtures

  Task 4.4.2 — Write parser tests
    Subtask 4.4.2.1 — Test successful text extraction
    Subtask 4.4.2.2 — Test page count accuracy
    Subtask 4.4.2.3 — Test metadata extraction
    Subtask 4.4.2.4 — Test corrupted PDF handling
    Subtask 4.4.2.5 — Test empty PDF handling

---

## PHASE 5 — Text Cleaning
Goal: Transform raw extracted text into clean, processable text.

### Milestone 5.1 — Cleaning Pipeline
  Task 5.1.1 — Understand why text cleaning matters
    Subtask 5.1.1.1 — Learn common PDF extraction artifacts
    Subtask 5.1.1.2 — Understand what affects embedding quality
    Subtask 5.1.1.3 — Learn what NOT to clean (preserve meaning)

  Task 5.1.2 — Create app/services/pdf/cleaner.py
    Subtask 5.1.2.1 — Create TextCleaner class
    Subtask 5.1.2.2 — Implement remove_extra_whitespace()
    Subtask 5.1.2.3 — Implement fix_hyphenation()
    Subtask 5.1.2.4 — Implement remove_headers_footers()
    Subtask 5.1.2.5 — Implement normalize_unicode()
    Subtask 5.1.2.6 — Implement remove_page_numbers()
    Subtask 5.1.2.7 — Implement clean() master method
    Subtask 5.1.2.8 — Preserve paragraph structure

### Milestone 5.2 — Section Detection
  Task 5.2.1 — Create section detector
    Subtask 5.2.1.1 — Understand academic paper structure
    Subtask 5.2.1.2 — Create pattern matching for section headers
    Subtask 5.2.1.3 — Detect: Abstract, Introduction, Methods, Results
    Subtask 5.2.1.4 — Detect: Discussion, Conclusion, References
    Subtask 5.2.1.5 — Return sections as dict with content

### Milestone 5.3 — Cleaning Tests
  Task 5.3.1 — Write text cleaning tests
    Subtask 5.3.1.1 — Test whitespace normalization
    Subtask 5.3.1.2 — Test hyphenation fixing
    Subtask 5.3.1.3 — Test unicode normalization
    Subtask 5.3.1.4 — Test section detection

---

## PHASE 6 — Text Chunking
Goal: Split cleaned text into meaningful chunks for embedding.

### Milestone 6.1 — Chunking Concepts
  Task 6.1.1 — Understand chunking strategies
    Subtask 6.1.1.1 — Fixed-size chunking
    Subtask 6.1.1.2 — Sentence-based chunking
    Subtask 6.1.1.3 — Semantic chunking
    Subtask 6.1.1.4 — Overlapping chunks
    Subtask 6.1.1.5 — Why overlap matters for retrieval

### Milestone 6.2 — Chunker Implementation
  Task 6.2.1 — Create app/services/pdf/chunker.py
    Subtask 6.2.1.1 — Create Chunk dataclass (text, metadata)
    Subtask 6.2.1.2 — Create TextChunker class
    Subtask 6.2.1.3 — Implement fixed_size_chunk()
    Subtask 6.2.1.4 — Implement sentence_chunk()
    Subtask 6.2.1.5 — Add overlap parameter
    Subtask 6.2.1.6 — Attach metadata to each chunk
    Subtask 6.2.1.7 — Include paper_id in chunk metadata
    Subtask 6.2.1.8 — Include page_number in chunk metadata
    Subtask 6.2.1.9 — Include section_name in chunk metadata
    Subtask 6.2.1.10 — Include chunk_index in chunk metadata

### Milestone 6.3 — Chunking Tests
  Task 6.3.1 — Write chunking tests
    Subtask 6.3.1.1 — Test chunk size respects max_size
    Subtask 6.3.1.2 — Test overlap is applied correctly
    Subtask 6.3.1.3 — Test metadata is attached to all chunks
    Subtask 6.3.1.4 — Test empty text handling
    Subtask 6.3.1.5 — Test very long text handling

---

## PHASE 7 — Embedding Generation
Goal: Convert text chunks into vector embeddings.

### Milestone 7.1 — Embedding Concepts
  Task 7.1.1 — Understand vector embeddings
    Subtask 7.1.1.1 — What is a vector embedding?
    Subtask 7.1.1.2 — Why do embeddings enable semantic search?
    Subtask 7.1.1.3 — What is cosine similarity?
    Subtask 7.1.1.4 — Choosing embedding dimensions
    Subtask 7.1.1.5 — Embedding model options and tradeoffs

### Milestone 7.2 — Embedding Service
  Task 7.2.1 — Create embedding interface
    Subtask 7.2.1.1 — Create abstract BaseEmbedder class
    Subtask 7.2.1.2 — Define embed() method signature
    Subtask 7.2.1.3 — Define embed_batch() method signature

  Task 7.2.2 — Create OpenAI embedder
    Subtask 7.2.2.1 — Install openai library
    Subtask 7.2.2.2 — Create app/services/embeddings/openai_embedder.py
    Subtask 7.2.2.3 — Implement embed() using text-embedding-3-small
    Subtask 7.2.2.4 — Implement embed_batch() with rate limiting
    Subtask 7.2.2.5 — Handle API errors gracefully
    Subtask 7.2.2.6 — Add retry logic for transient failures

  Task 7.2.3 — Create local embedder (fallback)
    Subtask 7.2.3.1 — Install sentence-transformers
    Subtask 7.2.3.2 — Create app/services/embeddings/local_embedder.py
    Subtask 7.2.3.3 — Implement using all-MiniLM-L6-v2 model
    Subtask 7.2.3.4 — Match interface with OpenAI embedder

  Task 7.2.4 — Create embedder factory
    Subtask 7.2.4.1 — Create get_embedder() factory function
    Subtask 7.2.4.2 — Select embedder based on config
    Subtask 7.2.4.3 — Ensure both embedders are interchangeable

### Milestone 7.3 — Embedding Tests
  Task 7.3.1 — Write embedding tests
    Subtask 7.3.1.1 — Test embedding returns correct dimension
    Subtask 7.3.1.2 — Test batch embedding returns correct count
    Subtask 7.3.1.3 — Test similar texts have high cosine similarity
    Subtask 7.3.1.4 — Test API error handling
    Subtask 7.3.1.5 — Use mocks for API calls in tests

---

## PHASE 8 — Vector Database
Goal: Store and retrieve embeddings efficiently.

### Milestone 8.1 — Vector DB Concepts
  Task 8.1.1 — Understand vector databases
    Subtask 8.1.1.1 — What is a vector database?
    Subtask 8.1.1.2 — How similarity search works (ANN)
    Subtask 8.1.1.3 — ChromaDB vs Pinecone vs Weaviate
    Subtask 8.1.1.4 — When to use each option
    Subtask 8.1.1.5 — Understanding collections in ChromaDB

### Milestone 8.2 — ChromaDB Integration
  Task 8.2.1 — Set up ChromaDB
    Subtask 8.2.1.1 — Install chromadb
    Subtask 8.2.1.2 — Create app/services/vectordb/chroma_client.py
    Subtask 8.2.1.3 — Initialize persistent ChromaDB client
    Subtask 8.2.1.4 — Create papers collection
    Subtask 8.2.1.5 — Configure storage path from settings

  Task 8.2.2 — Create vector store service
    Subtask 8.2.2.1 — Create VectorStore class
    Subtask 8.2.2.2 — Implement add_chunks() method
    Subtask 8.2.2.3 — Implement search() method
    Subtask 8.2.2.4 — Implement delete_by_paper_id() method
    Subtask 8.2.2.5 — Implement get_collection_stats() method
    Subtask 8.2.2.6 — Store metadata with each embedding

### Milestone 8.3 — Indexing Pipeline
  Task 8.3.1 — Create end-to-end indexing pipeline
    Subtask 8.3.1.1 — Create app/services/indexing_pipeline.py
    Subtask 8.3.1.2 — Step 1: Parse PDF
    Subtask 8.3.1.3 — Step 2: Clean text
    Subtask 8.3.1.4 — Step 3: Chunk text
    Subtask 8.3.1.5 — Step 4: Generate embeddings
    Subtask 8.3.1.6 — Step 5: Store in vector DB
    Subtask 8.3.1.7 — Step 6: Update paper status in SQL DB
    Subtask 8.3.1.8 — Handle failures at each step
    Subtask 8.3.1.9 — Add progress tracking

  Task 8.3.2 — Create indexing API endpoint
    Subtask 8.3.2.1 — POST /papers/{paper_id}/index endpoint
    Subtask 8.3.2.2 — Run pipeline as background task
    Subtask 8.3.2.3 — Return job status response
    Subtask 8.3.2.4 — GET /papers/{paper_id}/status endpoint

### Milestone 8.4 — Vector DB Tests
  Task 8.4.1 — Write vector store tests
    Subtask 8.4.1.1 — Test add_chunks() stores correctly
    Subtask 8.4.1.2 — Test search() returns relevant results
    Subtask 8.4.1.3 — Test delete_by_paper_id() removes all chunks
    Subtask 8.4.1.4 — Test search with paper_id filter
    Subtask 8.4.1.5 — Use in-memory ChromaDB for tests

---

## PHASE 9 — Basic RAG
Goal: Answer user questions using retrieved paper chunks.

### Milestone 9.1 — RAG Concepts
  Task 9.1.1 — Understand RAG architecture
    Subtask 9.1.1.1 — What is Retrieval-Augmented Generation?
    Subtask 9.1.1.2 — Why RAG prevents hallucinations
    Subtask 9.1.1.3 — The retrieve-augment-generate pipeline
    Subtask 9.1.1.4 — Prompt engineering for RAG
    Subtask 9.1.1.5 — How to include citations in answers

### Milestone 9.2 — RAG Engine
  Task 9.2.1 — Create app/services/rag/retriever.py
    Subtask 9.2.1.1 — Create Retriever class
    Subtask 9.2.1.2 — Implement retrieve() method
    Subtask 9.2.1.3 — Embed the user query
    Subtask 9.2.1.4 — Search vector DB for similar chunks
    Subtask 9.2.1.5 — Filter by paper_ids if specified
    Subtask 9.2.1.6 — Return ranked RetrievedChunk objects

  Task 9.2.2 — Create app/services/rag/generator.py
    Subtask 9.2.2.1 — Create Generator class
    Subtask 9.2.2.2 — Build context string from retrieved chunks
    Subtask 9.2.2.3 — Create RAG system prompt
    Subtask 9.2.2.4 — Include citation instructions in prompt
    Subtask 9.2.2.5 — Call LLM with context + query
    Subtask 9.2.2.6 — Return RAGResponse with answer + sources

  Task 9.2.3 — Create app/services/rag/rag_engine.py
    Subtask 9.2.3.1 — Create RAGEngine class
    Subtask 9.2.3.2 — Combine retriever and generator
    Subtask 9.2.3.3 — Implement query() method
    Subtask 9.2.3.4 — Add configurable top_k parameter
    Subtask 9.2.3.5 — Add configurable temperature parameter

### Milestone 9.3 — RAG API Endpoint
  Task 9.3.1 — Create app/api/v1/query.py
    Subtask 9.3.1.1 — Create QueryRequest Pydantic model
    Subtask 9.3.1.2 — Create QueryResponse Pydantic model
    Subtask 9.3.1.3 — POST /query endpoint
    Subtask 9.3.1.4 — Support optional paper_ids filter
    Subtask 9.3.1.5 — Return answer with source citations

### Milestone 9.4 — RAG Tests
  Task 9.4.1 — Write RAG tests
    Subtask 9.4.1.1 — Test retriever returns relevant chunks
    Subtask 9.4.1.2 — Test generator produces non-empty answer
    Subtask 9.4.1.3 — Test citations are included in response
    Subtask 9.4.1.4 — Test with no matching chunks
    Subtask 9.4.1.5 — Mock LLM calls in unit tests

---

## PHASE 10 — Advanced RAG
Goal: Improve RAG quality with advanced techniques.

### Milestone 10.1 — Query Enhancement
  Task 10.1.1 — Query rewriting
    Subtask 10.1.1.1 — Understand why query rewriting helps
    Subtask 10.1.1.2 — Implement query expansion
    Subtask 10.1.1.3 — Implement HyDE (Hypothetical Document Embeddings)
    Subtask 10.1.1.4 — A/B test original vs rewritten queries

  Task 10.1.2 — Multi-query retrieval
    Subtask 10.1.2.1 — Generate multiple query variations
    Subtask 10.1.2.2 — Retrieve for each variation
    Subtask 10.1.2.3 — Deduplicate results
    Subtask 10.1.2.4 — Rerank combined results

### Milestone 10.2 — Reranking
  Task 10.2.1 — Implement result reranking
    Subtask 10.2.1.1 — Understand cross-encoder reranking
    Subtask 10.2.1.2 — Install sentence-transformers reranker
    Subtask 10.2.1.3 — Implement rerank() function
    Subtask 10.2.1.4 — Compare BM25 + rerank vs embedding-only

### Milestone 10.3 — Context Compression
  Task 10.3.1 — Implement context window management
    Subtask 10.3.1.1 — Understand LLM context limits
    Subtask 10.3.1.2 — Implement chunk compression
    Subtask 10.3.1.3 — Implement dynamic context sizing
    Subtask 10.3.1.4 — Handle context overflow gracefully

---

## PHASE 11 — Summarization Agent
Goal: Generate structured summaries of individual papers.

### Milestone 11.1 — Summarization Design
  Task 11.1.1 — Design summary structure
    Subtask 11.1.1.1 — Define what a good paper summary contains
    Subtask 11.1.1.2 — Create SummaryResult dataclass
    Subtask 11.1.1.3 — Define summary template

  Task 11.1.2 — Create summarization service
    Subtask 11.1.2.1 — Create app/services/summarization/
    Subtask 11.1.2.2 — Create summarizer.py
    Subtask 11.1.2.3 — Implement map-reduce summarization
    Subtask 11.1.2.4 — Summarize each section independently
    Subtask 11.1.2.5 — Combine section summaries
    Subtask 11.1.2.6 — Extract key contributions
    Subtask 11.1.2.7 — Extract methodology
    Subtask 11.1.2.8 — Extract main results
    Subtask 11.1.2.9 — Extract limitations

### Milestone 11.2 — Summarization Agent
  Task 11.2.1 — Create app/agents/summarization_agent.py
    Subtask 11.2.1.1 — Understand agent vs service distinction
    Subtask 11.2.1.2 — Create SummarizationAgent class
    Subtask 11.2.1.3 — Implement run() method
    Subtask 11.2.1.4 — Add prompt templates
    Subtask 11.2.1.5 — Handle long papers with chunking strategy

  Task 11.2.2 — Create summarization API endpoint
    Subtask 11.2.2.1 — POST /papers/{paper_id}/summarize
    Subtask 11.2.2.2 — Return structured summary
    Subtask 11.2.2.3 — Cache summaries in database
    Subtask 11.2.2.4 — Add force_refresh parameter

---

## PHASE 12 — Citation Agent
Goal: Track and format citations across papers.

### Milestone 12.1 — Citation Extraction
  Task 12.1.1 — Extract references from papers
    Subtask 12.1.1.1 — Parse references section
    Subtask 12.1.1.2 — Extract author, title, year, journal
    Subtask 12.1.1.3 — Store references in database
    Subtask 12.1.1.4 — Handle different citation formats

### Milestone 12.2 — Citation Linking
  Task 12.2.1 — Link citations to uploaded papers
    Subtask 12.2.1.1 — Match references to known papers
    Subtask 12.2.1.2 — Build citation graph
    Subtask 12.2.1.3 — Find highly cited papers in corpus

---

## PHASE 13 — Literature Review Agent
Goal: Synthesize multiple papers into a structured literature review.

### Milestone 13.1 — Review Design
  Task 13.1.1 — Understand literature review structure
    Subtask 13.1.1.1 — Introduction and scope
    Subtask 13.1.1.2 — Thematic sections
    Subtask 13.1.1.3 — Comparison tables
    Subtask 13.1.1.4 — Research trajectory analysis

  Task 13.1.2 — Create literature review agent
    Subtask 13.1.2.1 — Create app/agents/literature_review_agent.py
    Subtask 13.1.2.2 — Implement theme extraction from multiple papers
    Subtask 13.1.2.3 — Implement synthesis across papers
    Subtask 13.1.2.4 — Generate comparison tables
    Subtask 13.1.2.5 — Generate review sections
    Subtask 13.1.2.6 — Add citations to all claims

### Milestone 13.2 — Review API
  Task 13.2.1 — Create review generation endpoint
    Subtask 13.2.1.1 — POST /reviews/generate
    Subtask 13.2.1.2 — Accept list of paper_ids
    Subtask 13.2.1.3 — Accept review topic/focus
    Subtask 13.2.1.4 — Return structured review document
    Subtask 13.2.1.5 — Support export formats (markdown, text)

---

## PHASE 14 — Research Gap Agent
Goal: Identify unexplored research areas from existing literature.

### Milestone 14.1 — Gap Detection Design
  Task 14.1.1 — Understand research gap detection
    Subtask 14.1.1.1 — What constitutes a research gap?
    Subtask 14.1.1.2 — Explicit gaps (author-mentioned limitations)
    Subtask 14.1.1.3 — Implicit gaps (topics not studied)
    Subtask 14.1.1.4 — Methodological gaps

  Task 14.1.2 — Create gap detection agent
    Subtask 14.1.2.1 — Create app/agents/gap_agent.py
    Subtask 14.1.2.2 — Extract stated limitations from papers
    Subtask 14.1.2.3 — Identify coverage gaps across papers
    Subtask 14.1.2.4 — Generate gap hypotheses
    Subtask 14.1.2.5 — Rank gaps by importance
    Subtask 14.1.2.6 — Suggest research directions

---

## PHASE 15 — Research Planning Agent
Goal: Help researchers design experiments and plan research.

### Milestone 15.1 — Planning Agent Design
  Task 15.1.1 — Create research planning agent
    Subtask 15.1.1.1 — Create app/agents/planning_agent.py
    Subtask 15.1.1.2 — Implement methodology recommendation
    Subtask 15.1.1.3 — Implement experiment design generation
    Subtask 15.1.1.4 — Implement resource requirement estimation
    Subtask 15.1.1.5 — Generate research timeline
    Subtask 15.1.1.6 — Suggest evaluation metrics

---

## PHASE 16 — LangGraph Workflow
Goal: Orchestrate all agents using LangGraph state machines.

### Milestone 16.1 — LangGraph Concepts
  Task 16.1.1 — Understand LangGraph
    Subtask 16.1.1.1 — What is LangGraph?
    Subtask 16.1.1.2 — State vs Nodes vs Edges
    Subtask 16.1.1.3 — Conditional routing in graphs
    Subtask 16.1.1.4 — When to use LangGraph vs simple chains

### Milestone 16.2 — Research Workflow Graph
  Task 16.2.1 — Design the research workflow state
    Subtask 16.2.1.1 — Define ResearchState TypedDict
    Subtask 16.2.1.2 — Map agent outputs to state fields
    Subtask 16.2.1.3 — Design routing conditions

  Task 16.2.2 — Build LangGraph workflow
    Subtask 16.2.2.1 — Create app/agents/workflow.py
    Subtask 16.2.2.2 — Add upload node
    Subtask 16.2.2.3 — Add parsing node
    Subtask 16.2.2.4 — Add indexing node
    Subtask 16.2.2.5 — Add summarization node
    Subtask 16.2.2.6 — Add gap detection node
    Subtask 16.2.2.7 — Add review generation node
    Subtask 16.2.2.8 — Add conditional routing
    Subtask 16.2.2.9 — Add error handling nodes
    Subtask 16.2.2.10 — Compile and test graph

---

## PHASE 17 — Multi-Agent System
Goal: Enable agents to collaborate on complex research tasks.

### Milestone 17.1 — Agent Communication
  Task 17.1.1 — Design agent communication protocol
    Subtask 17.1.1.1 — Define AgentMessage schema
    Subtask 17.1.1.2 — Create agent registry
    Subtask 17.1.1.3 — Implement agent routing

  Task 17.1.2 — Create orchestrator agent
    Subtask 17.1.2.1 — Create OrchestratorAgent class
    Subtask 17.1.2.2 — Implement task decomposition
    Subtask 17.1.2.3 — Route subtasks to specialist agents
    Subtask 17.1.2.4 — Aggregate results from agents

---

## PHASE 18 — Full FastAPI Backend
Goal: Complete, production-ready API with all endpoints.

### Milestone 18.1 — API Completeness
  Task 18.1.1 — Audit all endpoints
    Subtask 18.1.1.1 — List all endpoints across all routers
    Subtask 18.1.1.2 — Verify consistent response models
    Subtask 18.1.1.3 — Verify consistent error responses
    Subtask 18.1.1.4 — Verify consistent HTTP status codes

  Task 18.1.2 — API versioning
    Subtask 18.1.2.1 — Ensure all routes use /api/v1 prefix
    Subtask 18.1.2.2 — Plan for /api/v2 compatibility

### Milestone 18.2 — API Quality
  Task 18.2.1 — Add middleware
    Subtask 18.2.1.1 — Add CORS middleware
    Subtask 18.2.1.2 — Add request logging middleware
    Subtask 18.2.1.3 — Add request ID middleware

  Task 18.2.2 — Error handling
    Subtask 18.2.2.1 — Create custom exception classes
    Subtask 18.2.2.2 — Create exception handlers
    Subtask 18.2.2.3 — Ensure consistent error response format

  Task 18.2.3 — Performance
    Subtask 18.2.3.1 — Implement response caching
    Subtask 18.2.3.2 — Add database connection pooling
    Subtask 18.2.3.3 — Profile slow endpoints

---

## PHASE 19 — Frontend (Optional v1)
Goal: Basic web interface for ResearchOS.

### Milestone 19.1 — Minimal Frontend
  Task 19.1.1 — Choose frontend approach
    Subtask 19.1.1.1 — Option A: Streamlit (fast, Python)
    Subtask 19.1.1.2 — Option B: React (full-featured)
    Subtask 19.1.1.3 — Decision: Start with Streamlit

  Task 19.1.2 — Build Streamlit interface
    Subtask 19.1.2.1 — Create upload interface
    Subtask 19.1.2.2 — Create paper list view
    Subtask 19.1.2.3 — Create Q&A chat interface
    Subtask 19.1.2.4 — Create summary view
    Subtask 19.1.2.5 — Create literature review interface

---

## PHASE 20 — Authentication
Goal: Secure the API with user authentication.

### Milestone 20.1 — Auth System
  Task 20.1.1 — Implement JWT authentication
    Subtask 20.1.1.1 — Install python-jose
    Subtask 20.1.1.2 — Create User model
    Subtask 20.1.1.3 — Create login endpoint
    Subtask 20.1.1.4 — Create register endpoint
    Subtask 20.1.1.5 — Create JWT token generation
    Subtask 20.1.1.6 — Create JWT verification dependency
    Subtask 20.1.1.7 — Protect all endpoints

---

## PHASE 21 — Docker
Goal: Containerize the entire application.

### Milestone 21.1 — Docker Setup
  Task 21.1.1 — Create Dockerfile
    Subtask 21.1.1.1 — Choose base image (python:3.11-slim)
    Subtask 21.1.1.2 — Set working directory
    Subtask 21.1.1.3 — Copy requirements.txt
    Subtask 21.1.1.4 — Install dependencies
    Subtask 21.1.1.5 — Copy application code
    Subtask 21.1.1.6 — Set entrypoint command
    Subtask 21.1.1.7 — Build and test image

  Task 21.1.2 — Create docker-compose.yml
    Subtask 21.1.2.1 — Add api service
    Subtask 21.1.2.2 — Add volumes for data persistence
    Subtask 21.1.2.3 — Add environment variables
    Subtask 21.1.2.4 — Add port mappings
    Subtask 21.1.2.5 — Test full stack with compose

  Task 21.1.3 — Create .dockerignore
    Subtask 21.1.3.1 — Exclude venv/
    Subtask 21.1.3.2 — Exclude .env
    Subtask 21.1.3.3 — Exclude __pycache__
    Subtask 21.1.3.4 — Exclude tests/

---

## PHASE 22 — Testing
Goal: Achieve 70%+ test coverage across all modules.

### Milestone 22.1 — Test Infrastructure
  Task 22.1.1 — Set up pytest configuration
    Subtask 22.1.1.1 — Create pytest.ini or pyproject.toml config
    Subtask 22.1.1.2 — Configure test discovery
    Subtask 22.1.1.3 — Set up test database (separate from dev)
    Subtask 22.1.1.4 — Create conftest.py with shared fixtures

  Task 22.1.2 — Set up coverage reporting
    Subtask 22.1.2.1 — Install pytest-cov
    Subtask 22.1.2.2 — Configure coverage settings
    Subtask 22.1.2.3 — Generate HTML coverage report
    Subtask 22.1.2.4 — Identify uncovered critical paths

### Milestone 22.2 — Test Coverage
  Task 22.2.1 — Write missing unit tests
  Task 22.2.2 — Write integration tests
  Task 22.2.3 — Write end-to-end tests
  Task 22.2.4 — Achieve 70% overall coverage

---

## PHASE 23 — Deployment
Goal: Deploy ResearchOS to cloud infrastructure.

### Milestone 23.1 — Cloud Deployment
  Task 23.1.1 — Choose deployment platform
    Subtask 23.1.1.1 — Option A: Railway (easiest)
    Subtask 23.1.1.2 — Option B: Render (free tier)
    Subtask 23.1.1.3 — Option C: AWS EC2 (most resume value)

  Task 23.1.2 — Prepare for production
    Subtask 23.1.2.1 — Switch to PostgreSQL
    Subtask 23.1.2.2 — Configure production settings
    Subtask 23.1.2.3 — Set up environment secrets
    Subtask 23.1.2.4 — Configure production logging

---

## PHASE 24 — Optimization
Goal: Make the system faster and more efficient.

### Milestone 24.1 — Performance Optimization
  Task 24.1.1 — Profile API response times
  Task 24.1.2 — Optimize slow endpoints
  Task 24.1.3 — Implement caching layer (Redis)
  Task 24.1.4 — Optimize vector search parameters
  Task 24.1.5 — Implement async PDF processing

---

## PHASE 25 — Production Release
Goal: Complete, polished, portfolio-ready release.

### Milestone 25.1 — Final Polish
  Task 25.1.1 — Final code review
  Task 25.1.2 — Update all documentation
  Task 25.1.3 — Record demo video
  Task 25.1.4 — Write blog post about architecture
  Task 25.1.5 — Create architecture diagrams
  Task 25.1.6 — Final README polish
  Task 25.1.7 — Tag v1.0.0 release

---

## TOTAL ESTIMATED TASKS: ~420
## ESTIMATED COMPLETION TIME: 3–6 months (part-time)
## CURRENT PROGRESS: 2% (Planning Complete)
