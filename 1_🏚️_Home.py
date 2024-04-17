import streamlit as st

st.set_page_config(
    page_title ="PhishProbe: Be concerned, stay safe",
    page_icon = "🛡️",
    layout="wide"
)

st.markdown("<h1 style='text-align: center'>PhishProbe</h1>",unsafe_allow_html=True)
st.write("<p style='text-align: center; font-size: 18px;'><b>Be concerned, stay safe</b><p>",unsafe_allow_html=True)


# Introduction about PhishProbe
#st.markdown("<h1 style='text-align: center; color: #0066cc;'>PhishProbe</h1>", unsafe_allow_html=True)
#st.write("<p style='text-align: center; font-size: 18px;'>A Phishing URL and Spam Message Detection system</p>", unsafe_allow_html=True)

st.write("<p style='text-align: center;'><br><b>PhishProbe</b> is a <b>''Phishing URL and Spam Message Detection system''</b> based on cybersecurity which utilizes machine learning for enhanced accuracy and efficiency. For phishing URL detection, it employs a content-based URL detection technique. It parses features of websites and compares them with legitimate and phishing URL characteristics to identify suspicious URLs. On the other hand, for spam message detection, PhishProbe utilizes stemmed root words extracted from both analyzed ham and spam messages using machine learning mechanisms. These advanced techniques enable PhishProbe to effectively distinguish between legitimate and potentially harmful URLs and messages, thereby enhancing user security in the digital realm.</p>",unsafe_allow_html=True)
st.write("<br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br>",unsafe_allow_html=True)
import streamlit as st
from bs4 import BeautifulSoup
import requests as re
import pickle
import numpy as np

# Define feature extraction functions
# has_title
def has_title(soup):
    if soup.title is None:
        return 0
    if len(soup.title.text) > 0:
        return 1
    else:
        return 0


# has_input
def has_input(soup):
    if len(soup.find_all("input")):
        return 1
    else:
        return 0


# has_button
def has_button(soup):
    if len(soup.find_all("button")) > 0:
        return 1
    else:
        return 0


# has_image
def has_image(soup):
    if len(soup.find_all("image")) == 0:
        return 0
    else:
        return 1


# has_submit
def has_submit(soup):
    for button in soup.find_all("input"):
        if button.get("type") == "submit":
            return 1
        else:
            pass
    return 0


# has_link
def has_link(soup):
    if len(soup.find_all("link")) > 0:
        return 1
    else:
        return 0


# has_password
def has_password(soup):
    for input in soup.find_all("input"):
        if (input.get("type") or input.get("name") or input.get("id")) == "password":
            return 1
        else:
            pass
    return 0


# has_email_input
def has_email_input(soup):
    for input in soup.find_all("input"):
        if (input.get("type") or input.get("id") or input.get("name")) == "email":
            return 1
        else:
            pass
    return 0


# has_hidden_element
def has_hidden_element(soup):
    for input in soup.find_all("input"):
        if input.get("type") == "hidden":
            return 1
        else:
            pass
    return 0


# has_audio
def has_audio(soup):
    if len(soup.find_all("audio")) > 0:
        return 1
    else:
        return 0


# has_video
def has_video(soup):
    if len(soup.find_all("video")) > 0:
        return 1
    else:
        return 0


# number_of_inputs
def number_of_inputs(soup):
    return len(soup.find_all("input"))


# number_of_buttons
def number_of_buttons(soup):
    return len(soup.find_all("button"))


# number_of_images
def number_of_images(soup):
    image_tags = len(soup.find_all("image"))
    count = 0
    for meta in soup.find_all("meta"):
        if meta.get("type") or meta.get("name") == "image":
            count += 1
    return image_tags + count


# number_of_option
def number_of_option(soup):
    return len(soup.find_all("option"))


# number_of_list
def number_of_list(soup):
    return len(soup.find_all("li"))


# number_of_TH
def number_of_TH(soup):
    return len(soup.find_all("th"))


# number_of_TR
def number_of_TR(soup):
    return len(soup.find_all("tr"))


# number_of_href
def number_of_href(soup):
    count = 0
    for link in soup.find_all("link"):
        if link.get("href"):
            count += 1
    return count


# number_of_paragraph
def number_of_paragraph(soup):
    return len(soup.find_all("p"))


# number_of_script
def number_of_script(soup):
    return len(soup.find_all("script"))


# length_of_title
def length_of_title(soup):
    if soup.title == None:
        return 0
    return len(soup.title.text)


# has h1
def has_h1(soup):
    if len(soup.find_all("h1")) > 0:
        return 1
    else:
        return 0


# has h2
def has_h2(soup):
    if len(soup.find_all("h2")) > 0:
        return 1
    else:
        return 0


# has h3
def has_h3(soup):
    if len(soup.find_all("h3")) > 0:
        return 1
    else:
        return 0


