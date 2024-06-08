# data_fetch/Dockerfile
FROM python:3.8-slim

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY fetch_air_quality_data.py .
COPY requirements.txt .

# Upgrade pip and install any needed packages specified in requirements.txt
RUN pip install --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

# Run fetch_air_quality_data.py when the container launches
CMD ["python", "fetch_air_quality_data.py"]
