
# # # # # # # # # # # # # # import streamlit as st
# # # # # # # # # # # # # # from PIL import Image
# # # # # # # # # # # # # # import tempfile

# # # # # # # # # # # # # # # =========================
# # # # # # # # # # # # # # # AGENTS
# # # # # # # # # # # # # # # =========================
# # # # # # # # # # # # # # from agents.parser_agent import parse_input
# # # # # # # # # # # # # # from agents.solver_agent import solve_problem
# # # # # # # # # # # # # # from agents.verifier_agent import verify_solution

# # # # # # # # # # # # # # # =========================
# # # # # # # # # # # # # # # UTILS
# # # # # # # # # # # # # # # =========================
# # # # # # # # # # # # # # from utils.ocr import extract_text_from_image
# # # # # # # # # # # # # # from utils.asr import transcribe_audio
# # # # # # # # # # # # # # from utils.rag import retrieve_context

# # # # # # # # # # # # # # # =========================
# # # # # # # # # # # # # # # MEMORY
# # # # # # # # # # # # # # # =========================
# # # # # # # # # # # # # # from memory.memory_store import add_memory, retrieve_similar


# # # # # # # # # # # # # # # =========================
# # # # # # # # # # # # # # # PAGE CONFIG
# # # # # # # # # # # # # # # =========================
# # # # # # # # # # # # # # st.set_page_config(page_title="Math Mentor AI", layout="centered")
# # # # # # # # # # # # # # st.title("🧠 Math Mentor AI")
# # # # # # # # # # # # # # st.caption("Reliable Multimodal Math Mentor (RAG + Agents + HITL + Memory)")


# # # # # # # # # # # # # # # =========================
# # # # # # # # # # # # # # # INPUT MODE
# # # # # # # # # # # # # # # =========================
# # # # # # # # # # # # # # input_mode = st.radio(
# # # # # # # # # # # # # #     "Select Input Type:",
# # # # # # # # # # # # # #     ["Text", "Image", "Audio"]
# # # # # # # # # # # # # # )

# # # # # # # # # # # # # # final_input = ""


# # # # # # # # # # # # # # # =========================
# # # # # # # # # # # # # # # TEXT INPUT
# # # # # # # # # # # # # # # =========================
# # # # # # # # # # # # # # if input_mode == "Text":
# # # # # # # # # # # # # #     final_input = st.text_area(
# # # # # # # # # # # # # #         "Enter a math problem:",
# # # # # # # # # # # # # #         placeholder="e.g., solve x^2 - 5x + 6 = 0"
# # # # # # # # # # # # # #     )


# # # # # # # # # # # # # # # =========================
# # # # # # # # # # # # # # # IMAGE INPUT (OCR)
# # # # # # # # # # # # # # # =========================
# # # # # # # # # # # # # # elif input_mode == "Image":
# # # # # # # # # # # # # #     image_file = st.file_uploader(
# # # # # # # # # # # # # #         "Upload a math problem image (JPG / PNG)",
# # # # # # # # # # # # # #         type=["jpg", "png"]
# # # # # # # # # # # # # #     )

# # # # # # # # # # # # # #     if image_file:
# # # # # # # # # # # # # #         image = Image.open(image_file)
# # # # # # # # # # # # # #         st.image(image, caption="Uploaded Image", use_column_width=True)

# # # # # # # # # # # # # #         ocr_text, confidence = extract_text_from_image(image)

# # # # # # # # # # # # # #         if confidence < 0.6:
# # # # # # # # # # # # # #             st.warning("⚠️ OCR confidence is low. Please verify or correct the text.")

# # # # # # # # # # # # # #         final_input = st.text_area(
# # # # # # # # # # # # # #             "OCR Extracted Text (Edit if needed):",
# # # # # # # # # # # # # #             value=ocr_text
# # # # # # # # # # # # # #         )


# # # # # # # # # # # # # # # =========================
# # # # # # # # # # # # # # # AUDIO INPUT (ASR)
# # # # # # # # # # # # # # # =========================
# # # # # # # # # # # # # # elif input_mode == "Audio":
# # # # # # # # # # # # # #     audio_file = st.file_uploader(
# # # # # # # # # # # # # #         "Upload audio file (wav / mp3)",
# # # # # # # # # # # # # #         type=["wav", "mp3"]
# # # # # # # # # # # # # #     )

# # # # # # # # # # # # # #     if audio_file:
# # # # # # # # # # # # # #         with tempfile.NamedTemporaryFile(delete=False, suffix=".wav") as tmp:
# # # # # # # # # # # # # #             tmp.write(audio_file.read())
# # # # # # # # # # # # # #             audio_path = tmp.name

# # # # # # # # # # # # # #         transcript = transcribe_audio(audio_path)

# # # # # # # # # # # # # #         st.info("Please verify the transcription below:")
# # # # # # # # # # # # # #         final_input = st.text_area(
# # # # # # # # # # # # # #             "Transcribed Math Question:",
# # # # # # # # # # # # # #             value=transcript
# # # # # # # # # # # # # #         )


# # # # # # # # # # # # # # # =========================
# # # # # # # # # # # # # # # SOLVE BUTTON
# # # # # # # # # # # # # # # =========================
# # # # # # # # # # # # # # if st.button("Solve"):
# # # # # # # # # # # # # #     if not final_input.strip():
# # # # # # # # # # # # # #         st.warning("Please provide a math problem first.")
# # # # # # # # # # # # # #         st.stop()

# # # # # # # # # # # # # #     # ---------- PARSER ----------
# # # # # # # # # # # # # #     parsed = parse_input(final_input)

# # # # # # # # # # # # # #     st.subheader("🧩 Parsed Problem")
# # # # # # # # # # # # # #     st.json(parsed)

# # # # # # # # # # # # # #     if parsed["needs_clarification"]:
# # # # # # # # # # # # # #         st.warning("❓ Problem needs clarification before solving.")
# # # # # # # # # # # # # #         st.stop()

# # # # # # # # # # # # # #     # ---------- MEMORY LOOKUP ----------
# # # # # # # # # # # # # #     past = retrieve_similar(parsed["problem_text"])

# # # # # # # # # # # # # #     if past:
# # # # # # # # # # # # # #         st.info("🧠 Similar problem found in memory. Reusing solution.")

