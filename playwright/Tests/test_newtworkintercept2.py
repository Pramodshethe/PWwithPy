from playwright.sync_api import Page, Playwright

from utils.apiBase import APIUtils


def intercept_req(route):
    route.continue_( url= ""
    )

def test_network1(page:Page):
    page.goto("https://rahulshettyacademy.com/client/#/auth/login")
    page.route("https://rahulshettyacademy.com/api/ecom/order/get-orders-details?id=*", intercept_req)

    page.get_by_placeholder('email@example.com').fill("PWTest@gmail.com")
    page.get_by_placeholder('enter your passsword').fill("PWTestPWTest1")
    page.locator('#login').click()
    page.get_by_role("button", name='ORDERS').click()
    page.get_by_role("button", name="View").first.click()
    message = page.locator(".blink_me").text_content()
    print(message)

def test_sessionstorage(playwright:Playwright):
    apiutils = APIUtils()
    getToken = apiutils.getToken(playwright)
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()

    #inject session token
    page.add_init_script(f"""localStorage.setItem('token', '{getToken}')""")
    page.goto("https://www.rahulshettyacademy.com/client")
    page.get_by_role("button", name='ORDERS').click()