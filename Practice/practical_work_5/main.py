import random
import game_utils

def choose_word(words):
    return random.choice(words)

def display_word(word, guessed_letters):
    return ''.join([letter if letter in guessed_letters else '■' for letter in word])

def play_game(words, difficulty):
    word = choose_word(words)
    guessed_letters = set()
    lives = difficulty
    record = 0

    while lives > 0:
        print(display_word(word, guessed_letters))
        print(f"Количество жизней: {'♥' * lives}")
        guess = input("Назовите букву или слово целиком: ").strip().lower()

        if len(guess) == 1:
            if guess in guessed_letters:
                print("Вы уже называли эту букву.")
                continue
            guessed_letters.add(guess)
            if guess in word:
                print(f"Буква '{guess}' есть в слове.")
            else:
                print(f"Буквы '{guess}' нет в слове. Вы теряете жизнь.")
                lives -= 1
        elif guess == word:
            print(f"Слово отгадано: {word}")
            print("Вы выиграли! Приз в студию!")
            record += 1
            return record
        else:
            print("Неправильно. Вы теряете жизнь.")
            lives -= 1

    print(f"Вы проиграли. Загаданное слово было: {word}")
    return record

def main():
    words = game_utils.load_words('words.txt')
    record = game_utils.load_record('record.txt')
    current_record = 0

    while True:
        print("Выберите уровень сложности:")
        print("1. Лёгкий (7 жизней)")
        print("2. Средний (5 жизней)")
        print("3. Сложный (3 жизни)")
        difficulty_choice = input("Введите номер уровня сложности: ").strip()

        if difficulty_choice == '1':
            difficulty = 7
        elif difficulty_choice == '2':
            difficulty = 5
        elif difficulty_choice == '3':
            difficulty = 3
        else:
            print("Неверный ввод. Попробуйте ещё раз.")
            continue

        current_record += play_game(words, difficulty)
        print(f"Ваш текущий рекорд: {current_record}")

        if current_record > record:
            game_utils.save_record('record.txt', current_record)
            record = current_record

        play_again = input("Хотите сыграть ещё раз? (да/нет): ").strip().lower()
        if play_again != 'да':
            break

    print(f"Ваш финальный рекорд: {record}")

if __name__ == "__main__":
    main()
