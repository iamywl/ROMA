docker build -t roma:1.0 .

docker run -d -p 12345:12345 --name roma -v "$(pwd):/app" roma:1.0 bash -c " \
  if [ ! -f manage.py ]; then \
    django-admin startproject roma .; \
  fi && \
  python manage.py migrate && \
  exec python manage.py runserver 0.0.0.0:12345 >> local.log 2>&1 \
"

##### 잘 못 된 빌 드 했 을 경 우 이 미 지 삭 제 하 는 명 령 어
##### docker rm roma
##### docker rmi roma:latest

##### 아래 명령어 실행해서 각자의 로커 로그는 무시하는걸로
```shell
echo "local.log" >> .gitignore

```
