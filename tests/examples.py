import streamlit as st

import st_tailwind as tw

st.set_page_config("Streamlit Tailwind Examples")


def main():
    tw.initialize_tailwind()

    tw.write("Grid Container", classes="text-blue-500 pb-4")
    with tw.container(classes="grid grid-cols-4"):
        for idx in range(1, 9):
            st.button(f"Button {idx}")

    tw.write("Colored Button", classes="text-purple-500 pb-4")
    tw.button("Button", classes="bg-red-500")


if __name__ == "__main__":
    main()
