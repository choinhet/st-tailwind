import streamlit as st
import st_tailwind as tw

#  st.set_page_config(layout="wide")


def kpi_header():
    tw.initialize_tailwind()

    with tw.container(
        classes="w-screen flex flex-row bg-red-500 justify-between gap-4 mb-6"
    ):
        # R2 Score Card
        with tw.container(classes="shrink w-auto p-4 bg-white rounded-lg shadow"):
            st.metric(
                label="R²",
                value="50%",
                help="R-squared (R²) measures how well the curve fits the data. Higher is better.",
            )
        # MAPE Card
        with tw.container(classes="shrink w-auto p-4 bg-white rounded-lg shadow"):
            st.metric(
                label="MAPE",
                value="5%",
                help="Mean Absolute Percentage Error measures prediction accuracy. Lower is better.",
            )
        # Unhealthy Curves Card
        with tw.container(classes="shrink w-auto p-4 bg-white rounded-lg shadow"):
            st.metric(
                label="Unhealthy Curves",
                value="3",
                help="Number of curves that need attention due to poor performance metrics.",
            )
        # Resolved Curves Card
        with tw.container(classes="shrink w-auto p-4 bg-white rounded-lg shadow"):
            st.metric(
                label="Resolved Curves",
                value=0.15,
                help="Number of curves that have been successfully optimized and validated.",
            )


if __name__ == "__main__":
    kpi_header()
