# Use official Python image
FROM python:3.10-slim

# Set working directory
WORKDIR /app

# Copy requirements if you have one, else install dependencies manually
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy all code
COPY . .

# Expose port for FastAPI
EXPOSE 8080

# Run FastAPI app
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8080"]