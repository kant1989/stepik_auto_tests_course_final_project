from .base_page import BasePage
from .locators import BasketPageLocators, BasePageLocators


class BasketPage(BasePage):
    empty_basket_text_languages = {
        "ar": "سلة التسوق فارغة",
        "ca": "La seva cistella està buida.",
        "cs": "Váš košík je prázdný.",
        "da": "Din indkøbskurv er tom.",
        "de": "Ihr Warenkorb ist leer.",
        "en": "Your basket is empty.",
        "en-gb": "Your basket is empty.",
        "el": "Το καλάθι σας είναι άδειο.",
        "es": "Tu carrito esta vacío.",
        "fi": "Korisi on tyhjä",
        "fr": "Votre panier est vide.",
        "it": "Il tuo carrello è vuoto.",
        "ko": "장바구니가 비었습니다.",
        "nl": "Je winkelmand is leeg",
        "pl": "Twój koszyk jest pusty.",
        "pt": "O carrinho está vazio.",
        "pt-br": "Sua cesta está vazia.",
        "ro": "Cosul tau este gol.",
        "ru": "Ваша корзина пуста",
        "sk": "Váš košík je prázdny",
        "uk": "Ваш кошик пустий.",
        "zh-cn": "Your basket is empty.",
    }

    def should_be_empty_basket_message(self):
        assert self.is_element_present(*BasketPageLocators.EMPTY_BASKET_MESSAGE), \
            "Empty basket message is not presented, but should be"

    def should_not_be_empty_basket_message(self):
        assert self.is_not_element_present(*BasketPageLocators.EMPTY_BASKET_MESSAGE), \
            "Empty basket message is presented, but should not be"

    def check_empty_basket_message_text(self):
        empty_basket_message_text = self.browser.find_element(*BasketPageLocators.EMPTY_BASKET_MESSAGE).text
        continue_shopping_link = self.browser.find_element(*BasketPageLocators.CONTINUE_SHOPPING_LINK).text
        empty_basket_message_text_short = empty_basket_message_text.replace(" " + continue_shopping_link, "")

        selected_language = self.browser.find_element(*BasePageLocators.SELECTED_LANGUAGE).get_attribute("value")
        empty_basket_message_text_short_template = BasketPage.empty_basket_text_languages[selected_language]

        assert empty_basket_message_text_short == empty_basket_message_text_short_template, \
            "Empty basket text in message does not match the empty basket text template"
