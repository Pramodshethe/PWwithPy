import json
from pathlib import Path

import pytest
from playwright.sync_api import Playwright, expect
from pageobjects.login import LoginPage
from utils.apiBase import APIUtils

current_directory = Path(__file__).parent
file_path = current_directory / "data" / "creds.json"

with open(file_path) as file:
    test_data = json.load(file)
    user_credentials_list = test_data["user_creds"]

@pytest.mark.parametrize('user_credentials', user_credentials_list)
def test_e2e_web_api(playwright:Playwright, browser_instance, user_credentials):
    user_email = user_credentials['userEmail']
    user_password = user_credentials['userPassword']

    apiutils = APIUtils()
    order_id = apiutils.createorder(playwright, user_credentials)

    #Login page
    login_page = LoginPage(browser_instance)
    login_page.navigate()
    dashboard_page = login_page.login(user_email, user_password)

    order_page = dashboard_page.selectOrdersNavLink()   #dashboard page

    order_detail = order_page.select_order(order_id)    #Order page

    order_detail.verify_order_message() #order details page
