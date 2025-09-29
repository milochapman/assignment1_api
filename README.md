# Assignment 1 API

This is the implementation for **Assignment 1 (Modules 1–3)**.  
It includes:
- A **Bigram Text Generator API** (Module 1 & 3)
- A **Word Embedding API using spaCy** (Module 2 integration)
- Docker deployment support

---

## 📂 Project Structure
assignment1_api/
├── app/
│ ├── init.py
│ ├── main.py # FastAPI app entrypoint
│ ├── bigram_model.py # Bigram model implementation
│ └── spacy_service.py # spaCy embedding service
├── requirements.txt # Dependencies
├── Dockerfile # Docker configuration
├── .dockerignore # Ignore unnecessary files in Docker
└── README.md # Documentation

yaml
Copy code

---

## 🚀 Running Locally

### 1. Install dependencies
```bash
uv pip install -r requirements.txt
2. Run the FastAPI server
bash
Copy code
uv run uvicorn app.main:app --reload
3. Access the API
Root health check: http://127.0.0.1:8000

Swagger UI: http://127.0.0.1:8000/docs

📡 API Endpoints
POST /generate
Generate text using the bigram model.

Request body:

json
Copy code
{
  "start_word": "the",
  "length": 5
}
Response:

json
Copy code
{
  "generated_text": "the count of monte cristo"
}
POST /embed
Get the embedding vector of a word using spaCy.

Request body:

json
Copy code
{
  "word": "analytics"
}
Response:

json
Copy code
{
  "word": "analytics",
  "dim": 300,
  "vector": [0.123, -0.456, ...]
}
🐳 Docker Deployment
This project can also be run inside a Docker container.

1. Build the Docker image
From the project root directory, run:

bash
Copy code
docker build -t assignment1-api .
2. Run the container
bash
Copy code
docker run -p 8000:80 assignment1-api
This will map the container’s port 80 to your local port 8000.

3. Access the API
Once the container is running, open your browser and visit:

Swagger UI: http://127.0.0.1:8000/docs

Root health check: http://127.0.0.1:8000

4. Example requests
Generate text:

bash
Copy code
curl -X POST "http://127.0.0.1:8000/generate" \
  -H "Content-Type: application/json" \
  -d '{"start_word": "the", "length": 5}'
Get word embedding:

bash
Copy code
curl -X POST "http://127.0.0.1:8000/embed" \
  -H "Content-Type: application/json" \
  -d '{"word": "analytics"}'