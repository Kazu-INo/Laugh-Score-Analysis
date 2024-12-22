import argparse
import os
from src.config import configure_api_key, MODEL
from src.video_utils import upload_video
from src.analyzer import HumorVideoAnalysis

def parse_args():
    """コマンドライン引数をパースする"""
    parser = argparse.ArgumentParser(description='動画のユーモア分析を行うプログラム')
    parser.add_argument('video_path', help='分析する動画ファイルのパス')
    return parser.parse_args()

def main():
    args = parse_args()
    
    # 動画ファイルの存在確認
    if not os.path.exists(args.video_path):
        print(f"エラー: 指定されたファイル '{args.video_path}' が見つかりません。")
        return

    # APIキーの設定
    configure_api_key()

    # 解析器の初期化
    humor_analyzer = HumorVideoAnalysis(model=MODEL)

    try:
        # 動画ファイルのアップロード
        print("\n--- 動画をアップロード中 ---\n")
        video_file = upload_video(humor_analyzer.client, args.video_path)

        # 動画解析の実行
        print("\n--- ユーモア解析を開始 ---\n")
        humor_results = humor_analyzer.analyze_video_humor(video_file)

        # 結果の出力
        print("\n--- 解析完了 ---\n")
        print(humor_results)

    except Exception as e:
        print(f"エラーが発生しました: {str(e)}")

if __name__ == "__main__":
    main()
