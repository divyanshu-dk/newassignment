# 🖼️ Image Processor Backend

This project processes image URLs from uploaded CSV files asynchronously and returns compressed versions.

## 🚀 Features
- Upload CSV file with product names and image URLs
- Compress images by 50% and store locally
- Check status via API
- Download result CSV
- Optional webhook support after processing

## 🔧 Tech Stack
- FastAPI
- Celery + Redis
- SQLAlchemy + SQLite
- Pillow (for image compression)
- Pandas (for CSV export)

## 🔄 Setup

```bash
# 1. Install dependencies
pip install -r requirements.txt

# 2. Start Redis
redis-server

# 3. Start FastAPI
uvicorn main:app --reload

# 4. Start Celery worker
celery -A worker.celery_app worker --loglevel=info -Q images
```

## 📬 API Endpoints

- `POST /upload`: Upload CSV (form-data: file, webhook_url)
- `GET /status/{request_id}`: Check processing status
- `GET /download/{request_id}`: Download result CSV

## 🧪 Postman
Import `Image_Processor_API.postman_collection.json` into Postman to test the APIs.
