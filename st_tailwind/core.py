"""
Core module for Streamlit Tailwind.

This module provides the core functionality for applying Tailwind CSS styles to Streamlit components.
It includes functions for initializing Tailwind CSS and wrapping Streamlit components with Tailwind classes.
"""

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

log = logging.getLogger("st_tailwind")


def initialize_tailwind():
    """
    Initialize Tailwind CSS in the Streamlit application.

    This function injects the necessary JavaScript code to enable Tailwind CSS styling
    for Streamlit components. It should be called at the start of your Streamlit app.

    Returns:
        streamlit.components.v1.html: The initialized Tailwind component
    """
    return html(f"<script>{INIT}</script>")


def get_style_frame(cls, classes=""):
    """
    Create a style frame for a Streamlit component.

    Args:
        cls: The Streamlit component class to style
        classes (str): Tailwind CSS classes to apply to the component

    Returns:
        streamlit.components.v1.html: The styled component frame
    """
    current_id = correspondence.get(cls)
    if current_id is None:
        log.debug(f"Correspondence to component of class '{cls}' not found.")
        return
    text = f'<script>parent.document.addTokens("{current_id}", "{classes}", window)</script>'
    return html(text)


def tw_wrap(component, classes=""):
    """
    Wrap a Streamlit component with Tailwind CSS classes.

    This is the main utility function that allows any Streamlit component to be styled
    with Tailwind CSS classes. It can be used either as a decorator or a function wrapper.

    Args:
        component: The Streamlit component to wrap
        classes (str): Default Tailwind CSS classes to apply to the component

    Returns:
        function: The wrapped component function that accepts Tailwind classes

    Example:
        >>> import streamlit as st
        >>> import st_tailwind as tw
        >>> styled_button = tw.tw_wrap(st.button, "bg-blue-500 hover:bg-blue-700")
        >>> styled_button("Click me!")
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


# Pre-wrapped Streamlit components with Tailwind support
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
