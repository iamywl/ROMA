# Dockerfile (최종 버전 - /app 디렉토리 명시적 생성 추가)
FROM python:3.9-slim-buster
WORKDIR /app # WORKDIR은 이후 명령의 작업 디렉토리를 설정.

# --- 이 줄을 새로 추가합니다! ---
RUN mkdir -p /app # /app 디렉토리가 이미 존재하더라도 안전하게 생성

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY . /app/ # 이 명령으로 entrypoint.sh 포함 모든 소스 코드가 /app에 복사됩니다.

EXPOSE 12345

RUN chmod +x /app/entrypoint.sh
ENTRYPOINT ["/app/entrypoint.sh"]