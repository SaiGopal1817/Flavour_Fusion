# ================================
# Flavour Fusion: AI-Driven Recipe Blogging (Premium UI)
# ================================

import streamlit as st
import google.generativeai as genai
import os
import random
from dotenv import load_dotenv
import streamlit.components.v1 as components


# -----------------------
# Load API Key
# -----------------------
load_dotenv()
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# Latest Gemini model
model = genai.GenerativeModel("gemini-flash-latest")


# -----------------------
# GSAP Animated Hero Section
# -----------------------
components.html("""
<!DOCTYPE html>
<html>
<head>
<script src="https://cdnjs.cloudflare.com/ajax/libs/gsap/3.12.2/gsap.min.js"></script>
<style>
body {
  margin:0;
  overflow:hidden;
  background: linear-gradient(135deg, #0f2027, #2c5364);
}

.hero {
  height: 280px;
  display:flex;
  justify-content:center;
  align-items:center;
  flex-direction:column;
  color:white;
  font-family: 'Poppins', sans-serif;
}

.title {
  font-size: 42px;
  font-weight: bold;
}

.subtitle {
  font-size: 18px;
  opacity:0.8;
}

.circle {
  position:absolute;
  border-radius:50%;
  background: rgba(255,255,255,0.12);
}
</style>
</head>

<body>

<div class="hero">
  <div class="title">Flavour Fusion 🍲</div>
  <div class="subtitle">AI Powered Recipe Experience</div>
</div>

<script>

// floating animation
for(let i=0;i<20;i++){
  let c = document.createElement("div");
  c.classList.add("circle");
  document.body.appendChild(c);

  let size = Math.random()*80+20;
  gsap.set(c,{
    width:size,
    height:size,
    x:Math.random()*window.innerWidth,
    y:Math.random()*window.innerHeight
  });

  gsap.to(c,{
    y:"+=120",
    duration:Math.random()*6+3,
    repeat:-1,
    yoyo:true,
    ease:"sine.inOut"
  });
}

// title animation
gsap.from(".title",{y:-60, opacity:0, duration:1.5});
gsap.from(".subtitle",{y:60, opacity:0, duration:1.5});

</script>

</body>
</html>
""", height=300)


# -----------------------
# Joke Generator
# -----------------------
def get_joke():
    jokes = [
        "Why do programmers prefer dark mode? Because light attracts bugs!",
        "Why do Python developers wear glasses? Because they can’t C!",
        "Why was the JavaScript developer sad? Because he didn’t Node how to Express himself!",
        "Why do programmers hate nature? Too many bugs!",
    ]
    return random.choice(jokes)


# -----------------------
# Recipe Generator
# -----------------------
def recipe_generation(topic, words, language):
    joke = get_joke()
    st.success(joke)

    prompt = f"""
    Write a detailed and engaging recipe blog in {language} about {topic}.
    Length: {words} words.

    Include:
    Introduction, ingredients, steps, tips, and conclusion.
    """

    response = model.generate_content(prompt)
    return response.text


# -----------------------
# Nutrition Generator
# -----------------------
def nutrition_summary(topic):
    prompt = f"Give a short nutrition summary for {topic}"
    response = model.generate_content(prompt)
    return response.text


# -----------------------
# Main UI
# -----------------------
st.write("Create stunning AI-powered recipe blogs with animations.")

dark = st.toggle("🌙 Dark Mode")

topic = st.text_input("Enter your recipe topic")

word_count = st.slider("Word count", 200, 2000, 800)

language = st.selectbox(
    "Language",
    ["English", "Hindi", "Telugu", "Spanish", "French"]
)

if st.button("✨ Generate Recipe"):
    if topic:
        with st.spinner("Cooking your recipe... 🍳"):
            output = recipe_generation(topic, word_count, language)

        st.subheader("📖 Recipe Blog")
        st.write(output)

        st.subheader("🥗 Nutrition Summary")
        nutrition = nutrition_summary(topic)
        st.write(nutrition)

        st.download_button(
            "Download",
            output,
            file_name="recipe.txt"
        )
    else:
        st.warning("Please enter a topic.")
