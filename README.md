<p align="center">
  <img src="screenshots/talkspace-ai-banner.png" width="100%" />
</p>

<p align="center">
 <img src="https://readme-typing-svg.herokuapp.com?font=Inter&weight=500&size=28&duration=3500&pause=1000&color=4F8F7F&center=true&vCenter=true&width=600&lines=Hey%2C+I%E2%80%99m+Nira+%F0%9F%8C%BF;I%E2%80%99m+here+to+listen;You+can+talk+about+anything;No+pressure%2C+just+talk" />
</p>

<p align="center">
  A calm digital space where thoughts feel safe to be shared.
</p>
Built with emotionally-aware AI, real-time UI adaptation, and human-centered design.
<p align="center">
  <b>🌿 Your companion Nira is here to listen.</b>
</p>


---

## 🚀 Live Demo

👉 **Try TalkSpace Live:**
https://talkspace-ai.streamlit.app/

---

## 🏷 Tech Badges

<p align="center">

![Python](https://img.shields.io/badge/Python-3.10-blue?style=for-the-badge&logo=python)
![Streamlit](https://img.shields.io/badge/Streamlit-App-red?style=for-the-badge&logo=streamlit)
![Scikit-Learn](https://img.shields.io/badge/Scikit--Learn-ML-orange?style=for-the-badge&logo=scikitlearn)
![NLP](https://img.shields.io/badge/NLP-Text%20Analysis-green?style=for-the-badge)
![LLM](https://img.shields.io/badge/LLM-LLaMA%203-purple?style=for-the-badge)
![Supabase](https://img.shields.io/badge/Database-Supabase-3ECF8E?style=for-the-badge&logo=supabase)
![UI/UX](https://img.shields.io/badge/UI-Emotion%20Aware-teal?style=for-the-badge)
![Status](https://img.shields.io/badge/Status-Active-success?style=for-the-badge)
![AI Companion](https://img.shields.io/badge/Product-AI%20Companion-ff69b4?style=for-the-badge)

</p>

---

## 🌱 The Idea

TalkSpace is designed as a calm digital environment for conversation.

Unlike traditional chatbots focused on quick answers, TalkSpace focuses on:
- helping users feel heard
- maintaining natural, human-like dialogue
- offering gentle, supportive responses

The goal is not just interaction — but emotional understanding.


---

## ✨ Core Features

🌿 **AI Companion – Nira**
- Conversational agent designed for warmth and empathy
- Supports dual modes: Supportive Friend / Counselor

🧠 **Emotion-Aware Responses**
- Detects emotional signals (loneliness, stress, anxiety, etc.)
- Adapts tone and response strategy dynamically

💬 **Conversation Memory**
- Maintains short-term context across turns
- References previous emotional themes naturally

🎨 **Emotion-Aware UI**
- Sidebar dynamically reflects user emotional state
- Includes:
  - 🌿 “Right now” emotional summary
  - 🧘 Mood ring (color-coded emotional state)
- Real-time updates based on detected emotion

🚨 **Crisis Detection System**
- Detects high-risk emotional signals (self-harm, hopelessness)
- Triggers:
  - Critical state indicator in UI
  - Emotion-aware response handling
- Prioritized over normal conversation flow

🗂 **Multi-Conversation Support**
- Users can create and switch between multiple chats
- Conversations are stored and retrieved dynamically

🔁 **Non-Repetitive Responses**
- Dynamic response generation using LLM
- Avoids repeated phrasing patterns
- More natural and human-like interaction

🌬 **Calm Tools**
- Guided breathing
- Grounding suggestions
- Reflection prompts

🌱 **Gentle Reminders**
- Soft affirmations to maintain a supportive environment

---

## 🧠 System Architecture
TalkSpace follows a hybrid architecture combining machine learning classification with rule-based conversational logic.

The system processes user input through multiple stages to generate context-aware, emotionally aligned responses.

### Pipeline

User Input → Text Vectorization → ML Prediction → Emotion Detection → Response Generation → Memory Update

### 🧩 Component Overview

| Component                  | Description |
|---------------------------|------------|
| Text Vectorization        | Converts user input into TF-IDF numerical features |
| ML Classifier             | Predicts emotional intensity (probability score) |
| Emotion Detection Layer   | Identifies emotional themes using keyword signals |
| Response Strategy Engine  | Generates responses using validation, support, and suggestions |
| Conversation Memory       | Maintains short-term context for multi-turn conversations |
| UI Layer (Streamlit)      | Provides chat interface and emotional visualization |
| Crisis Detection Layer    | Identifies high-risk emotional signals and overrides response strategy |

### 🔍 Decision Logic

The response strategy is dynamically selected based on:

- predicted emotional intensity (ML output)
- detected emotion category (rule-based layer)
- selected conversation mode (user preference)

This hybrid approach allows the system to remain both adaptive and controllable.

Each component works together to ensure responses are:
- emotionally aware
- context-aware
- conversationally natural


### 🎨 UI Layer

Built with Streamlit, the interface is designed to feel:
- minimal
- calm
- conversational

Includes:
- chat interface
- mood visualization
- emotional signal tracking
- calming interaction tools


---

## ⚙️ Tech Stack

| Category        | Tools |
|----------------|------|
| Language       | Python |
| Framework      | Streamlit |
| ML Library     | Scikit-learn |
| Data Handling  | Pandas |
| Model Storage  | Joblib |
| Backend / DB   | Supabase |
| LLM API        | OpenRouter (LLaMA 3) |

A trained machine learning model estimates emotional intensity and guides conversation responses.

---

## ⚙️ Technical Highlights

- Designed a **hybrid conversational architecture** combining ML classification with rule-based response logic  
- Implemented **TF-IDF based text vectorization and probabilistic prediction using Scikit-learn**  
- Built an **emotion-aware response system** driven by keyword-based signal detection  
- Developed a **dynamic response strategy engine** adapting to emotional intensity and context  
- Implemented **multi-turn conversation memory** using session-based state tracking  
- Integrated **real-time UI and interaction flow** using Streamlit  
- Designed and implemented **calming tools (guided breathing, grounding prompts)** 
- Implemented **real-time emotion-driven UI updates** (mood ring + sidebar state)
- Designed a **crisis detection and response override system**
- Integrated **multi-conversation persistence using Supabase**
- Built **non-repetitive response generation using LLM (OpenRouter)** 

---

# 🚀 Running Locally

Clone the repository:

```
git clone https://github.com/Keertilata20/talkspace-ai
```

Navigate into the project:

```
cd talkspace-ai
```

Install dependencies:

```
pip install -r requirements.txt
```

Run the app:

```
streamlit run app.py
```

---

# 🔭 Future Improvements

Planned upgrades include:

* richer emotional understanding
* improved conversation memory
* animated mood ring and intensity-based UI
* voice-based interaction
* expanded calming tools

---

# ⚠️ Disclaimer

TalkSpace is **not a medical or diagnostic tool**.

It is designed as a supportive conversation environment only.

If you are experiencing severe emotional distress, please consider reaching out to a trained professional or someone you trust.

---

# 👤 Author

Built with care while exploring the intersection of:

**AI • conversation design • human-centered technology**
