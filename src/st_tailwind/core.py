import os
from functools import wraps
from pathlib import Path
from typing import TypeVar, Optional

import streamlit as st
import streamlit.components.v1 as components

_st_map = {
    st.tabs: "[data-testid='stTabs']",
    st.columns: "[data-testid='stHorizontalBlock']",
    st.container: "[data-testid='stVerticalBlockBorderWrapper']",
    st.multiselect: "[data-testid='stMultiSelect']",
    st.selectbox: "[data-testid='stSelectbox']",
    st.text: "[data-testid='stText']",
    st.markdown: "[data-testid='stMarkdown']",
    st.button: "[data-testid='stButton']",
    st.dataframe: "[data-testid='stDataFrameResizable']",
    st.data_editor: "[data-testid='stDataFrameResizable']",
    st.checkbox: "[data-testid='stCheckbox']",
    st.text_input: "[data-testid='stTextInput']",
    st.text_area: "[data-testid='stTextArea']",
    st.spinner: "[data-testid='stSpinner']",
    st.toast: "[data-testid='stToast']",
    st.divider: "[data-testid='stMarkdown']",
    st.progress: "[data-baseweb='progress-bar']",
    st.date_input: "[data-testid='stDateInput']",
    st.status: "[data-testid='stExpander']",
}

instance_cache = {}

T = TypeVar("T")


def tw_wrap(
    element: T,
    classes: str = "",
    pos: Optional[int] = None
) -> T:
    """
    :param element: element to be wrapped
    :param classes: tailwind classes separated by spaces ("w-full bg-color-red")
    :param pos: Instantiation position (e.g. `N` instance of a given streamlit object)
    :return: wrapped element with tailwind classes
    """

    @wraps(element)
    def wrapped(*args, **kwargs):
        popped_classes = kwargs.pop("classes", classes)
        popped_pos = kwargs.pop("pos", pos) or 0

        selector = _st_map.get(element)

        if not popped_classes:
            _increase_pos_and_get(selector)
            return element(*args, **kwargs)

        _add_classes(classes=popped_classes, selector=selector, pos=popped_pos)

        return element(*args, **kwargs)

    return wrapped


def _add_classes(classes: str, selector: str, pos: Optional[int] = None):
    classful_js = _read_text_with_cache("classful.min.js")

    if pos:
        _increase_pos_and_get(selector)
        cur_pos = pos
    else:
        cur_pos = _increase_pos_and_get(selector)

    classful_js = classful_js \
        .replace("%CLASSES%", str(classes)) \
        .replace("%POS%", str(cur_pos)) \
        .replace("%SELECTOR%", str(selector))

    components.html(
        f"<script>{classful_js}</script>",
        height=0,
        width=0
    )


def _increase_pos_and_get(selector):
    pos = instance_cache.setdefault(selector, -1) + 1
    instance_cache[selector] = pos
    return pos


@st.cache_resource
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
