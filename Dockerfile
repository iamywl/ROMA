# Dockerfile (수정 후)
FROM python:3.9-slim-buster
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY . /app/
EXPOSE 12345 # 컨테이너 내부 포트. 중요: 이 포트로 리스닝하도록 CMD/ENTRYPOINT 설정!
CMD sh -c "python manage.py migrate && python manage.py runserver 0.0.0.0:12345"