# # # # # # # # # # # # # #         solution = past["solution"]
# # # # # # # # # # # # # #         verification = {
# # # # # # # # # # # # # #             "verified": past["verified"],
# # # # # # # # # # # # # #             "confidence": past["confidence"],
# # # # # # # # # # # # # #             "reason": "Reused from memory",
# # # # # # # # # # # # # #             "needs_hitl": False
# # # # # # # # # # # # # #         }

# # # # # # # # # # # # # #     else:
# # # # # # # # # # # # # #         # ---------- RAG ----------
# # # # # # # # # # # # # #         retrieved_context = retrieve_context(parsed["problem_text"])

# # # # # # # # # # # # # #         # ---------- SOLVER ----------
# # # # # # # # # # # # # #         solution = solve_problem(parsed["problem_text"])

# # # # # # # # # # # # # #         # ---------- VERIFIER ----------
# # # # # # # # # # # # # #         verification = verify_solution(parsed, solution)

# # # # # # # # # # # # # #     # ---------- OUTPUT ----------
# # # # # # # # # # # # # #     st.subheader("✅ Solution")
# # # # # # # # # # # # # #     st.text(solution)

# # # # # # # # # # # # # #     st.subheader("🔍 Verification")
# # # # # # # # # # # # # #     st.write(f"✔️ Verified: **{verification['verified']}**")
# # # # # # # # # # # # # #     st.write(f"📊 Confidence: **{verification['confidence']}**")
# # # # # # # # # # # # # #     st.write(f"🧠 Reason: {verification['reason']}")

# # # # # # # # # # # # # #     # ---------- HITL ----------
# # # # # # # # # # # # # #     if verification["needs_hitl"]:
# # # # # # # # # # # # # #         st.warning("⚠️ Human review required")

# # # # # # # # # # # # # #         corrected_solution = st.text_area(
# # # # # # # # # # # # # #             "Edit / correct the solution:",
# # # # # # # # # # # # # #             value=solution
# # # # # # # # # # # # # #         )

# # # # # # # # # # # # # #         if st.button("Approve Correction"):
# # # # # # # # # # # # # #             st.success("✔️ Correction approved and saved to memory")

# # # # # # # # # # # # # #             add_memory({
# # # # # # # # # # # # # #                 "input": final_input,
# # # # # # # # # # # # # #                 "parsed": parsed,
# # # # # # # # # # # # # #                 "solution": corrected_solution,
# # # # # # # # # # # # # #                 "verified": True,
# # # # # # # # # # # # # #                 "confidence": 1.0,
# # # # # # # # # # # # # #                 "feedback": "human_corrected"
# # # # # # # # # # # # # #             })

# # # # # # # # # # # # # #             st.stop()

# # # # # # # # # # # # # #     else:
# # # # # # # # # # # # # #         st.success("✔️ Solution verified automatically")

# # # # # # # # # # # # # #         # ---------- SAVE TO MEMORY ----------
# # # # # # # # # # # # # #         add_memory({
# # # # # # # # # # # # # #             "input": final_input,
# # # # # # # # # # # # # #             "parsed": parsed,
# # # # # # # # # # # # # #             "solution": solution,
# # # # # # # # # # # # # #             "verified": verification["verified"],
# # # # # # # # # # # # # #             "confidence": verification["confidence"],
# # # # # # # # # # # # # #             "feedback": "correct"
# # # # # # # # # # # # # #         })

# # # # # # # # # # # # # #     # ---------- RAG DISPLAY ----------
# # # # # # # # # # # # # #     st.subheader("📚 Retrieved Knowledge (RAG)")
# # # # # # # # # # # # # #     st.text(retrieve_context(parsed["problem_text"]))


# # # # # # # # # # # # # import streamlit as st
# # # # # # # # # # # # # from utils.ocr import extract_text_from_image
# # # # # # # # # # # # # from utils.asr import transcribe_audio
# # # # # # # # # # # # # from agents.parser_agent import parse_input
# # # # # # # # # # # # # from agents.intent_router import route_intent
# # # # # # # # # # # # # from agents.solver_agent import solve_problem
# # # # # # # # # # # # # from agents.verifier_agent import verify_solution
# # # # # # # # # # # # # from utils.rag import retrieve_context
# # # # # # # # # # # # # from memory.memory_store import save_to_memory

# # # # # # # # # # # # # st.set_page_config("Math Mentor AI")
# # # # # # # # # # # # # st.title("🧠 Math Mentor AI")

# # # # # # # # # # # # # mode = st.selectbox("Select Input Type", ["Text", "Image", "Audio"])

# # # # # # # # # # # # # question = ""

# # # # # # # # # # # # # if mode == "Text":
# # # # # # # # # # # # #     question = st.text_area("Enter math problem")

# # # # # # # # # # # # # elif mode == "Image":
# # # # # # # # # # # # #     img = st.file_uploader("Upload image", type=["png", "jpg"])
# # # # # # # # # # # # #     if img:
# # # # # # # # # # # # #         question = extract_text_from_image(img)
# # # # # # # # # # # # #         question = st.text_area("OCR Text", question)

# # # # # # # # # # # # # elif mode == "Audio":
# # # # # # # # # # # # #     audio = st.file_uploader("Upload audio", type=["wav", "mp3"])
# # # # # # # # # # # # #     if audio:
# # # # # # # # # # # # #         question, low = transcribe_audio(audio)
# # # # # # # # # # # # #         if low:
# # # # # # # # # # # # #             st.warning("Low confidence transcription")
# # # # # # # # # # # # #         question = st.text_area("Transcript", question)

# # # # # # # # # # # # # if st.button("Solve"):
# # # # # # # # # # # # #     parsed = parse_input(question)
# # # # # # # # # # # # #     intent = route_intent(parsed)
# # # # # # # # # # # # #     context = retrieve_context(parsed["problem_text"])
# # # # # # # # # # # # #     solution = solve_problem(parsed["problem_text"])
# # # # # # # # # # # # #     ok, status = verify_solution(solution)

# # # # # # # # # # # # #     st.subheader("✅ Solution")
# # # # # # # # # # # # #     st.write(solution)

# # # # # # # # # # # # #     st.subheader("📚 Retrieved Knowledge")
# # # # # # # # # # # # #     st.write(context)

# # # # # # # # # # # # #     save_to_memory({
# # # # # # # # # # # # #         "question": question,
# # # # # # # # # # # # #         "solution": solution,
# # # # # # # # # # # # #         "verified": ok
# # # # # # # # # # # # #     })


# # # # # # # # # # # # import streamlit as st
# # # # # # # # # # # # from PIL import Image

