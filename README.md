# Playwright Python Automation Project

This project demonstrates a comprehensive test automation framework using Playwright and pytest for end-to-end testing of a web application. It includes UI tests, API-based scenarios, and Behavior-Driven Development (BDD) with `pytest-bdd`.

## Features

*   **UI Automation**: Automates browser actions to validate web application functionality.
*   **API Integration**: Uses API calls to set up test data and preconditions, leading to faster and more stable tests.
*   **Behavior-Driven Development (BDD)**: Implements BDD scenarios using `pytest-bdd` for clear and business-readable tests.
*   **Cross-Browser Support**: Supports multiple browsers like Chrome and Firefox, configurable via command-line arguments.
*   **Page Object Model (POM)**: Organizes UI elements and interactions into reusable classes for better maintainability.

## Technologies Used

*   **Playwright**: For reliable end-to-end browser automation.
*   **pytest**: As the core test runner for organizing and executing tests.
*   **pytest-bdd**: For implementing BDD scenarios.
*   **Python**: The programming language used for writing the tests.

## Project Structure

The project is organized into the following directories:

```
├── playwright
│   ├── data
│   │   └── creds.json         # Test data, including credentials
│   ├── features
│   │   └── ordertransaction.feature # BDD feature files
│   ├── pageobjects
│   │   └── login.py           # Page Object Model classes
│   ├── utils
│   │   └── apiBase.py         # Utility class for API interactions
│   ├── conftest.py            # Pytest configuration and fixtures
│   ├── test_*.py              # Test files
└── README.md                  # This file
```

*   `data/`: Stores test data files, such as user credentials.
*   `features/`: Contains `.feature` files for `pytest-bdd`.
*   `pageobjects/`: Implements the Page Object Model design pattern.
*   `utils/`: Includes helper classes, such as `APIUtils` for handling API calls.
*   `conftest.py`: Defines shared pytest fixtures and command-line options.

## Setup and Installation

1.  **Clone the repository:**
    ```sh
    git clone <your-repository-url>
    cd PythonPlay
    ```

2.  **Install dependencies:**
    It is recommended to use a virtual environment.
    ```sh
    python -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    ```
    Install the required packages:
    ```sh
    pip install -r requirements.txt
    ```

3.  **Install Playwright browsers:**
    ```sh
    playwright install
    ```

## Running the Tests

You can run the tests using the `pytest` command.

### Basic Execution

To run all tests, simply execute:
```sh
pytest
```

### Command-Line Options

The framework supports custom command-line options for flexible test execution.

*   **Browser Selection**:
    You can specify the browser (e.g., `chrome` or `firefox`) using the `--browser_name` flag.
    ```sh
    pytest --browser_name chrome
    ```
    The default browser is Chrome.

*   **URL Selection**:
    You can specify the target URL using the `--url_link` flag.
    ```sh
    pytest --url_link https://your-test-environment.com
    ```

### Running BDD Scenarios

To run only the BDD tests, you can target the specific test file:
```sh
pytest playwright/test_pytest_bdd.py
```

## Configuration

The `playwright/conftest.py` file contains the primary configuration for the test suite. It defines fixtures for:
*   **Browser Management**: The `browser_instance` fixture handles launching and closing the browser.
*   **Command-Line Options**: The `pytest_addoption` function registers custom flags like `--browser_name`.

## API and BDD Integration

This framework demonstrates how to combine UI and API tests for efficient test execution.

*   **API Utils**: The `APIUtils` class in `playwright/utils/apiBase.py` provides methods to interact with the application's API. For example, it can programmatically log in a user and create an order, setting up a clean state for a subsequent UI test.

*   **BDD Scenarios**: The `ordertransaction.feature` file defines a test scenario in a business-readable format. The steps in this feature file are implemented in `playwright/test_pytest_bdd.py`, which uses the `APIUtils` to create an order via an API call before validating it on the UI. This approach significantly speeds up the test by bypassing unnecessary UI navigation.
