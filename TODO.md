docker build -t roma .

docker run -p 12345:12345 --name roma -v "$(pwd):/app" roma


### 잘 못 된 빌 드 했 을 경 우 이 미 지 삭 제 하 는 명 령 어
# docker rm roma

