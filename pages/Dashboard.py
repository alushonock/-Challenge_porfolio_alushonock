from pages.base_page import BasePage


class Dashboard(BasePage):
    scouts_panel_header_xpath = "//*[@id="__next"]/div[1]/header/div/h6"
    main_page_xpath = "//span[text() = 'Main page']"
    players_xpath = "//span[text() = 'Players']"
    sign_out_xpath = "//span[text() = 'Sign out']"
    players_count_xpath = "//div[text() = 'Players count']"
    number_10_xpath = "//b[text() = '10']"
    resports_count_xpath = "// div[text() = 'Reports count']"
    number_4_xpath = "//b[text()='4']"
    image_xpath = "//div[@class = 'MuiCardMedia-root jss8' and @title = 'Logo Scouts Panel']"
    inscription_ scouts_panel_xpath = "// div / h2[text() = 'Scouts Panel']"

   pass