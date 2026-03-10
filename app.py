import streamlit as st
import datetime
import pandas as pd
import matplotlib.pyplot as plt

from file_han import create_file, save_entry, read_data
from analysis import mood_analysis, stress_prediction
from recom import study_recommendation

st.set_page_config(
    page_title="Student Mood Tracker",
    layout="wide"
)

st.title("Student Mood & Stress Tracker Dashboard")

create_file()

menu = st.sidebar.selectbox(
    "Navigation Menu",
    ["Add Entry", "Mood History", "Analysis", "Recommendations"]
)

if menu == "Add Entry":
    st.header("Add Daily Mood Entry")
    
    mood = st.selectbox(
        "Select your mood",
        ["Happy", "Neutral", "Sad", "Stressed"]
    )
    
    stress = st.slider("Stress Level", 0, 10)
    
    note = st.text_area("Write about your day")
    
    date = datetime.date.today()
    
    if st.button("Save Entry"):
        save_entry(date, mood, stress, note)
        st.success("Entry saved successfully!")

elif menu == "Mood History":
    st.header("Mood History")
    
    data = read_data()
    
    if data:
        df = pd.DataFrame(data)
        st.dataframe(df)
    else:
        st.info("No data available yet.")

elif menu == "Analysis":
    st.header("Mood Analysis")
    
    data = read_data()
    
    if data:
        df = pd.DataFrame(data)
        
        st.subheader("Your Mood Patterns")
        mood_counts = df['mood'].value_counts()
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.write("**Mood Frequency**")
            for mood, count in mood_counts.items():
                st.write(f"{mood}: {count} times")
        
        with col2:
            avg_stress = df['stress'].astype(float).mean()
            st.write(f"**Average Stress Level:** {avg_stress:.1f}/10")
            
            if avg_stress < 4:
                st.write(" You're managing stress well!")
            elif avg_stress < 7:
                st.write(" Moderate stress levels")
            else:
                st.write(" High stress - consider taking breaks")
        
        st.subheader(" Mood Distribution")
        
        fig2, ax2 = plt.subplots(figsize=(8, 5))
        
        moods = list(mood_counts.index)
        counts = list(mood_counts.values)
        
        colors2 = ['blue', 'gray', 'purple', 'red']
        bars2 = ax2.bar(moods, counts, color=colors2[:len(moods)])
        ax2.set_xlabel('Mood')
        ax2.set_ylabel('Frequency')
        ax2.set_title('How Often You Feel Each Mood')
        
        for bar, count in zip(bars2, counts):
            height = bar.get_height()
            ax2.text(bar.get_x() + bar.get_width()/2., height,
                   f'{count}', ha='center', va='bottom')
        
        st.pyplot(fig2)
        

            
    else:
        st.info("No data available for analysis.")

elif menu == "Recommendations":
    st.header("Study Recommendations")
    
    mood = st.selectbox(
        "Select your current mood",
        ["Happy", "Neutral", "Sad", "Stressed"]
    )
    
    st.subheader(f"Recommendations for {mood} mood:")
    
    if mood == "Happy":
        st.write(" **Great time to learn!**")
        st.write("- Tackle difficult subjects")
        st.write("- Help classmates - teaching reinforces learning")
        st.write("- Set challenging study goals")
        
    elif mood == "Neutral":
        st.write(" **Steady study time**")
        st.write("- Review notes and revise")
        st.write("- Complete pending assignments")
        st.write("- Practice problems or exercises")
        
    elif mood == "Sad":
        st.write(" **Take care of yourself first**")
        st.write("- Take a short walk to refresh")
        st.write("- Study with a friend for support")
        st.write("- Focus on easy wins to build confidence")
        
    elif mood == "Stressed":
        st.write(" **Pause and breathe**")
        st.write("- Take a 5-minute break first")
        st.write("- Break study sessions into 25-min chunks")
        st.write("- Do light review, avoid new tough topics")
        st.write("- Drink water and stretch")
    
    st.divider()
    st.info(" Remember: Take regular breaks and stay hydrated!")
st.markdown("""
<style>
.stApp {
    background-color: #1E1E2F;
    primary-color: #00ADB5;
    sidebar-color: #393E46;
    text-color: #EEEEEE;gi
}
</style>
""", unsafe_allow_html=True)