# length of text
def length_of_text(soup):
    return len(soup.get_text())


# number of clickable button
def number_of_clickable_button(soup):
    count = 0
    for button in soup.find_all("button"):
        if button.get("type") == "button":
            count += 1
    return count


# number of a
def number_of_a(soup):
    return len(soup.find_all("a"))


# number of img
def number_of_img(soup):
    return len(soup.find_all("img"))


# number of div class
def number_of_div(soup):
    return len(soup.find_all("div"))


# number of figures
def number_of_figure(soup):
    return len(soup.find_all("figure"))


# has footer
def has_footer(soup):
    if len(soup.find_all("footer")) > 0:
        return 1
    else:
        return 0


# has form
def has_form(soup):
    if len(soup.find_all("form")) > 0:
        return 1
    else:
        return 0


# has textarea
def has_text_area(soup):
    if len(soup.find_all("textarea")) > 0:
        return 1
    else:
        return 0


# has iframe
def has_iframe(soup):
    if len(soup.find_all("iframe")) > 0:
        return 1
    else:
        return 0


# has text input
def has_text_input(soup):
    for input in soup.find_all("input"):
        if input.get("type") == "text":
            return 1
    return 0


# number of meta
def number_of_meta(soup):
    return len(soup.find_all("meta"))


# has nav
def has_nav(soup):
    if len(soup.find_all("nav")) > 0:
        return 1
    else:
        return 0


# has object
def has_object(soup):
    if len(soup.find_all("object")) > 0:
        return 1
    else:
        return 0


# has picture
def has_picture(soup):
    if len(soup.find_all("picture")) > 0:
        return 1
    else:
        return 0


# number of sources
def number_of_sources(soup):
    return len(soup.find_all("source"))


# number of span
def number_of_span(soup):
    return len(soup.find_all("span"))


# number of table
def number_of_table(soup):
    return len(soup.find_all("table"))

#Additional features
def has_domain(url):
    return '.' in url


def has_https(url):
    return url.startswith("https://")


def add_https(url):
    if not url.startswith("http"):
        url = "https://" + url
    return url

# Define a function for feature extraction
def create_vector(soup):
    features = [
        has_title(soup),
        has_input(soup),
        has_button(soup),
        has_image(soup),
        has_submit(soup),
        has_link(soup),
        has_password(soup),
        has_email_input(soup),
        has_hidden_element(soup),
        has_audio(soup),
        has_video(soup),
        number_of_inputs(soup),
        number_of_buttons(soup),
        number_of_images(soup),
        number_of_option(soup),
        number_of_list(soup),
        number_of_TH(soup),
        number_of_TR(soup),
        number_of_href(soup),
        number_of_paragraph(soup),
        number_of_script(soup),
        length_of_title(soup),
        has_h1(soup),
        has_h2(soup),
        has_h3(soup),
        length_of_text(soup),
        number_of_clickable_button(soup),
        number_of_a(soup),
        number_of_img(soup),
        number_of_div(soup),
        number_of_figure(soup),
        has_footer(soup),
        has_form(soup),
        has_text_area(soup),
        has_iframe(soup),
        has_text_input(soup),
        number_of_meta(soup),
        has_nav(soup),
        has_object(soup),
        has_picture(soup),
        number_of_sources(soup),
        number_of_span(soup),
        number_of_table(soup)
    ]
    return np.array(features)


# Load the model
model = pickle.load(open('phish_model.pkl', 'rb'))

# Streamlit app
st.title("Phishing URL Detection:")
url = st.text_input('Enter the URL')

# Check the URL and run prediction
if st.button('Check!'):
    if url:
        # Check if the URL contains a domain name
        if not has_domain(url):
            st.warning("Enter a valid url with correct domain")
        else:
            # Check if the URL has HTTPS, if not, add it
            if not has_https(url):
                url = add_https(url)
            try:
                # Send a GET request to check HTTPS connection
                user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
                response = re.get(url, headers={"User-Agent": user_agent}, timeout=4)
                if response.status_code == 200:
                    # If HTTPS is successful, proceed with feature extraction
                    soup = BeautifulSoup(response.content, "html.parser")
                    vector = [create_vector(soup)]
                    result = model.predict(vector)
                    if result[0] == 0:
                        if has_title(soup):
                            st.success("This web page seems legitimate!")
                        else:
                            st.warning("Attention! This web page is a potential phishing!")
                    else:
                        st.warning("Attention! This web page is a potential phishing!")
                else:
                    st.error("HTTPS connection was not successful for the URL: " + url)
                    st.warning("Attention! Web page might be phishing!")
            except re.exceptions.RequestException as e:
                st.error("Error: " + str(e))
                st.warning("Attention! Web page might be phishing!")
    else:
        st.warning("Please enter a URL to check.")

st.write("<br><br>",unsafe_allow_html=True)

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