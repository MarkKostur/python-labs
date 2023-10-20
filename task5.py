import datetime
from datetime import datetime


class DataBaseMeta(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance
        return cls._instances[cls]


class DataBase(metaclass=DataBaseMeta):
    info = []

    def read_file(self):
        with open("./lab5/база_даних_автомобілів.csv", "r") as file:
            for index, line in enumerate(file):
                if index == 0:
                    print(line)
                else:
                    print(self.info[index - 1].id, line)

    def write_in_file(self):
        list_keys = self.info[0].__dict__.keys()
        my_str = ""
        for index, key in enumerate(list_keys):
            my_str += f'{key if key != "id" else ""}{"," if index < len(list_keys) - 1 else ""}'
        my_str += "\n"
        with open("./lab5/база_даних_автомобілів.csv", "w") as file:
            file.write(my_str)
        for car in self.info:
            with open("./lab5/база_даних_автомобілів.csv", "a") as edited_file:
                str_info_car = f"{car.brand},{car.model},{car.year},{car.colour}\n"
                edited_file.write(str_info_car)

    def add_info(self, start_id):
        brand_answer, model_answer, year_answer, colour_answer = add_auto()
        auto_created_obj = Auto(
            brand_answer, model_answer, year_answer, colour_answer, start_id
        )
        self.info.append(auto_created_obj)
        self.write_in_file()

    def find_obj(self, array, cond, expect):
        found_obj = next(
            (obj for obj in array if getattr(obj, cond, None) == expect), None
        )
        if found_obj is not None:
            return found_obj
        else:
            return print("Не знайдено такого object")

    def edit_info(self, needed_number):
        found_car = self.find_obj(self.info, "id", needed_number)
        if found_car is not None:
            print(found_car.brand, found_car.id)
            list_keys = self.info[0].__dict__.keys()
            answer_field_change = input("Введіть поле, яке хочете змінити\n")
            found_key = next(
                (key for key in list_keys if key == answer_field_change), None
            )
            if found_key == "id":
                return print("Такий ключи не можна вводити")
            elif found_key:
                content_to_change = input("Введіть зміну до поля\n")
                setattr(found_car, found_key, content_to_change)
                self.write_in_file()
            else:
                return print("Такого ключа нема")
        else:
            return print("Машини за таким номером у списку нема")

    def delete_info(self, needed_number):
        found_car = self.find_obj(self.info, "id", needed_number)
        if found_car is not None:
            self.info.remove(found_car)
            self.write_in_file()
            print("Машину вилучено")
        else:
            return print("Машини з таким id нема у списку")

    def find_by(self):
        list_keys = self.info[0].__dict__.keys()
        param = input("Введіть параметер за яким будете шукати\n")
        found_key = next((key for key in list_keys if key == param), None)
        if found_key is not None:
            text_filter = input(f"Введіть текст для поля {param}\n")
            if text_filter.isnumeric():
                result = self.find_obj(self.info, param, int(text_filter))
            else:
                result = self.find_obj(self.info, param, text_filter)
            print(result.id, result.brand, result.model, result.year, result.colour)
        else:
            return print("Нема такого параметру, за яким можна посортувати")

    def sort_by(self):
        list_keys = self.info[0].__dict__.keys()
        param = input("Введіть параметр, за яким будете сортувати\n")
        found_key = next((key for key in list_keys if key == param), None)
        array_to_sort = []
        if found_key is not None:
            for car in self.info:
                array_to_sort.append(getattr(car, found_key))
            sorted_arr = sorted(array_to_sort)
            new_sorted_cars = []
            for value in sorted_arr:
                car_found = self.find_obj(self.info, found_key, value)
                new_sorted_cars.append(car_found)
            self.info = new_sorted_cars
            self.write_in_file()

        else:
            return print("Нема такого параметру за яким можна посортувати")

    def statistic_years(self):
        years = []
        for car in self.info:
            years.append(car.year)
        sum = 0
        for year in years:
            sum += year
        avg_year = sum / len(years)
        print("avg_year", round(avg_year))


class Auto:
    def __init__(self, brand, model, year, colour, id):
        self.brand = brand
        self.model = model
        self.year = year
        self.colour = colour
        self.id = id


auto1 = Auto("Toyota", "Camry", 2010, "black", 1)
auto2 = Auto("Lanos", "Mustang turo 911", 2022, "silver", 2)
auto3 = Auto("Lanos", "Deo", 2005, "silver", 3)
auto4 = Auto("Porshe 911", "Turbo S", 2020, "yellow", 4)
auto5 = Auto("Lamborghini", "Huracan", 2018, "red", 5)

list_autos = [auto1, auto2, auto3, auto4, auto5]

database_obj = DataBase()
database_obj.info.extend(list_autos)
print(database_obj.info)

database_obj.write_in_file()
start_id = 5


def add_auto():
    brand_answer = input("Введіть назву марки автомобіля\n")
    model_answer = input("Введіть назву моделі автомобіля\n")
    year_answer = int(input("Введіть рік автомобіля\n"))
    colour_answer = input("Введіть колір автомобіля\n")

    if year_answer < 0 or year_answer > datetime.now().year:
        return print("Рік не повинен бути меншим за 0 або більшим за сьогоднішній рік")

    return [brand_answer, model_answer, year_answer, colour_answer]


def quiz():
    answer_user_number = int(
        input("Введіть номер авто інформацію якого хочете змінити\n")
    )
    if answer_user_number <= 0:
        return print("Нема такого автомобіля, який починався б на номер 0 або менше")
    return answer_user_number


while True:
    print(
        "1)Прочитати Базу Даних\n2)Додати дані в базу\n3)Оновлення одного з полів у файлі\n4)Вилучити машинку зі списку\n5)Пошук за обраним критерієм\n6)Сортувати за критерієм\n7)Статистика по середньому році автомобілів\n8)Вийти\n"
    )
    answer = int(input("Введіть ваш вибір\n"))
    match answer:
        case 1:
            database_obj.read_file()
        case 2:
            start_id += 1
            database_obj.add_info(start_id)
        case 3:
            result_quiz = quiz()
            database_obj.edit_info(result_quiz)
        case 4:
            result_quiz = quiz()
            database_obj.delete_info(result_quiz)
        case 5:
            database_obj.find_by()
        case 6:
            database_obj.sort_by()
        case 7:
            database_obj.statistic_years()
        case 8:
            exit()
        case _:
            print("Введіть шось нормальне")
