#!/bin/bash

# Activate the virtual environment
#source /app/venv/bin/activate

# Start the FastAPI app in the background
uvicorn src.api:app --host 0.0.0.0 --port 8000 &

# Start the Streamlit app
streamlit run front.py --server.port 8501 --server.address 0.0.0.0