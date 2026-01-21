import asyncio

import pytest
from playwright.async_api import Page, expect, async_playwright


async def UIValidationDynamicSCript(browser):
    context = await browser.new_context()
    page = await context.new_page()

    await page.goto("https://rahulshettyacademy.com/loginpagePractise/")
    await page.get_by_label("Username:").fill("rahulshettyacademy")
    await page.get_by_label("Password:").fill("Learning@830$3mK2")
    await page.get_by_role("combobox").select_option("teach")
    await page.locator("#terms").check()
    await page.get_by_role("button", name="Sign In").click()
    iphone = page.locator("app-card").filter(has_text="iphone X")
    await iphone.get_by_role("button").click()
    nokia = page.locator("app-card").filter(has_text="Nokia Edge")
    await nokia.get_by_role("button").click()
    await page.get_by_text("Checkout").click()
    await expect(page.locator(".media-body")).to_have_count(2)
    #await context.close()


async def childwindowhandle(browser):
    context = await browser.new_context()
    page = await context.new_page()

    await page.goto("https://rahulshettyacademy.com/loginpagePractise/")
    async with page.expect_popup() as popup_info:
        await page.locator(".blinkingText").click()
        childpage = await popup_info.value
        txt = await childpage.locator(".red").text_content()
        print(txt)
        words = txt.split("at")[1]
        email = words.strip().split(" ")[0]
        print(email)
        assert email == "mentor@rahulshettyacademy.com"
    #await context.close()

async def main():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=False)

    await asyncio.gather(
        childwindowhandle(browser),
        UIValidationDynamicSCript(browser)
        )
    await browser.close()

if __name__ == "__main__":
    asyncio.run(main())