FROM python:3.8.16 

LABEL maintainer="Aghiles IZOUAOUEN, Fraoucen KACI, Claas HAMAIDI"

WORKDIR /app

COPY entrypoint.sh requirements.txt  /app/

RUN pip install --upgrade pip \
    && pip install -r requirements.txt 

RUN chmod +x entrypoint.sh

ENTRYPOINT /app/entrypoint.sh
