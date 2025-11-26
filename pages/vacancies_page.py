from pytest_playwright.pytest_playwright import page

class VacanciesPage:
    def __init__(self, page):
        self.page = page
        self.main_heading = page.locator('h1')
