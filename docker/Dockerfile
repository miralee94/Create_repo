# Use the official Python image as the base image
FROM python:3.11.3-alpine3.17

# Set the working directory
WORKDIR /app

# Copy the requirements file into the container
COPY requirements.txt .

# Install the Python dependencies
RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

# Copy script into the container
COPY ./src .

# Set the entrypoint to file
ENTRYPOINT ["python", "create_repo.py"]