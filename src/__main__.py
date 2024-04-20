import art

from src.game import Game
from src.mechanics import mechanic_list


def main():
    print(art.text2art("TicTacToe"))

    try:
        rows = int(input("Введите число строк игровой доски: "))
        cols = int(input("Введите число столбцов игровой доски: "))
        win_length = int(input("Введите длину победной линии: "))

        print("Игровые механики:")
        for i, (cls, desc) in enumerate(mechanic_list):
            print(f"{i + 1}. {desc}")

        mechanic_number = int(input("Выберите игровой режим: "))

        if rows <= 0 or cols <= 0 or win_length <= 0:
            print("Вводимые величины должны быть положительны")
            return

        if win_length > max(rows, cols):
            print(
                "Длина победной линии должна быть не меньше максимальной размерности игровой доски"
            )
            return

        if mechanic_number < 1 or mechanic_number > len(mechanic_list):
            print("Такой игровой механики не существует")
            return

    except ValueError:
        print("Некорректный формат данных")
    except (KeyboardInterrupt, EOFError):
        print("Приложение остановлено")
    else:
        print("Запускаем игру...")
        game = Game(mechanic_list[mechanic_number - 1][0], rows, cols, win_length)
        game.run()


if __name__ == "__main__":
    main()
