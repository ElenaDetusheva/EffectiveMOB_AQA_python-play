from pytest_playwright.pytest_playwright import page
from playwright.sync_api import sync_playwright, expect, Page
from pages.home_page import HomePage

def test_open_website(page :Page):
    home_page = HomePage(page)
    home_page.navigate()

    expect(page).to_have_title("Effective Mobile: Аутстафф и трудоустройство IT-специалистов")
    expect(home_page.main_header).to_have_text("Ваша карьера в ITначинается здесь")

def test_request_btn(page :Page):
    home_page = HomePage(page)
    home_page.navigate()
    home_page.click_request_btn()

    expect(page.get_by_text("Свяжитесь с нами")).to_be_in_viewport()

def test_contacts_form(page :Page):
    home_page = HomePage(page)
    home_page.navigate()
    home_page.click_request_btn()

    expect(home_page.name_field).to_be_in_viewport()
    expect(home_page.email_field).to_be_in_viewport()
    expect(home_page.job_field).to_be_in_viewport()
    expect(home_page.phone_field).to_be_in_viewport()
    expect(home_page.message_field).to_be_in_viewport()

def test_request_btn_default(page: Page):
    home_page = HomePage(page)
    home_page.navigate()
    home_page.click_request_btn()

    expect(home_page.send_request_btn).to_be_disabled()
