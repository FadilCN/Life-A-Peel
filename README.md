# 🍌 Life-a-Peel

A fun little machine learning project where a monkey named **Peel-O** asks questions and gives you a playful “life score”!  

Not a serious prediction tool — just an experiment to learn, build, and have fun with ML and Streamlit.

---

## 🧠 Project Idea

Predict a person's **Life Satisfaction Score** (1 to 10) using survey data, then simplify it into broad classes to make it more playful and easier to model.

---

## 📊 Dataset

I used a dataset from the **World Values Survey (WVS)**.  

**Steps taken:**
- Focused on columns most relevant to **life satisfaction / life expectation**
- Selected features with strong correlation
- Renamed columns for clarity
- Removed meaningless values like `-1`, `-2`, `-3`, `-5`, etc.

---

## 🛠️ Model Workflow

1. **Initial Attempts**
   - Tried basic **regression models**
   - Results weren’t great, so switched to **classification** instead

2. **Binning Life Score**
   - Converted the life score (1–10) into **3 classes**: `0`, `1`, and `2`
   - Binned other features (as needed) into ranges from `1` to `5`

3. **Balancing the Dataset**
   - Class `0` was underrepresented, while `1` and `2` were more common
   - Tried **SMOTE**, but faced compatibility issues
   - Instead, I wrote a custom script (with GPT's help) to **duplicate class `0` samples** for balance

---

## 🤖 Model Training

- Used **XGBoost Classifier**

### Results after tuning:

| Option | Train Accuracy | Test Accuracy | F1 Score Balance | Notes |
|--------|----------------|----------------|------------------|-------|
| Balanced Accuracy (v1) | ~71% | ~71% | Weak F1 Score | More stable, but less informative |
| Final Choice (v2) | 85% | 95% | Better F1 | Slight overfit, but more fun & engaging |

- Slight overfitting likely due to duplicated data  
- Chose final version for better balance between accuracy and fun

---

## 🐒 Meet Peel-O

To match the playful tone, I added a monkey mascot named **Peel-O** 🐵  
He's the one asking questions and rating your life score (with a bit of sass).

---

## 🚀 Try It Out

👉 **Live App:** [https://life-a-peel.streamlit.app/](https://life-a-peel.streamlit.app/)

---

## 📦 Built With

- Python  
- Pandas, NumPy  
- XGBoost  
- Streamlit  
- A bit of curiosity and fun 😄

---

## 📌 Note

This is not a serious life predictor — it’s just a creative ML experiment made for fun and learning. Please don’t take Peel-O’s scores too personally 😅

