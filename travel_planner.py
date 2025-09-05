import streamlit as st

st.title("Personalized Travel Itinerary Planner")

# User inputs
destination = st.text_input("Enter your travel destination:")
budget = st.selectbox("What's your budget?", ["Low", "Moderate", "High"])
duration = st.slider("How many days?", min_value=1, max_value=30)
purpose = st.text_area("Purpose of the trip (e.g., leisure, business, adventure):")
preferences = st.multiselect(
    "Select your preferences:",
    ["Historical Sites", "Nature", "Food & Dining", "Adventure Sports", "Relaxation", "Shopping"]
)

if st.button("Generate Itinerary"):
    # Example response (replace with AI-generated itinerary logic)
    st.subheader("Your Itinerary")
    st.write("Day 1: Explore the local attractions...")
