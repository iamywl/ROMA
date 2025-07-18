# Dockerfile (최종 버전 - entrypoint.sh 복사 부분 삭제)
FROM python:3.9-slim-buster

RUN mkdir -p /app
WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
# COPY . /app/ # 이 명령은 다시 사용하지 않습니다. (이것도 잠재적 문제의 소지)

# --- 이 두 줄을 삭제합니다! ---
# COPY entrypoint.sh /app/entrypoint.sh 

EXPOSE 12345

# --- 아래 두 줄은 유지합니다. 하지만 스크립트는 Jenkinsfile이 생성해 줄 것입니다. ---
RUN chmod +x /app/entrypoint.sh # 여전히 /app/entrypoint.sh 에 실행 권한이 필요
ENTRYPOINT ["/app/entrypoint.sh"] # 여전히 /app/entrypoint.sh를 실행하도록 설정