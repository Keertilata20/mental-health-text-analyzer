import streamlit as st
import joblib

# load model
model = joblib.load("model/depression_model.pkl")
vectorizer = joblib.load("model/vectorizer.pkl")

st.set_page_config(page_title="Mental Health AI", page_icon="🧠")

st.title("🧠 Mental Health AI Assistant")

st.write(
"""
Talk about how you're feeling and the AI will analyze emotional signals.

⚠️ This tool is **not a medical diagnosis**.
"""
)

# store chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# show previous messages
for msg in st.session_state.messages:
    st.chat_message(msg["role"]).write(msg["content"])

# chat input
user_input = st.chat_input("Tell me how you're feeling...")

low_information_words = ["hi","hello","hey","ok","okay","lol","yo"]

if user_input:

    st.chat_message("user").write(user_input)

    st.session_state.messages.append({
        "role": "user",
        "content": user_input
    })

    text = user_input.lower().strip()

    if len(text.split()) < 3 or text in low_information_words:

        response = """
Could you tell me a bit more about how you're feeling?

Example:
• "I feel tired and unmotivated lately"
• "I feel lonely and disconnected from people"
"""

    else:

        vector = vectorizer.transform([user_input])
        prob = model.predict_proba(vector)[0][1]

        if prob > 0.65:
            response = f"""
⚠️ I detect strong signs of emotional distress.

Confidence: {prob*100:.2f}%

If you're struggling, consider talking to someone you trust or a professional.
You are not alone ❤️
"""

        elif prob > 0.40:
            response = f"""
I detect some emotional distress signals.

Confidence: {prob*100:.2f}%

Take care of yourself and consider reaching out to someone supportive.
"""

        else:
            response = f"""
I don't detect strong depression signals.

Confidence: {prob*100:.2f}%

But your feelings still matter. Take care of yourself.
"""

    st.chat_message("assistant").write(response)

    st.session_state.messages.append({
        "role": "assistant",
        "content": response
    })