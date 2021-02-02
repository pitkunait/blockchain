FROM python:3.7-slim-buster

COPY . /app
WORKDIR /app

RUN pip3 install -r requirements.txt

ENTRYPOINT ["python", "app.py"]