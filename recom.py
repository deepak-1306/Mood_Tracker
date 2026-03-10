import streamlit as st

def study_recommendation(mood):

    st.subheader("Study Recommendation")

    if mood == "Happy":
        st.success("Great mood! Try studying difficult topics.")

    elif mood == "Neutral":
        st.info("You can revise notes or solve practice questions.")

    elif mood == "Sad":
        st.info("Take a short break and study light topics.")

    elif mood == "Stressed":
        st.warning("Relax for some time before studying.")

