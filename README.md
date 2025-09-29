# Assignment 1 API

This is the implementation for **Assignment 1 (Modules 1–3)** in APAN 5560.  
It demonstrates:

- ✅ **Bigram Text Generator API** (Modules 1 & 3)  
- ✅ **Word Embedding API** using spaCy (Module 2 integration)  
- ✅ **Docker deployment support** for containerized execution  

---

## 📂 Project Structure

```
assignment1_api/
├── app/
│   ├── __init__.py
│   ├── main.py          # FastAPI app entrypoint
│   ├── bigram_model.py  # Bigram model implementation
│   └── spacy_service.py # spaCy embedding service
├── requirements.txt     # Dependencies
├── Dockerfile           # Docker configuration
├── .dockerignore        # Ignore unnecessary files in Docker build
├── uv.lock              # Lockfile (if using uv)
├── pyproject.toml       # Project config (optional)
└── README.md            # Documentation
```

---

## 🚀 Running Locally

### 1. Install dependencies
```bash
uv pip install -r requirements.txt
```

### 2. Start the FastAPI server
```bash
uv run uvicorn app.main:app --reload
```

### 3. Access the API
- Health check: [http://127.0.0.1:8000](http://127.0.0.1:8000)  
- Swagger UI: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)  

---

## 📡 API Endpoints

### **POST /generate**
Generate text using the bigram model.

**Request body:**
```json
{
  "start_word": "the",
  "length": 5
}
```

**Response:**
```json
{
  "generated_text": "the count of monte cristo"
}
```

---

### **POST /embed**
Get the embedding vector of a word using **spaCy embeddings**.

**Request body:**
```json
{
  "word": "analytics"
}
```

**Response (truncated):**
```json
{
  "word": "analytics",
  "dim": 300,
  "vector": [0.124, -0.932, 0.581, ...]
}
```

---

## 🐳 Docker Deployment

This project can also run inside a **Docker container**.

### 1. Build the Docker image
```bash
docker build -t assignment1-api .
```

### 2. Run the container
```bash
docker run -p 8000:80 assignment1-api
```

This maps container port **80 → local port 8000**.

### 3. Access the API
- Swagger UI: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)  
- Health check: [http://127.0.0.1:8000](http://127.0.0.1:8000)  

### 4. Example requests

**Generate text:**
```bash
curl -X POST "http://127.0.0.1:8000/generate"   -H "Content-Type: application/json"   -d '{"start_word": "the", "length": 5}'
```

**Get word embedding:**
```bash
curl -X POST "http://127.0.0.1:8000/embed"   -H "Content-Type: application/json"   -d '{"word": "analytics"}'
```

---

## 🛠 Notes
- Requires Python **3.11** (compatible with spaCy model `en_core_web_md==3.7.1`).  
- If running locally, ensure the spaCy model is installed:  
  ```bash
  uv run python -m spacy download en_core_web_md
  ```
- Docker build installs all required dependencies automatically.

---

## 📑 License
For academic use only – Columbia University APAN 5560 Assignment.
