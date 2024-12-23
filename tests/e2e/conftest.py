import os
import subprocess
import time
from pathlib import Path

import psutil
import pytest
from playwright.sync_api import Page, expect


def find_free_port():
    """Find a free port on localhost."""
    import socket

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind(("", 0))
        s.listen(1)
        port = s.getsockname()[1]
    return port


@pytest.fixture(scope="session")
def streamlit_server():
    """Start a Streamlit server for testing."""
    port = find_free_port()
    server_cmd = f"streamlit run tests/basic_components_example.py --server.port {port} --server.headless true"

    # Start the server
    process = subprocess.Popen(
        server_cmd.split(), stdout=subprocess.PIPE, stderr=subprocess.PIPE
    )

    # Wait for server to start
    time.sleep(5)  # Give it some time to start

    yield f"http://localhost:{port}"

    # Cleanup: Kill the process and its children
    parent = psutil.Process(process.pid)
    for child in parent.children(recursive=True):
        child.kill()
    parent.kill()


@pytest.fixture
def page(playwright, streamlit_server):
    """Create a new page for each test."""
    browser = playwright.chromium.launch()
    context = browser.new_context()
    page = context.new_page()
    page.goto(streamlit_server)
    page.wait_for_load_state("networkidle")

    yield page

    context.close()
    browser.close()
