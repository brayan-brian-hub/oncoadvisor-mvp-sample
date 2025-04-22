
# OncoAdvisor MVP Sample

This is a minimal proof-of-concept for an oncology chatbot web application.

## Stack
- Backend: FastAPI
- Frontend: Placeholder
- AI: GPT-2 via Hugging Face Transformers

## Running the Backend
```bash
cd backend
pip install -r requirements.txt
uvicorn main:app --reload
```

## Training
```bash
cd training
python train_model.py
```

## Sample Data
See `sample_dataset.json` for example format.
