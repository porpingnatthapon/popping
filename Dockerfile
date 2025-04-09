# Use an official Python image
FROM python:3.11-slim

# Set the working directory
WORKDIR /app

# Copy the Python script into the container
COPY main.py .

# Run the script when the container starts
CMD ["python", "main.py"]
