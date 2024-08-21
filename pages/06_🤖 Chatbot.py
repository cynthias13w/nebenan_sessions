import streamlit as st
import random
import time

st.title("Mood Booster Bot 🤖")

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat messages from history on app rerun
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Mood-based responses
mood_responses = {
    "happy": [
        "That's awesome! Keep spreading those good vibes! 🌟",
        "I'm glad to hear that! Let's keep the positivity going!",
        "Yay! Happiness looks good on you! 😊"
    ],
    "sad": [
        "I'm sorry you're feeling down. Here's a virtual hug! 🤗",
        "It's okay to feel sad sometimes. I'm here for you!",
        "Take it easy, and remember, it's okay to ask for help if you need it."
    ],
    "stressed": [
        "Take a deep breath. You got this! 💪",
        "Stress is temporary. Let's find some calm together. 🧘",
        "Remember, one step at a time. You're doing great!"
    ],
    "excited": [
        "That's fantastic! Let's celebrate your excitement! 🎉",
        "Excitement is contagious! What's got you so pumped?",
        "Channel that energy into something amazing! 🚀"
    ],
    "bored": [
        "When boredom strikes, it's the perfect moment for a little adventure, even if it's just in your imagination!",
        "Boredom is just the universe telling you it's time for a little fun! Maybe it's a good time to dive into a hobby.",
        "Boredom can be the gateway to something exciting. Maybe it's time to explore a new interest or revisit an old one."
    ]
}

# Accept user input
if prompt := st.chat_input("How are you feeling today?"):
    # Display user message in chat message container
    with st.chat_message("user"):
        st.markdown(prompt)
    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": prompt})

    # Determine the mood based on user input
    mood = None
    for key in mood_responses.keys():
        if key in prompt.lower():
            mood = key
            break

    # Generate a response based on the detected mood
    def response_generator(mood):
        if mood:
            response = random.choice(mood_responses[mood])
        else:
            response = "I'm here to boost your mood! Tell me more about how you're feeling. Are you happy, sad, stressed, excited or bored?"
        for word in response.split():
            yield word + " "
            time.sleep(0.05)

    # Display assistant response in chat message container
    with st.chat_message("assistant"):
        response = "".join(response_generator(mood))
        st.markdown(response)

    # Add assistant response to chat history
    st.session_state.messages.append({"role": "assistant", "content": response})
