import pytest
import re
import time
from pytest_playwright.pytest_playwright import page
from playwright.sync_api import sync_playwright, expect, Page, BrowserContext
from pages.home_page import HomePage
from pages.vacancies_page import VacanciesPage

# BASE_URL = 'https://www.effective-mobile.ru'

def test_go_to_about(page :Page):
    home_page = HomePage(page)
    home_page.navigate()
    home_page.click_about_btn()
    expect(page.get_by_text("Форматы сотрудничества")).to_be_in_viewport()
    # expect(page.get_by_text("Аутстафф")).to_be_in_viewport()
    # expect(page.get_by_text("Помощь в трудоустройстве")).to_be_in_viewport()


def test_goto_out_staff(page :Page):
    home_page = HomePage(page)
    home_page.navigate()
    home_page.click_about_btn()
    home_page.click_out_staff_submit_btn()
    #
    expect(page.get_by_text("Свяжитесь с нами")).to_be_in_viewport()

    # expect(page.get_by_text("Форматы сотрудничества")).to_be_in_viewport()
    # expect(page.get_by_text("Аутстафф")).to_be_in_viewport()
    # expect(page.get_by_text("Помощь в трудоустройстве")).to_be_in_viewport()


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





# def test_open_website(page :Page):
#   # page.goto(BASE_URL)
#   home_page = HomePage(page)
#   home_page.navigate()
#   expect(page).to_have_title("Effective Mobile: Аутстафф и трудоустройство IT-специалистов")
#   # print(page.title())
# def test_main_header(page :Page):
#     home_page = HomePage(page)
#     home_page.navigate()
#     home_page.click_request_btn()
#
#     # page.get_by_role("button", name="Оставить заявку").click()
#
#     expect(page.get_by_text("Свяжитесь с нами")).to_be_in_viewport()
#     expect(page.get_by_label("Имя")).to_be_in_viewport()
#     expect(page.get_by_role("textbox",name="Имя *")).to_be_in_viewport()
#     # expect(page.locator('#name')).to_have_attribute("placeholder", 'Вашe имя')
#     # expect(page.locator("#name")).to_have_attribute("placeholder","Вашe имя")


