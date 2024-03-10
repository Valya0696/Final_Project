from playwright.sync_api import sync_playwright, Playwright


class Sinsay:
    def __init__(self, playwright: Playwright):
        self.browser = playwright.chromium.launch(headless=False)
        self.context = self.browser.new_context()
        self.page = self.context.new_page()

    def open_url_and_accept_cookies(self, url: str):
        def handler():
            self.page.get_by_role("button", name="Так").click()
        self.page.goto(url)
        self.page.add_locator_handler(self.page.get_by_role("button", name="Так"), handler)
        # self.page.get_by_role("button", name="Так").click()
        return self

    def open_login_form(self):
        self.page.get_by_test_id("account-info-logged-false").click()
        return self

    def login(self, login: str):
        self.page.get_by_label("Електронна пошта").fill(login)
        return self

    def password(self, password: str):
        self.page.get_by_label("Пароль").fill(password)
        return self

    def click_login_button(self):
        self.page.get_by_role("button", name="Увійдіть", exact=True).click()
        return self

    def authorization(self):
        self.page.get_by_test_id("account-info-logged-false").click()
        self.login('xiyito4140@comsb.com')
        self.password('Valya1112')
        self.click_login_button()

    def close_popup(self):
        self.page.locator(".checkbox-container").click()
        self.page.locator(".sc-dmlqKv > button").click()
        return self

    def search_shorts(self):
        self.page.get_by_test_id("search-open-button").click()
        self.page.get_by_placeholder("Шукати").fill("шорти")
        self.page.get_by_placeholder("Шукати").press("Enter")
        return self

    def filter_result(self):
        self.page.get_by_test_id("category-filters-box").get_by_text("Жінка").click()
        self.page.wait_for_timeout(1500)
        self.page.click('div.filter__StyledChip-gx7onf-0>> text="44"')
        return self

    def open_page_short(self):
        self.page.locator("li").filter(has_text="Джинсові шорти").get_by_role("link").first.click()
        return self

    def check_size_chart(self):
        size_chart = self.page.get_by_role("button", name="Таблиця розмірів")
        if size_chart:
            size_chart.click()
            self.page.get_by_text("Як вимірювати?").click()
            self.page.mouse.click(0, 0)
        return self

    def add_to_cart(self):
        self.page.locator("li").filter(has_text="32 I UA 40").click()
        self.page.get_by_role("button", name="Додати").click()
        return self

    def check_cart(self):
        self.page.get_by_role("link", name="Перейти у кошик").click()
        self.page.wait_for_load_state('networkidle')
        self.page.wait_for_timeout(1500)
        assert self.page.locator('.product-list__Wrapper-mh8fks-0').is_visible()
        return self

    def check_favorites(self):
        self.page.get_by_test_id("heart").click()
        self.page.goto("https://www.sinsay.com/ua/uk/wishlist/")
        self.page.wait_for_load_state('networkidle')
        self.page.wait_for_timeout(1500)
        assert self.page.locator('.products-container').is_visible()
        return self

    def product_removal(self):
        self.page.get_by_test_id("wishlist_options_button").click()
        self.page.wait_for_selector('[data-testid="wishlist_options_modal"]')
        self.page.get_by_test_id("wishlist_Видалити з вибраних").click()
        return self

    def check_payment_page(self):
        self.page.goto("https://www.sinsay.com/ua/uk/help-types-of-payment")
        self.page.wait_for_load_state('networkidle')
        page_text = self.page.inner_text('.std h1')
        assert 'Оплата готівкою при отриманні' in page_text
        return self

    def check_about_us_page(self):
        self.page.goto("https://www.sinsay.com/ua/uk/about-us")
        self.page.wait_for_load_state('networkidle')
        page_text = self.page.inner_text('.view-2-box-1 h2.header')
        assert 'Давайте познайомимось!' in page_text
        return self

    def check_storelocator_page(self):
        self.page.goto("https://www.sinsay.com/ua/uk/storelocator")
        self.page.wait_for_load_state('networkidle')
        page_text = self.page.inner_text('.info-about-stores')
        assert 'За актуальною інформацією щодо графіка роботи магазинів, будь ласка, зверніться до співробітників контакт-центру' in page_text
        return self

    def check_error_message_login_field(self, message: str):
        page_text = self.page.inner_text('[data-name="login[username]"] .text-field__ErrorMessage-sc-1vll61a-4')
        assert message in page_text
        return self

    def check_error_message_password_field(self, message: str):
        page_text = self.page.inner_text('[data-name="login[password]"] .text-field__ErrorMessage-sc-1vll61a-4')
        assert message in page_text
        return self

    def check_error_message(self, message: str):
        page_text = self.page.inner_text('.sc-TmdmN')
        assert message in page_text
        return self

    def close(self):
        self.page.close()
        self.context.close()
        self.browser.close()
