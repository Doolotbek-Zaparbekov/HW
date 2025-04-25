from decouple import config
from random import randint, choice

min_num = config('min_number', cast=int)
max_num = config('max_number', cast=int)
attempt = config('attempts', cast=int)
initial_cap = config('initial_capital', cast=int)

def play_game():
    secret_num = randint(min_num, max_num)
    capital = initial_cap
    attempts = attempt
    print(f"Добро пожаловать в игру 'Угадай число'!")
    print(f"Угадайте число от {min_num} до {max_num}. У вас {attempts} попыток.")
    print(f"Начальный капитал: {capital} единиц.")
    while capital > 0 and attempts > 0:
        print(f'Попытка {attempts}')
        attempts -= 1
        try:
            guess = int(input("Ваше число: "))
            bet = int(input("Ставка: "))
        except ValueError:
            print("Ошибка ввода. Попробуйте снова.")
            continue
        if bet > capital or bet <= 0:
            print("Недопустимая ставка.")
            continue
        if guess == secret_num:
            capital += (bet * 2)
            print(f'Поздравляем! Вы угадали число! Ваш капитал увеличен до {capital}')
        else:
            capital -= bet

            print(f'Неверно! Осталось {attempt} попыток. Капитал: {capital}')
        if capital <= 0:
            print("Вы проиграли весь капитал. Игра окончена.")
            break
    print(f"Загаданное число было: {secret_num}")
    print(f"Игра окончена. Ваш итоговый капитал: {capital}")