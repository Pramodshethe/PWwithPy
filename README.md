# Playwright Python Automation Project

This project demonstrates a comprehensive test automation framework using Playwright and pytest for end-to-end testing of a web application. It includes UI tests, API-based scenarios, network interception, and Behavior-Driven Development (BDD) with `pytest-bdd`.

## Features

*   **UI Automation**: Automates browser actions to validate web application functionality.
*   **API Integration**: Uses API calls to set up test data and preconditions, leading to faster and more stable tests.
*   **Network Interception**: Demonstrates how to mock API responses and modify requests to test edge cases (e.g., no orders found).
*   **Session Storage Injection**: Shows how to bypass login by injecting authentication tokens directly into local storage.
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
│   ├── assets             # Static assets (e.g., CSS files)
│   ├── data
│   │   └── creds.json     # Test data, including credentials
│   ├── features
│   │   └── ordertransaction.feature # BDD feature files
│   ├── pageobjects        # Page Object Model classes
│   │   ├── login.py
│   │   ├── dashboard.py
│   │   ├── orderpage.py
│   │   └── orderdetails.py
│   ├── Tests              # Test files
│   │   ├── test_Validate.py
│   │   ├── test_web_api.py
│   │   ├── test_pytest_bdd.py
│   │   ├── test_newtworkintercept1.py
│   │   └── test_newtworkintercept2.py
│   ├── utils
│   │   └── apiBase.py     # Utility class for API interactions
│   ├── conftest.py        # Pytest configuration and fixtures
│   └── Notes.txt          # Project notes
└── README.md              # This file
```

*   `Tests/`: Contains all the test files, including UI, API, and network interception tests.
*   `data/`: Stores test data files, such as user credentials.
*   `features/`: Contains `.feature` files for `pytest-bdd`.
*   `pageobjects/`: Implements the Page Object Model design pattern with separate classes for Login, Dashboard, Orders, and Order Details.
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

### Running Specific Tests

*   **Run BDD Scenarios**:
    ```sh
    pytest playwright/Tests/test_pytest_bdd.py
    ```

*   **Run Network Interception Tests**:
    ```sh
    pytest playwright/Tests/test_newtworkintercept1.py
    ```

## Advanced Concepts Demonstrated

*   **Network Interception**: `test_newtworkintercept1.py` mocks the "get orders" API response to simulate a "No Orders" scenario without needing to actually delete orders in the backend.
*   **Session Storage**: `test_newtworkintercept2.py` demonstrates how to inject a valid authentication token into the browser's local storage to skip the login screen and go directly to the dashboard.
*   **Hybrid Testing**: The BDD tests combine API calls (to create an order) with UI interactions (to verify the order), showcasing a hybrid approach that is both fast and reliable.
