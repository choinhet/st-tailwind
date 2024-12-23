import subprocess
import time
import psutil
import pytest
from playwright.sync_api import expect
from .conftest import find_free_port


@pytest.fixture
def kpi_page(page, streamlit_server):
    """Create a new page for the KPI dashboard example."""
    port = find_free_port()
    server_cmd = f"streamlit run tests/kpi_dashboard_example.py --server.port {port} --server.headless true"
    process = subprocess.Popen(
        server_cmd.split(), stdout=subprocess.PIPE, stderr=subprocess.PIPE
    )
    time.sleep(5)  # Give it some time to start

    # Navigate to the KPI dashboard example
    page.goto(f"http://localhost:{port}")
    page.wait_for_load_state("networkidle")

    yield page

    # Cleanup
    parent = psutil.Process(process.pid)
    for child in parent.children(recursive=True):
        child.kill()
    parent.kill()


def test_kpi_dashboard_layout(kpi_page):
    """Test that the KPI dashboard example loads and shows styled components."""
    # Check the container layout
    container = kpi_page.locator("[data-testid='stVerticalBlock']").nth(1)
    expect(container).to_be_visible()
    expect(container).to_have_css("display", "flex")
    expect(container).to_have_css("flex-wrap", "wrap")
    expect(container).to_have_css("gap", "16px")  # gap-4
    expect(container).to_have_css("justify-content", "space-between")
    expect(container).to_have_css("margin-bottom", "24px")  # mb-6

    # Check that we have 4 cards
    cards = container.locator("[data-testid='stVerticalBlock']")
    expect(cards).to_have_count(4)

    # Check each card's styling
    for card in cards.all():
        expect(card).to_have_css("width", "192px")  # w-48 (12rem)
        expect(card).to_have_css("padding", "16px")  # p-4
        expect(card).to_have_css("background-color", "rgb(255, 255, 255)")  # bg-white
        expect(card).to_have_css("border-radius", "8px")  # rounded-lg
