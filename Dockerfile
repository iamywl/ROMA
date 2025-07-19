FROM python:3.9-slim-buster
RUN mkdir -p /app
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY entrypoint.sh .
COPY . /app/ 
EXPOSE 12345
RUN chmod +x ./entrypoint.sh
ENTRYPOINT ["./entrypoint.sh"]