from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless= False, slow_mo=1000)
    page = browser.new_page()
    page.goto("https://formy-project.herokuapp.com/form")

    first_name = page.locator("#first-name")    # Locating by ID
    first_name.fill("Sujan")

    last_name = page.locator("#last-name")  # For locating by class
    last_name.fill("Rijal")

    job_title = page.get_by_label("Job title")
    job_title.fill("Quality Assurance Engineer")

    highest_education = page.locator("#radio-button-1")
    highest_education.click()

    sex = page.locator("#checkbox-1")
    sex.check()

    experience = page.locator("#select-menu")
    experience.select_option("0-1")

    date = page.locator("#datepicker")
    date.fill("12/25/2001")

    browser.close()