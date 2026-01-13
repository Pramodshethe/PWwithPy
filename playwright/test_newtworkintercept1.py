from playwright.sync_api import Page

fakepayload = {"data": [], "message": "No Orders"}

def intercept_resp(route):
    route.fulfill(
        json= fakepayload
    )

def test_network1(page:Page):
    page.goto("https://rahulshettyacademy.com/client/#/auth/login")
    page.route("https://rahulshettyacademy.com/api/ecom/order/get-orders-for-customer/*", intercept_resp)

    page.get_by_placeholder('email@example.com').fill("PWTest@gmail.com")
    page.get_by_placeholder('enter your passsword').fill("PWTestPWTest1")
    page.locator('#login').click()
    page.get_by_role("button", name='ORDERS').click()
    noorder = page.locator(".mt-4").text_content()
    print(noorder)