from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import StaleElementReferenceException
import matplotlib.pyplot as plt
import re


driver = webdriver.Chrome()


class DataBaseMeta(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance
        return cls._instances[cls]


class DataBase(metaclass=DataBaseMeta):
    def __init__(self, file_path):
        self.file_path = file_path

    def write_in_database(self, data_to_write):
        with open(self.file_path, "a", encoding="utf-8") as file:
            file.write("\n".join(data_to_write) + "\n")

    def read_database(self):
        text_to_use = ''
        with open(self.file_path, 'r', encoding="utf-8") as file:
            for line in file:
                text_to_use += line
            return text_to_use




all_textes_news = []
months = [12]
years = [2023]


def format_link(y, m):
    if m < 10:
        return f"https://www.unian.ua/news/archive/{y}0{m}02"
    elif m >= 10 and m < 13:
        return f"https://www.unian.ua/news/archive/{y}{m}02"


def get_news_text(href: str):
    driver.get(href)

    try:
        container_with_news = driver.find_elements(By.CSS_SELECTOR, ".article-text > p")
        for piece_news in container_with_news:
            all_textes_news.append(piece_news.text)
    except StaleElementReferenceException:
        driver.refresh()
        container_with_news = driver.find_elements(By.CSS_SELECTOR, ".article-text > p")
        for piece_news in container_with_news:
            all_textes_news.append(piece_news.text)
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        driver.back()


def open_news_page():
    links = driver.find_elements(By.CSS_SELECTOR, "h3 > .list-thumbs__title")

    for i, link in enumerate(links):
        href = link.get_attribute("href")
        print("href", href)
        get_news_text(href)
        if i >= 60:
            break


for year in years:
    for month in months:
        driver.get(format_link(year, month))
        open_news_page()

database_obj = DataBase("./lab11/data.txt")
database_obj.write_in_database(all_textes_news)

driver.close()

# working with text

def find_top_words(dict_words_with_count, wished_count_words=5):

    max(dict_words_with_count, key=dict_words_with_count.get)

    sorted_dict = dict(sorted(dict_words_with_count.items(), key=lambda item: item[1], reverse=True))

    result_dict = {key: sorted_dict[key] for key in sorted_dict}

    print('result_dict', result_dict)
    keys_dict = list(result_dict.keys())
    values_dict = list(result_dict.values())
    formed_dict_keys = keys_dict[0:wished_count_words]
    formed_dict_values = values_dict[0:wished_count_words]

    return formed_dict_keys, formed_dict_values


def count_words(all_words_list, unique_words_list):
    counter = 0
    global temp_word
    word_dict_with_frequency = {}
    for word in unique_words_list:
        temp_word = word
        for word_from_all in all_words_list:
            if word == word_from_all:
               counter+=1 
        word_dict_with_frequency[temp_word] = counter
        counter = 0
    print('word_dict_with_frequency', word_dict_with_frequency)
    return word_dict_with_frequency


    
def show_result(data_for_x_label, data_for_y_label):
    plt.bar(data_for_x_label, data_for_y_label)

    plt.title('Top 5 words by frequency')
    plt.xlabel('words')
    plt.ylabel('count')

    plt.show()

database_obj = DataBase('./lab11/data.txt')
text = database_obj.read_database()

words = re.findall(r'\b\w+\b', text)

filtered_words = [word.lower() for word in words if len(word) > 3]

print('filtered_words', len(filtered_words))

# receive unique words
unique_words = set(filtered_words)
print('unique_words', unique_words)
print('length', len(unique_words))

# converting set to list
unique_words_list = list(unique_words)

needed_dict = count_words(filtered_words, unique_words_list)

first_list, second_list = find_top_words(needed_dict)
show_result(first_list, second_list)