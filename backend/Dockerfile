# Pythonの公式イメージをベースとして使用
FROM python:3.11

# ソースディレクトリを作成
WORKDIR /backend

RUN pip install --upgrade pip

# Poetryのインストール
RUN curl -sSL https://install.python-poetry.org | python -

ENV PATH /root/.local/bin:$PATH

RUN poetry config virtualenvs.create false

COPY ./pyproject.toml /backend/pyproject.toml

COPY ./poetry.lock /backend/poetry.lock

RUN poetry install

# ソースコードをコピー
COPY . .

WORKDIR /backend/app

EXPOSE 8001

# コンテナ起動時に実行するコマンドを指定
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--reload", "--port", "8001"]
