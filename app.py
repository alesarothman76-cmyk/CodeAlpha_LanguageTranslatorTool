import streamlit as st
from deep_translator import GoogleTranslator

# Page Configuration
st.set_page_config(page_title="Language Translation Tool", layout="centered")

st.title("🌐 Language Translation Tool")

# Supported Languages mapping for deep-translator
LANGUAGES = {
    "Auto-Detect": "auto",
    "English": "en",
    "Spanish": "es",
    "French": "fr",
    "German": "de",
    "Arabic": "ar",
    "Chinese (Simplified)": "zh-CN",
    "Japanese": "ja"
}

# Language Selection Layout (Phase 1)
col1, col2 = st.columns(2)

with col1:
    source_lang_name = st.selectbox("Source Language", list(LANGUAGES.keys()), index=0)

with col2:
    target_lang_name = st.selectbox("Target Language", [k for k in LANGUAGES.keys() if k != "Auto-Detect"], index=0)

# Input Text Area
source_text = st.text_area("Enter text to translate:", height=150, placeholder="Type your text here...")

# Translate Button & Logic (Phase 2)
if st.button("Translate", type="primary", use_container_width=True):
    if not source_text.strip():
        st.warning("Please enter some text first.")
    else:
        try:
            source_code = LANGUAGES[source_lang_name]
            target_code = LANGUAGES[target_lang_name]

            # Call API wrapper
            translated = GoogleTranslator(source=source_code, target=target_code).translate(source_text)

            # Output Display
            st.success("Translation Complete!")
            st.text_area("Translated Text:", value=translated, height=150)
            
        except Exception as e:
            st.error(f"Translation failed: {str(e)}")