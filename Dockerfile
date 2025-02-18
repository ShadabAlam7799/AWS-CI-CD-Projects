FROM python:3.8-slim-buster
WORKDIR /app
COPY app.py /app/
COPY templates /app/templates/
COPY requirements.txt /app/requirements.txt

RUN apt update -y && apt install awscli -y

RUN apt-get update && apt-get install ffmpeg libsm6 libxext6 unzip -y && pip install -r requirements.txt
CMD ["python3", "app.py"]
