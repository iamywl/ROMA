# Dockerfile (수정)
FROM python:3.9-slim-buster
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY . /app/
EXPOSE 12345
# CMD는 docker-compose.yml에서 관리하므로 삭제 또는 주석 처리
# CMD sh -c "python manage.py migrate && python manage.py runserver 0.0.0.0:12345"