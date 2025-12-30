# from faster_whisper import WhisperModel
# import re

# model = WhisperModel("small", device="cpu", compute_type="int8")

# def transcribe_audio(audio_path: str) -> str:
#     """
#     Transcribe math speech to text
#     """
#     segments, _ = model.transcribe(audio_path)
#     text = " ".join(seg.text for seg in segments)
#     return normalize_math_text(text)


# def normalize_math_text(text: str) -> str:
#     """
#     Normalize spoken math into symbolic math
#     """
#     text = text.lower()

#     replacements = {
#         "equals to": "=",
#         "equal to": "=",
#         "equals": "=",
#         "plus": "+",
#         "minus": "-",
#         "times": "*",
#         "into": "*",
#         "divided by": "/",
#         "square": "^2",
#         "cube": "^3"
#     }

#     for k, v in replacements.items():
#         text = text.replace(k, v)

#     text = re.sub(r"\s+", "", text)
#     return text


from faster_whisper import WhisperModel

model = WhisperModel("small", device="cpu", compute_type="int8")

def transcribe_audio(audio_file):
    segments, _ = model.transcribe(audio_file)
    text = " ".join([seg.text for seg in segments])
    low_confidence = any(seg.avg_logprob < -1.0 for seg in segments)
    return text.strip(), low_confidence
