import nltk
from nltk.stem.snowball import SnowballStemmer
import streamlit as st
import pickle
import string
from nltk.corpus import stopwords

import nltk
nltk.download('punkt')

import nltk
nltk.download('stopwords')

st.set_page_config(
    page_title ="Spam Message Detector",
    page_icon = "📧"
)

ss = SnowballStemmer("english")

def transform_message(message):
    message = message.lower()  # for lower case initialization
    message = nltk.word_tokenize(message)  ## for word based tokenization

    # to remove special characters
    y = []
    for i in message:
        if i.isalnum():
            y.append(i)

    message = y[:]
    y.clear()

    # to remove stop words and punctuation
    for i in message:
        if i not in stopwords.words('english') and i not in string.punctuation:
            y.append(i)

    message = y[:]
    y.clear()

    # stemming to get the root words only
    for i in message:
        y.append(ss.stem(i))

    return " ".join(y)

tfidf = pickle.load(open('vectorizer.pkl', 'rb'))
model = pickle.load(open('model.pkl', 'rb'))

st.title("Spam Message Detector")

input_message = st.text_area("Enter your message")

if st.button('Submit'):
    if not input_message.strip():  # Check if input message is empty
        st.warning("Please enter a message!")
    else:
        # 1. Preprocess
        transformed_msg = transform_message(input_message)
        # 2. Vectorize
        vector_input = tfidf.transform([transformed_msg])
        # 3. Predict
        result = model.predict(vector_input)[0]
        # 4. Display
        if result == 1:
            st.warning("It's a spam message")
        else:
            st.success("It's a ham message")