from playwright.sync_api import sync_playwright, expect, Page
from pytest_playwright.pytest_playwright import page
from pages.home_page import HomePage

def test_footer_contacts_link(page: Page):
    home_page = HomePage(page)
    home_page.navigate()
    home_page.click_footer_contacts()

    expect(page.get_by_text("Свяжитесь с нами")).to_be_in_viewport()

def test_footer_outstaff_link(page: Page):
    home_page = HomePage(page)
    home_page.navigate()
    home_page.click_footer_outstaff()

    expect(page.get_by_text("Форматы сотрудничества")).to_be_in_viewport()

def test_footer_employment_link(page: Page):
    home_page = HomePage(page)
    home_page.navigate()
    home_page.click_footer_employment()

    expect(page.get_by_text("Форматы сотрудничества")).to_be_in_viewport()

def test_footer_consulting_link(page: Page):
    home_page = HomePage(page)
    home_page.navigate()
    home_page.click_footer_consulting()

    expect(page.get_by_text("Свяжитесь с нами")).to_be_in_viewport()
