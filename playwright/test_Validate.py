from IPython.core.page import page_file
from IPython.terminal.shortcuts.auto_suggest import accept
from playwright.sync_api import Page, expect


def test_validatenew(page:Page):
    page.goto("https://rahulshettyacademy.com/AutomationPractice")
    expect(page.get_by_placeholder("Hide/Show Example")).to_be_visible()
    page.get_by_role("button", name="Hide").click()
    expect(page.get_by_placeholder("Hide/Show Example")).to_be_hidden()

def test_handleAlerts(page:Page):
    page.goto("https://rahulshettyacademy.com/AutomationPractice")
    page.on("dialog", lambda dialog:dialog.accept())
    page.get_by_role("button", name="Confirm").click()

    #frame
    pf = page.frame_locator("#courses-iframe")
    print("Here: ", pf.get_by_role("link", name="Courses").nth(0))
    pf.get_by_role("link", name="Courses").nth(0).click()
    #expect(pf.locator("body")).to_contain_text("Browse products")
    #print("Here is the value",pf.get_by_role("link", name="Courses"))

def test_handleTable(page:Page):
    #table
    global pricecolvalue
    page.goto("https://rahulshettyacademy.com/seleniumPractise/#/offers/")

    for index in range(page.locator("th").count()):
        if page.locator("th").nth(index).filter(has_text="Price").count() > 0:
            pricecolvalue = index
            break

    riceRow = page.locator("tr").filter(has_text="Rice")
    print(riceRow)
    expect(riceRow.locator("td").nth(pricecolvalue)).to_have_text("37")

def test_mouseHover(page:Page):
    page.goto("https://rahulshettyacademy.com/AutomationPractice")
    page.locator("#mousehover").hover()
    page.get_by_role("link", name="Top").click()

