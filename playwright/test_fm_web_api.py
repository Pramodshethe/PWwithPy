import json
import time
import pytest
from playwright.sync_api import Playwright, expect
from pageobjects.login import LoginPage
from pageobjects.dashboard import Dashboard
from utils.apiBase import APIUtils

with open('playwright/data/creds.json') as file:
    test_data = json.load(file)
    user_credentials_list = test_data["user_creds"]

@pytest.mark.parametrize('user_credentials', user_credentials_list)
def test_e2e_web_api(playwright:Playwright, user_credentials):
    user_email = user_credentials['userEmail']
    user_password = user_credentials['userPassword']
    browser =  playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()

    apiutils = APIUtils()
    order_id = apiutils.createorder(playwright, user_credentials)

    #Login page
    login_page = LoginPage(page)
    login_page.navigate()
    dashboard_page = login_page.login(user_email, user_password)
    
    #dashboard page
    order_page = dashboard_page.selectOrdersNavLink()
    
    #Order page
    order_detail = order_page.select_order(order_id)

    #order details page
    order_detail.verify_order_message()

    context.close()
    #time.sleep(5)