import pytest
from playwright.sync_api import sync_playwright

@pytest.fixture(scope="session")
def browser():
    """Open Chrome browser in visible mode."""
    with sync_playwright() as p:
        # Launch Chrome/Chromium
        browser = p.chromium.launch(headless=False)  # headless=False opens the window
        yield browser
        browser.close()

# # Parametrized fixture for cross-browser testing
# @pytest.fixture(params=["chromium", "firefox", "webkit"])
# def browser(request):
#     browser_name = request.param
#     print(f"\n===== Running test on: {browser_name} =====")

#     with sync_playwright() as p:
#         if browser_name == "chromium":
#             browser = p.chromium.launch(headless=False)
#         elif browser_name == "firefox":
#             browser = p.firefox.launch(headless=False)
#         elif browser_name == "webkit":
#             browser = p.webkit.launch(headless=False)
#         else:
#             raise ValueError(f"Unsupported browser: {browser_name}")

#         yield browser
#         browser.close()

@pytest.fixture
def page(browser):
    """Create a new page/tab and maximize the window."""
    # Create a new context with a large viewport
    context = browser.new_context(
        viewport={"width": 1920, "height": 1080}  # Maximize-like size
    )
    page = context.new_page()
    yield page
    context.close()

@pytest.fixture
def mobile_page(browser):
    context = browser.new_context(
        viewport={"width": 375, "height": 667},
        user_agent="iPhone"
    )
    page = context.new_page()
    yield page
    context.close()




