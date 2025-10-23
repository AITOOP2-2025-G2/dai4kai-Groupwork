from pydub import AudioSegment

# WAVファイルを読み込む
# from_wav()の代わりに、from_file()を使って様々な形式のファイルを読み込むこともできます。
audio = AudioSegment.from_file("python-audio-output.wav", format="wav")

# pydubは時間をミリ秒単位で扱う
end_ms= 4000
extracted_audio = audio[:end_ms]

# 抽出した部分を新しいファイルとしてエクスポート
extracted_audio.export("audio-output-before.wav", format="wav")

# 4秒以降の範囲を抽出（4000msから）
start_ms=4000
extracted_audio = audio[start_ms:]

# 抽出した部分を新しいファイルとしてエクスポート
extracted_audio.export("audio-output-after.wav", format="wav")

print("音声が4秒前後でスライスされ、wavとして保存されました。")