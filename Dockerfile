# Use an official Python runtime as a base image
FROM python:3.9-slim

# Add a label for author info
LABEL authors="HP_LAPTOP"

# Set the working directory
WORKDIR /app

# Copy dependency file and install dependencies
COPY requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code
COPY . .

# Expose the port the app runs on
EXPOSE 5000

# Command to run the application
CMD ["python", "app.py"]
