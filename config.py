import os

from dotenv import load_dotenv


load_dotenv()


def get_required_secret(name: str) -> str:
    value = os.getenv(name)

    if not value:
        try:
            import streamlit as st

            value = st.secrets.get(name)
        except Exception:
            value = None

    if not value:
        raise RuntimeError(
            f"Missing {name}. Add it to the local .env file or Streamlit Cloud secrets."
        )

    return str(value)