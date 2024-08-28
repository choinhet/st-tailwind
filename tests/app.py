import pandas as pd

import st_tailwind as tw

tab1, tab2 = tw.tabs(["tab1", "tab2"], classes="border-l-8")
with tab1:
    col1, col2 = tw.columns(2, classes="bg-blue-600")
    with col1:
        tw.text("a")
    with col2:
        tw.text("b")

    with tw.container(classes="bg-blue-600"):
        tw.text("c")

    tw.multiselect("test", [], [], classes="bg-blue-600")
    tw.selectbox("test", [], classes="bg-blue-600")

    tw.text("test", classes="bg-blue-600")
    tw.button("test", classes="bg-blue-600")

    tw.dataframe(pd.DataFrame(), classes="bg-blue-600")
    tw.data_editor(pd.DataFrame(), classes="bg-blue-600")

    tw.checkbox("test", classes="bg-blue-600")

    tw.text_input("test", classes="bg-blue-600")
    tw.text_area("test", classes="bg-blue-600")

    tw.spinner("test", classes="w-full")
    tw.toast("test", classes="w-full")
    tw.divider(classes="w-full")
    tw.progress(10, classes="w-full")
    tw.date_input("test", classes="w-full")
    tw.status("test", classes="w-full")

with tab2:
    tw.button("hello", classes="bg-red-600")
    tw.button("hey", classes="bg-red-600")
