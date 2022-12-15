import time

from selenium import webdriver
#поиск элементов
from selenium.webdriver.common.by import By
#ожидание элементов
from selenium.webdriver.support.ui import  WebDriverWait
#использование исключительного ожидания
from selenium.webdriver.support import expected_conditions as EC

link = "https://rozetka.com.ua"
browser = webdriver.Chrome()
#раскрыть окно браузера
browser.maximize_window()
browser.get(link)
#16 элементов, индекс определенный номер каждого элемента
#введем новую переменную она равно пустому списку в квадратных скобках
name_rosetka_16_el = ['Компьютеры и ноутбуки', 'Смартфоны, ТВ и Электроника', 'Товары для геймеров', 'Бытовая техника', 'Товары для дома', 'Инструменты и автотовары', 'Сантехника и ремонт', 'Дача, сад, огород', 'Спорт и увлечения', 'Fashion', 'Красота и здоровье', 'Товары для детей', 'Зоотовары', 'Офис, школа, книги', 'Алкогольные напитки и продукты', 'Товары для бизнеса и услуги']
proverka_name = []
#запускаем цикл из 16 повторений
for indx in range (16):
     #находим элемент на странице
    elements_by_rosetka = WebDriverWait(browser, 10).until(
        EC.visibility_of_all_elements_located((By.CSS_SELECTOR, "ul[class*=menu-categories_type_main]>li")))
    #далее кликакем по индексу каждому нашему элементу
    elements_by_rosetka[indx].click()
    #когда кликнули ищем его и берем с него текст
    name_rosetkas_elements = WebDriverWait(browser, 10).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, "h1.ng-star-inserted"))).text
    #наша переменная пустая добавляет текст этого элемента
    proverka_name.append(name_rosetkas_elements)
    time.sleep(4)
     #надо вернуться обратно
    browser.back()
assert name_rosetka_16_el == proverka_name, f"названия не совпадают, вот что получилось {proverka_name}"

browser.quit()


