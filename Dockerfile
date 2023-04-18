FROM python:3.11
MAINTAINER Aktan Ishenkulov

WORKDIR /app

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .

CMD ["python", "main.py"]