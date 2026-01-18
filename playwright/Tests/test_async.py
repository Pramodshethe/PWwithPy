from playwright.async_api import async_playwright


async def run_new_async():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless= False)
        context = await browser.new_context()
        page = await context.new_page()

        await page.goto("www.google.com")
        title = page.title()
        print(f"{title}")

