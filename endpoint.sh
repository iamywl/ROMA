# entrypoint.sh (ROMA 프로젝트 루트에 생성)
#!/bin/sh

echo "Running database migrations..."
# 마이그레이션 명령 실행. 오류 발생 시 컨테이너가 즉시 종료되지 않도록 '|| exit 1' 추가 (선택 사항)
python manage.py migrate || exit 1

echo "Starting Roma app server..."
# 'exec' 명령을 사용하여 현재 쉘 프로세스를 웹 서버 프로세스로 교체합니다.
# 이렇게 해야 웹 서버가 컨테이너의 메인 프로세스가 되어 포그라운드에서 계속 실행됩니다.
exec python manage.py runserver 0.0.0.0:12345