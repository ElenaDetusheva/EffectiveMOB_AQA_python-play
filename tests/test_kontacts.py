import pytest
import re
import time
from pytest_playwright.pytest_playwright import page
from playwright.sync_api import sync_playwright, expect, Page
from pages.home_page import HomePage

# BASE_URL = 'https://www.effective-mobile.ru'
def test_open_website(page :Page):
  # page.goto(BASE_URL)
    home_page = HomePage(page)
    home_page.navigate()
    expect(page).to_have_title("Effective Mobile: Аутстафф и трудоустройство IT-специалистов")
  # print(page.title())
def test_main_header(page :Page):
    home_page = HomePage(page)
    home_page.navigate()
    home_page.click_request_btn()

    # page.get_by_role("button", name="Оставить заявку").click()

    expect(page.get_by_text("Свяжитесь с нами")).to_be_in_viewport()
    expect(page.get_by_label("Имя")).to_be_in_viewport()
    expect(page.get_by_role("textbox",name="Имя *")).to_be_in_viewport()
    # expect(page.locator('#name')).to_have_attribute("placeholder", 'Вашe имя')
    # expect(page.locator("#name")).to_have_attribute("placeholder","Вашe имя")


def test_request_btn_default(page: Page):
    home_page = HomePage(page)
    home_page.navigate()
    home_page.click_request_btn()

    expect(home_page.send_request_btn).to_be_disabled()

def test_empty_fields(page: Page):
    home_page = HomePage(page)
    home_page.navigate()
    home_page.click_request_btn()

    page.frame_locator('iframe[title="reCAPTCHA"]').locator("#recaptcha-anchor[role='checkbox']").set_checked(True)
    # home_page.check_im_not_robot()

    # expect(home_page.send_request_btn).not_to_be_disabled()


# def test_iframe(page: Page):
#    page.goto("https://www.qa-practice.com/elements/iframe/iframe_page")
#    page.frame_locator('iframe').locator('.navbar-toggler-icon').click()

def test_iframe(page: Page):
    home_page = HomePage(page)
    home_page.navigate()
    home_page.click_request_btn()
    # page.goto("https://www.effective-mobile.ru")
    # frame = home_page.page.frame_locator('iframe[title="reCAPTCHA"]')
    # frame.locator("#recaptcha-anchor[role='checkbox']").click()
    home_page.page.pause()
    home_page.page.frame_locator('iframe[title="reCAPTCHA"]').locator("#recaptcha-anchor[role='checkbox']").click()
    # new_page = frame.

    # time.sleep(8)
    # home_page = HomePage(page)
    # home_page.click_send_request_btn()


    # expect(home_page.send_request_btn).not_to_be_disabled()

# page.frame_locator('iframe[title="reCAPTCHA"]').locator("#recaptcha-anchor[role='checkbox']").set_checked(True)