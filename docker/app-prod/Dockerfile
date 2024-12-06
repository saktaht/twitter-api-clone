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

# エントリーポイントスクリプトをコピー
COPY entrypoint.sh /root/app/src/mysite/
RUN chmod +x /root/app/src/mysite/entrypoint.sh

ENTRYPOINT ["/root/app/src/mysite/entrypoint.sh"]