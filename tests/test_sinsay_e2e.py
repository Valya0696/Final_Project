def test_final_project_sinsay_e2e(final_project):
    final_project.open_url_and_accept_cookies('https://www.sinsay.com/ua/uk/')
    final_project.authorization()
    final_project.close_popup()

    final_project.search_shorts()

    final_project.filter_result()

    final_project.open_page_short()
    final_project.check_size_chart()

    final_project.add_to_cart()

    final_project.check_cart()
    final_project.check_favorites()
    final_project.product_removal()
    final_project.check_payment_page()
    final_project.check_about_us_page()
    final_project.check_storelocator_page()