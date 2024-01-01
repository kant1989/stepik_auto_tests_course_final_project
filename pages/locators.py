from selenium.webdriver.common.by import By


class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    BASKET_LINK = (By.XPATH, "//span[@class='btn-group']/a[contains(@href, 'basket')]")
    SELECTED_LANGUAGE = (By.CSS_SELECTOR, "select[name='language']>option[selected]")


class MainPageLocators():
    pass


class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")


class ProductPageLocators():
    ADD_TO_BASKET_BUTTON = (By.CSS_SELECTOR, ".btn-add-to-basket")
    PRODUCT_NAME = (By.CSS_SELECTOR, ".product_main h1")
    PRODUCT_ADD_TO_BASKET_MESSAGE = (By.CSS_SELECTOR, "#messages>div:nth-child(1)")
    PRODUCT_NAME_IN_MESSAGE = (By.XPATH, "//div[@id='messages']/div[1]//strong")
    PRODUCT_PRICE = (By.CSS_SELECTOR, ".product_main .price_color")
    BASKET_PRICE_MESSAGE = (By.CSS_SELECTOR, "#messages>div.alert-info")
    BASKET_PRICE_IN_MESSAGE = (By.XPATH, "//div[@id='messages']/div[3]//strong")


class BasketPageLocators():
    EMPTY_BASKET_MESSAGE = (By.CSS_SELECTOR, "#content_inner>p")
    CONTINUE_SHOPPING_LINK = (By.CSS_SELECTOR, "#content_inner>p>a")
