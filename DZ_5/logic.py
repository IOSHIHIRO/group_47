from random import randint

def play_game(min_number, max_number, max_attempts, initial_capital):

    secret_number = randint(min_number, max_number)
    capital = initial_capital
    attempts = 0

    while attempts < max_attempts and capital > 0:
        print(f'Ваш макс капитал составляет {capital}')
        guess = int(input("Угадайте число от 1 до 20: "))
        attempts += 1

        if guess == secret_number:
            capital *= 2
            print("Вы угадали! Ваш капитал составляет:", capital)
            break
        else:
            capital -= 10
            print("Вы не угадали. Осталось попыток:", max_attempts - attempts)

    if capital == 0:
        print("Увы, вы проиграли!")
    else:
        print("Игра окончена. Ваш итоговый капитал:", capital)
        