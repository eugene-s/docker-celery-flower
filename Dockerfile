FROM python:3.6-alpine3.8

ENV PYTHONUNBUFFERED true

RUN apk -U --no-cache add build-base --virtual build-dependencies && \
    pip install --no-cache-dir requests celery flower && \
    apk del build-dependencies

EXPOSE 5555

ENTRYPOINT ["celery", "flower"]
