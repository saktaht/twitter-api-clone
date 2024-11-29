FROM python:3.12

ENV PYTHONUNBUFFERED=1

RUN mkdir -p /root/app

WORKDIR /root/app

RUN pip install --upgrade pip \
    && pip install --upgrade setuptools \
    && pip install poetry \
    && poetry config virtualenvs.create false 

COPY pyproject.toml poetry.lock /root/app/

RUN poetry install

COPY src /root/app/src

WORKDIR /root/app/src/mysite

CMD ["gunicorn", "--bind", "0.0.0.0:8080", "mysite.wsgi:application"]