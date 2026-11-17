import streamlit as st

st.set_page_config(page_title="MindCheck", page_icon="💚")
st.title("💚 MindCheck")
st.write("Check in with your mental health in under 2 minutes. Free. No login.")

mood = st.slider("1. How is your MOOD today? 1 = Very low, 5 = Great", 1, 5, 3)
stress = st.slider("2. How STRESSED are you? 1 = Not at all, 5 = Very stressed", 1, 5, 3)
sleep = st.slider("3. How did you SLEEP? 1 = Very bad, 5 = Great", 1, 5, 3)

if st.button("Get My Wellness Score"):
    score = round(((mood + (6-stress) + sleep) / 15) * 100)
    st.subheader(f"Your Wellness Score: {score}/100")
    if score >= 70:
        st.success("You're doing well! Keep it up 💚")
        st.write("Tip: Take a short walk, drink water, and keep your routine.")
    elif score >= 40:
        st.warning("You're a bit stressed. Take care of yourself today.")
        st.write("Tip: Try 5 minutes of deep breathing, take a break from your phone, and talk to a friend.")
    else:
        st.error("You seem to be struggling today. Please reach out.")
        st.write("Tip: Talk to a school counsellor, a trusted adult, or call SADAG 0800 567 567. You are not alone.")
    st.write("---")
    st.write("Progress Tracker: Come back tomorrow and check in again to see your pattern.")