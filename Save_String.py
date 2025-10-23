# save_string.py
from datetime import datetime

class SaveString:
    """文字起こし結果をREADME.mdに追記保存するクラス"""

    def __init__(self, readme_path="README.md"):
        self.readme_path = readme_path

    def save_to_readme(self, text: str):
        """README.mdに追記（上書きしない）"""
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        formatted_text = (
            f"\n\n### 文字起こし結果（{timestamp}）\n"
            f"{text}\n"
            "---"
        )

        try:
            with open(self.readme_path, "a", encoding="utf-8") as f:
                f.write(formatted_text)
            print(f"✅ README.md に追記しました: {self.readme_path}")
        except Exception as e:
            print(f"⚠️ 書き込みエラー: {e}")
