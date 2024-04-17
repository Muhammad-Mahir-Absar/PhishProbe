import streamlit as st
from bs4 import BeautifulSoup
import requests as re
import pickle
import numpy as np

st.set_page_config(
    page_title ="Phishing URL Detection",
    page_icon = "🔗"
)

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