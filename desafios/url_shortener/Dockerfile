# # Base on offical Python Slim image
FROM python:3.10-slim

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONOPTIMIZE=1 \
    PYTHONUNBUFFERED=1

# Set working directory
WORKDIR /app

# Install dependencies with poetry
RUN apt-get update && apt-get install -y \
    build-essential \
    gettext \
    libpq-dev \
    libcurl4-openssl-dev \
    libssl-dev

#

# Copy all files
COPY . .

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

CMD ["uvicorn", "app:shortener_api", "--host", "0.0.0.0", "--port", "8000" , "--reload"]