# # # # # # # # # # # # from agents.parser_agent import parse_input
# # # # # # # # # # # # from agents.solver_agent import solve_problem
# # # # # # # # # # # # from utils.ocr import extract_text_from_image
# # # # # # # # # # # # from utils.asr import transcribe_audio
# # # # # # # # # # # # from utils.rag import retrieve_context

# # # # # # # # # # # # # =========================
# # # # # # # # # # # # # PAGE CONFIG
# # # # # # # # # # # # # =========================
# # # # # # # # # # # # st.set_page_config(
# # # # # # # # # # # #     page_title="🧠 Math Mentor AI",
# # # # # # # # # # # #     layout="centered"
# # # # # # # # # # # # )

# # # # # # # # # # # # st.title("🧠 Math Mentor AI")
# # # # # # # # # # # # st.caption("Reliable Multimodal Math Solver (Text | Image | Audio)")

# # # # # # # # # # # # # =========================
# # # # # # # # # # # # # INPUT TYPE SELECTION
# # # # # # # # # # # # # =========================
# # # # # # # # # # # # input_type = st.radio(
# # # # # # # # # # # #     "Select Input Type",
# # # # # # # # # # # #     ["Text", "Image", "Audio"]
# # # # # # # # # # # # )

# # # # # # # # # # # # user_input = ""

# # # # # # # # # # # # # =========================
# # # # # # # # # # # # # TEXT INPUT
# # # # # # # # # # # # # =========================
# # # # # # # # # # # # if input_type == "Text":
# # # # # # # # # # # #     user_input = st.text_area(
# # # # # # # # # # # #         "Enter math problem",
# # # # # # # # # # # #         placeholder="e.g. solve x^2 + 4x + 3 = 0"
# # # # # # # # # # # #     )

# # # # # # # # # # # # # =========================
# # # # # # # # # # # # # IMAGE INPUT (OCR)
# # # # # # # # # # # # # =========================
# # # # # # # # # # # # elif input_type == "Image":
# # # # # # # # # # # #     uploaded_image = st.file_uploader(
# # # # # # # # # # # #         "Upload math problem image",
# # # # # # # # # # # #         type=["png", "jpg", "jpeg"]
# # # # # # # # # # # #     )

# # # # # # # # # # # #     if uploaded_image:
# # # # # # # # # # # #         image = Image.open(uploaded_image)
# # # # # # # # # # # #         st.image(image, caption="Uploaded Image", use_column_width=True)

# # # # # # # # # # # #         extracted_text = extract_text_from_image(uploaded_image)
# # # # # # # # # # # #         user_input = st.text_area(
# # # # # # # # # # # #             "Extracted text (edit if needed)",
# # # # # # # # # # # #             value=extracted_text
# # # # # # # # # # # #         )

# # # # # # # # # # # # # =========================
# # # # # # # # # # # # # AUDIO INPUT (ASR)
# # # # # # # # # # # # # =========================
# # # # # # # # # # # # elif input_type == "Audio":
# # # # # # # # # # # #     uploaded_audio = st.file_uploader(
# # # # # # # # # # # #         "Upload audio file",
# # # # # # # # # # # #         type=["wav", "mp3", "m4a"]
# # # # # # # # # # # #     )

# # # # # # # # # # # #     if uploaded_audio:
# # # # # # # # # # # #         with st.spinner("Transcribing audio..."):
# # # # # # # # # # # #             transcription = transcribe_audio(uploaded_audio)

# # # # # # # # # # # #         user_input = st.text_area(
# # # # # # # # # # # #             "Transcribed text (edit if needed)",
# # # # # # # # # # # #             value=transcription
# # # # # # # # # # # #         )

# # # # # # # # # # # # # =========================
# # # # # # # # # # # # # SOLVE BUTTON
# # # # # # # # # # # # # =========================
# # # # # # # # # # # # if st.button("Solve"):
# # # # # # # # # # # #     if not user_input.strip():
# # # # # # # # # # # #         st.warning("Please provide a math problem.")
# # # # # # # # # # # #     else:
# # # # # # # # # # # #         # -------------------------
# # # # # # # # # # # #         # PARSE
# # # # # # # # # # # #         # -------------------------
# # # # # # # # # # # #         parsed_problem = parse_input(user_input)

# # # # # # # # # # # #         # -------------------------
# # # # # # # # # # # #         # RAG CONTEXT
# # # # # # # # # # # #         # -------------------------
# # # # # # # # # # # #         context = retrieve_context(parsed_problem)

# # # # # # # # # # # #         # -------------------------
# # # # # # # # # # # #         # SOLVE
# # # # # # # # # # # #         # -------------------------
# # # # # # # # # # # #         solution = solve_problem(parsed_problem)

# # # # # # # # # # # #         # =========================
# # # # # # # # # # # #         # OUTPUT
# # # # # # # # # # # #         # =========================
# # # # # # # # # # # #         st.subheader("✅ Solution")
# # # # # # # # # # # #         st.write(solution)

# # # # # # # # # # # #         st.subheader("📚 Retrieved Knowledge (RAG)")
# # # # # # # # # # # #         st.write(context)


# # # # # # # # # # # # app.py
# # # # # # # # # # # import streamlit as st
# # # # # # # # # # # from agents.parser_agent import parse_input
# # # # # # # # # # # from agents.solver_agent import solve_problem

# # # # # # # # # # # st.set_page_config(page_title="Math Mentor AI", layout="wide")
# # # # # # # # # # # st.title("🧠 Math Mentor AI")
# # # # # # # # # # # st.write("Reliable Multimodal Math Solver (Text | Image | Audio)")

# # # # # # # # # # # input_type = st.selectbox("Select Input Type", ["Text", "Image", "Audio"])

# # # # # # # # # # # user_input = None

# # # # # # # # # # # if input_type == "Text":
# # # # # # # # # # #     user_input = st.text_area("Enter math problem")
# # # # # # # # # # # elif input_type == "Image":
# # # # # # # # # # #     uploaded_file = st.file_uploader("Upload math image", type=["png", "jpg", "jpeg"])
# # # # # # # # # # #     if uploaded_file:
# # # # # # # # # # #         from utils.ocr import extract_text_from_image
# # # # # # # # # # #         user_input = extract_text_from_image(uploaded_file)
# # # # # # # # # # # elif input_type == "Audio":
# # # # # # # # # # #     uploaded_audio = st.file_uploader("Upload audio", type=["mp3", "wav"])
# # # # # # # # # # #     if uploaded_audio:
# # # # # # # # # # #         from utils.asr import transcribe_audio
# # # # # # # # # # #         user_input = transcribe_audio(uploaded_audio)

