import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import  WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

link = "https://rozetka.com.ua"
browser = webdriver.Chrome()
#раскрыть окно браузера
browser.maximize_window()
browser.get(link)

serch_string = browser.find_element(By.CSS_SELECTOR, "input[class*=search-form__input]")
serch_string.send_keys("Мебель")

#поиск кнопки
knopka = browser.find_element(By.CSS_SELECTOR, "button[class*= button_color_green]").click()

#проверяем текст поиска
proverka = WebDriverWait(browser, 10).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, "h1[class*=portal__heading]"))).text


proverka1 = "Мебель"
assert proverka == proverka1, f"test failed, вот что удалось найти вместо-  {proverka}"
browser.quit()

