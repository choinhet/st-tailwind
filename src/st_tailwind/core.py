import logging
import os
from functools import wraps
from pathlib import Path
from typing import TypeVar

import streamlit as st
import streamlit.components.v1 as components

nth_child_map = {
    st.tabs: 0,
    st.columns: 0,
    st.container: 0,
    st.multiselect: 5,
    st.selectbox: 5,
    st.text: 1,
    st.markdown: 0,
    st.button: 2,
    st.download_button: 2,
    st.file_uploader: 5,
    st.dataframe: 2,
    st.data_editor: 2,
    st.checkbox: 2,
    st.text_input: 6,
    st.text_area: 6,
    st.spinner: 1,
    st.toast: 2,
    st.divider: 3,
    st.progress: 4,
    st.date_input: 5,
    st.status: 2,
}

T = TypeVar("T")
log = logging.getLogger(__name__)


def tw_wrap(
    element: T,
    classes: str = "",
) -> T:
    """
    :param element: element to be wrapped
    :param classes: tailwind classes separated by spaces ("w-full bg-color-red")
    :return: wrapped element with tailwind classes
    """

    # noinspection PyDefaultArgument
    @wraps(element)
    def wrapped(*args, **kwargs):
        popped_classes = kwargs.pop("classes", classes)
        result = element(*args, **kwargs)
        if not popped_classes:
            return result
        _add_classes(classes=popped_classes, cur_type=element)
        return result

    return wrapped


def _add_classes(classes: str, cur_type: str):
    classful_js = _read_text_with_cache("classful.js")
    classful_js = classful_js \
        .replace("%CLASSES%", str(classes)) \
        .replace("%IDX%", str(nth_child_map[cur_type]))

    components.html(
        f"<script>{classful_js}</script>",
        height=0,
        width=0
    )


@st.cache_resource
def _read_text_with_cache(name: str) -> str:
    cache = {}
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
download_button = tw_wrap(st.download_button)
file_uploader = tw_wrap(st.file_uploader)