# # # # # # # # # # # if user_input:
# # # # # # # # # # #     parsed_problem = parse_input(user_input)
# # # # # # # # # # #     solution = solve_problem(parsed_problem)
    
# # # # # # # # # # #     st.subheader("✅ Solution")
# # # # # # # # # # #     st.write(solution["solution"])


# # # # # # # # # # import streamlit as st
# # # # # # # # # # from agents.parser_agent import parse_input
# # # # # # # # # # from agents.solver_agent import solve_problem
# # # # # # # # # # from utils.rag import retrieve_context
# # # # # # # # # # from utils.ocr import extract_text_from_image
# # # # # # # # # # from utils.asr import transcribe_audio

# # # # # # # # # # # --- Streamlit Page Configuration ---
# # # # # # # # # # st.set_page_config(
# # # # # # # # # #     page_title="Math Mentor AI",
# # # # # # # # # #     layout="centered",
# # # # # # # # # #     page_icon="🧠"
# # # # # # # # # # )

# # # # # # # # # # st.title("🧠 Math Mentor AI")
# # # # # # # # # # st.markdown("**Reliable Multimodal Math Solver (Text | Image | Audio)**")

# # # # # # # # # # # --- Input Type Selection ---
# # # # # # # # # # input_type = st.radio(
# # # # # # # # # #     "Select Input Type",
# # # # # # # # # #     ("Text", "Image", "Audio")
# # # # # # # # # # )

# # # # # # # # # # user_input = None

# # # # # # # # # # # --- Input Section ---
# # # # # # # # # # if input_type == "Text":
# # # # # # # # # #     user_input = st.text_area("Enter math problem", height=100, placeholder="Example: x^2 + 4x + 3 = 0")
# # # # # # # # # # elif input_type == "Image":
# # # # # # # # # #     uploaded_file = st.file_uploader("Upload math image", type=["png", "jpg", "jpeg"])
# # # # # # # # # #     if uploaded_file:
# # # # # # # # # #         user_input = extract_text_from_image(uploaded_file)
# # # # # # # # # #         st.info(f"Extracted Text: {user_input}")
# # # # # # # # # # elif input_type == "Audio":
# # # # # # # # # #     uploaded_audio = st.file_uploader("Upload audio", type=["mp3", "wav"])
# # # # # # # # # #     if uploaded_audio:
# # # # # # # # # #         user_input = transcribe_audio(uploaded_audio)
# # # # # # # # # #         st.info(f"Transcribed Text: {user_input}")

# # # # # # # # # # # --- Solve Button ---
# # # # # # # # # # if st.button("Solve"):
# # # # # # # # # #     if user_input:
# # # # # # # # # #         try:
# # # # # # # # # #             # Parse the problem
# # # # # # # # # #             parsed_problem = parse_input(user_input)

# # # # # # # # # #             # Retrieve context using RAG
# # # # # # # # # #             context = retrieve_context(parsed_problem["problem_text"])

# # # # # # # # # #             # Solve the problem
# # # # # # # # # #             solution = solve_problem(parsed_problem)

# # # # # # # # # #             # --- Display Solution ---
# # # # # # # # # #             st.subheader("✅ Solution")
# # # # # # # # # #             if isinstance(solution["solution"], list):
# # # # # # # # # #                 for i, val in enumerate(solution["solution"], start=1):
# # # # # # # # # #                     st.write(f"x{i} = {val}")
# # # # # # # # # #             else:
# # # # # # # # # #                 st.write(solution["solution"])

# # # # # # # # # #             # --- Display Retrieved Knowledge ---
# # # # # # # # # #             st.subheader("📚 Retrieved Knowledge (RAG)")
# # # # # # # # # #             if context:
# # # # # # # # # #                 for section in context:
# # # # # # # # # #                     st.markdown(f"- {section}")
# # # # # # # # # #             else:
# # # # # # # # # #                 st.write("No additional context found.")

# # # # # # # # # #         except Exception as e:
# # # # # # # # # #             st.error(f"Error: {e}")
# # # # # # # # # #     else:
# # # # # # # # # #         st.warning("Please provide input before solving.")


# # # # # # # # # # app.py
# # # # # # # # # import streamlit as st
# # # # # # # # # from agents.parser_agent import parse_input
# # # # # # # # # from agents.solver_agent import solve_problem
# # # # # # # # # from utils.rag import retrieve_context
# # # # # # # # # from utils.ocr import extract_text_from_image
# # # # # # # # # from utils.asr import audio_to_text

# # # # # # # # # st.set_page_config(page_title="Math Mentor AI", layout="wide")
# # # # # # # # # st.title("🧠 Math Mentor AI")
# # # # # # # # # st.subheader("Reliable Multimodal Math Solver (Text | Image | Audio)")

# # # # # # # # # # --- Input Type Selection ---
# # # # # # # # # input_type = st.radio("Select Input Type", ["Text", "Image", "Audio"])

# # # # # # # # # problem_text = ""
# # # # # # # # # if input_type == "Text":
# # # # # # # # #     problem_text = st.text_area("Enter math problem")
# # # # # # # # # elif input_type == "Image":
# # # # # # # # #     uploaded_file = st.file_uploader("Upload image", type=["png", "jpg", "jpeg"])
# # # # # # # # #     if uploaded_file:
# # # # # # # # #         problem_text = extract_text_from_image(uploaded_file)
# # # # # # # # # elif input_type == "Audio":
# # # # # # # # #     uploaded_audio = st.file_uploader("Upload audio", type=["mp3", "wav"])
# # # # # # # # #     if uploaded_audio:
# # # # # # # # #         problem_text = audio_to_text(uploaded_audio)

# # # # # # # # # if problem_text:
# # # # # # # # #     parsed_problem = parse_input(problem_text)

# # # # # # # # #     # Retrieve RAG knowledge
# # # # # # # # #     context = retrieve_context(parsed_problem["problem_text"])

# # # # # # # # #     # Solve the problem
# # # # # # # # #     solution_obj = solve_problem(parsed_problem)

# # # # # # # # #     # --- Display Solution ---
# # # # # # # # #     st.subheader("✅ Solution")
# # # # # # # # #     solution = solution_obj["solution"]
# # # # # # # # #     steps = solution_obj["steps"]

