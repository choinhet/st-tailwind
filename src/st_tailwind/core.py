import inspect
import logging
import os
from functools import wraps
from pathlib import Path
from typing import TypeVar

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
    st.button: "[data-testid='stBaseButton-secondary']",
    st.download_button: "[data-testid='stBaseButton-secondary']",
    st.file_uploader: "[data-testid='stFileUploaderDropzone']",
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

T = TypeVar("T")
pos_cache = {}
log = logging.getLogger(__name__)
previous_call = None


def tw_wrap(
    element: T,
    classes: str = "",
) -> T:
    """
    :param element: element to be wrapped
    :param classes: tailwind classes separated by spaces ("w-full bg-color-red")
    :param pos: Instantiation position (e.g. `N` instance of a given streamlit object)
    :return: wrapped element with tailwind classes
    """

    # noinspection PyDefaultArgument
    @wraps(element)
    def wrapped(*args, **kwargs):
        frame = inspect.currentframe()
        caller_frame = frame.f_back
        file_name = caller_frame.f_code.co_filename.split(os.sep)[-1].replace(".py", "")
        line_number = caller_frame.f_lineno
        id_ = f"{file_name}L{line_number}"

        popped_classes = kwargs.pop("classes", classes)
        selector = _st_map.get(element)

        result = element(*args, **kwargs)

        if not popped_classes:
            _get_from_cache(selector, id_)
            return result

        _add_classes(classes=popped_classes, selector=selector, id=id_)

        return result

    return wrapped


def _get_from_cache(selector, id) -> int:
    global previous_call
    global pos_cache

    semi_id = f"{selector}-{id}"

    for key in pos_cache:
        if key.startswith(semi_id) and previous_call != semi_id:
            log.debug(f"Returning from cache {key}")
            return pos_cache[key]

    previous_call = semi_id

    num_instances = []
    for key in pos_cache:
        if key.startswith(selector):
            num_instances.append(int(key.split("-")[-1]))

    if num_instances:
        new_pos = max(num_instances) + 1
        new_key = f"{selector}-{id}-{new_pos}"
        pos_cache[new_key] = new_pos
        log.debug(f"Returning a new instance {new_key}")
        return new_pos

    new_key = f"{selector}-{id}-0"
    pos_cache[new_key] = 0

    log.debug(f"Creating new entry {new_key}")
    return 0


def _add_classes(classes: str, selector: str, id: str):
    classful_js = _read_text_with_cache("classful.min.js")

    cur_pos = _get_from_cache(selector, id)

    classful_js = classful_js \
        .replace("%CLASSES%", str(classes)) \
        .replace("%POS%", str(cur_pos)) \
        .replace("%SELECTOR%", str(selector))

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
