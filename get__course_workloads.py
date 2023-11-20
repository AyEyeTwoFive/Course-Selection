import asyncio
from pyppeteer import launch
from bs4 import BeautifulSoup

async def take_screenshot(url, output_path='screenshot.png'):
    browser = await launch(headless=True)
    page = await browser.newPage()
    await page.goto(url)
    await page.screenshot({'path': output_path})
    await browser.close()

# Example usage
url_to_open = "https://oncourse.college/CS131"
output_path = 'screenshot.png'

# Create an event loop
loop = asyncio.get_event_loop()

# Run the coroutine in the event loop
loop.run_until_complete(take_screenshot(url_to_open, output_path))