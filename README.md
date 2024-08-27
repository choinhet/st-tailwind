# Streamlit Tailwind

## If you find this project useful, please consider leaving a star <3

This project, Streamlit Tailwind, is designed to simplify the process of creating user interfaces. It provides a straightforward way to incorporate Tailwind CSS into your Streamlit
applications. So, without further ado:

## Install

Same as always, good ol' pip (or equivalents)

```sh
pip install st_tailwind
```

## Usage

### First way:

Use the tailwind wrapper components.

```python
import st_tailwind as tw

tw.selectbox("test", [], classes="w-fit")
```

### Second way:

Wrap the component yourself. You can add the `classes` keyword argument either in the wrapper method or on the wrapped method.

```python
import streamlit as st

from st_tailwind import tw_wrap

tw_wrap(st.selectbox, classes="w-fit")("test", [])
tw_wrap(st.selectbox)("test", [], classes="w-fit")
```
