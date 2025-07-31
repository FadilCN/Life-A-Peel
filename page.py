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

model = joblib.load("model.pkl")


st.image("tetx.png") 
st.title("Let's Check Your Life Score!")

left, right = st.columns([1, 2])

with left:
    st.image("monkeypls-monkey-dancing.gif")  # Replace with your own monkey image

with right:
    st.write(" Yo! I'm Monkey Peel-o")
    st.write("I might look like a monkey... because I am one. ")
    st.success("🍌 My life score predictions are **about 75%–85% accurate**… unless I get distracted by bananas.")
    st.caption("No guarantees. I'm literally a monkey with a model.")

st.markdown("Answer these simple questions — your banana buddy is listening! 🍌")


# -------------------------------
# 😄 HOW YOU FEEL
# -------------------------------
import streamlit as st
st.header("🏠 Your Living Standard")

income_level_options = [2, 3, 1]
income_level_labels = {
    1: "Low",
    2: "Medium",
    3: "High"
}

Income_Level_Grouped = st.radio(
    "What is your income level group?",
    options=income_level_options,
    format_func=lambda x: income_level_labels[x],
    index=0  # default 2 (Medium)
)
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

# Freedom_of_Choice_Binned
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

# -------------------------------
# 🍽️ BASIC NEEDS
# -------------------------------
st.header("🍽️ Did You Face Any Problems This Year?")

basic_needs_options = [4, 2, 3, 1]
basic_needs_labels = {
    1: "Never",
    2: "Rarely",
    3: "Sometimes",
    4: "Often"
}

No_Cash_Income = st.radio(
    "Did you run out of cash/money?",
    options=basic_needs_options,
    format_func=lambda x: basic_needs_labels[x],
    index=0  # default 4 (Often)
)

No_Food = st.radio(
    "Did you ever go without food?",
    options=basic_needs_options,
    format_func=lambda x: basic_needs_labels[x],
    index=0  # default 4 (Often)
)

No_Medicine = st.radio(
    "Did you miss medicine or treatment?",
    options=basic_needs_options,
    format_func=lambda x: basic_needs_labels[x],
    index=0  # default 4 (Often)
)

No_Shelter = st.radio(
    "Did you lack shelter?",
    options=basic_needs_options,
    format_func=lambda x: basic_needs_labels[x],
    index=0  # default 4 (Often)
)

unsafe_at_home_options = [4, 3, 2, 1]
unsafe_at_home_labels = {
    1: "Never",
    2: "Rarely",
    3: "Sometimes",
    4: "Often"
}

Unsafe_at_Home = st.radio(
    "Did you feel unsafe at home?",
    options=unsafe_at_home_options,
    format_func=lambda x: unsafe_at_home_labels[x],
    index=0  # default 4 (Often)
)

# -------------------------------
# 🏠 LIVING STANDARD
# -------------------------------


# -------------------------------
# 😄 How You Feel
# -------------------------------
st.header("😄 How You Feel")

happiness_options = [1, 2, 3, 4]
happiness_labels = {
    1: "Very unhappy",
    2: "Unhappy",
    3: "Happy",
    4: "Very happy"
}

Happiness_Rev = st.radio(
    "How happy do you feel generally?",
    options=happiness_options,
    format_func=lambda x: happiness_labels[x],
    index=3  # default 4 (Very happy)
)

health_options = [3, 2, 1, 5, 4]
health_labels = {
    1: "Very poor",
    2: "Poor",
    3: "Fair",
    4: "Very good",
    5: "Good"
}

Health_Rev = st.radio(
    "How would you rate your health?",
    options=health_options,
    format_func=lambda x: health_labels[x],
    index=4  # default 4 (Very good)
)

national_pride_options = [0.0, 0.33, 0.66, 1.0]
national_pride_labels = {
    0.0: "Not proud",
    0.33: "Slightly proud",
    0.66: "Proud",
    1.0: "Very proud"
}

National_Pride_Rev = st.radio(
    "How proud are you of your country?",
    options=national_pride_options,
    format_func=lambda x: national_pride_labels[x],
    index=3  # default 1.0 (Very proud)
)

secure_in_neighborhood_options = [3, 2, 1, 4]
secure_in_neighborhood_labels = {
    1: "Not secure",
    2: "Somewhat secure",
    3: "Secure",
    4: "Very secure"
}

Secure_in_Neighborhood = st.radio(
    "Do you feel secure in your neighborhood?",
    options=secure_in_neighborhood_options,
    format_func=lambda x: secure_in_neighborhood_labels[x],
    index=3  # default 4 (Very secure)
)

freedom_of_choice_recoded_options = [3, 4, 1, 2, 5]
freedom_of_choice_recoded_labels = {
    1: "Very restricted",
    2: "Restricted",
    3: "Neutral",
    4: "Free",
    5: "Completely free"
}

Freedom_of_Choice_Recoded = st.radio(
    "Recoded: How free do you feel in your choices?",
    options=freedom_of_choice_recoded_options,
    format_func=lambda x: freedom_of_choice_recoded_labels[x],
    index=4  # default 5 (Completely free)
)

