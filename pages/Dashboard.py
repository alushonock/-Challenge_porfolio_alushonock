from pages.base_page import BasePage


class Dashboard(BasePage):
    button_xpath = "//*[@id='login']"
    login_field_xpath = "//*[@id='login']"
    password_field_xpath = "//*[@id='password']"
    sign_in_xpath = "//*[@id='__next']/form/div/div[2]/button/span[1]"
    remind_password_xpath = "//*[@id='__next']/form/div/div[1]/a"
    english_xpath = "//*[@id='__next']/form/div/div[1]/a"
    polski_xpath = "//*[@id='__next']/form/div/div[2]/div/div"
    muicardcontentroot_xpath = "//div[@class='MuiCardContent-root']"
    