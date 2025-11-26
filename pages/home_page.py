from pytest_playwright.pytest_playwright import page

from pages.vacancies_page import VacanciesPage

class HomePage:
    def __init__(self, page):
        self.page = page
        self.main_header = page.locator('h1')
        self.search_term_input = page.locator('[aria-label="Enter your search term"]')
        self.request_btn = page.get_by_role("button", name="Оставить заявку")
        self.about_btn = page.get_by_role("button", name="Узнать больше")
        self.vacancies_btn = page.get_by_role("link",name="Актуальные вакансии")
        self.name_field = page.get_by_role("textbox",name="Имя *")
        self.email_field = page.get_by_role("textbox", name="Email *")
        self.phone_field = page.get_by_role("textbox", name="Телефон")
        self.job_field = page.get_by_role("textbox", name="Специализация *")
        self.message_field = page.get_by_role("textbox", name="Сообщение")
        self.submit_btn = page.locator('ul + button')
        self.send_request_btn = page.get_by_role("button", name="Отправить заявку")
        self.outstaff_heading = page.locator('#services [data-slot="card"] h3').nth(0)
        self.help_heading = page.locator('#services [data-slot="card"] h3').nth(1)
        self.footer = page.locator('footer')
        self.footer_contacts = self.footer.get_by_role("link",name="Контакты")
        self.footer_outstaff = self.footer.get_by_role("link", name="Аутстафф")
        self.footer_employment = self.footer.get_by_role("link", name="Трудоустройство")
        self.footer_consulting = self.footer.get_by_role("link", name="Консультация")

    def navigate(self):
        self.page.goto("https://www.effective-mobile.ru")

    def click_request_btn(self):
        self.request_btn.click()

    def click_about_btn(self):
        self.about_btn.click()

    def click_out_staff_submit_btn(self):
        self.submit_btn.nth(0).click()

    def click_employment_submit_btn(self):
        self.submit_btn.nth(1).click()

    def click_vacancies_btn(self):
        self.vacancies_btn.click()
        return VacanciesPage(self.page)

    def click_send_request_btn(self):
        self.send_request_btn.click()

    def click_footer_contacts(self):
        self.footer_contacts.click()

    def click_footer_outstaff(self):
        self.footer_outstaff.click()

    def click_footer_employment(self):
        self.footer_employment.click()

    def click_footer_consulting(self):
        self.footer_consulting.click()
