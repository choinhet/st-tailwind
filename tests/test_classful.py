import unittest

from streamlit.testing.v1 import AppTest


def _all_instances():
    import st_tailwind as tw
    import pandas as pd

    tw.tabs("test")
    tw.columns(2)
    tw.container()
    tw.multiselect("test", [], [])
    tw.selectbox("test", [])
    tw.text("test")
    tw.button("test")
    tw.dataframe(pd.DataFrame())
    tw.data_editor(pd.DataFrame())
    tw.checkbox("test")
    tw.text_input("test")
    tw.text_area("test")
    tw.spinner("test")
    tw.toast("test")
    tw.divider()
    tw.progress(10)
    tw.date_input("test")
    tw.status("test")


class MyTestCase(unittest.TestCase):
    @staticmethod
    def test_component_instances():
        at = AppTest.from_function(_all_instances)
        at.run()
        assert not at.exception


if __name__ == '__main__':
    unittest.main()
