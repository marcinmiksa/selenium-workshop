from selenium import webdriver

driver = webdriver.Chrome(executable_path=r"C:\chromedriver\chromedriver.exe")

try:
    driver.get('http://python.org')
    input('W nowym oknie Chrome powinna załadować się strona python.org')
finally:
    driver.quit()

