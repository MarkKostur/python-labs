import re
class RegistryMeta(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance
        return cls._instances[cls]


class Registry(metaclass=RegistryMeta):
    def __init__(self, author):
       self.author = author
       self.books = []
    
    def show_info_books(self):
        for i in range(len(self.books)):
            print(i+1,'Книга', 'Автор', self.books[i].author, self.books[i].quantity_pages, 'сторінок',  self.books[i].name, "ім'я")
            
    def show_info_page_by_num(self, needed_book, index): 
        print('Текст', needed_book.arr_pages[index].text, 'Номер сторінки', needed_book.arr_pages[index].number)
        print('Якщо хочете продовжиити читати книгу, то введіть номер наступної сторінки, якщо ні, то напишіть ні')
        answer = input('Введіть ваш вибір\n')
        if answer == 'ні' or not answer.isnumeric(): quit()
        else:
            if needed_book.arr_pages[int(answer) - 1]: return self.show_info_page_by_num(needed_book, int(answer) - 1) 
            else: return print('Такої сторінки за вказаним номером нема')

    def read_book(self):
        self.show_info_books()
        print('Введіть номер книги, яку б хотіли прочитати')
        answer = int(input('Введіть ваш вибір\n'))
        if answer > len(self.books) or answer < 0: return print('Ви ввели неправильне число введіть шось нормальне')
        self.show_info_page_by_num(self.books[answer - 1], 0)



class FormedBook:
    def __init__(self, author, quantity_pages, name, size_page, arr_pages):
        self.author = author
        self.quantity_pages = quantity_pages
        self.name = name
        self.size_page = size_page
        self.arr_pages = arr_pages

class Book: 
    def __init__(self, author, quantity_pages, name, size_page):
        self.author = author
        self.quantity_pages = quantity_pages
        self.name = name
        self.size_page = size_page

    def write_book(self):
        text_content_book = input('Введіть текст\n')
        if len(text_content_book) > self.size_page:
            print('Ви ввели більше ніж', self.size_page, ' символів на сторінці')
            print('Ви можете залишити цю сторінку так як вона написана або написати заново.\n1)Залишити цю сторінку такою\n2)Переписати заново')
            answer_choice = int(input("Введіть ваш вибір\n"))
            match answer_choice:
                case 1:
                    return text_content_book[:self.size_page]
                case 2:
                    return self.write_book()
                case _:
                    print('Введіть шось нормальне')
        else: return text_content_book

class ScienceBook(Book):
    def __init__(self, author, quantity_pages, name, size_page, list_science_literature='not now', glossary='not now'):
        self.list_science_literature = list_science_literature
        self.glossary = glossary
        super().__init__(author, quantity_pages, name, size_page)

class BelestricBook(Book):
    def __init__(self, author, quantity_pages, name, size_page, list_characters='not now'):
        self.list_characters = list_characters
        super().__init__(author, quantity_pages, name, size_page)

class ManualBook(Book):
    def __init__(self, author, quantity_pages, name, size_page, picture_url='not now'):
        self.picture_url = picture_url
        super().__init__(author, quantity_pages, name, size_page)
    def add_img_url_func(self, i):
        print('Чи хочете додати картинку на цю сторінку?\n1)Так\n2)Ні')
        answer = int(input('Введіть ваш вибір\n'))
        match answer:
            case 1:
                url = input('Введіть посилання на картинку\n')
                # перевірка чи подається посилання на картинку
                regex = r'\.(jpg|jpeg|png|gif|bmp|svg|webp)'
                checked_url = re.search(regex, url, re.IGNORECASE)
                if checked_url == None: return print('Це не картинка')
                obj_page_with_img = Page(url, i+1, 'image')
                return obj_page_with_img
            case 2:
                return 'no image'
            case _:
                print('Введіть шось нормальне')
                return self.add_img_url_func(i)

class Page:
    def __init__(self, text, number, type):
        self.text = text
        self.number = number
        self.type = type
        
class WriterDirector:
    __pages_arr = []
    def __init__(self, writer_type):
        self.writer_type = writer_type

    def write_book_page_by_page(self, add_img_url='no'):
        for i in range(self.writer_type.quantity_pages):
            page = self.writer_type.write_book()
            obj_page = Page(page, i+1, 'ordinary page')            
            self.__pages_arr.append(obj_page)
            if add_img_url != 'no': 
                page_with_img = self.writer_type.add_img_url_func(i+1)
                if page_with_img != 'no image': self.__pages_arr.append(page_with_img)
                

    def write_science_book(self):
        self.write_book_page_by_page()
        print('Додайте список літератури\n')
        list_literature = self.writer_type.write_book()
        self.__pages_arr.append(Page(list_literature, len(self.__pages_arr) + 1, 'list_literature'))
        print('Додайте глосарій')
        glossary = self.writer_type.write_book()
        self.__pages_arr.append(Page(glossary, len(self.__pages_arr) + 1, 'glossary'))
        formed_science_book = FormedBook(self.writer_type.author, self.writer_type.quantity_pages, self.writer_type.name, self.writer_type.size_page, self.__pages_arr)
        return formed_science_book

    def write_belestric_book(self):
        self.write_book_page_by_page()
        print('Додайте список персонажів і їхній опис')
        list_characters_and_description = self.writer_type.write_book()
        self.__pages_arr.append(Page(list_characters_and_description, len(self.__pages_arr), 'list_characters_and_description'))
        formed_belestric_book = FormedBook(self.writer_type.author, self.writer_type.quantity_pages, self.writer_type.name, self.writer_type.size_page, self.__pages_arr)
        return formed_belestric_book
    
    def write_manual_book(self):
        self.write_book_page_by_page('yes')
        formed_manual_book = FormedBook(self.writer_type.author, self.writer_type.quantity_pages, self.writer_type.name, self.writer_type.size_page, self.__pages_arr)
        return formed_manual_book

def standard_quiz():
    answer_author = input("Хто є автором книги? Введіть ім'я\n")
    answer_quantity_pages = int(input("Скільки сторінок буде у книзі?\n"))
    answer_size_page = int(input("Введіть розмір сторінки у символах\n"))
    answer_name_book = input("Введіть ім'я книги\n")
    if answer_author and answer_quantity_pages and answer_name_book and answer_size_page > 0: return [answer_author, answer_quantity_pages, answer_name_book, answer_size_page]

def ask_if_continue():
    answer = input('Введіть так або ні\n')
    match answer:
        case 'так':
            return 'yes'
        case 'ні':
            return 'no'
        case _:
            print('Введіть щось нормальне')

def end_writing_book():
    print('Написання книги завершено. Чи хочете продовжити писати книги?')
    result_if_continue = ask_if_continue()
    if result_if_continue == 'yes': return start_write_book()



def start_write_book():
    print('Вибери тип книги, яку ти б хотів написати.\n1)Науковий\n2)Белетристичний\n3)Посібник\n4)Читати книги')
    answer = int(input("Введіть ваш вибір\n"))
    match answer:
        case 1:
            print('Ви вибрали науковий тип')
            standard_result = standard_quiz()
            author, quantity_pages, name_book, size_page = standard_result #деструктиризація
            writer = WriterDirector(ScienceBook(author, quantity_pages, name_book, size_page))
            science_book = writer.write_science_book()
            for page in science_book.arr_pages:
                print('Текст', page.text, 'номер сторінки', page.number)
            Registry_obj = Registry(author)
            Registry_obj.books.append(science_book)
            end_writing_book()
        case 2:
            print('Ви вибрали Белестричний тип')
            standard_result = standard_quiz()
            author, quantity_pages, name_book, size_page = standard_result
            writer = WriterDirector(BelestricBook(author, quantity_pages, name_book, size_page))
            belestric_book = writer.write_belestric_book()
            Registry_obj2 = Registry(author)
            Registry_obj2.books.append(belestric_book)
            end_writing_book() 
        case 3:
            print('Ви вибрали Посібник')
            standard_result = standard_quiz()
            author, quantity_pages, name_book, size_page = standard_result
            writer = WriterDirector(ManualBook(author, quantity_pages, name_book, size_page))
            manual_book = writer.write_manual_book()
            Registry_obj3 = Registry(author)
            Registry_obj3.books.append(manual_book)
            end_writing_book()
        case 4:
            Registry_obj4 = Registry('test')
            if not Registry_obj4.books: 
                print('У вас нема книг, які можна прочитати')
                return start_write_book()
            else: Registry_obj4.read_book()
        case _:
            print('Введіть шось нормальне')

start_write_book()