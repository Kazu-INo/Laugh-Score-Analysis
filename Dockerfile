FROM python:3.10-slim

# Poetryのインストール
RUN pip install poetry

# 作業ディレクトリの設定
WORKDIR /app

# Poetry設定（仮想環境を作成しない）
RUN poetry config virtualenvs.create false

# 依存関係ファイルのコピー
COPY pyproject.toml ./

# 依存関係のインストール
RUN poetry install --only main --no-interaction --no-ansi --no-root

# ソースコードのコピー
COPY . .

# 実行コマンド
CMD ["python", "main.py"]
