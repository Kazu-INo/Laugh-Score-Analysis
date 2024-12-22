import os
from google import genai
from google.genai import types
from IPython.display import display, Markdown

class HumorVideoAnalysis:
    """動画のユーモア分析を行うクラス"""
    
    def __init__(self, model):
        """
        Args:
            model (str): 使用するGeminiモデルの名前
        """
        self.client = genai.Client(api_key=os.getenv('GOOGLE_API_KEY'))
        self.model = model

    def analyze_video_humor(self, video_file):
        """動画のユーモア分析を実行する

        Args:
            video_file: 分析対象の動画ファイルオブジェクト

        Returns:
            str: 分析結果のテキスト
        """
        prompt = """
        Analyze this video and identify humorous scenes. For each scene, provide:
        - Timecode
        - Description of the humorous element
        - Estimated laughter level (scale of 1 to 10)
        """

        response = self.client.models.generate_content(
            model=self.model,
            contents=[
                types.Content(
                    role="user",
                    parts=[
                        types.Part.from_uri(
                            file_uri=video_file.uri,
                            mime_type=video_file.mime_type
                        ),
                    ]),
                prompt,
            ]
        )

        print("\n--- ユーモア解析結果 ---\n")
        display(Markdown(response.text))
        return response.text
