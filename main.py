from random import randint
import datetime
import codecs

def receive_data():
    current_date_time = datetime.datetime.now()
    return current_date_time


def new_game():
    number = randint(10, 99)
    print("В этой игре Вам загадано случайное двухзначное число, вам предстоит его угадать")
    print("Количество Ваших попыток 10")
    print("Приятной игры!")
    with open("log.txt", "a", encoding="utf-8") as fin:
        now_data = receive_data()
        new_record = "[" + str(now_data) + u"][INFO][System]: Загадано число " + str(number) + "\n"
        fin.write(new_record)
    return number


def record_try(number):
    with open("log.txt", "a", encoding="utf-8") as fin:
        now_data = receive_data()
        new_record = "[" + str(now_data) + u"][INFO][User]: Введено число " + str(number)
        fin.write(new_record + "\n")


def record_win(number):
    with open("log.txt", "a", encoding="utf-8") as fin:
        now_data = receive_data()
        new_record = "[" + str(now_data) + u"][INFO][System]: Число угаданно"
        fin.write(new_record + "\n")
        new_record = "Попыток " + str(number)
        fin.write(new_record + "\n")


def main():
    win_number = new_game()
    attempts = 0
    more_salaries =[]
    less_salaries = []
    while attempts <= 10:
        try:
            player_number = int(input("Введите двухзначное число: "))
            if player_number > 9 and player_number < 100:
                if player_number > win_number:
                    attempts += 1
                    print("Ваше число больше загаданного")
                    record_try(player_number)
                    more_salaries.append(player_number)
                elif player_number < win_number:
                    attempts += 1
                    print("Ваше число меньше загаданного")
                    record_try(player_number)
                    less_salaries.append(player_number)
                else:
                    print("Число угаданно")
                    attempts += 1
                    print("Число попыток: " + str(attempts))
                    record_win(attempts)
                    break
            else:
                print("Введенно не двухзначное число, повторите попытку")
        except ValueError:
            print("Введене не число, повторите попытку")


if __name__ == "__main__":
    main()