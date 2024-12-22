import os

# モデル設定
MODEL = "gemini-2.0-flash-exp"

def configure_api_key():
    """APIキーを環境変数に設定する"""
    os.environ['GOOGLE_API_KEY'] = ''
