FROM continuumio/miniconda3
MAINTAINER Markus Lippus <markus.lippus@mindtitan.com>

EXPOSE 5000

COPY . /app
WORKDIR /app

RUN pip install -r requirements.txt

CMD ["python3", "./main.py"]
