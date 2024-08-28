import os
import sys

import streamlit.web.cli as stcli


def resolve_path(path):
    resolved_path = os.path.abspath(os.path.join(os.getcwd(), path))
    return resolved_path


if __name__ == '__main__':
    try:
        # noinspection PyTypeChecker
        sys.argv = [
            "streamlit",
            "run",
            resolve_path("app.py"),
            "--global.developmentMode=false",
            "--server.port=8080"
        ]
        sys.exit(stcli.main())

    except Exception as e:
        raise RuntimeError("Error while running application", e)
