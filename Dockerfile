FROM python:3.13-slim

WORKDIR /AI_Agent_Research_Assistant
COPY . .
RUN pip install --no-cache-dir -r requirements.txt

CMD ["python", "main:app", "--host", "0.0.0.0", "--port", "8000"]
