# transcriber.py
from pydub import AudioSegment
import numpy as np
import mlx_whisper

def preprocess_audio(sound: AudioSegment) -> AudioSegment:
    """音声データをWhisper入力用に整形"""
    if sound.frame_rate != 16000:
        sound = sound.set_frame_rate(16000)
    if sound.sample_width != 2:
        sound = sound.set_sample_width(2)
    if sound.channels != 1:
        sound = sound.set_channels(1)
    return sound


def transcribe_audio(audio_input):
    """
    音声ファイルまたはAudioSegmentを受け取り文字起こし結果を返す関数。

    Parameters
    ----------
    audio_input : str | AudioSegment
        音声ファイルパス、またはpydub.AudioSegment。

    Returns
    -------
    str
        文字起こし結果のテキスト。
    """
    if isinstance(audio_input, str):
        result = mlx_whisper.transcribe(audio_input, path_or_hf_repo="whisper-base-mlx")
        return result["text"]

    elif isinstance(audio_input, AudioSegment):
        sound = preprocess_audio(audio_input)
        arr = np.array(sound.get_array_of_samples()).astype(np.float32) / 32768.0
        result = mlx_whisper.transcribe(arr, path_or_hf_repo="whisper-base-mlx")
        return result["text"]

    else:
        raise TypeError("audio_input must be a file path or AudioSegment.")


if __name__ == "__main__":
    # 動作確認用
    text = transcribe_audio("python-audio-output.wav")
    print(text)
