from playwright.sync_api import sync_playwright,expect

with sync_playwright() as p:
    browser = p.chromium.launch(headless = False, slow_mo=2000)
    iphone = p.devices["iPhone 13"]
    context= browser.new_context(**iphone)
    page= context.new_page()
    url = "https://www.saucedemo.com/"
    page.goto(url)
    page.go_back()
    page.go_forward()

    print(page.title())
    print(page.url)

    username = page.locator("#user-name")
    username.fill("standard_user")
    password = page.locator("#password")
    password.fill("secret_sauce")
    login_button = page.get_by_role("button", name="Login")
    login_button.click()

    browser.close()