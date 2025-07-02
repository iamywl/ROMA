# Python
FROM python:3.9-slim-buster

# 컨테이너 내 작업 디렉토리 설정
WORKDIR /app

# Python 의존성 파일 복사 및 설치
# requirements.txt에 파이썬버전 등등 패키키지 버전 정리해둘 것 
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
# Django 프로젝트 파일 복사 (전체 프로젝트 디렉토리 복사)
# .dockerignore 파일에 불필요한 파일(예: .git, .env) 복사예방가능
COPY . /app/
# iamywl 쓰고있는 포트가 많아서 그냥 가장 뜬금 없는 포트사용함
EXPOSE 12345
# 컨테이너 시작 시 Django 개발 서버 실행
CMD ["python", "roma/manage.py", "runserver", "0.0.0.0:12345"]
