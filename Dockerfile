FROM python:3.10-alpine

ENV PYTHONUNBUFFERED 1

COPY requirements.txt ./

RUN apk update
RUN apk add --no-cache --virtual .tmp-build-deps gcc libffi-dev musl-dev && pip install cython \
&& pip install cffi && pip install --no-cache-dir -r requirements.txt
RUN apk del .tmp-build-deps

RUN mkdir /app
COPY . /app
WORKDIR /app

CMD ["python", "app.py"]