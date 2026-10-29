
import streamlit as st
import joblib
import re
import nltk

from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer

# Download required NLTK resources
@st.cache_resource
def load_nltk_resources():
    nltk.download("stopwords", quiet=True)
    nltk.download("wordnet", quiet=True)
    nltk.download("omw-1.4", quiet=True)

    stop_words = set(stopwords.words("english"))
    stop_words -= {"not", "no", "nor"}

    lemmatizer = WordNetLemmatizer()

    return stop_words, lemmatizer

stop_words, lemmatizer = load_nltk_resources()

# Load the trained model
@st.cache_resource
def load_model():
    return joblib.load("sentiment_model.pkl")

saved = load_model()
model = saved["model"]
vectorizer = saved["vectorizer"]


# Clean the review
def clean_text(text):
    text = text.lower()
    text = re.sub(r"\d+", "", text)
    text = re.sub(r"[^a-z\s]", " ", text)

    words = text.split()

    words = [
        lemmatizer.lemmatize(word)
        for word in words
        if word not in stop_words
    ]

    return " ".join(words)


# Streamlit interface
st.title("Restaurant Review Sentiment Analysis")

st.write(
    "Enter a restaurant review to predict whether "
    "the sentiment is positive or negative."
)

review = st.text_area(
    "Enter your review",
    placeholder="Example: The food was fantastic!"
)

if st.button("Predict Sentiment"):
    if not review.strip():
        st.warning("Please enter a review first.")
    else:
        cleaned_review = clean_text(review)
        features = vectorizer.transform([cleaned_review])

        prediction = model.predict(features)[0]
        probabilities = model.predict_proba(features)[0]

        confidence = max(probabilities) * 100

        if prediction == 1:
            st.success("Positive Review 😊")
        else:
            st.error("Negative Review 😞")

        st.write(f"Estimated model confidence: {confidence:.2f}%")
