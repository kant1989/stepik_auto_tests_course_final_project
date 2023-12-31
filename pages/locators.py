from selenium.webdriver.common.by import By


class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")


class MainPageLocators():
    pass


class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")


class ProductPageLocators():
    ADD_TO_BASKET_BUTTON = (By.CSS_SELECTOR, ".btn-add-to-basket")
    PRODUCT_NAME = (By.CSS_SELECTOR, ".product_main h1")
    PRODUCT_ADD_TO_BASKET_MESSAGE = (By.XPATH, "//div[contains(strong/following-sibling::text(), 'has been added to "
                                               "your basket.')]")
    PRODUCT_NAME_IN_MESSAGE = (By.XPATH, "//div[@id='messages']/div[1]//strong")
    PRODUCT_PRICE = (By.CSS_SELECTOR, ".product_main .price_color")
    BASKET_PRICE_MESSAGE = (By.XPATH, "//p[contains(text(), 'Your basket total is now')]")
    BASKET_PRICE_IN_MESSAGE = (By.XPATH, "//div[@id='messages']/div[3]//strong")
