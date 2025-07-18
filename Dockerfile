# Dockerfile (수정 후 최종 버전 - entrypoint.sh를 /app 에 직접 복사)
FROM python:3.9-slim-buster
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY . /app/ # 이 명령으로 entrypoint.sh 포함 모든 소스 코드가 /app에 복사됩니다.

EXPOSE 12345

# entrypoint.sh 파일을 /app 디렉토리로 복사 (이전 COPY . /app/가 이미 처리하므로 불필요할 수 있지만, 명시적으로 유지)
# COPY entrypoint.sh /app/ # <-- 이 줄을 이렇게 변경하면 좋음. 하지만 COPY . /app/가 이미 처리함.
# 최신 Jenkinsfile은 Dockerfile의 COPY . /app/가 entrypoint.sh를 포함한다고 가정하므로,
# 아래 RUN chmod 와 ENTRYPOINT를 /app/ 경로로 변경하는 것이 핵심.
RUN chmod +x /app/entrypoint.sh 

# ENTRYPOINT를 사용하여 스크립트 실행
ENTRYPOINT ["/app/entrypoint.sh"]