FROM python:latest
WORKDIR /app
COPY requirements.txt .
COPY src/api/ .
RUN pip install --no-cache-dir -r requirements.txt
EXPOSE 8000
CMD ["python", "main.py"]
