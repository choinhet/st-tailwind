"""
Tests for the st_tailwind package.
"""

import streamlit as st
import st_tailwind as tw


def test_initialize_tailwind():
    """Test that initialize_tailwind returns an HTML component."""
    result = tw.initialize_tailwind()
    assert result is not None
    assert hasattr(result, "_html")


def test_tw_wrap():
    """Test that tw_wrap correctly wraps a Streamlit component."""
    wrapped = tw.tw_wrap(st.button, "test-class")
    assert wrapped is not None
    assert callable(wrapped)


def test_tw_wrap_with_kwargs():
    """Test that tw_wrap handles classes passed as kwargs."""
    wrapped = tw.tw_wrap(st.button)
    # Call the wrapped component with classes in kwargs
    result = wrapped("Click me", classes="test-class-2")
    assert result is not None


def test_get_style_frame():
    """Test that get_style_frame generates correct HTML."""
    from st_tailwind.core import get_style_frame

    result = get_style_frame(st.button, "test-class")
    assert result is not None
    assert hasattr(result, "_html")


def test_get_style_frame_unknown_component():
    """Test that get_style_frame handles unknown components gracefully."""
    from st_tailwind.core import get_style_frame

    # Create a dummy component not in the correspondence mapping
    def dummy_component():
        pass

    result = get_style_frame(dummy_component, "test-class")
    assert result is None


def test_correspondence_mapping():
    """Test that all components have correct CSS selectors."""
    from st_tailwind.const import correspondence

    assert correspondence[st.button] == "[data-testid='stBaseButton-secondary']"
    assert correspondence[st.container] == "[data-testid='stVerticalBlock']"
    assert correspondence[st.text] == "[data-testid='stText']"


def test_wrapped_components_exist():
    """Test that all pre-wrapped components exist and are callable."""
    components = [
        tw.write,
        tw.tabs,
        tw.columns,
        tw.container,
        tw.multiselect,
        tw.selectbox,
        tw.text,
        tw.markdown,
        tw.button,
        tw.dataframe,
        tw.data_editor,
        tw.checkbox,
        tw.text_input,
        tw.text_area,
        tw.spinner,
        tw.toast,
        tw.divider,
        tw.progress,
        tw.date_input,
        tw.status,
        tw.download_button,
        tw.file_uploader,
    ]

    for component in components:
        assert callable(component), f"{component.__name__} should be callable"
