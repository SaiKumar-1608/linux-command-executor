# ============================
# Base Image
# ============================
FROM python:3.11-slim

# ============================
# Environment Variables
# ============================
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# ============================
# Set Working Directory
# ============================
WORKDIR /app

# ============================
# Install System Dependencies
# ============================
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

# ============================
# Copy Requirements First (for caching)
# ============================
COPY requirements.txt .

RUN pip install --no-cache-dir --upgrade pip \
    && pip install --no-cache-dir -r requirements.txt

# ============================
# Copy Application Code
# ============================
COPY app ./app
COPY .env .env

# ============================
# Create Non-Root User (Security Best Practice)
# ============================
RUN useradd -m appuser
USER appuser

# ============================
# Expose Port
# ============================
EXPOSE 8000

# ============================
# Run Application
# ============================
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]