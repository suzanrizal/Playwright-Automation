import re
from playwright.sync_api import Playwright, sync_playwright, expect


def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False, slow_mo=500)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://www.mindrisers.com.np/")
    page.get_by_text("X", exact=True).click()
    page.locator("//input[@id='header-search']").click()
    page.get_by_role("textbox", name="Search courses of your liking").fill("quality assura")
    page.get_by_role("link", name="Quality Assurance Training with AI Quality Assurance Training with AI Course").click()
    page.get_by_role("button", name="Send Enquiry").click()
    page.get_by_role("textbox", name="Enter your full name").click()
    page.get_by_role("textbox", name="Enter your full name").press("CapsLock")
    page.get_by_role("textbox", name="Enter your full name").fill("S")
    page.get_by_role("textbox", name="Enter your full name").press("CapsLock")
    page.get_by_role("textbox", name="Enter your full name").fill("Sujan")
    page.get_by_role("textbox", name="Enter your email address").click()
    page.get_by_role("textbox", name="Enter your email address").fill("rizalsuzan2@gmail.com")
    page.get_by_role("textbox", name="Enter your phone number").click()
    page.get_by_role("textbox", name="Enter your phone number").fill("9840308352")
    page.get_by_role("textbox", name="Enter your Subject").click()
    page.get_by_role("textbox", name="Enter your Subject").press("CapsLock")
    page.get_by_role("textbox", name="Enter your Subject").fill("Q")
    page.get_by_role("textbox", name="Enter your Subject").press("CapsLock")
    page.get_by_role("textbox", name="Enter your Subject").fill("Quality assurance")
    page.get_by_role("textbox", name="Enter your queries or any").click()
    page.get_by_role("textbox", name="Enter your queries or any").press("CapsLock")
    page.get_by_role("textbox", name="Enter your queries or any").fill("H")
    page.get_by_role("textbox", name="Enter your queries or any").press("CapsLock")
    page.get_by_role("textbox", name="Enter your queries or any").fill("Hello im practicing codegen")

    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)
