
# import streamlit as st
# from PIL import Image
# import tempfile

# # =========================
# # AGENTS
# # =========================
# from agents.parser_agent import parse_input
# from agents.solver_agent import solve_problem
# from agents.verifier_agent import verify_solution

# # =========================
# # UTILS
# # =========================
# from utils.ocr import extract_text_from_image
# from utils.asr import transcribe_audio
# from utils.rag import retrieve_context

# # =========================
# # MEMORY
# # =========================
# from memory.memory_store import add_memory, retrieve_similar


# # =========================
# # PAGE CONFIG
# # =========================
# st.set_page_config(page_title="Math Mentor AI", layout="centered")
# st.title("🧠 Math Mentor AI")
# st.caption("Reliable Multimodal Math Mentor (RAG + Agents + HITL + Memory)")


# # =========================
# # INPUT MODE
# # =========================
# input_mode = st.radio(
#     "Select Input Type:",
#     ["Text", "Image", "Audio"]
# )

# final_input = ""


# # =========================
# # TEXT INPUT
# # =========================
# if input_mode == "Text":
#     final_input = st.text_area(
#         "Enter a math problem:",
#         placeholder="e.g., solve x^2 - 5x + 6 = 0"
#     )


# # =========================
# # IMAGE INPUT (OCR)
# # =========================
# elif input_mode == "Image":
#     image_file = st.file_uploader(
#         "Upload a math problem image (JPG / PNG)",
#         type=["jpg", "png"]
#     )

#     if image_file:
#         image = Image.open(image_file)
#         st.image(image, caption="Uploaded Image", use_column_width=True)

#         ocr_text, confidence = extract_text_from_image(image)

#         if confidence < 0.6:
#             st.warning("⚠️ OCR confidence is low. Please verify or correct the text.")

#         final_input = st.text_area(
#             "OCR Extracted Text (Edit if needed):",
#             value=ocr_text
#         )


# # =========================
# # AUDIO INPUT (ASR)
# # =========================
# elif input_mode == "Audio":
#     audio_file = st.file_uploader(
#         "Upload audio file (wav / mp3)",
#         type=["wav", "mp3"]
#     )

#     if audio_file:
#         with tempfile.NamedTemporaryFile(delete=False, suffix=".wav") as tmp:
#             tmp.write(audio_file.read())
#             audio_path = tmp.name

#         transcript = transcribe_audio(audio_path)

#         st.info("Please verify the transcription below:")
#         final_input = st.text_area(
#             "Transcribed Math Question:",
#             value=transcript
#         )


# # =========================
# # SOLVE BUTTON
# # =========================
# if st.button("Solve"):
#     if not final_input.strip():
#         st.warning("Please provide a math problem first.")
#         st.stop()

#     # ---------- PARSER ----------
#     parsed = parse_input(final_input)

#     st.subheader("🧩 Parsed Problem")
#     st.json(parsed)

#     if parsed["needs_clarification"]:
#         st.warning("❓ Problem needs clarification before solving.")
#         st.stop()

#     # ---------- MEMORY LOOKUP ----------
#     past = retrieve_similar(parsed["problem_text"])

#     if past:
#         st.info("🧠 Similar problem found in memory. Reusing solution.")

#         solution = past["solution"]
#         verification = {
#             "verified": past["verified"],
#             "confidence": past["confidence"],
#             "reason": "Reused from memory",
#             "needs_hitl": False
#         }

#     else:
#         # ---------- RAG ----------
#         retrieved_context = retrieve_context(parsed["problem_text"])

#         # ---------- SOLVER ----------
#         solution = solve_problem(parsed["problem_text"])

#         # ---------- VERIFIER ----------
#         verification = verify_solution(parsed, solution)

#     # ---------- OUTPUT ----------
#     st.subheader("✅ Solution")
#     st.text(solution)

#     st.subheader("🔍 Verification")
#     st.write(f"✔️ Verified: **{verification['verified']}**")
#     st.write(f"📊 Confidence: **{verification['confidence']}**")
#     st.write(f"🧠 Reason: {verification['reason']}")

#     # ---------- HITL ----------
#     if verification["needs_hitl"]:
#         st.warning("⚠️ Human review required")

#         corrected_solution = st.text_area(
#             "Edit / correct the solution:",
#             value=solution
#         )

#         if st.button("Approve Correction"):
#             st.success("✔️ Correction approved and saved to memory")

#             add_memory({
#                 "input": final_input,
#                 "parsed": parsed,
#                 "solution": corrected_solution,
#                 "verified": True,
#                 "confidence": 1.0,
#                 "feedback": "human_corrected"
#             })

#             st.stop()

#     else:
#         st.success("✔️ Solution verified automatically")

#         # ---------- SAVE TO MEMORY ----------
#         add_memory({
#             "input": final_input,
#             "parsed": parsed,
#             "solution": solution,
#             "verified": verification["verified"],
#             "confidence": verification["confidence"],
#             "feedback": "correct"
#         })

#     # ---------- RAG DISPLAY ----------
#     st.subheader("📚 Retrieved Knowledge (RAG)")
#     st.text(retrieve_context(parsed["problem_text"]))


import streamlit as st
from utils.ocr import extract_text_from_image
from utils.asr import transcribe_audio
from agents.parser_agent import parse_input
from agents.intent_router import route_intent
from agents.solver_agent import solve_problem
from agents.verifier_agent import verify_solution
from utils.rag import retrieve_context
from memory.memory_store import save_to_memory

st.set_page_config("Math Mentor AI")
st.title("🧠 Math Mentor AI")

mode = st.selectbox("Select Input Type", ["Text", "Image", "Audio"])

question = ""

if mode == "Text":
    question = st.text_area("Enter math problem")

elif mode == "Image":
    img = st.file_uploader("Upload image", type=["png", "jpg"])
    if img:
        question = extract_text_from_image(img)
        question = st.text_area("OCR Text", question)

elif mode == "Audio":
    audio = st.file_uploader("Upload audio", type=["wav", "mp3"])
    if audio:
        question, low = transcribe_audio(audio)
        if low:
            st.warning("Low confidence transcription")
        question = st.text_area("Transcript", question)

if st.button("Solve"):
    parsed = parse_input(question)
    intent = route_intent(parsed)
    context = retrieve_context(parsed["problem_text"])
    solution = solve_problem(parsed["problem_text"])
    ok, status = verify_solution(solution)

    st.subheader("✅ Solution")
    st.write(solution)

    st.subheader("📚 Retrieved Knowledge")
    st.write(context)

    save_to_memory({
        "question": question,
        "solution": solution,
        "verified": ok
    })
