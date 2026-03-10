import streamlit as st
import pandas as pd

def mood_analysis(data):
    df = pd.DataFrame(data)

    st.subheader("Weekly Mood Analysis")

    mood_count = df["mood"].value_counts()

    st.bar_chart(mood_count)


def stress_prediction(data, stress):

    df = pd.DataFrame(data)

    st.subheader("Stress Prediction")

    avg_stress = df["stress"].mean()

    if stress > avg_stress:
        st.warning("Your stress level is higher than your average.")
    else:
        st.success("Your stress level is normal.")

