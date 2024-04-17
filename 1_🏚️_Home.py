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
# Add any additional content or features below as needed