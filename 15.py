import numpy as np
import random


# Функция для создания начального состояния игрового поля
def create_board():
    numbers = list(range(1, 16)) + [0]  # Числа от 1 до 15 + пустая клетка (0)
    random.shuffle(numbers)  # Перемешиваем числа
    board = np.array(numbers).reshape(4, 4)  # Превращаем в 4x4 массив
    return board


# Функция для отображения игрового поля
def display_board(board):
    print("\nТекущее состояние:")
    for row in board:
        print(" ".join(f"{x:2}" if x != 0 else " ." for x in row))
    print()


# Функция для нахождения позиции пустой клетки (0)
def find_empty(board):
    return np.argwhere(board == 0)[0]  # Возвращает координаты пустой клетки


# Функция для перемещения плитки
def move_tile(board, direction):
    empty_pos = find_empty(board)
    x, y = empty_pos
    if direction == "up" and x > 0:
        board[x, y], board[x - 1, y] = board[x - 1, y], board[x, y]
    elif direction == "down" and x < 3:
        board[x, y], board[x + 1, y] = board[x + 1, y], board[x, y]
    elif direction == "left" and y > 0:
        board[x, y], board[x, y - 1] = board[x, y - 1], board[x, y]
    elif direction == "right" and y < 3:
        board[x, y], board[x, y + 1] = board[x, y + 1], board[x, y]
    else:
        print("Недопустимый ход!")
    return board


# Функция для проверки, решена ли головоломка
def is_solved(board):
    solution = list(range(1, 16)) + [0]  # Ожидаемое состояние
    return np.array_equal(board.flatten(), solution)


# Основная игра
def play_game():
    board = create_board()
    while is_solved(board):
        board = create_board()  # Создаем новое поле, если оно уже решено
    display_board(board)

    while True:
        if is_solved(board):
            print("Поздравляем, вы решили головоломку!")
            break
        print("Введите направление для перемещения (up, down, left, right):")
        move = input().strip().lower()
        if move in ["up", "down", "left", "right"]:
            board = move_tile(board, move)
            display_board(board)
        else:
            print("Некорректный ввод, попробуйте снова!")


# Запуск игры
if __name__ == "__main__":
    play_game()