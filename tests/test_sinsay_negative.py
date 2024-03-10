def test_empty_fields_authorization(final_project):
    final_project.open_url_and_accept_cookies('https://www.sinsay.com/ua/uk/')
    final_project.open_login_form()
    final_project.click_login_button()
    final_project.check_error_message_login_field('Це обов’язкове поле')
    final_project.check_error_message_password_field('Це обов’язкове поле')


def test_authorization_incorrect_login(final_project):
    final_project.open_url_and_accept_cookies('https://www.sinsay.com/ua/uk/')
    final_project.open_login_form()
    final_project.login('incorrect_data')
    final_project.check_error_message_login_field('Введіть лише дійсні символи')


def test_authorization_incorrect_password(final_project):
    final_project.open_url_and_accept_cookies('https://www.sinsay.com/ua/uk/')
    final_project.open_login_form()
    final_project.login('xiyito4140@comsb.com')
    final_project.password('incorrect_data')
    final_project.click_login_button()
    final_project.check_error_message('Недійсний логін або пароль.')


