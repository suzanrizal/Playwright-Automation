from playwright.sync_api import Page

class loginpage:
    def __init__(self, page:Page):
        self.username= page.locator("#user-name")
        self.password= page.locator("#password")
        self.login_button= page.locator("//input[@id='login-button']")

    def enter_username(self,username):
        self.username.fill(username)

    def enter_password(self, password):
        self.password.fill(password)

    def click_login(self):
        self.login_button.click()

        