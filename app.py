import streamlit as st
from openapi import get_travel_ideas
from weather import get_weather
import openai
import os
from dotenv import load_dotenv
load_dotenv()


st.title("Travel buddy for fun travelling")

interests = st.text_input("What are your travel interests? (e.g. beaches, history, adventure)")
budget = st.text_input("Budget (optional, e.g. $1000, 'low', 'high')")
season = st.text_input("Season (optional, e.g. summer, winter)")

if st.button("Suggest Destinations"):
    if not interests:
        st.warning("Please enter your interests.")
    else:
        with st.spinner("Thinking..."):
            ideas = get_travel_ideas(interests, budget, season)
        st.subheader("🌟 Suggested Destinations")
        st.write(ideas)
        st.subheader("🌦️ Weather Info")
        for line in ideas.split("\n"):
            if line.strip() and not line.strip().startswith(("1.", "2.", "3.")):
                city = line.strip().split(',')[0]
                weather = get_weather(city)
                st.write(weather)