# # # # # # # # #     if solution:
# # # # # # # # #         for i, val in enumerate(solution, start=1):
# # # # # # # # #             st.write(f"x{i} = {val}")
# # # # # # # # #     else:
# # # # # # # # #         st.write("Unsupported problem type")

# # # # # # # # #     # --- Display Step-by-Step Solution ---
# # # # # # # # #     st.subheader("📝 Step-by-Step Solution")
# # # # # # # # #     st.text(steps)

# # # # # # # # #     # --- Display RAG Knowledge ---
# # # # # # # # #     st.subheader("📚 Retrieved Knowledge (RAG)")
# # # # # # # # #     if context:
# # # # # # # # #         st.markdown(context.replace("\n", "  \n"))  # keep line breaks


# # # # # # # # import streamlit as st
# # # # # # # # from agents.parser_agent import parse_input
# # # # # # # # from agents.solver_agent import solve_problem
# # # # # # # # from utils.rag import retrieve_context
# # # # # # # # from utils.ocr import extract_text_from_image
# # # # # # # # from utils.asr import audio_to_text

# # # # # # # # # Page config
# # # # # # # # st.set_page_config(page_title="Math Mentor AI", page_icon="🧠", layout="centered")

# # # # # # # # st.title("🧠 Math Mentor AI")
# # # # # # # # st.subheader("Reliable Multimodal Math Solver (Text | Image | Audio)")

# # # # # # # # # --- Input selection ---
# # # # # # # # input_type = st.radio("Select Input Type", ["Text", "Image", "Audio"])

# # # # # # # # user_input = None

# # # # # # # # if input_type == "Text":
# # # # # # # #     user_input = st.text_area("Enter math problem", height=100)
# # # # # # # # elif input_type == "Image":
# # # # # # # #     image_file = st.file_uploader("Upload Image", type=["png", "jpg", "jpeg"])
# # # # # # # #     if image_file is not None:
# # # # # # # #         user_input = extract_text_from_image(image_file)
# # # # # # # #         st.info(f"Extracted Text: {user_input}")
# # # # # # # # elif input_type == "Audio":
# # # # # # # #     audio_file = st.file_uploader("Upload Audio", type=["wav", "mp3"])
# # # # # # # #     if audio_file is not None:
# # # # # # # #         user_input = audio_to_text(audio_file)
# # # # # # # #         st.info(f"Transcribed Text: {user_input}")

# # # # # # # # # --- Solve button ---
# # # # # # # # if st.button("Solve"):

# # # # # # # #     if not user_input:
# # # # # # # #         st.warning("Please provide an input first!")
# # # # # # # #     else:
# # # # # # # #         # --- Parse ---
# # # # # # # #         parsed = parse_input(user_input)
# # # # # # # #         problem_text = parsed["problem_text"]

# # # # # # # #         # --- Retrieve context ---
# # # # # # # #         context = retrieve_context(problem_text)

# # # # # # # #         # --- Solve problem ---
# # # # # # # #         solution, steps = solve_problem(problem_text)

# # # # # # # #         # --- Display ---
# # # # # # # #         st.success("✅ Solution")
# # # # # # # #         for key, value in solution.items():
# # # # # # # #             st.write(f"{key} = {value}")

# # # # # # # #         st.subheader("📚 Retrieved Knowledge (RAG)")
# # # # # # # #         st.text(context)

# # # # # # # #         st.subheader("📝 Step-by-Step Explanation")
# # # # # # # #         st.text(steps)


# # # # # # # # app.py
# # # # # # # import streamlit as st
# # # # # # # from agents.parser_agent import parse_input
# # # # # # # from agents.solver_agent import solve_problem

# # # # # # # st.set_page_config(page_title="Math Mentor AI", layout="centered")
# # # # # # # st.title("🧠 Math Mentor AI")
# # # # # # # st.subheader("Reliable Multimodal Math Solver (Text | Image | Audio)")

# # # # # # # # Select input type
# # # # # # # input_type = st.radio("Select Input Type", ["Text", "Image", "Audio"])

# # # # # # # user_input = None

# # # # # # # if input_type == "Text":
# # # # # # #     user_input = st.text_input("Enter math problem", "solve x^2 + 4x + 3 = 0")
# # # # # # # elif input_type == "Image":
# # # # # # #     uploaded_file = st.file_uploader("Upload an image", type=["png", "jpg", "jpeg"])
# # # # # # #     if uploaded_file is not None:
# # # # # # #         from utils.ocr import extract_text_from_image
# # # # # # #         user_input = extract_text_from_image(uploaded_file)
# # # # # # # elif input_type == "Audio":
# # # # # # #     uploaded_audio = st.file_uploader("Upload audio", type=["wav", "mp3"])
# # # # # # #     if uploaded_audio is not None:
# # # # # # #         from utils.asr import audio_to_text
# # # # # # #         user_input = audio_to_text(uploaded_audio)

# # # # # # # # Solve button
# # # # # # # if st.button("Solve") and user_input:
# # # # # # #     parsed = parse_input(user_input)
# # # # # # #     problem_text = parsed["problem_text"]
# # # # # # #     solution, steps = solve_problem(problem_text)

# # # # # # #     st.success("✅ Solution")
# # # # # # #     st.code(solution)
# # # # # # #     st.subheader("Step-by-Step Explanation")
# # # # # # #     st.text(steps)


# # # # # # import streamlit as st
# # # # # # from agents.parser_agent import parse_input
# # # # # # from agents.solver_agent import solve_problem
# # # # # # from utils.rag import retrieve_context
# # # # # # from utils.ocr import extract_text_from_image
# # # # # # from utils.asr import transcribe_audio

# # # # # # st.set_page_config(page_title="Math Mentor AI", layout="centered")
# # # # # # st.title("🧠 Math Mentor AI")
# # # # # # st.subheader("Reliable Multimodal Math Solver (Text | Image | Audio)")

# # # # # # # Select Input Type
# # # # # # input_type = st.radio("Select Input Type", ["Text", "Image", "Audio"])

# # # # # # problem_text = ""

# # # # # # # ====================== TEXT INPUT ======================
# # # # # # if input_type == "Text":
# # # # # #     problem_text = st.text_input("Enter math problem", "")

