# Dockerfile (최종 버전 - entrypoint.sh 복사 부분 삭제)
FROM python:3.9-slim-buster
RUN mkdir -p /app
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY . /app/
EXPOSE 12345
RUN chmod +x /app/entrypoint.sh 
ENTRYPOINT ["/app/entrypoint.sh"] 