import time

def upload_video(client, video_file_name):
    """動画ファイルをアップロードし、処理が完了するまで待機する

    Args:
        client: Gemini APIクライアント
        video_file_name (str): アップロードする動画ファイルのパス

    Returns:
        video_file: アップロードされた動画ファイルオブジェクト

    Raises:
        ValueError: 動画の処理が失敗した場合
    """
    video_file = client.files.upload(path=video_file_name)

    while video_file.state == "PROCESSING":
        print('Waiting for video to be processed.')
        time.sleep(10)
        video_file = client.files.get(name=video_file.name)

    if video_file.state == "FAILED":
        raise ValueError(video_file.state)
    print(f'Video processing complete: ' + video_file.uri)

    return video_file