# # # # # # # ====================== IMAGE INPUT ======================
# # # # # # elif input_type == "Image":
# # # # # #     uploaded_file = st.file_uploader("Upload an image", type=["png", "jpg", "jpeg"])
# # # # # #     if uploaded_file is not None:
# # # # # #         problem_text = extract_text_from_image(uploaded_file)
# # # # # #         # Normalize OCR output
# # # # # #         problem_text = problem_text.replace(" ", "").replace("\n", "").replace("×", "x")
# # # # # #         st.text("📄 OCR Extracted Text:")
# # # # # #         st.write(problem_text)

# # # # # # # ====================== AUDIO INPUT ======================
# # # # # # elif input_type == "Audio":
# # # # # #     audio_file = st.file_uploader("Upload audio", type=["mp3", "wav"])
# # # # # #     if audio_file is not None:
# # # # # #         problem_text = transcribe_audio(audio_file)
# # # # # #         # Normalize audio text
# # # # # #         problem_text = problem_text.replace(" ", "").replace("\n", "")
# # # # # #         st.text("🎙️ Audio Transcribed Text:")
# # # # # #         st.write(problem_text)

# # # # # # # ====================== SOLVE BUTTON ======================
# # # # # # if st.button("Solve") and problem_text:
# # # # # #     try:
# # # # # #         # Parse the input
# # # # # #         parsed_problem = parse_input(problem_text)

# # # # # #         # Retrieve RAG context
# # # # # #         context = retrieve_context(parsed_problem.get("problem_text", problem_text))

# # # # # #         # Solve the problem
# # # # # #         solution, steps = solve_problem(parsed_problem.get("problem_text", problem_text))

# # # # # #         # Display solution
# # # # # #         st.success("✅ Solution")
# # # # # #         st.write(solution)

# # # # # #         # Display step-by-step explanation
# # # # # #         st.subheader("Step-by-Step Explanation")
# # # # # #         for step in steps:
# # # # # #             st.write(step)

# # # # # #         # Display retrieved knowledge
# # # # # #         st.subheader("📚 Retrieved Knowledge (RAG)")
# # # # # #         st.write(context)

# # # # # #     except Exception as e:
# # # # # #         st.error(f"Error: {str(e)}")


# # # # # import streamlit as st
# # # # # from PIL import Image
# # # # # from utils.ocr import extract_text_from_image
# # # # # from utils.asr import transcribe_audio
# # # # # from agents.parser_agent import parse_input
# # # # # from agents.solver_agent import solve_problem
# # # # # from utils.rag import retrieve_context


# # # # # st.set_page_config(page_title="Math Mentor AI", layout="wide")

# # # # # st.title("🧠 Math Mentor AI")
# # # # # st.subheader("Reliable Multimodal Math Solver (Text | Image | Audio)")

# # # # # # -----------------------------
# # # # # # Sidebar: Input Type Selection
# # # # # # -----------------------------
# # # # # input_type = st.radio("Select Input Type", ["Text", "Image", "Audio"])

# # # # # problem_text = ""

# # # # # if input_type == "Text":
# # # # #     problem_text = st.text_area("Enter math problem", height=100)

# # # # # elif input_type == "Image":
# # # # #     uploaded_file = st.file_uploader("Upload an image", type=["png", "jpg", "jpeg"])
# # # # #     if uploaded_file is not None:
# # # # #         image = Image.open(uploaded_file)
# # # # #         problem_text = extract_text_from_image(image)
# # # # #         st.image(image, caption="Uploaded Image", use_column_width=True)

# # # # # elif input_type == "Audio":
# # # # #     uploaded_audio = st.file_uploader("Upload audio", type=["mp3", "wav", "m4a"])
# # # # #     if uploaded_audio is not None:
# # # # #         problem_text = transcribe_audio(uploaded_audio)
# # # # #         st.audio(uploaded_audio, format='audio/mp3')

# # # # # # -----------------------------
# # # # # # Solve Button
# # # # # # -----------------------------
# # # # # if st.button("Solve"):

# # # # #     if not problem_text:
# # # # #         st.warning("Please provide a math problem first!")
# # # # #     else:
# # # # #         # Step 1: Parse input
# # # # #         parsed_problem = parse_input(problem_text)

# # # # #         # Step 2: Retrieve context (RAG)
# # # # #         context = retrieve_context(parsed_problem["problem_text"])

# # # # #         # Step 3: Solve the problem
# # # # #         solution, steps = solve_problem(parsed_problem)

# # # # #         # Step 4: Display solution
# # # # #         st.markdown("✅ **Solution:**")
# # # # #         st.write(solution)

# # # # #         st.markdown("### Step-by-Step Explanation:")
# # # # #         for step in steps:
# # # # #             st.write(step)

# # # # #         st.markdown("### 📚 Retrieved Knowledge (RAG):")
# # # # #         st.write(context)


# # # # import streamlit as st
# # # # from utils.ocr import extract_text_from_image
# # # # from utils.asr import transcribe_audio
# # # # from utils.rag import retrieve_context
# # # # from agents.solver_agent import solve_problem

# # # # st.set_page_config(page_title="Math Mentor AI", layout="wide")

# # # # st.title("🧠 Math Mentor AI")
# # # # st.subheader("Reliable Multimodal Math Solver (Text | Image | Audio)")

# # # # # --- Input selection ---
# # # # input_type = st.radio("Select Input Type", ["Text", "Image", "Audio"])

# # # # problem_text = ""

# # # # if input_type == "Text":
# # # #     problem_text = st.text_input("Enter math problem", "")

# # # # elif input_type == "Image":
# # # #     image_file = st.file_uploader("Upload an image", type=["png", "jpg", "jpeg"])
# # # #     if image_file:
# # # #         problem_text = extract_text_from_image(image_file)
# # # #         st.info(f"Extracted Text: {problem_text}")

# # # # elif input_type == "Audio":
# # # #     audio_file = st.file_uploader("Upload an audio file", type=["wav", "mp3", "m4a"])
# # # #     if audio_file:
# # # #         problem_text = transcribe_audio(audio_file)
# # # #         st.info(f"Transcribed Text: {problem_text}")

# # # # # --- Solve button ---
# # # # if st.button("Solve") and problem_text:
# # # #     try:
# # # #         # Step 1: retrieve context from RAG
# # # #         context = retrieve_context(problem_text)

# # # #         # Step 2: solve problem
# # # #         solution, steps = solve_problem(problem_text)

# # # #         # --- Display results ---
# # # #         st.success("✅ Solution:")
# # # #         if isinstance(solution, list):
# # # #             for idx, sol in enumerate(solution):
# # # #                 st.write(f"x{idx+1} = {sol}")
# # # #         else:
# # # #             st.write(solution)

