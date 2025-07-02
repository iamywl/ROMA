docker build -t roma .

docker run -p 12345:12345 --name roma -v "$(pwd):/app" roma

