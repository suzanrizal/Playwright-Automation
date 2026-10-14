from playwright.sync_api import Page

def test_login(page:Page):
    page.goto("https://www.saucedemo.com")
    page.locator("#user-name").fill("standard_user")
    page.locator("#password").fill("secret_sauce")
    page.locator("#login-button").click()


#pytest --headed --slowmo=3000
#pytest --tracing on
#playwright show-trace trace.zip