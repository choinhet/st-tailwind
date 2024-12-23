"""
Constants module for Streamlit Tailwind.

This module contains mappings between Streamlit components and their corresponding CSS selectors
used for applying Tailwind styles to the components.
"""

import streamlit as st

# Mapping of Streamlit components to their CSS selectors
correspondence = {
    st.button: "[data-testid='stBaseButton-secondary']",
    st.container: "[data-testid='stVerticalBlock']",
    st.tabs: "[data-testid='stTabs']",
    st.columns: "[data-testid='stHorizontalBlock']",
    st.multiselect: "[data-testid='stMultiSelect']",
    st.selectbox: "[data-testid='stSelectbox']",
    st.text: "[data-testid='stText']",
    st.markdown: "[data-testid='stMarkdown']",
    st.dataframe: "[data-testid='stDataFrameResizable']",
    st.data_editor: "[data-testid='stDataFrameResizable']",
    st.checkbox: "[data-testid='stCheckbox']",
    st.text_input: "[data-testid='stTextInput']",
    st.text_area: "[data-testid='stTextArea']",
    st.spinner: "[data-testid='stSpinner']",
    st.toast: "[data-testid='stToast']",
    st.divider: "[data-testid='stMarkdown']",
    st.write: "[data-testid='stMarkdown']",
    st.progress: "[data-baseweb='progress-bar']",
    st.date_input: "[data-testid='stDateInput']",
    st.status: "[data-testid='stExpander']",
}
