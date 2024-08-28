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


def _test_container(classes=""):
    import st_tailwind as tw
    tw.container(classes=classes)


class MyTestCase(unittest.TestCase):
    @staticmethod
    def test_component_instances():
        at = AppTest.from_function(_all_instances)
        at.run()
        assert not at.exception

    @staticmethod
    def test_one_class_add():
        at = AppTest.from_function(lambda: _test_container(classes="w-full"))
        at.run()
        assert not at.exception

    @staticmethod
    def test_two_classes_add():
        at = AppTest.from_function(lambda: _test_container(classes="flex flex-col"))
        at.run()
        assert not at.exception


if __name__ == '__main__':
    unittest.main()
