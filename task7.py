import random, re

answers = ['yes', 'no', 'maybe']

def check_question(question):
    regex = '^[a-zA-Z0-9 ?]*$' 
    if len(question) == 0 or not re.match(regex, question) or not isinstance(question, str): return 1
    print('Your question', question)

def charivna_kulka_changed_chances(question, indexes_and_probabilities_arr, answers_array):
    if check_question(question) == 1: return 'it is not a question'
    random_chance = random.random()
    coefficient = 0
    for i,chance in indexes_and_probabilities_arr:
        coefficient += chance
        if random_chance < coefficient:
            return answers_array[i]

def charivna_kulka(question, choices):
    """
    _summary_

    Args:
        question (_type_): string
        we receive a string and depending on question return a result

    Returns:
        _type_: string
        if it is not a question or just set of numbers,
        it will return that it is not a question
    """
    if check_question(question) == 1: return 'it is not a question'
    answer = random.randint(0, len(choices) - 1)
    return choices[answer]

def show_answers(answers_bulb):
    for answer in answers_bulb:
        print(answer)

def configure_magic_ball(question, additional_answers, original_answers):
    original_answers.extend(additional_answers)
    new_answers = set(original_answers)
    answers = list(new_answers)
    show_answers(new_answers)
    answers_for_configured_bulb = []
    print('Задайте шанси для кульки')
    for i in range(len(new_answers)):
        chance = eval(input(f'Введіть ваш шанс для {i+1} відповіді\n'))
        cortage = (i, chance)
        answers_for_configured_bulb.append(cortage)
    result = charivna_kulka_changed_chances(question, answers_for_configured_bulb, answers)
    print('result', result)


while True:
    print('Задайте ваше питання і отримайте відпоідь.\n1)Задати питання\n2)Змінити налаштування кульки\n3)Вийти')
    answer = int(input('Введіть ваш вибір\n'))
    match answer:
        case 1:
            question = input('Введіть ваше питання\n')
            result = charivna_kulka(question, answers)
            print('answer', result)
        case 2:
            question = input('Введіть ваше питання\n')
            answers_from_user = input('Введіть додаткові відповіді кульки, які ви б хотіли бачити розділяючи пробілом\n')
            addititonal_answers = answers_from_user.split(', ')
            configure_magic_ball(question, addititonal_answers, answers)
        case 3:
            exit()
        case _:
            print('Введіть шось нормальне')

