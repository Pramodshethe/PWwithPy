import asyncio
from playwright.async_api import async_playwright


async def test_scrape_page(browser, url):
    """Helper function to scrape a single URL."""
    context = await browser.new_context()
    page = await context.new_page()

    print(f"Starting: {url}")
    await page.goto(url, wait_until="domcontentloaded")

    # Example: Extract the h1 text
    h1_text = await page.inner_text("h1")
    print(f"Finished {url}: {h1_text}")

    await context.close()
    return h1_text


async def main():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=False)

        urls = [
            "https://wikipedia.org",
            "https://github.com",
            "https://python.org"
        ]

        # Schedule all scraping tasks to run concurrently
        tasks = [test_scrape_page(browser, url) for url in urls]
        results = await asyncio.gather(*tasks)

        print("\nAll results collected:", results)
        await browser.close()


if __name__ == "__main__":
    asyncio.run(main())