# # # #         st.subheader("Step-by-Step Explanation:")
# # # #         if isinstance(steps, list):
# # # #             for step in steps:
# # # #                 st.write(step)
# # # #         else:
# # # #             st.write(steps)

# # # #         st.subheader("📚 Retrieved Knowledge (RAG):")
# # # #         st.write(context)

# # # #     except Exception as e:
# # # #         st.error(f"Error: {str(e)}")


# # # import streamlit as st
# # # from PIL import Image
# # # import tempfile

# # # # =========================
# # # # AGENTS
# # # # =========================
# # # from agents.parser_agent import parse_input
# # # from agents.solver_agent import solve_problem
# # # from agents.verifier_agent import verify_solution

# # # # =========================
# # # # UTILS
# # # # =========================
# # # from utils.ocr import extract_text_from_image
# # # from utils.asr import transcribe_audio
# # # from utils.rag import retrieve_context

# # # # =========================
# # # # MEMORY
# # # # =========================
# # # from memory.memory_store import add_memory, retrieve_similar


# # # # =========================
# # # # PAGE CONFIG
# # # # =========================
# # # st.set_page_config(page_title="Math Mentor AI", layout="centered")
# # # st.title("🧠 Math Mentor AI")
# # # st.caption("Reliable Multimodal Math Mentor (RAG + Agents + HITL + Memory)")


# # # # =========================
# # # # INPUT MODE
# # # # =========================
# # # input_mode = st.radio(
# # #     "Select Input Type:",
# # #     ["Text", "Image", "Audio"]
# # # )

# # # final_input = ""


# # # # =========================
# # # # TEXT INPUT
# # # # =========================
# # # if input_mode == "Text":
# # #     final_input = st.text_area(
# # #         "Enter a math problem:",
# # #         placeholder="e.g., solve x^2 - 5x + 6 = 0"
# # #     )


# # # # =========================
# # # # IMAGE INPUT (OCR)
# # # # =========================
# # # elif input_mode == "Image":
# # #     image_file = st.file_uploader(
# # #         "Upload a math problem image (JPG / PNG)",
# # #         type=["jpg", "png"]
# # #     )

# # #     if image_file:
# # #         image = Image.open(image_file)
# # #         st.image(image, caption="Uploaded Image", use_column_width=True)

# # #         ocr_text, confidence = extract_text_from_image(image)

# # #         if confidence < 0.6:
# # #             st.warning("⚠️ OCR confidence is low. Please verify or correct the text.")

# # #         final_input = st.text_area(
# # #             "OCR Extracted Text (Edit if needed):",
# # #             value=ocr_text
# # #         )


# # # # =========================
# # # # AUDIO INPUT (ASR)
# # # # =========================
# # # elif input_mode == "Audio":
# # #     audio_file = st.file_uploader(
# # #         "Upload audio file (wav / mp3)",
# # #         type=["wav", "mp3"]
# # #     )

# # #     if audio_file:
# # #         with tempfile.NamedTemporaryFile(delete=False, suffix=".wav") as tmp:
# # #             tmp.write(audio_file.read())
# # #             audio_path = tmp.name

# # #         transcript = transcribe_audio(audio_path)

# # #         st.info("Please verify the transcription below:")
# # #         final_input = st.text_area(
# # #             "Transcribed Math Question:",
# # #             value=transcript
# # #         )


# # # # =========================
# # # # SOLVE BUTTON
# # # # =========================
# # # if st.button("Solve"):
# # #     if not final_input.strip():
# # #         st.warning("Please provide a math problem first.")
# # #         st.stop()

# # #     # ---------- PARSER ----------
# # #     parsed = parse_input(final_input)

# # #     st.subheader("🧩 Parsed Problem")
# # #     st.json(parsed)

# # #     if parsed["needs_clarification"]:
# # #         st.warning("❓ Problem needs clarification before solving.")
# # #         st.stop()

# # #     # ---------- MEMORY LOOKUP ----------
# # #     past = retrieve_similar(parsed["problem_text"])

# # #     if past:
# # #         st.info("🧠 Similar problem found in memory. Reusing solution.")

# # #         solution = past["solution"]
# # #         verification = {
# # #             "verified": past["verified"],
# # #             "confidence": past["confidence"],
# # #             "reason": "Reused from memory",
# # #             "needs_hitl": False
# # #         }

# # #     else:
# # #         # ---------- RAG ----------
# # #         retrieved_context = retrieve_context(parsed["problem_text"])

# # #         # ---------- SOLVER ----------
# # #         solution = solve_problem(parsed["problem_text"])

# # #         # ---------- VERIFIER ----------
# # #         verification = verify_solution(parsed, solution)

# # #     # ---------- OUTPUT ----------
# # #     st.subheader("✅ Solution")
# # #     st.text(solution)

# # #     st.subheader("🔍 Verification")
# # #     st.write(f"✔️ Verified: **{verification['verified']}**")
# # #     st.write(f"📊 Confidence: **{verification['confidence']}**")
# # #     st.write(f"🧠 Reason: {verification['reason']}")

# # #     # ---------- HITL ----------
# # #     if verification["needs_hitl"]:
# # #         st.warning("⚠️ Human review required")

# # #         corrected_solution = st.text_area(
# # #             "Edit / correct the solution:",
# # #             value=solution
# # #         )

# # #         if st.button("Approve Correction"):
# # #             st.success("✔️ Correction approved and saved to memory")

# # #             add_memory({
# # #                 "input": final_input,
# # #                 "parsed": parsed,
# # #                 "solution": corrected_solution,
# # #                 "verified": True,
# # #                 "confidence": 1.0,
# # #                 "feedback": "human_corrected"
# # #             })

# # #             st.stop()

# # #     else:
# # #         st.success("✔️ Solution verified automatically")

# # #         # ---------- SAVE TO MEMORY ----------
# # #         add_memory({
# # #             "input": final_input,
# # #             "parsed": parsed,
# # #             "solution": solution,
# # #             "verified": verification["verified"],
# # #             "confidence": verification["confidence"],
# # #             "feedback": "correct"
# # #         })

# # #     # ---------- RAG DISPLAY ----------
# # #     st.subheader("📚 Retrieved Knowledge (RAG)")
# # #     st.text(retrieve_context(parsed["problem_text"]))

# # import streamlit as st
# # from PIL import Image
# # import pytesseract

