from .pages.product_page import ProductPage


def test_guest_can_add_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"
    page = ProductPage(browser, link)
    page.open()
    page.click_to_add_basket_button()
    page.solve_quiz_and_get_code()
    page.should_be_messages()
    page.check_product_name_in_message()
    page.check_basket_price_in_message()
