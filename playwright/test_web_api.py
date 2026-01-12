from playwright.sync_api import Playwright

from utils.apiBase import APIUtils

def test_e2e_web_api(playwright:Playwright):
    browser =  playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()

    apiutils = APIUtils()
    apiutils.createorder(playwright)

    page.goto("https://rahulshettyacademy.com")