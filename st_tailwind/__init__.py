"""
Streamlit Tailwind - A Python package for adding Tailwind CSS styling to Streamlit components.

This package provides a set of wrapped Streamlit components that can be styled using Tailwind CSS classes.
It allows for easy and flexible styling of Streamlit applications without the need for custom CSS.

Available components:
    - tabs: Styled tab container
    - columns: Styled column layout
    - multiselect: Styled multiselect input
    - selectbox: Styled select input
    - text: Styled text display
    - button: Styled button
    - download_button: Styled download button
    - file_uploader: Styled file upload
    - dataframe: Styled dataframe display
    - data_editor: Styled data editor
    - checkbox: Styled checkbox input
    - text_input: Styled text input
    - text_area: Styled text area
    - spinner: Styled loading spinner
    - toast: Styled toast notifications
    - divider: Styled divider
    - progress: Styled progress bar
    - date_input: Styled date picker
    - status: Styled status indicator
    - container: Styled container
    - tw_wrap: Utility function to wrap any Streamlit component with Tailwind classes
"""

__all__ = [
    "tabs",
    "columns",
    "multiselect",
    "selectbox",
    "text",
    "button",
    "download_button",
    "file_uploader",
    "dataframe",
    "data_editor",
    "checkbox",
    "text_input",
    "text_area",
    "spinner",
    "toast",
    "divider",
    "progress",
    "date_input",
    "status",
    "container",
    "tw_wrap",
]

from .core import *
