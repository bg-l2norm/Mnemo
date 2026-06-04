from playwright.sync_api import sync_playwright
import time
import os

def capture():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page(viewport={'width': 1280, 'height': 800})

        # 1. Capture Hub
        page.goto('http://localhost:8000/index.html')
        time.sleep(3) # Wait for animations
        page.screenshot(path='screenshots/hub.png')
        print("Captured hub.png")

        # 2. Capture Stats
        page.get_by_role("button", name="Stats", exact=True).click()
        time.sleep(2)
        page.screenshot(path='screenshots/stats.png')
        print("Captured stats.png")

        # 3. Capture Deck Detail
        page.get_by_role("button", name="Library", exact=True).click()
        time.sleep(1)
        page.get_by_text("Philosophy", exact=True).first.click()
        time.sleep(2)
        page.screenshot(path='screenshots/deck_detail.png')
        print("Captured deck_detail.png")

        browser.close()

if __name__ == "__main__":
    if not os.path.exists('screenshots'):
        os.makedirs('screenshots')
    capture()
