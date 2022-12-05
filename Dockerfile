FROM python:3.10-slim
ENV PYTHONUNBUFFERED 1
RUN apt update && \
    apt install -y default-libmysqlclient-dev gcc libmariadb-dev
RUN mkdir /code
WORKDIR /code
COPY requirements.txt /code/
RUN pip install --upgrade pip && pip install -r requirements.txt
COPY . /code/
