from playwright.sync_api import sync_playwright, expect, Page, BrowserContext
from pytest_playwright.pytest_playwright import page
from pages.home_page import HomePage
from pages.vacancies_page import VacanciesPage

def test_go_to_about(page :Page):
    home_page = HomePage(page)
    home_page.navigate()
    home_page.click_about_btn()

    expect(page.get_by_text("Форматы сотрудничества")).to_be_in_viewport()
    expect(home_page.outstaff_heading).to_be_in_viewport()
    expect(home_page.outstaff_heading).to_have_text("Аутстафф")
    expect(home_page.help_heading).to_be_in_viewport()
    expect(home_page.help_heading).to_have_text("Помощь в трудоустройстве")

def test_goto_out_staff(page :Page):
    home_page = HomePage(page)
    home_page.navigate()
    home_page.click_about_btn()
    home_page.click_out_staff_submit_btn()

    expect(page.get_by_text("Свяжитесь с нами")).to_be_in_viewport()

def test_goto_employment(page :Page):
    home_page = HomePage(page)
    home_page.navigate()
    home_page.click_about_btn()
    home_page.click_employment_submit_btn()

    expect(page.get_by_text("Свяжитесь с нами")).to_be_in_viewport()

def test_goto_vacancies(page :Page, context:BrowserContext):
    home_page = HomePage(page)
    home_page.navigate()
    with context.expect_page() as new_tab_event:
        home_page.click_vacancies_btn()
        new_tab = new_tab_event.value
    vacancies_page = VacanciesPage(new_tab)

    expect(vacancies_page.main_heading).to_have_text("Наши Junior вакансии")
    expect(new_tab).to_have_title("Вакансии")
    expect(new_tab).to_have_url("https://ai-hunt.ru/vacancies/")
