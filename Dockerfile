FROM python:3.9-slim-buster
RUN mkdir -p /app
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY . /app/ 
EXPOSE 12345
RUN echo '#!/bin/sh' > /app/entrypoint.sh && \
    echo 'echo "Running database migrations..."' >> /app/entrypoint.sh && \
    echo 'python manage.py migrate || exit 1' >> /app/entrypoint.sh && \
    echo 'echo "Starting Roma app server..."' >> /app/entrypoint.sh && \
    echo 'exec python manage.py runserver 0.0.0.0:12345' >> /app/entrypoint.sh && \
    chmod +x /app/entrypoint.sh # 생성 후 바로 실행 권한 부여
ENTRYPOINT ["/app/entrypoint.sh"]