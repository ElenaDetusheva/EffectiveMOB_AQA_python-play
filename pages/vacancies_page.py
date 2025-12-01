from pytest_playwright.pytest_playwright import page

class VacanciesPage:
    def __init__(self, page):
        self.page = page
        self.main_heading = page.locator('h1')
        self.aqa_python_link = page.locator('a[href = "/vacancies/AQA_PYTHON"]')

    def click_aqa_python_link(self):
        self.aqa_python_link.click()
