import streamlit as st
from googletrans import Translator, LANGUAGES

st.set_page_config(page_title="CodeAlpha Translation Tool")
st.title("🌍 Language Translation Tool - CodeAlpha")

translator = Translator()

text = st.text_area("Enter text to translate", height=150)
src_lang = st.selectbox("From", list(LANGUAGES.values()))
dest_lang = st.selectbox("To", list(LANGUAGES.values()))

if st.button("Translate"):
    if text:
        result = translator.translate(text, src=src_lang, dest=dest_lang)
        st.success("Translated Text:")
        st.write(result.text)
    else:
        st.warning("Please enter some text")