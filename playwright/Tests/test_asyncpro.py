import asyncio
import pytest
from playwright.async_api import async_playwright


@pytest.mark.asyncio
async def test_concurrent_navigation():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=False)

        # Run both navigations concurrently
        await asyncio.gather(
            navigate_to_google(browser),
            navigate_to_yahoo(browser)
        )

        await browser.close()


async def navigate_to_google(browser):
    page = await browser.new_page()
    await page.goto("https://www.google.com")
    print("Google loaded!")
    await page.wait_for_timeout(3000)
    await page.close()


async def navigate_to_yahoo(browser):
    page = await browser.new_page()
    await page.goto("https://www.yahoo.in")
    print("Yahoo loaded!")
    await page.wait_for_timeout(3000)
    await page.close()