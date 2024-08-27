import os
from functools import cache, wraps
from pathlib import Path
from typing import TypeVar

import streamlit as st
import streamlit.components.v1 as components

_st_map = {
    st.tabs: "[data-baseweb='tab-panel']",
    st.columns: "[data-testid='stHorizontalBlock']",
    st.container: "[data-testid='stVerticalBlockBorderWrapper']",
    st.multiselect: "[data-testid='stMultiSelect']",
    st.selectbox: "[data-testid='stSelectbox']",
    st.text: "[data-testid='stMarkdown']",
    st.button: "button",
    st.dataframe: ".dvn-scroller.glideDataEditor",
    st.data_editor: ".dvn-scroller.glideDataEditor",
    st.checkbox: "[data-baseweb='checkbox']",
    st.text_input: "[data-testid='stTextInput']",
    st.text_area: "[data-testid='stTextArea']",
    st.spinner: "[data-testid='stSpinner']",
    st.toast: "[data-testid='stToast']",
    st.divider: ".stMarkdown > div > hr",
    st.progress: "[data-baseweb='progress-bar']",
    st.date_input: "[data-testid='stDateInput']",
    st.status: "[data-testid='stExpander']",
}

T = TypeVar("T")


def tw_wrap(element: T, classes="") -> T:
    @wraps(element)
    def wrapped(*args, **kwargs):
        popped_classes = kwargs.pop("classes", "")
        print(kwargs)
        clz = classes or popped_classes
        first_arg = next(iter(args), None)
        if first_arg is None or not _is_valid_text(first_arg):
            first_arg = ""
        _add_class(element, first_arg, clz)
        return element(*args, **kwargs)

    return wrapped


def _add_class(element: T, text: str, classes="") -> T:
    selector = _st_map.get(element, "div")
    _create_html(classes, text, selector)
    return element


def _is_valid_text(text: str) -> bool:
    return (
        isinstance(text, str)
        or isinstance(text, float)
        or isinstance(text, int)
    )


def _create_html(classes, text, selector):
    classful_js = _read_text_with_cache("classful.min.js")
    classful_js = classful_js \
        .replace("%CLASSES%", str(classes)) \
        .replace("%TEXT%", str(text)) \
        .replace("%SELECTOR%", str(selector))
    components.html(
        f"<script>{classful_js}</script>",
        height=0,
        width=0
    )


@cache
def _read_text_with_cache(name: str) -> str:
    full_path = Path(os.path.dirname(__file__)) / name
    with open(str(full_path), "r") as f:
        return f.read()


tabs = tw_wrap(st.tabs)
columns = tw_wrap(st.columns)
container = tw_wrap(st.container)
multiselect = tw_wrap(st.multiselect)
selectbox = tw_wrap(st.selectbox)
text = tw_wrap(st.text)
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
