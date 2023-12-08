from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.common.exceptions import NoSuchElementException, WebDriverException
import constans as data
from time import sleep

hrefs = []
product_info = []


def delay_print(value):
    for i in value:
        search_field.send_keys(i)
        sleep(0.3)


def write_in_file():
    try:
        with open('products.csv', 'w', encoding="utf-8") as file:
            for item in product_info:
                file.write(f"{item['name']},{item['price']}\n")
    except FileNotFoundError as e:
        print(f"Помилка: Файл не знайдено. {e}")

    except PermissionError as e:
        print(f"Помилка: Немає прав для запису у файл. {e}")

    except Exception as e:
        print(f"Помилка при збереженні у файл. {e}")

            
        

try:
    #Open page with smartphones
    driver = webdriver.Chrome()
    driver.get(data.url)
    search_field = driver.find_element(By.CLASS_NAME, 'header-search__field')
    search_button = driver.find_element(By.CLASS_NAME, 'header-search__button')
    delay_print(data.info["phones"])
    search_button.click()

    # get all links and hrefs
    links = [a for a in driver.find_elements(By.CSS_SELECTOR, ".card__image > a")]
    for link in links:
        href = link.get_attribute('href')
        hrefs.append(href)

    #open each href get name and price of the good
    for href in hrefs:
        driver.get(href)
        good_name = driver.find_element(By.CSS_SELECTOR, '.page__title')
        price = driver.find_element(By.CSS_SELECTOR, '.product-box__main_price')
        print(good_name.text)
        print(price.text)
        product_info.append({"name": good_name.text, "price": price.text})

        driver.back()

    driver.close()

except NoSuchElementException as e:
        print(f"Помилка: Елемент не знайдено. {e}")

except WebDriverException as e:
        print(f"Помилка: Проблема з веб-драйвером. {e}")


#Запис даних в файл
write_in_file()