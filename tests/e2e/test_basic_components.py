import subprocess
import time
import psutil
import pytest
from playwright.sync_api import expect
from .conftest import find_free_port


@pytest.fixture
def basic_page(page, streamlit_server):
    """Create a new page for the basic components example."""
    port = find_free_port()
    server_cmd = f"streamlit run tests/basic_components_example.py --server.port {port} --server.headless true"
    process = subprocess.Popen(
        server_cmd.split(), stdout=subprocess.PIPE, stderr=subprocess.PIPE
    )
    time.sleep(5)  # Give it some time to start

    # Navigate to the basic components example
    page.goto(f"http://localhost:{port}")
    page.wait_for_load_state("networkidle")

    yield page

    # Cleanup
    parent = psutil.Process(process.pid)
    for child in parent.children(recursive=True):
        child.kill()
    parent.kill()


def test_basic_components_layout(basic_page):
    """Test that the basic components example loads and shows styled components."""
    # Check the grid container title
    grid_title = basic_page.get_by_text("Grid Container")
    expect(grid_title).to_be_visible()
    expect(grid_title).to_have_css("color", "rgb(59, 130, 246)")  # text-blue-500

    # Check the grid layout
    grid_container = basic_page.locator("[data-testid='stVerticalBlock']").nth(1)
    expect(grid_container).to_be_visible()
    expect(grid_container).to_have_css("display", "grid")

    # Verify that we have 4 columns by checking the number of buttons per row
    buttons_in_first_row = basic_page.locator("button:has-text('Button')").all()[:4]
    assert len(buttons_in_first_row) == 4, "First row should have 4 buttons"

    # Check all 8 buttons in the grid
    for i in range(1, 9):
        button = basic_page.get_by_role("button", name=f"Button {i}")
        expect(button).to_be_visible()

    # Check the colored button section
    colored_button_title = basic_page.get_by_text("Colored Button")
    expect(colored_button_title).to_be_visible()
    expect(colored_button_title).to_have_css(
        "color", "rgb(168, 85, 247)"
    )  # text-purple-500

    # Check the red button
    red_button = basic_page.get_by_role("button", name="Button").last
    expect(red_button).to_be_visible()
    expect(red_button).to_have_css("background-color", "rgb(239, 68, 68)")  # bg-red-500
