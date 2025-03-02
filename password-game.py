import random
import string
import time

def hack_game():
    print("=== Добро пожаловать в симуляцию хакера! ===")
    print("Ваша цель - пройти два этапа взлома:")
    print("1. Угадать секретный буквенный пароль.")
    print("2. После этого за минуту угадать трехзначный числовой пароль.")
    print("\nВыберите уровень сложности для первого пароля:\n")
    print("1. Легкий (4 символа)")
    print("2. Средний (5 символов)")
    print("3. Сложный (6 символов)")
    
    while True:
        try:
            difficulty = int(input("\nВыберите уровень сложности (введите 1, 2 или 3): "))
            if difficulty not in [1, 2, 3]:
                raise ValueError
            break
        except ValueError:
            print("Пожалуйста, введите 1, 2 или 3.")
    
    code_length = 4 + (difficulty - 1)
    attempts = 10 - difficulty

    secret_word = ''.join(random.choices(string.ascii_lowercase, k=code_length))
    
    print(f"\nСекретный буквенный пароль состоит из {code_length} букв.")
    print(f"У вас есть {attempts} попыток угадать пароль.\n")

    for attempt in range(1, attempts + 1):
        guess = input(f"Попытка {attempt}/{attempts}. Введите {code_length}-буквенный пароль: ").lower()
        
        if guess == secret_word:
            print("\n=== Успех! Вы угадали буквенный пароль! ===")
            break
        else:
            common_letters = sum(1 for a, b in zip(secret_word, guess) if a == b)
            print(f"Неверно. Совпадающих букв в правильных местах: {common_letters}")
    else:
        print(f"\nВы исчерпали все попытки! Секретный буквенный пароль был: {secret_word}")
        time.sleep(4)
        return
    
    print("\nТеперь вы должны угадать трехзначный числовой пароль за 60 секунд!")
    secret_number = random.randint(100, 999)
    start_time = time.time()
    guessed = False

    while time.time() - start_time < 60:
        guess = input("Введите трехзначный числовой пароль: ")
        if not guess.isdigit() or len(guess) != 3:
            print("Пожалуйста, введите корректный трехзначный числовой пароль.")
            continue
        
        if int(guess) == secret_number:
            guessed = True
            print("\n=== Успех! Вы угадали числовой пароль! ===")
            break
        elif int(guess) < secret_number:
            print("Неверно. Пароль больше.")
        else:
            print("Неверно. Пароль меньше.")
    
    if not guessed:
        print(f"\nВремя вышло! Секретный числовой пароль был: {secret_number}")
    else:
        print("\nПоздравляем! Вы успешно завершили хакерскую симуляцию!")

hack_game()
