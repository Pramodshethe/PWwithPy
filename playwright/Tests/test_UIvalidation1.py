import pytest
from playwright.sync_api import Page, expect


#css selector - class: .classname, tagname, #id
def test_UIValidationDynamicSCript(page:Page):
    #iphone X, Nokia Edge
    page.goto("https://rahulshettyacademy.com/loginpagePractise/")
    page.get_by_label("Username:").fill("rahulshettyacademy")
    page.get_by_label("Password:").fill("learning")
    page.get_by_role("combobox").select_option("teach")
    page.locator("#terms").check()
    page.get_by_role("button", name="Sign In").click()
    iphone = page.locator("app-card").filter(has_text="iphone X")
    iphone.get_by_role("button").click()
    nokia = page.locator("app-card").filter(has_text="Nokia Edge")
    nokia.get_by_role("button").click()
    page.get_by_text("Checkout").click()
    expect(page.locator(".media-body")).to_have_count(2)

@pytest.mark.smoke
def test_childwindowhandle(page:Page):
    page.goto("https://rahulshettyacademy.com/loginpagePractise/")
    with page.expect_popup() as newpage:    #closure
        page.locator(".blinkingText").click()
        childpage = newpage.value
        txt = childpage.locator(".red").text_content()
        print(txt)
        words = txt.split("at")[1]
        email = words.strip().split(" ")[0]
        print(email)
        assert email == "mentor@rahulshettyacademy.com"