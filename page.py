import streamlit as st
import pandas as pd
import joblib


st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Silkscreen&display=swap');

/* Apply to whole app layout */
html, body, [class*="css"] {
    font-family: 'Silkscreen', monospace !important;
    background-color: #FFF7DC !important;
    color: #3E2723 !important;
}

/* General typography scaling */
h1, h2, h3 {
    font-family: 'Silkscreen', monospace !important;
    font-size: 24px !important;
}
h4, h5, h6 {
    font-size: 18px !important;
}
p, label, .stTextInput, .stRadio, .stSlider, .stSelectbox, .stMultiSelect, .stTextArea, .stButton, .stCheckbox {
    font-family: 'Silkscreen', monospace !important;
    font-size: 14px !important;
}

/* Sliders and buttons for banana theme */
.stSlider > div[data-baseweb="slider"] {
    background-color: #FFE6A7 !important;
    padding: 8px;
    border-radius: 10px;
}
.stButton>button {
    background-color: #FFB347 !important;
    color: black !important;
    border: none;
    padding: 10px 20px;
    border-radius: 6px;
    font-weight: bold;
    box-shadow: 2px 2px 0 #999;
    font-size: 14px !important;
}
</style>
""", unsafe_allow_html=True)
import lightgbm as lgb
model = lgb.Booster(model_file="lgbm_model.txt")



st.image("tetx.png") 
st.title("Let's Check Your Life Score!")

left, right = st.columns([1, 2])

with left:
    st.image("monkeypls-monkey-dancing.gif")  # Replace with your own monkey image

with right:
    st.write(" Yo! I'm Monkey Peel-o")
    st.write("I might look like a monkey... because I am one. ")
    st.success("🍌 My life score predictions are **about 60%–70% accurate**… unless I get distracted by bananas.")
    st.caption("No guarantees. I'm literally a monkey with a model.")

st.markdown("Answer these simple questions — your banana buddy is listening! 🍌")


# -------------------------------
# 😄 HOW YOU FEEL
# -------------------------------
st.header("😄 How You Feel")

happiness = st.radio("How happy are you these days?", [
    (1, "Very happy"), (2, "Rather happy"), (3, "Not very happy"), (4, "Not at all happy")
], format_func=lambda x: x[1])[0]

health = st.radio("How is your health?", [
    (1, "Very good"), (2, "Good"), (3, "Fair"), (4, "Poor"), (5, "Very poor")
], format_func=lambda x: x[1])[0]

# Freedom of choice (scaled from 1–10 → 1–8)
freedom_options = {
    "Very Restricted": 1,
    "Somewhat Restricted": 2,
    "Somewhat Free": 3,
    "Completely Free": 4
}

# Freedom of choice with hardcoded scaled values
freedom_options = {
    "Limited Freedom": 1,
    "Moderate Freedom": 6,
    "Full Freedom": 10
}

selected_freedom_label = st.radio(
    "How much freedom do you feel in making your own life choices?",
    options=list(freedom_options.keys())
)

freedom = freedom_options[selected_freedom_label]

st.write(f"Selected: **{selected_freedom_label}** → Scaled value: **{freedom}**")

#freedom = round(1 + ((freedom_input - 1) / 9) * 7, 2)
# Financial satisfaction (scaled from 1–3 → 1–8, no decimals)
# Financial satisfaction with hardcoded scaled values
financial_options = {
    "Dissatisfied": 1,
    "Neutral": 6,
    "Satisfied": 8
}

selected_finance_label = st.radio(
    "How satisfied are you with your financial situation?",
    options=list(financial_options.keys())
)

financial_satisfaction = financial_options[selected_finance_label]

st.write(f"Selected: **{selected_finance_label}** → Scaled value: **{financial_satisfaction}**")


#financial_satisfaction = round(1 + ((financial_satisfaction_input - 1) / 9) * 7, 2)



# -------------------------------
# 🍽️ BASIC NEEDS
# -------------------------------
st.header("🍽️ Did You Face Any Problems This Year?")

went_without_food = st.radio("Did you ever go without food?", [
    (1, "Often"), (2, "Sometimes"), (3, "Rarely"), (4, "Never")
], format_func=lambda x: x[1])[0]

went_without_medicine = st.radio("Did you miss medicine or treatment?", [
    (1, "Often"), (2, "Sometimes"), (3, "Rarely"), (4, "Never")
], format_func=lambda x: x[1])[0]

went_without_cash = st.radio("Did you run out of money?", [
    (1, "Often"), (2, "Sometimes"), (3, "Rarely"), (4, "Never")
], format_func=lambda x: x[1])[0]

went_without_shelter = st.radio("Did you not have a place to stay?", [
    (1, "Often"), (2, "Sometimes"), (3, "Rarely"), (4, "Never")
], format_func=lambda x: x[1])[0]

unsafe_at_home = st.radio("Did you feel unsafe at home?", [
    (1, "Often"), (2, "Sometimes"), (3, "Rarely"), (4, "Never")
], format_func=lambda x: x[1])[0]

living_standard_vs_parents = st.radio("Compared to your parents, are you better off?", [
    (1, "Better off"), (2, "Worse off"), (3, "About the same")
], format_func=lambda x: x[1])[0]

# -------------------------------
# 💖 VALUES
# -------------------------------
st.header("💖 What Matters to You?")

importance_family = st.radio("Is family important to you?", [
    (1, "Very important"), (2, "Important"), (3, "Not very"), (4, "Not at all")
], format_func=lambda x: x[1])[0]

importance_friends = st.radio("Are friends important?", [
    (1, "Very important"), (2, "Important"), (3, "Not very"), (4, "Not at all")
], format_func=lambda x: x[1])[0]

importance_work = st.radio("Is work important?", [
    (1, "Very important"), (2, "Important"), (3, "Not very"), (4, "Not at all")
], format_func=lambda x: x[1])[0]

importance_religion = st.radio("Is religion important?", [
    (1, "Very important"), (2, "Important"), (3, "Not very"), (4, "Not at all")
], format_func=lambda x: x[1])[0]

importance_leisure_time = st.radio("Is free time important?", [
    (1, "Very important"), (2, "Important"), (3, "Not very"), (4, "Not at all")
], format_func=lambda x: x[1])[0]

# -------------------------------
# 🧒 CHILD VALUES
# -------------------------------
st.header("🧒 What Should Kids Learn?")

teach_responsibility = st.radio("Should kids learn responsibility?", [(1, "Yes"), (0, "No")],
                                format_func=lambda x: x[1])[0]
teach_determination = st.radio("Should kids learn to never give up?", [(1, "Yes"), (0, "No")],
                               format_func=lambda x: x[1])[0]
teach_religion = st.radio("Should kids learn religion?", [(1, "Yes"), (0, "No")],
                          format_func=lambda x: x[1])[0]

# -------------------------------
# 🎯 GOALS & DUTIES
# -------------------------------
st.header("🎯 Your Life Goals")

goal_make_parents_proud = st.radio("Do you try to make your parents proud?", [
    (1, "Strongly agree"), (2, "Agree"), (3, "Disagree"), (4, "Strongly disagree")
], format_func=lambda x: x[1])[0]

duty_care_parents = st.radio("Should children care for their parents?", [
    (1, "Strongly agree"), (2, "Agree"), (3, "Disagree"), (4, "Strongly disagree")
], format_func=lambda x: x[1])[0]

work_as_duty = st.radio("Is work a duty to society?", [
    (1, "Strongly agree"), (2, "Agree"), (3, "Disagree"), (4, "Strongly disagree")
], format_func=lambda x: x[1])[0]

# -------------------------------
# 🤝 TRUST
# -------------------------------
st.header("🤝 Trust-o-Meter")

general_trust = st.radio("Can most people be trusted?", [
    (1, "Most people can be trusted"), (2, "Need to be very careful")
], format_func=lambda x: x[1])[0]

trust_family = st.radio("Do you trust your family?", [
    (1, "Trust completely"), (2, "Trust somewhat"), (3, "Don't trust much"), (4, "Don't trust at all")
], format_func=lambda x: x[1])[0]

trust_neighborhood = st.radio("Do you trust your neighbors?", [
    (1, "Trust completely"), (2, "Trust somewhat"), (3, "Don't trust much"), (4, "Don't trust at all")
], format_func=lambda x: x[1])[0]

trust_known_people = st.radio("Do you trust people you know?", [
    (1, "Trust completely"), (2, "Trust somewhat"), (3, "Don't trust much"), (4, "Don't trust at all")
], format_func=lambda x: x[1])[0]

trust_strangers = st.radio("Do you trust strangers?", [
    (1, "Trust completely"), (2, "Trust somewhat"), (3, "Don't trust much"), (4, "Don't trust at all")
], format_func=lambda x: x[1])[0]

trust_other_religions = st.radio("Do you trust people of other religions?", [
    (1, "Trust completely"), (2, "Trust somewhat"), (3, "Don't trust much"), (4, "Don't trust at all")
], format_func=lambda x: x[1])[0]

trust_other_nationalities = st.radio("Do you trust people from other countries?", [
    (1, "Trust completely"), (2, "Trust somewhat"), (3, "Don't trust much"), (4, "Don't trust at all")
], format_func=lambda x: x[1])[0]

# -------------------------------
# 🏛️ INSTITUTIONS
# -------------------------------
st.header("🏛️ How Much Do You Trust These?")

confidence_police = st.radio("Do you trust the police?", [
    (1, "A lot"), (2, "Quite a lot"), (3, "Not much"), (4, "None at all")
], format_func=lambda x: x[1])[0]

confidence_courts = st.radio("Do you trust the courts?", [
    (1, "A lot"), (2, "Quite a lot"), (3, "Not much"), (4, "None at all")
], format_func=lambda x: x[1])[0]

confidence_government = st.radio("Do you trust the government?", [
    (1, "A lot"), (2, "Quite a lot"), (3, "Not much"), (4, "None at all")
], format_func=lambda x: x[1])[0]

# -------------------------------
# 📤 SUBMIT
# -------------------------------
if st.button("🍌 See My Life-O-Peel Score"):
    features = {
        "happiness": happiness,
        "self_rated_health": health,
        "freedom_of_choice": freedom,
        "financial_satisfaction": financial_satisfaction,
        "went_without_food": went_without_food,
        "went_without_medicine": went_without_medicine,
        "went_without_cash": went_without_cash,
        "went_without_shelter": went_without_shelter,
        "unsafe_at_home": unsafe_at_home,
        "living_standard_vs_parents": living_standard_vs_parents,
        "importance_family": importance_family,
        "importance_friends": importance_friends,
        "importance_work": importance_work,
        "importance_religion": importance_religion,
        "importance_leisure_time": importance_leisure_time,
        "teach_responsibility": teach_responsibility,
        "teach_determination": teach_determination,
        "teach_religion": teach_religion,
        "goal_make_parents_proud": goal_make_parents_proud,
        "duty_care_parents": duty_care_parents,
        "work_as_duty": work_as_duty,
        "general_trust": general_trust,
        "trust_family": trust_family,
        "trust_neighborhood": trust_neighborhood,
        "trust_known_people": trust_known_people,
        "trust_strangers": trust_strangers,
        "trust_other_religions": trust_other_religions,
        "trust_other_nationalities": trust_other_nationalities,
        "confidence_police": confidence_police,
        "confidence_courts": confidence_courts,
        "confidence_government": confidence_government,

        # Interaction features
        "trust_x_money": trust_strangers * financial_satisfaction,
        "health_x_food": health * went_without_food,
        "safety": trust_family * trust_neighborhood * trust_strangers * general_trust,
        "finance_x_choice": freedom * financial_satisfaction,

        # Engineered features
        "safety_score": (
            confidence_police +
            confidence_courts +
            confidence_government +
            (5 - unsafe_at_home)
        ) / 4,

        "hardship_score": (
            went_without_food +
            went_without_medicine +
            went_without_cash +
            went_without_shelter
        ) / 4,

        "family_value_score": (
            importance_family +
            goal_make_parents_proud +
            duty_care_parents +
            trust_family
        ) / 4,

        "religiosity_score": (
            importance_religion +
            teach_religion
        ) / 2,

        "social_trust_score": (
            general_trust +
            trust_strangers +
            trust_known_people +
            trust_neighborhood +
            trust_other_religions +
            trust_other_nationalities
        ) / 6,

        "satisfaction_factor_score": (
            freedom +
            health +
            happiness +
            financial_satisfaction
        ) / 4,

        "education_value_score": (
            teach_determination +
            teach_responsibility +
            work_as_duty
        ) / 3,

        "personal_aspiration_score": (
            importance_work +
            importance_friends +
            importance_leisure_time +
            living_standard_vs_parents
        ) / 4,
    }

    # Add country code if used
    for code in country_lookup.values():
        features[f"country_code_{code}"] = 1 if code == selected_country_code else 0

    # Create DataFrame and reorder columns to match model
    df = pd.DataFrame([features])
    df = df[model.feature_names_in_]

    # Apply transformations if needed (e.g., log) — uncomment and adapt as needed
    # df["financial_satisfaction"] = np.log1p(df["financial_satisfaction"])

    # Predict
    prediction = model.predict(df)[0]

    # Correct mapping based on your class labels (1 = low, 2 = medium, 3 = high)
    if prediction == 3:
        monkey_message = "🍌 *Ooo-oo-aa-aa!* You're doing amazing! Life’s good, you’re on top of the banana tree! 🍃"
        bg_color = "#DFFFD6"  # light green
        text_color = "#1B5E20"  # dark green
    elif prediction == 1:
        monkey_message = "😟 *Oh no...* That’s a low score. Things aren’t going great right now. Time to take care of yourself and ask for help if you need it. 🍂"
        bg_color = "#FFD6D6"  # light red
        text_color = "#B71C1C"  # dark red
    elif prediction == 2:
        monkey_message = "🤔 *Hmm...* You're somewhere in the middle. Not bad, but not great either. Let’s find ways to improve and swing higher! 🍌"
        bg_color = "#FFF9C4"  # light yellow
        text_color = "#F57F17"  # dark yellow/brown

    # Display result
    st.header("🎉 Monkey Peel-o Says:")
    st.markdown(f"""
    <div style="background-color: {bg_color}; padding: 20px; border-radius: 10px; color: {text_color}; font-size: 16px; font-family: 'Silkscreen', monospace;">
        {monkey_message}
    </div>
    """, unsafe_allow_html=True)
