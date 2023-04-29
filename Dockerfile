FROM python:3.11-slim-buster

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY Create_repo.py .

CMD [ "python", "Create_repo.py" ]
