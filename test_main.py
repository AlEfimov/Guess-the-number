from main import new_game
from main import record_try
from main import record_win
from main import main

def test_new_game():
    assert new_game() == new_game_last()


def new_game_last():
    with open("log.txt") as fin:
        text_log = fin.read()
        number = int(text_log[-3:-1])
        return number


def test_record_try():
    assert record_try(25) == None


def test_record_win():
    assert record_win(9) == None


def test_main_if_end_try(monkeypatch, capfd):
    inputs = iter(['12', "12", '12', "12", '12', "12", '12', "12", '12', "12"])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    main()
    out, err = capfd.readouterr()
    out_salaries = out.split("\n")
    out = out_salaries[-2]
    assert out == "Вы проиграли: закончились попытки"
