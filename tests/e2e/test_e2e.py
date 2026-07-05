# tests/e2e/test_e2e.py

import pytest  # Import the pytest framework for writing and running tests

# The following decorators and functions define E2E tests for the FastAPI calculator application.

@pytest.mark.e2e
def test_hello_world(page, fastapi_server):
    """
    Test that the homepage displays "Hello World".

    This test verifies that when a user navigates to the homepage of the application,
    the main header (`<h1>`) correctly displays the text "Hello World". This ensures
    that the server is running and serving the correct template.
    """
    # Navigate the browser to the homepage URL of the FastAPI application.
    page.goto('http://localhost:8000')
    
    # Use an assertion to check that the text within the first <h1> tag is exactly "Hello World".
    # If the text does not match, the test will fail.
    assert page.inner_text('h1') == 'Hello World'

@pytest.mark.e2e
def test_calculator_add(page, fastapi_server):
    page.goto("http://localhost:8000")

    page.fill("#a", "10")
    page.fill("#b", "5")

    page.click('button:text("Add")')

    page.wait_for_function(
        "document.querySelector('#result').innerText === 'Calculation Result: 15'"
    )

    assert page.inner_text("#result") == "Calculation Result: 15"
@pytest.mark.e2e
def test_calculator_divide_by_zero(page, fastapi_server):
    page.goto("http://localhost:8000")

    page.fill("#a", "10")
    page.fill("#b", "0")

    page.click('button:text("Divide")')

    page.wait_for_function(
        "document.querySelector('#result').innerText.includes('Cannot divide by zero')"
    )

    assert page.inner_text("#result") == "Error: Cannot divide by zero!"
