import streamlit as st

st.set_page_config(
    page_title="Redirecting to AAPL SOAP...",
    page_icon="🔄",
    layout="centered",
)

TARGET_URL = "https://aapl-soap.streamlit.app"

# JavaScript instant redirect with meta refresh fallback
st.markdown(
    f"""
    <meta http-equiv="refresh" content="0; url={TARGET_URL}">
    <script>
        window.location.replace("{TARGET_URL}");
    </script>
    """,
    unsafe_allow_html=True,
)

st.info("The AAPL Reporting portal has migrated to the unified SOAP platform.")
st.link_button("👉 Click here to proceed to AAPL SOAP", TARGET_URL, type="primary")
st.stop()
