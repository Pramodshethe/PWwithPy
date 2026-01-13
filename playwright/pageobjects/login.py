from .dashboard import Dashboard


class LoginPage:
    def __init__(self, page):
        self.page = page

    def navigate(self):
        self.page.goto("https://rahulshettyacademy.com/client/#/auth/login")

    def login(self, userEmail, userPassword):
        self.page.get_by_placeholder('email@example.com').fill(userEmail)
        self.page.get_by_placeholder('enter your passsword').fill(userPassword)
        self.page.locator('#login').click()
        dashboard_page = Dashboard(self.page)
        return dashboard_page