# 🧠 Math Mentor AI

## A Reliable Multimodal Math Tutor using RAG, Multi-Agents, HITL, and Memory

Math Mentor AI is an end-to-end AI application designed to **solve JEE-style math problems reliably**.  
It supports **text, image, and audio inputs**, explains solutions step-by-step, verifies correctness, and improves over time using feedback and memory.

This project demonstrates **real-world AI system design**, not just model usage.

---

## 🚀 Key Features

### 🔹 Multimodal Input
- **Text**: Type math questions directly  
- **Image**: Upload textbook screenshots or handwritten notes (OCR)  
- **Audio**: Ask questions using voice (Speech-to-Text)

### 🔹 Reliable Reasoning Pipeline
- Clean parsing of noisy OCR / ASR outputs  
- Retrieval-Augmented Generation (RAG) using curated math knowledge  
- Tool-based solving (Python for calculations)  
- Independent verification before final answer  

### 🔹 Human-in-the-Loop (HITL)
Triggered when:
- OCR / ASR confidence is low  
- Question is ambiguous  
- Verifier is uncertain  

Users can correct or approve results.

### 🔹 Memory & Self-Learning
Stores:
- Original input  
- Parsed question  
- Retrieved context  
- Final solution  
- User feedback  

Reuses past solutions and correction patterns for similar problems.

---

## 📚 Supported Math Scope
- Algebra (linear & quadratic equations)  
- Probability (basic)  
- Calculus (limits, derivatives – basic)  
- Linear Algebra (intro level)  

*(JEE-style difficulty, not olympiad)*


## 🏗️ System Architecture

```mermaid
flowchart TD
    A[User Input<br/>(Text / Image / Audio)]
    B[OCR / ASR]
    C[Parser Agent]
    D[Intent Router]
    E[Retriever<br/>(RAG)]
    F[Solver Agent]
    G[Verifier Agent]
    H[Explainer Agent]
    I[User Feedback<br/>(HITL)]
    J[Memory Store]

    A --> B --> C --> D
    D --> E --> F --> G --> H
    G -->|Low Confidence| I
    H --> I
    I --> J
    J --> E

