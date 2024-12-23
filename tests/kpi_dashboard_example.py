"""
Example Streamlit app demonstrating a KPI dashboard with Tailwind styling.
"""

from typing import Union
import streamlit as st
import st_tailwind as tw

st.set_page_config(layout="wide")


def get_card(label: str, value: Union[str, float, int], help: str):
    with tw.container(classes="w-48 p-4 bg-white rounded-lg shadow"):
        st.metric(label=label, value=value, help=help)


def kpi_header():
    tw.initialize_tailwind()

    with tw.container(
        classes="flex flex-row flex-wrap w-fit justify-between gap-4 mb-6"
    ):
        # R2 Score Card
        get_card(
            label="R²",
            value="50%",
            help="R-squared (R²) measures how well the curve fits the data. Higher is better.",
        )
        # MAPE Card
        get_card(
            label="MAPE",
            value="5%",
            help="Mean Absolute Percentage Error measures prediction accuracy. Lower is better.",
        )
        # Unhealthy Curves Card
        get_card(
            label="Unhealthy Curves",
            value="3",
            help="Number of curves that need attention due to poor performance metrics.",
        )
        # Resolved Curves Card
        get_card(
            label="Resolved Curves",
            value=0.15,
            help="Number of curves that have been successfully optimized and validated.",
        )


if __name__ == "__main__":
    kpi_header()
