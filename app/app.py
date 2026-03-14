import streamlit as st
import joblib
import random
import time

# Load ML model
model = joblib.load("model/depression_model.pkl")
vectorizer = joblib.load("model/vectorizer.pkl")

st.set_page_config(
    page_title="TalkSpace AI",
    page_icon="🌿",
    layout="wide"
)

# Warm UI theme
st.markdown("""
<style>
body {
    background-color:#faf7f2;
}

.stChatMessage {
    padding:14px;
    border-radius:14px;
}

[data-testid="stChatInput"] {
    border-radius:20px;
}

.block-container {
    padding-top:2rem;
}

</style>
""", unsafe_allow_html=True)

# Header
st.markdown("""
# 🌿 TalkSpace AI
*A quiet place to talk.*

Share what's on your mind.  
I'm here to listen.
""")

# Sidebar
mode = st.sidebar.selectbox(
    "Conversation Style",
    ["Supportive Friend", "Counselor"]
)

if st.sidebar.button("Clear Conversation"):
    st.session_state.messages = []
    st.rerun()

# Emotion keywords
emotion_keywords = {
    "loneliness": ["lonely","alone","isolated","nobody"],
    "sadness": ["sad","hopeless","empty","worthless"],
    "stress": ["tired","exhausted","overwhelmed","burnt"],
    "social": ["ignored","rejected","friends","roommates"]
}

def detect_emotion(text):
    text = text.lower()
    for emotion, words in emotion_keywords.items():
        for w in words:
            if w in text:
                return emotion
    return "general"


# Coping suggestions
def coping_suggestions():

    suggestions = [
        "Take 5 slow deep breaths and focus on breathing.",
        "Step outside for a short walk or fresh air.",
        "Write what you're feeling in a journal.",
        "Send a small message to someone you trust.",
        "Listen to a song that comforts you.",
        "Drink some water and pause for a moment."
    ]

    chosen = random.sample(suggestions,3)
    return "\n".join([f"• {c}" for c in chosen])


# Emotion empathy
emotion_empathy = {
    "loneliness":[
        "Feeling alone for a long time can be really heavy.",
        "Humans naturally need connection. Feeling lonely can hurt deeply."
    ],
    "stress":[
        "It sounds like a lot has been draining your energy.",
        "That kind of exhaustion can slowly build up."
    ],
    "sadness":[
        "That kind of feeling can weigh on someone quietly.",
        "It's understandable that this would affect you."
    ],
    "social":[
        "Difficult social environments can affect us more than we realize.",
        "Being around people who make you feel small can be exhausting."
    ],
    "general":[
        "Thanks for sharing that.",
        "I'm really glad you felt comfortable saying that."
    ]
}


# Friend reactions
friend_support = [
    "I'm here with you.",
    "You don't have to carry this alone.",
    "Your feelings make sense.",
    "Talking about it is a strong step."
]


# Response generator
def generate_response(prob, emotion, mode):

    empathy = random.choice(emotion_empathy.get(emotion,emotion_empathy["general"]))
    support = random.choice(friend_support)
    suggestions = coping_suggestions()

    if mode == "Supportive Friend":

        if prob > 0.65:

            return f"""
{empathy}

{support}

Feeling this way for a long time can be exhausting.

🌿 Something small that might help right now:

{suggestions}

You’re not alone in this.
"""

        elif prob > 0.40:

            return f"""
{empathy}

{support}

Sometimes even small things can shift the feeling a little.

🌿 Maybe try one of these:

{suggestions}
"""

        else:

            return f"""
{support}

If you'd like, you can tell me more about what's been on your mind.
"""

    else:

        if prob > 0.65:

            return f"""
Thank you for sharing that.

{empathy}

Sometimes when emotions build up they can start to feel overwhelming.

🌿 One grounding step you might try:

{suggestions}

If you'd like, you can tell me more about what's been happening.
"""

        elif prob > 0.40:

            return f"""
I appreciate you opening up.

{empathy}

🌿 One small step that sometimes helps:

{suggestions}
"""

        else:

            return """
Thank you for reflecting on how you're feeling.

If you'd like, you can share more about what's on your mind.
"""


# Chat memory
if "messages" not in st.session_state:
    st.session_state.messages = []

# Welcome message
if len(st.session_state.messages) == 0:
    st.info("""
You can talk about anything that's on your mind.

Examples:
• "I feel lonely lately"
• "I'm overwhelmed with work"
• "My roommates make me feel inferior"

This is a space to talk.
""")

# Show chat history
for msg in st.session_state.messages:
    st.chat_message(msg["role"]).write(msg["content"])


# User input
user_input = st.chat_input("Share what's on your mind...")

greeting_words = ["hi","hello","hey","yo"]
closing_words = ["bye","thanks","thank you","no thanks","im done","i'm done"]

if user_input:

    st.chat_message("user").write(user_input)

    st.session_state.messages.append({
        "role":"user",
        "content":user_input
    })

    text = user_input.lower().strip()

    # Greeting
    if text in greeting_words:

        response = random.choice([
            "Hey. I'm here. How are you feeling today?",
            "Hi there. What's been on your mind lately?",
            "Hello. What would you like to talk about today?",
            "Hey. I'm listening."
        ])

    # Closing
    elif any(c in text for c in closing_words):

        response = random.choice([
            "Take care of yourself. I'm here anytime you want to talk.",
            "That's completely okay. Be kind to yourself today.",
            "No worries at all. I'm here whenever you want to come back."
        ])

    else:

        vector = vectorizer.transform([user_input])
        prob = model.predict_proba(vector)[0][1]

        emotion = detect_emotion(user_input)

        response = generate_response(prob, emotion, mode)

    # Thinking indicator
    with st.chat_message("assistant"):

        placeholder = st.empty()
        placeholder.markdown("💭 *thinking...*")
        time.sleep(1)

        typed = ""
        for char in response:
            typed += char
            placeholder.markdown(typed)
            time.sleep(0.01)

    st.session_state.messages.append({
        "role":"assistant",
        "content":response
    })