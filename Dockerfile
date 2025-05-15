# Use official Python image based on Ubuntu
FROM python:3.11-slim

# Install system dependencies
RUN apt-get update && apt-get install -y \
    g++ \
    gcc \
    libgdal-dev \
    libpq-dev \
    python3-dev \
    && apt-get clean

# Set environment variables for GDAL
ENV CPLUS_INCLUDE_PATH=/usr/include/gdal
ENV C_INCLUDE_PATH=/usr/include/gdal

# Install Python dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Install system dependencies
# NOTE this is needed to be performed as 
# workaround for pq
RUN apt-get update \
    && apt-get clean

# Copy application code
COPY . /app
WORKDIR /app

CMD ["python", "app.py"]
