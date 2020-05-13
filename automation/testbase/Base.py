from selenium import webdriver

class Base(object):
    """
    Initiating browser
    """

    driver = webdriver.Chrome('C:/Users/com/PycharmProjects/Assembly/Drivers/chromedriver.exe')
