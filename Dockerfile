# Dockerfile (수정 후)
# FROM python:3.9-slim-buster
# WORKDIR /app
# COPY requirements.txt .
# RUN pip install --no-cache-dir -r requirements.txt
# COPY . /app/
# EXPOSE 12345 # 컨테이너 내부 포트. 중요: 이 포트로 리스닝하도록 CMD/ENTRYPOINT 설정!
# CMD sh -c "python manage.py migrate && python manage.py runserver 0.0.0.0:12345"

# Dockerfile (수정 후 최종 버전 - entrypoint.sh 사용)
FROM python:3.9-slim-buster
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY . /app/
EXPOSE 12345

# 새로 추가된 entrypoint.sh 파일을 컨테이너에 복사하고 실행 권한 부여
COPY entrypoint.sh /usr/local/bin/entrypoint.sh
RUN chmod +x /usr/local/bin/entrypoint.sh

# ENTRYPOINT를 사용하여 스크립트 실행 (CMD 대신 사용)
ENTRYPOINT ["/usr/local/bin/entrypoint.sh"] # <-- 이 줄로 변경합니다!
# 기존 CMD 라인은 삭제하거나 주석 처리 유지 (더 이상 사용되지 않음)
# CMD sh -c "python manage.py migrate && python manage.py runserver 0.0.0.0:12345"