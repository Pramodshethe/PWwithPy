import time

from playwright.sync_api import Playwright, expect

from ..utils.apiBase import APIUtils

def test_e2e_web_api(playwright:Playwright):
    browser =  playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()

    apiutils = APIUtils()
    orderID = apiutils.createorder(playwright)

    page.goto("https://rahulshettyacademy.com/client/#/auth/login")
    page.get_by_placeholder('email@example.com').fill("PWTest@gmail.com")
    page.get_by_placeholder('enter your passsword').fill("PWTestPWTest1")
    page.locator('#login').click()
    page.get_by_role("button", name='ORDERS').click()

    row = page.locator("tr").filter(has_text=orderID)
    row.get_by_role("button", name="View").click()
    expect(page.locator(".tagline")).to_have_text("Thank you for Shopping With Us")
    context.close()
    time.sleep(5)