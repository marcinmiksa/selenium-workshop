import unittest
from selenium import webdriver
from selenium.webdriver.support.ui import Select


class WorkshopTests(unittest.TestCase):
    """
    URL: https://breadcrumbscollector.tech/pl/selenium/01.html

    Wcisnij przyciski z sylabami tytułu popularnej piosenki w odpowiedniej kolejności
    i z rozwijanego menu wybierz język w jakim piosenka jest napisana.

    Podpowiedź:
    Pole wyboru to HTMLowski select. Można zobaczyć jak się nim posługiwać w dokumentacji:
    https://selenium-python.readthedocs.io/navigating.html#filling-in-forms
    """

    def setUp(self):
        self.driver = webdriver.Chrome(executable_path=r"C:\chromedriver\chromedriver.exe")

    def tearDown(self):
        self.driver.quit()

    def test_exercise(self):
        self.driver.get("https://breadcrumbscollector.tech/pl/selenium/01.html")

        element = self.driver.find_element_by_css_selector("button.de.btn")
        element.click()
        element1 = self.driver.find_element_by_css_selector("button.spa.btn")
        element1.click()
        element2 = self.driver.find_element_by_css_selector("button.ci.btn")
        element2.click()
        element3 = self.driver.find_element_by_css_selector("button.to.btn")
        element3.click()

        select = Select(self.driver.find_element_by_id("lang"))
        select.select_by_value("SPA")
        next_url = self.driver.switch_to.alert.text
        self.driver.switch_to.alert.accept()
        print(f'Nastepny URL: {next_url}')


if __name__ == "__main__":
    unittest.main()