# # st.set_page_config(page_title="Math Mentor AI", layout="wide")

# # st.title("📘 Math Mentor AI")
# # st.subheader("Step 1: Image → OCR → User Confirmation")

# # uploaded_image = st.file_uploader(
# #     "Upload a math problem image",
# #     type=["png", "jpg", "jpeg"]
# # )

# # if uploaded_image:
# #     image = Image.open(uploaded_image)

# #     col1, col2 = st.columns(2)

# #     with col1:
# #         st.image(image, caption="Uploaded Image", use_column_width=True)

# #     with col2:
# #         with st.spinner("Extracting text from image..."):
# #             extracted_text = pytesseract.image_to_string(image)

# #         st.markdown("### 📝 Extracted Text (Edit if needed)")
# #         user_corrected_text = st.text_area(
# #             "OCR Output",
# #             value=extracted_text,
# #             height=200
# #         )

# #         if st.button("Confirm & Proceed"):
# #             st.success("Text confirmed successfully!")
# #             st.code(user_corrected_text)


# from utils.ocr import extract_text_from_image

# cleaned_text, confidence, issues = extract_text_from_image(image)

# st.markdown("### 📝 Extracted Math Text")
# user_text = st.text_area(
#     "Edit if needed",
#     value=cleaned_text,
#     height=200
# )

# st.markdown(f"**OCR Confidence:** `{confidence:.2f}`")

# if issues:
#     st.warning("⚠️ OCR Issues Detected:")
#     for issue in issues:
#         st.write(f"- {issue}")

# if confidence < 0.8:
#     st.warning("Please verify the extracted text carefully.")

# if st.button("Confirm & Proceed"):
#     st.success("Text confirmed!")
#     st.code(user_text)


import streamlit as st
from PIL import Image
import tempfile

# =========================
# AGENTS
# =========================
from agents.parser_agent import parse_input
from agents.solver_agent import solve_problem
from agents.verifier_agent import verify_solution

# =========================
# UTILS
# =========================
from utils.ocr import extract_text_from_image
from utils.asr import transcribe_audio
from utils.rag import retrieve_context

# =========================
# MEMORY
# =========================
from memory.memory_store import add_memory, retrieve_similar

# =========================
# PAGE CONFIG
# =========================
st.set_page_config(page_title="Math Mentor AI", layout="centered")
st.title("🧠 Math Mentor AI")
st.caption("Reliable Multimodal Math Mentor (RAG + Agents + HITL + Memory)")

# =========================
# INPUT MODE
# =========================
input_mode = st.radio(
    "Select Input Type:",
    ["Text", "Image", "Audio"]
)

final_input = ""

# =========================
# TEXT INPUT
# =========================
if input_mode == "Text":
    final_input = st.text_area(
        "Enter a math problem:",
        placeholder="e.g., solve x^2 - 5x + 6 = 0"
    )

# =========================
# IMAGE INPUT (OCR)
# =========================
elif input_mode == "Image":
    image_file = st.file_uploader(
        "Upload a math problem image (JPG / PNG)",
        type=["jpg", "png"]
    )

    if image_file is not None:
        image = Image.open(image_file)
        st.image(image, caption="Uploaded Image", width = 500)

        cleaned_text, confidence = extract_text_from_image(image)

        if confidence < 0.6:
            st.warning("⚠️ OCR confidence is low. Please verify or correct the text.")

        final_input = st.text_area(
            "OCR Extracted Text (Edit if needed):",
            value=cleaned_text
        )

# =========================
# AUDIO INPUT (ASR)
# =========================
elif input_mode == "Audio":
    audio_file = st.file_uploader(
        "Upload audio file (wav / mp3)",
        type=["wav", "mp3"]
    )

    if audio_file is not None:
        with tempfile.NamedTemporaryFile(delete=False, suffix=".wav") as tmp:
            tmp.write(audio_file.read())
            audio_path = tmp.name

        transcript = transcribe_audio(audio_path)

        st.info("Please verify the transcription below:")
        final_input = st.text_area(
            "Transcribed Math Question:",
            value=transcript
        )

# =========================
# SOLVE BUTTON
# =========================
if st.button("Solve"):

    if not final_input.strip():
        st.warning("Please provide a math problem first.")
        st.stop()

    # ---------- PARSER ----------
    parsed = parse_input(final_input)
    st.subheader("🧩 Parsed Problem")
    st.json(parsed)

    if parsed.get("needs_clarification", False):
        st.warning("❓ Problem needs clarification before solving.")
        st.stop()

    # ---------- MEMORY LOOKUP ----------
    past = retrieve_similar(parsed["problem_text"])

    if past:
        st.info("🧠 Similar problem found in memory. Reusing solution.")
        solution = past["solution"]
        verification = {
            "verified": past["verified"],
            "confidence": past["confidence"],
            "reason": "Reused from memory",
            "needs_hitl": False
        }
    else:
        # ---------- RAG ----------
        retrieved_context = retrieve_context(parsed["problem_text"])

        # ---------- SOLVER ----------
        solution = solve_problem(parsed["problem_text"])

        # ---------- VERIFIER ----------
        verification = verify_solution(parsed, solution)

    # ---------- OUTPUT ----------
    st.subheader("✅ Solution")
    st.text(solution)

    st.subheader("🔍 Verification")
    st.write(f"✔️ Verified: **{verification['verified']}**")
    st.write(f"📊 Confidence: **{verification['confidence']}**")
    st.write(f"🧠 Reason: {verification['reason']}")

    # ---------- HITL ----------
    if verification["needs_hitl"]:
        st.warning("⚠️ Human review required")

        corrected_solution = st.text_area(
            "Edit / correct the solution:",
            value=solution
        )

        if st.button("Approve Correction"):
            st.success("✔️ Correction approved and saved to memory")
            add_memory({
                "input": final_input,
                "parsed": parsed,
                "solution": corrected_solution,
                "verified": True,
                "confidence": 1.0,
                "feedback": "human_corrected"
            })
            st.stop()
    else:
        st.success("✔️ Solution verified automatically")

        # ---------- SAVE TO MEMORY ----------
        add_memory({
            "input": final_input,
            "parsed": parsed,
            "solution": solution,
            "verified": verification["verified"],
            "confidence": verification["confidence"],
            "feedback": "correct"
        })

    # ---------- RAG DISPLAY ----------
    st.subheader("📚 Retrieved Knowledge (RAG)")
    st.text(retrieve_context(parsed["problem_text"]))
