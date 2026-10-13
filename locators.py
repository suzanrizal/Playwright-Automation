from playwright.sync_api import sync_playwright, Expect

with sync_playwright() as p:
    browser = p.chromium.launch(headless = False, slow_mo=2000)
    page = browser.new_page()
    url = "https://www.saucedemo.com/"
    page.goto(url)
    # username = page.locator("#user-name")  # For ID 

    # By placeholder
    # username = page.get_by_placeholder("Username")
    # password = page.get_by_placeholder("Password")
    # login_button = page.get_by_role("button", name = "Login")

    # By 
    username = page.get_by_label("Username")
    password = page.get_by_label("Password")
    login_button = page.get_by_role("button",name="Login")

    username.fill("standard_user")
    password.fill("secret_sauce")
    login_button.press("Enter")

    # Expect.
    

    print(page.title())
    print(page.url)

    browser.close()



