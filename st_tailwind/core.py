import importlib.resources as importlib_resources
import logging
from functools import wraps
from pathlib import Path

import streamlit as st
from streamlit.components.v1 import html

import st_tailwind.resources.frontend as front_resources
from st_tailwind.const import correspondence

FRONT_PATH = Path(str(importlib_resources.files(front_resources)))
INIT = (FRONT_PATH / "init.min.js").read_text()
TEMPLATE = (FRONT_PATH / "add.min.js").read_text()

log = logging.getLogger("st_tailwind")


def initialize_tailwind():
    """
    Function to inject Tailwind CDN into the page.
    """

    return html(f"<script>{INIT}</script>")


def get_style_frame(cls, classes=""):
    current_id = correspondence.get(cls)
    if current_id is None:
        log.debug("Correspondence to component of class '' not found.")
        return
    filled_template = TEMPLATE.replace("%ID%", current_id).replace("%CLASSES%", classes)
    return html(f"<script>{filled_template}</script>")


def tw_wrap(component, classes=""):
    """
    Tailwind wrapper to add style to component.
    """

    @wraps(component)
    def wrapper(*args, **kwargs):
        nonlocal classes
        clz = None
        if "classes" in kwargs:
            clz = kwargs.pop("classes")
        all_clz = clz or classes
        get_style_frame(component, all_clz)
        result = component(*args, **kwargs)
        return result

    return wrapper


write = tw_wrap(st.write)
tabs = tw_wrap(st.tabs)
columns = tw_wrap(st.columns)
container = tw_wrap(st.container)
multiselect = tw_wrap(st.multiselect)
selectbox = tw_wrap(st.selectbox)
text = tw_wrap(st.text)
markdown = tw_wrap(st.markdown)
button = tw_wrap(st.button)
dataframe = tw_wrap(st.dataframe)
data_editor = tw_wrap(st.data_editor)
checkbox = tw_wrap(st.checkbox)
text_input = tw_wrap(st.text_input)
text_area = tw_wrap(st.text_area)
spinner = tw_wrap(st.spinner)
toast = tw_wrap(st.toast)
divider = tw_wrap(st.divider)
progress = tw_wrap(st.progress)
date_input = tw_wrap(st.date_input)
status = tw_wrap(st.status)
download_button = tw_wrap(st.download_button)
file_uploader = tw_wrap(st.file_uploader)