# -------------------------------
# 🏛️ GOVERNMENT & RESPONSIBILITY
# -------------------------------
st.header("🌍 Beliefs, Trust & Responsibility")

Importance_of_God = st.radio(
    "How important is God/religion to you?",
    options=[1, 2, 3, 4, 5],
    format_func=lambda x: {
        1: "Not important",
        2: "Slightly important",
        3: "Moderately important",
        4: "Important",
        5: "Very important"
    }[x],
    index=2
) * 2

Science_Makes_Life_Better = st.radio(
    "Do you believe science makes life better?",
    options=[1, 2, 3, 4, 5],
    format_func=lambda x: {
        1: "Strongly disagree",
        2: "Disagree",
        3: "Neutral",
        4: "Agree",
        5: "Strongly agree"
    }[x],
    index=2
) * 2

Science_Benefits_World = st.radio(
    "Do you believe science benefits the world?",
    options=[1, 2, 3, 4, 5],
    format_func=lambda x: {
        1: "Strongly disagree",
        2: "Disagree",
        3: "Neutral",
        4: "Agree",
        5: "Strongly agree"
    }[x],
    index=2
) * 2

General_Trust = st.radio(
    "How much do you trust people in general?",
    options=[1, 2, 3, 4, 5],
    format_func=lambda x: {
        1: "Don't trust at all",
        2: "Slightly trust",
        3: "Somewhat trust",
        4: "Mostly trust",
        5: "Fully trust"
    }[x],
    index=2
) * 2

Govt_vs_Self_Responsibility = st.radio(
    "Who is more responsible for your well-being?",
    options=[1, 2, 3, 4, 5],
    format_func=lambda x: {
        1: "Entirely Government",
        2: "Mostly Government",
        3: "Both equally",
        4: "Mostly Myself",
        5: "Entirely Myself"
    }[x],
    index=2
) * 2



# -------------------------------
# 📤 SUBMIT
# -------------------------------
if st.button("🍌 See My Life-O-Peel Score"):
    features = {
        "Satisfaction_Financial_Binned": financial_satisfaction,  # from your finance radio input
        "Freedom_of_Choice_Binned": freedom,                      # from your freedom radio input
        "No_Cash_Income": No_Cash_Income,
        "No_Food": No_Food,
        "No_Medicine": No_Medicine,
        "No_Shelter": No_Shelter,
        "Unsafe_at_Home": Unsafe_at_Home,
        "Income_Level_Grouped": Income_Level_Grouped,
        "Happiness_Rev": Happiness_Rev,
        "Health_Rev": Health_Rev,
        "National_Pride_Rev": National_Pride_Rev,
        "Secure_in_Neighborhood": Secure_in_Neighborhood,
        "Freedom_of_Choice_Recoded": Freedom_of_Choice_Recoded,
        "Govt_vs_Self_Responsibility": Govt_vs_Self_Responsibility,
        "General_Trust": General_Trust,
        "Importance_of_God": Importance_of_God,
        "Science_Makes_Life_Better": Science_Makes_Life_Better,
        "Science_Benefits_World": Science_Benefits_World,
    }

    input_df = pd.DataFrame([features])

    # If your model expects columns in a certain order, reorder explicitly:
    input_df = input_df[model.feature_names_in_]

    prediction = model.predict(input_df)[0]

    # ... (rest of your display code)
   

    # Correct mapping based on your class labels (1 = low, 2 = medium, 3 = high)
    if prediction == 2:
        monkey_message = "🍌 *Ooo-oo-aa-aa!* You're doing amazing! Life’s good, you’re on top of the banana tree! 🍃"
        bg_color = "#DFFFD6"  # light green
        text_color = "#1B5E20"  # dark green
    elif prediction == 0:
        monkey_message = "😟 *Oh no...* That’s a low score. Things aren’t going great right now. Time to take care of yourself and ask for help if you need it. 🍂"
        bg_color = "#FFD6D6"  # light red
        text_color = "#B71C1C"  # dark red
    elif prediction == 1:
        monkey_message = "🤔 *Hmm...* You're somewhere in the middle. Not bad, but not great either. Let’s find ways to improve and swing higher! 🍌"
        bg_color = "#FFF9C4"  # light yellow
        text_color = "#F57F17"  # dark yellow/brown
    else:
    # Fallback (in case prediction is unexpected)
        monkey_message = "🤷‍♂️ Hmm, something went unexpected. Let's try again!"
        bg_color = "#E0E0E0"  # light gray
        text_color = "#000000"  # black

    # Display result
    st.header("🎉 Monkey Peel-o Says:")
    st.markdown(f"""
    <div style="background-color: {bg_color}; padding: 20px; border-radius: 10px; color: {text_color}; font-size: 16px; font-family: 'Silkscreen', monospace;">
        {monkey_message}
    </div>
    """, unsafe_allow_html=True)
