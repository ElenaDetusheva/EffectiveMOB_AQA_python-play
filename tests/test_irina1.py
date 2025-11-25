import pytest
import re
import time

from playwright.sync_api import sync_playwright, expect, Page

BASE_URL = 'https://www.effective-mobile.ru'
# @pytest.fixture(scope='session')
# def playwright_instance():
#     with sync_playwright() as p:
#         yield p
#
# @pytest.fixture(scope='function')
# def browser_page(playwright_instance):
#     browser = playwright_instance.chromium.launch(headless=False)
#     page = browser.new_page()
#     yield page
#     browser.close()

# def test_open_website():
#     # browser = sync_playwright().start()
#     with sync_playwright() as p:
#         browser = p.chromium.launch(headless=False)
#         page = browser.new_page()
#         # page.goto("https://www.google.com")
#         page.goto("https://www.effective-mobile.ru")
#
#         expect(page).to_have_title("Effective Mobile: Аутстафф и трудоустройство IT-специалистов")
#
#         # expect(page).to_have_title("Google")
#         # time.sleep(500)
#
#         # assert page.title == "ITIRINA Web 3455 DB Browser"
#         # assert "Web Product Simulation for QA Engineers" in page.title
#         browser.close()


def test_open_website(page :Page):
  page.goto(BASE_URL)
  expect(page).to_have_title("Effective Mobile: Аутстафф и трудоустройство IT-специалистов")
  print(page.title())
# def test_open_website(browser_page):
#      browser_page.goto(BASE_URL)
#
#      expect(browser_page).to_have_title("Effective Mobile: Аутстафф и трудоустройство IT-специалистов")
#
#
# def test_main_header(browser_page):
#     browser_page.goto(BASE_URL)
#
#     browser_page.get_by_role("button", name="Оставить заявку").click()
#
#     expect(browser_page.get_by_text('Свяжитесь с нами')).to_be_in_viewport()
#     expect(browser_page.get_by_label("Имя")).to_be_in_viewport()
#     expect(browser_page.get_by_role("textbox",name="Имя *")).to_be_in_viewport()
#     expect(browser_page.get_by_role("textbox", name="Имя *")).to_have_attribute("placeholder", "Ваше имя")


# def test_main_header(page :Page):
#     page.goto(BASE_URL)
#
#     page.get_by_role("button", name="Оставить заявку").click()
#
#     expect(page.get_by_text('Свяжитесь с нами')).to_be_in_viewport()
#     expect(page.get_by_label("Имя")).to_be_in_viewport()
#     expect(page.get_by_role("textbox",name="Имя *")).to_be_in_viewport()
#     expect(page.get_by_role("textbox", name="Имя *")).to_have_attribute("placeholder", "Вашe имя")