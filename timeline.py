descripttion_years = {
    2018: "Champions League winner - Real Madrid",
    2019: "Champions League winner - Liverpool",
    2020: "Champions League winner - Bayern",
    2021: "Champions League winner - Chelsea ",
    2022: "Champions League winner - Real Madrid",
    2023: "Champions League winner - Manchester City ",
    2024: "Champions League winner - Real Madrid (of course)"
}

list_visited_years = []
wanted_years = set()


def create_events_checking_errors(year, years):
    if year in years:
        raise Exception("Такий рік уже є в словнику")


def check_for_error(year, years, setting="visit"):
    if year not in years:
        raise Exception("Такого року нема в словнику")
    if setting == "visit":
        for i in range(len(list_visited_years)):
            if list_visited_years[i][0] == year:
                raise Exception(
                    "Ти уже відвідував цей рік, тому ти не можеш його відвідати ще раз"
                )


def print_info_years():
    print("Виводжу список років і подій для вибору\n")
    list_keys = list(descripttion_years.keys())
    list_values = list(descripttion_years.values())

    for index in range(len(list_keys)):
        print("Рік", list_keys[index], "Подія", list_values[index])
    return list_keys


def start_visiting_years(years, wanted_user_years):
    for answer_wanted_year in wanted_user_years:
        if descripttion_years[answer_wanted_year]:
            check_for_error(answer_wanted_year, years)
            visited_event = (answer_wanted_year, descripttion_years[answer_wanted_year])
            list_visited_years.append(visited_event)
            print("list_visited_years", list_visited_years)


def quiz():
    years = print_info_years()
    print("Введіть скільки дат ви б хотіли відвідати")
    answer = int(input("Введіть ваше число\n"))
    if answer > len(descripttion_years):
        raise Exception(
            "Не можна відвідати більшу кількість подій ніж самих подій у словнику"
        )
    for _ in range(answer):
        print("Який рік хочеш вибрати серед запропонованих?")
        year_answer = int(input("Введіть ваш рік\n"))
        check_for_error(year_answer, years)
        wanted_years.add(year_answer)

    start_visiting_years(years, wanted_years)


def validate_year(year):
    if int(year) > 2100 or int(year) < 0 or len(year) > 4:
        raise Exception("Це не рік або неправильний формат")


def start():
    print(
        """
          
Вітаю, футбольний фанате, тепер ти можеш вибрати переможця Ліги Чемпіонів будь-якого року
          
"""
    )
    answer = int(
        input(
            "1)Ввести роки, які хочеш відвідати\n2)Вийти\n3)Додати подію і рік\n4)Видалити подію і рік\n"
        )
    )
    match answer:
        case 1:
            quiz()
            start()
        case 2:
            print("Ви вибрали вихід")
            quit()
        case 3:
            year = input("Введіть рік\n")
            validate_year(year)
            event = input("Введіть подію\n")
            create_events_checking_errors(year, list(descripttion_years.keys()))
            descripttion_years[int(year)] = event
            print_info_years()
            return start()
        case 4:
            year = int(input("Введіть рік, який хочете видалити\n"))
            check_for_error(year, list(descripttion_years.keys()), 'delete')
            del descripttion_years[year]
            print_info_years()
            return start()
start()
