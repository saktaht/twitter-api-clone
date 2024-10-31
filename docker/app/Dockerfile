FROM python:3.12

ENV PYTHONUNBUFFERED 1

RUN mkdir -p /root/app

WORKDIR /root/app

RUN pip install --upgrade pip \
    && pip install --upgrade setuptools \
    && pip install poetry \
    # poetryの仮想環境に入らないようにする
    && poetry config virtualenvs.create false 

COPY ./pyproject.toml ./poetry.lock* /root/app/

RUN poetry install