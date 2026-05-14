#!/usr/bin/env python3
"""
Тестирование логики игры Крестики-нолики
"""

import sys
sys.path.insert(0, '/Users/radionpetrov/project_c606-52/Raed/lab08')

from lab08 import TicTacToe, InvalidMoveException, GameOverException, Player

def test_basic_game():
    """Тест: базовая игра"""
    print("=" * 50)
    print("Тест 1: Базовая игра (X выигрывает)")
    print("=" * 50)
    
    game = TicTacToe()
    
    # X побеждает по горизонтали (верхняя строка)
    moves = [
        (0, 0, "X"),  # X в верхний левый
        (1, 0, "O"),  # O в средний левый
        (0, 1, "X"),  # X в верхний центр
        (1, 1, "O"),  # O в центр
        (0, 2, "X"),  # X в верхний правый - ВЫИГРЫШ!
    ]
    
    for row, col, expected_player in moves:
        print(f"Ход: {expected_player} на позицию ({row}, {col})")
        game.make_move(row, col)
        
        board_state = game.get_board_state()
        print_board(board_state)
        
        if game.game_over:
            if game.winner:
                print(f"✓ {game.winner.value} выиграл!")
            else:
                print("✓ Ничья!")
    
    assert game.game_over, "Игра должна быть закончена"
    assert game.winner == Player.X, "X должен быть победителем"
    print("\n✓ Тест 1 ПРОЙДЕН\n")


def test_draw():
    """Тест: ничья"""
    print("=" * 50)
    print("Тест 2: Ничья")
    print("=" * 50)
    
    game = TicTacToe()
    
    # Ничья - тщательно выбранная последовательность
    # Финальная доска:
    # X O X
    # O X X
    # O X O
    moves = [
        (0, 0, "X"),  # X
        (0, 1, "O"),  # O
        (0, 2, "X"),  # X
        (1, 0, "O"),  # O
        (1, 1, "X"),  # X
        (2, 2, "O"),  # O
        (1, 2, "X"),  # X
        (2, 0, "O"),  # O
        (2, 1, "X"),  # X - ничья
    ]
    
    for row, col, expected_player in moves:
        print(f"Ход: {expected_player} на позицию ({row}, {col})")
        game.make_move(row, col)
        
        board_state = game.get_board_state()
        print_board(board_state)
    
    assert game.game_over, "Игра должна быть закончена"
    assert game.winner is None, "Не должно быть победителя"
    print("\n✓ Тест 2 ПРОЙДЕН\n")


def test_invalid_move():
    """Тест: невалидный ход"""
    print("=" * 50)
    print("Тест 3: Обработка невалидных ходов")
    print("=" * 50)
    
    game = TicTacToe()
    
    # Делаем валидный ход
    game.make_move(0, 0)
    print("✓ Ход на пустую позицию - OK")
    
    # Пытаемся ходить на ту же позицию
    try:
        game.make_move(0, 0)
        print("✗ Ошибка: должно было быть исключение!")
        assert False
    except InvalidMoveException as e:
        print(f"✓ Попытка повторного хода - перехвачено: {e}")
    
    # Пытаемся ходить за границы
    try:
        game.make_move(5, 5)
        print("✗ Ошибка: должно было быть исключение!")
        assert False
    except InvalidMoveException as e:
        print(f"✓ Ход за границы - перехвачено: {e}")
    
    print("\n✓ Тест 3 ПРОЙДЕН\n")


def test_game_over():
    """Тест: попытка хода в закончившейся игре"""
    print("=" * 50)
    print("Тест 4: Попытка хода в закончившейся игре")
    print("=" * 50)
    
    game = TicTacToe()
    
    # Создаём выигрыш X
    moves = [(0, 0), (1, 0), (0, 1), (1, 1), (0, 2)]
    for row, col in moves:
        game.make_move(row, col)
    
    print("✓ Игра закончена (X выиграл)")
    
    # Пытаемся ходить в закончившейся игре
    try:
        game.make_move(2, 2)
        print("✗ Ошибка: должно было быть исключение!")
        assert False
    except GameOverException as e:
        print(f"✓ Попытка хода в закончившейся игре - перехвачено: {e}")
    
    print("\n✓ Тест 4 ПРОЙДЕН\n")


def test_reset():
    """Тест: сброс игры"""
    print("=" * 50)
    print("Тест 5: Сброс игры")
    print("=" * 50)
    
    game = TicTacToe()
    
    # Делаем несколько ходов
    game.make_move(0, 0)
    game.make_move(1, 1)
    print("Сделано 2 хода")
    
    # Сбрасываем
    game.reset()
    print("✓ Игра сброшена")
    
    # Проверяем, что доска пуста
    board_state = game.get_board_state()
    print_board(board_state)
    
    assert game.current_player == Player.X
    assert not game.game_over
    assert game.winner is None
    
    print("\n✓ Тест 5 ПРОЙДЕН\n")


def test_diagonal_win():
    """Тест: победа по диагонали"""
    print("=" * 50)
    print("Тест 6: Победа O по диагонали")
    print("=" * 50)
    
    game = TicTacToe()
    
    # O побеждает по главной диагонали
    moves = [
        (0, 1, "X"),
        (0, 0, "O"),
        (1, 0, "X"),
        (1, 1, "O"),
        (2, 2, "X"),
        (2, 2, "O"),  # Это не будет выполнено, так как позиция занята
    ]
    
    # Правильная последовательность
    game.make_move(0, 1)  # X
    game.make_move(0, 0)  # O
    game.make_move(1, 0)  # X
    game.make_move(1, 1)  # O
    game.make_move(0, 2)  # X
    game.make_move(2, 2)  # O выигрывает (диагональ)
    
    board_state = game.get_board_state()
    print_board(board_state)
    
    assert game.game_over
    assert game.winner == Player.O
    print("\n✓ Тест 6 ПРОЙДЕН\n")


def print_board(board_state):
    """Вывести доску"""
    print("\n  0 1 2")
    for row_idx, row in enumerate(board_state):
        print(f"{row_idx} {' '.join('|' + cell + '|' for cell in row)}")
    print()


def main():
    """Запуск всех тестов"""
    print("\n" + "=" * 50)
    print("ЗАПУСК ТЕСТОВ ДЛЯ КРЕСТИКОВ-НОЛИКОВ")
    print("=" * 50 + "\n")
    
    try:
        test_basic_game()
        test_draw()
        test_invalid_move()
        test_game_over()
        test_reset()
        test_diagonal_win()
        
        print("=" * 50)
        print("ВСЕ ТЕСТЫ ПРОЙДЕНЫ ✓")
        print("=" * 50)
        
    except Exception as e:
        print(f"\n✗ ОШИБКА: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)


if __name__ == "__main__":
    main()
