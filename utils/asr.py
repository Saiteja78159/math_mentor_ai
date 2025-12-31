# # # # # # from faster_whisper import WhisperModel
# # # # # # import re

# # # # # # model = WhisperModel("small", device="cpu", compute_type="int8")

# # # # # # def transcribe_audio(audio_path: str) -> str:
# # # # # #     """
# # # # # #     Transcribe math speech to text
# # # # # #     """
# # # # # #     segments, _ = model.transcribe(audio_path)
# # # # # #     text = " ".join(seg.text for seg in segments)
# # # # # #     return normalize_math_text(text)


# # # # # # def normalize_math_text(text: str) -> str:
# # # # # #     """
# # # # # #     Normalize spoken math into symbolic math
# # # # # #     """
# # # # # #     text = text.lower()

# # # # # #     replacements = {
# # # # # #         "equals to": "=",
# # # # # #         "equal to": "=",
# # # # # #         "equals": "=",
# # # # # #         "plus": "+",
# # # # # #         "minus": "-",
# # # # # #         "times": "*",
# # # # # #         "into": "*",
# # # # # #         "divided by": "/",
# # # # # #         "square": "^2",
# # # # # #         "cube": "^3"
# # # # # #     }

# # # # # #     for k, v in replacements.items():
# # # # # #         text = text.replace(k, v)

# # # # # #     text = re.sub(r"\s+", "", text)
# # # # # #     return text


# # # # # from faster_whisper import WhisperModel

# # # # # model = WhisperModel("small", device="cpu", compute_type="int8")

# # # # # def transcribe_audio(audio_file):
# # # # #     segments, _ = model.transcribe(audio_file)
# # # # #     text = " ".join([seg.text for seg in segments])
# # # # #     low_confidence = any(seg.avg_logprob < -1.0 for seg in segments)
# # # # #     return text.strip(), low_confidence


# # # # # utils/asr.py
# # # # import tempfile
# # # # from faster_whisper import WhisperModel

# # # # # Load model once
# # # # model = WhisperModel("small")  # you can choose "tiny", "base", etc.

# # # # def audio_to_text(audio_file):
# # # #     """
# # # #     Convert uploaded audio (mp3/wav) to text using Whisper
# # # #     """
# # # #     with tempfile.NamedTemporaryFile(suffix=".wav") as temp_audio:
# # # #         temp_audio.write(audio_file.read())
# # # #         temp_audio.flush()
# # # #         segments, info = model.transcribe(temp_audio.name)
# # # #         text = " ".join([segment.text for segment in segments])
# # # #     return text


# # # # utils/asr.py
# # # import whisper

# # # model = whisper.load_model("base")

# # # def audio_to_text(audio_file):
# # #     result = model.transcribe(audio_file)
# # #     return result["text"]


# # from faster_whisper import WhisperModel
# # import tempfile

# # model = WhisperModel("small")

# # def transcribe_audio(audio_file):
# #     with tempfile.NamedTemporaryFile(delete=False) as tmp:
# #         tmp.write(audio_file.read())
# #         tmp_path = tmp.name

# #     segments, info = model.transcribe(tmp_path)
# #     text = " ".join([segment.text for segment in segments])
# #     return text


# def transcribe_audio(audio_file):
#     # Replace with your faster-whisper or any STT
#     # For now, simple placeholder:
#     return "x^2 + 4*x + 3 = 0"


from faster_whisper import WhisperModel
import re

model = WhisperModel("small", device="cpu", compute_type="int8")

def transcribe_audio(audio_path: str) -> str:
    """
    Transcribe math speech to text
    """
    segments, _ = model.transcribe(audio_path)
    text = " ".join(seg.text for seg in segments)
    return normalize_math_text(text)


def normalize_math_text(text: str) -> str:
    """
    Normalize spoken math into symbolic math
    """
    text = text.lower()

    replacements = {
        "equals to": "=",
        "equal to": "=",
        "equals": "=",
        "plus": "+",
        "minus": "-",
        "times": "*",
        "into": "*",
        "divided by": "/",
        "square": "^2",
        "cube": "^3"
    }

    for k, v in replacements.items():
        text = text.replace(k, v)

    text = re.sub(r"\s+", "", text)
    return text
