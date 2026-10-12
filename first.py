from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.webkit.launch(headless = False, slow_mo=2000)
    page = browser.new_page()
    browser1 = p.chromium.launch(headless = False, slow_mo =2000)
    page1 = browser1.new_page()
    url = "https://opensource-demo.orangehrmlive.com/web/index.php/auth/login"
    page.goto(url)
    page.go_back()
    page.go_forward()
    page.reload()

    print(page.title())
    print(page.url)
    
    page1.goto("https://www.mindrisers.com.np/")
    print(page1.title())
    print(page1.url)
    # page.screenshot(path=r"C:\Users\rizal\OneDrive\Documents\MindrisersPython\Playwright\Screenshot\Firstscreenshot.png")

    browser.close()
    browser1.close()
    

    # Headed and headless 
    # By default playwright is in headless
# Understand device - in chromium , webkit
