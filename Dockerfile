# Use an official Python runtime as a parent image
FROM python:3.10-slim

# Set the working directory in the container
WORKDIR /app

# Copy only the necessary files
COPY lib /app/lib
COPY main.py /app/
COPY requirements.txt /app/

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r /app/requirements.txt

# Expose the port on which FastAPI will run
EXPOSE 8000

# Run the FastAPI service
CMD ["python", "main.py"]