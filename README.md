# Laugh Score Analysis

動画内の笑いやユーモアのある場面を分析し、スコアリングを行うツールです。Google Gemini 2.0を使用して、動画内の面白い場面を検出し、その強度を評価します。

## 機能

- 動画ファイルのアップロードと解析
- 笑いを含むシーンの検出
- タイムコードごとの笑いの強度評価（1-10スケール）
- シーンの説明と分析結果の出力

## 必要条件

- Python 3.9以上
- Poetry（依存関係管理）
- Docker（オプション）
- Google API Key（Gemini APIアクセス用）

## セットアップ

### 1. リポジトリのクローン

```bash
git clone [repository-url]
cd laugh-score-analysis
```

### 2. Google API Keyの設定

`src/config.py`の`YOUR_API_KEY_HERE`を実際のGoogle API Keyに置き換えてください。

### 3. Poetryを使用したセットアップ

```bash
# 依存関係のインストール
poetry install
```

### 4. Dockerを使用したセットアップ（オプション）

```bash
# Dockerイメージのビルド
docker build -t laugh-score .
```

## 使用方法

### Poetryを使用する場合

```bash
poetry run python main.py path/to/your/video.mp4
```

### Dockerを使用する場合

```bash
# 動画ファイルがカレントディレクトリにある場合
docker run -v $(pwd):/app laugh-score python main.py /app/video.mp4

# 動画ファイルが input ディレクトリにある場合
docker run -v $(pwd):/app laugh-score python main.py /app/input/video.mp4
```

## 出力例

```
--- 動画をアップロード中 ---

Video processing complete: [video-uri]

--- ユーモア解析を開始 ---

[タイムコード] シーンの説明
笑いレベル: X/10

--- 解析完了 ---
```

## プロジェクト構造

```
laugh-score-analysis/
├── src/
│   ├── config.py      # 設定関連
│   ├── video_utils.py # 動画アップロード機能
│   └── analyzer.py    # ユーモア分析クラス
├── main.py            # メインスクリプト
├── pyproject.toml     # Poetry設定
├── Dockerfile         # Docker設定
└── README.md         # このファイル
```

## ライセンス

このプロジェクトはMITライセンスの下で公開されています。詳細は[LICENSE](LICENSE)ファイルを参照してください。
