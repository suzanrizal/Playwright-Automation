from playwright.sync_api import sync_playwright,expect
from pages.login import loginpage

def test_login():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False, slow_mo=2000)
        page = browser.new_page()

        page.goto("https://www.saucedemo.com/")

        login = loginpage(page)

        login.enter_username("standard_user")
        login.enter_password("secret_sauce")
        login.click_login()

        # Assertions
        expect(page).to_have_url(
            "https://www.saucedemo.com/inventory.html"
        )
        # expect(page.locator(".inventory_list")).to_be_visible()
        # expect(page.locator(".title")).to_have_text("Products")

        browser.close()