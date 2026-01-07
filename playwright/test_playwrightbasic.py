import time

from playwright.sync_api import Page, expect, Playwright


def test_playbasic(playwright):
    browser = playwright.chromium.launch(headless=False) #launched engine
    context = browser.new_context()     #creating a context has
    page = context.new_page() # new page is created like tab
    page.goto("https://rahulshettyacademy.com")

def test_playwrightpage(page:Page):
    # without creating browser, context and Page is a built in fixture
    # headless and single context
    # explicitly need to import
    page.goto("https://rahulshettyacademy.com")

def test_coreLocaters(page:Page):
    # to use label - it should have label tag
    # that textbox should be wrapped in the label tag OR label 'for' linked with id of the textbox
    #
    page.goto("https://rahulshettyacademy.com/loginpagePractise/")
    page.get_by_label("Username:").fill("rahulshettyacademy")
    page.get_by_label("Password:").fill("learning")
    page.get_by_role("combobox").select_option("teach")
    page.locator("#terms").check()
    page.get_by_role("button", name="Sign In").click()
    time.sleep(5)

def test_wrongCoreLocaters(page:Page):
    # to use label - it should have label tag
    # that textbox should be wrapped in the label tag OR label 'for' linked with id of the textbox
    #
    page.goto("https://rahulshettyacademy.com/loginpagePractise/")
    page.get_by_label("Username:").fill("rahulshettyacadem")
    page.get_by_label("Password:").fill("learning")
    page.get_by_role("combobox").select_option("teach")
    page.locator("#terms").check()
    page.get_by_role("button", name="Sign In").click()
    #Incorrect username/password.
    expect(page.get_by_text("Incorrect username/password.")).to_be_visible()
    #time.sleep(5)

def test_firefocbrowser(playwright:Playwright):
    fb = playwright.firefox.launch(headless=False)
    page = fb.new_page()
    page.goto("https://rahulshettyacademy.com/loginpagePractise/")
    page.get_by_label("Username:").fill("rahulshettyacademy")
    page.get_by_label("Password:").fill("learning")
    page.get_by_role("combobox").select_option("teach")
    page.locator("#terms").check()
    page.get_by_role("button", name="Sign In").click()