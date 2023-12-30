from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def click_to_add_basket_button(self):
        add_to_basket_button = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_BUTTON)
        add_to_basket_button.click()

    def should_be_messages(self):
        self.should_be_add_basket_message()
        self.should_be_basket_price_message()

    def should_be_add_basket_message(self):
        assert self.is_element_present(*ProductPageLocators.PRODUCT_ADD_TO_BASKET_MESSAGE), ("Add basket message is "
                                                                                             "not presented")

    def should_be_basket_price_message(self):
        assert self.is_element_present(*ProductPageLocators.BASKET_PRICE_MESSAGE), ("Basket price message is not "
                                                                                    "presented")

    def check_product_name_in_message(self):
        product_name = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text
        product_name_in_message = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME_IN_MESSAGE).text
        assert product_name == product_name_in_message, "Product name does not match the product name in message"

    def check_basket_price_in_message(self):
        product_price = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text
        basket_price_in_message = self.browser.find_element(*ProductPageLocators.BASKET_PRICE_IN_MESSAGE).text
        assert product_price == basket_price_in_message, "Product price does not match the basket price in message"
