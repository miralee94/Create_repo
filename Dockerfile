FROM python:3.11.3-alpine3.17

# Set the working directory
WORKDIR /app

# Copy the requirements file into the container
COPY requirements.txt .

# Install the Python dependencies
RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

# Copy script into the container
COPY Create_repo.py .

# Set the entrypoint to file
ENTRYPOINT ["python", "Create_repo.py"]