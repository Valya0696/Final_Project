from playwright.sync_api import sync_playwright
from pytest import fixture

from sinsay_model.sinsay import Sinsay


@fixture
def get_playwright():
    with sync_playwright() as playwright:
        yield playwright


@fixture
def final_project(get_playwright):
    sinsay = Sinsay(get_playwright)
    yield sinsay
    sinsay.close()