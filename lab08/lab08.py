"""
Приложение "Крестики-нолики" (Tic-Tac-Toe)
Реализовано с использованием Tkinter GUI фреймворка
Использует ООП парадигму и собственные исключения
"""

import tkinter as tk
from tkinter import messagebox
from enum import Enum
from typing import Optional, Tuple


# Исключения 

class GameException(Exception):
    """Базовое исключение для игры"""
    pass


class InvalidMoveException(GameException):
    """Выброс когда ход невалиден"""
    pass


class GameOverException(GameException):
    """Выброс когда игра закончена"""
    pass


# Перечисления

class Player(Enum):
    """Перечисление игроков"""
    X = "X"
    O = "O"
    EMPTY = " "


#  Игровая логика 

class TicTacToe:
    """Класс для логики игры Крестики-нолики"""
    
    BOARD_SIZE = 3
    
    def __init__(self):
        """Инициализация игры"""
        self.board = [[Player.EMPTY for _ in range(self.BOARD_SIZE)] 
                      for _ in range(self.BOARD_SIZE)]
        self.current_player = Player.X
        self.game_over = False
        self.winner = None
    
    def make_move(self, row: int, col: int) -> None:
        """
        Сделать ход в позицию (row, col)
        
        Args:
            row: Номер строки (0-2)
            col: Номер колонки (0-2)
            
        Raises:
            GameOverException: Если игра уже закончена
            InvalidMoveException: Если ход невалиден
        """
        if self.game_over:
            raise GameOverException("Игра уже закончена!")
        
        if not (0 <= row < self.BOARD_SIZE and 0 <= col < self.BOARD_SIZE):
            raise InvalidMoveException("Позиция вне доски!")
        
        if self.board[row][col] != Player.EMPTY:
            raise InvalidMoveException("Эта позиция уже занята!")
        
        self.board[row][col] = self.current_player
        
        # Проверяем победу
        if self._check_winner(self.current_player):
            self.winner = self.current_player
            self.game_over = True
        # Проверяем ничью
        elif self._is_board_full():
            self.game_over = True
        else:
            # Переключаемся на другого игрока
            self.current_player = Player.O if self.current_player == Player.X else Player.X
    
    def _check_winner(self, player: Player) -> bool:
        """Проверить, выиграл ли игрок"""
        # Проверяем строки
        for row in self.board:
            if all(cell == player for cell in row):
                return True
        
        # Проверяем колонки
        for col in range(self.BOARD_SIZE):
            if all(self.board[row][col] == player for row in range(self.BOARD_SIZE)):
                return True
        
        # Проверяем диагонали
        if all(self.board[i][i] == player for i in range(self.BOARD_SIZE)):
            return True
        
        if all(self.board[i][self.BOARD_SIZE - 1 - i] == player for i in range(self.BOARD_SIZE)):
            return True
        
        return False
    
    def _is_board_full(self) -> bool:
        """Проверить, полная ли доска"""
        return all(self.board[row][col] != Player.EMPTY 
                   for row in range(self.BOARD_SIZE) 
                   for col in range(self.BOARD_SIZE))
    
    def reset(self) -> None:
        """Сбросить игру"""
        self.board = [[Player.EMPTY for _ in range(self.BOARD_SIZE)] 
                      for _ in range(self.BOARD_SIZE)]
        self.current_player = Player.X
        self.game_over = False
        self.winner = None
    
    def get_board_state(self) -> list:
        """Получить текущее состояние доски"""
        return [[cell.value for cell in row] for row in self.board]


# GUI 

class TicTacToeApp:
    """Класс для GUI приложения Крестики-нолики"""
    
    BUTTON_SIZE = 6
    FONT_SIZE = ("Arial", 20, "bold")
    
    def __init__(self, root: tk.Tk):
        """
        Инициализация приложения
        
        Args:
            root: Корневой виджет Tkinter
        """
        self.root = root
        self.root.title("Крестики-нолики")
        self.root.resizable(False, False)
        
        self.game = TicTacToe()
        self.buttons = [[None for _ in range(3)] for _ in range(3)]
        
        self._create_widgets()
        self._update_display()
    
    def _create_widgets(self) -> None:
        """Создать виджеты интерфейса"""
        # Фрейм для информации
        info_frame = tk.Frame(self.root, bg="#f0f0f0", pady=10)
        info_frame.pack(fill=tk.X)
        
        self.status_label = tk.Label(
            info_frame,
            text="",
            font=("Arial", 14),
            bg="#f0f0f0"
        )
        self.status_label.pack()
        
        # Фрейм для доски
        board_frame = tk.Frame(self.root, bg="#333", padx=5, pady=5)
        board_frame.pack(padx=10, pady=10)
        
        for row in range(3):
            for col in range(3):
                button = tk.Button(
                    board_frame,
                    text="",
                    font=self.FONT_SIZE,
                    width=self.BUTTON_SIZE,
                    height=3,
                    bg="#ffffff",
                    command=lambda r=row, c=col: self._on_button_click(r, c)
                )
                button.grid(row=row, column=col, padx=2, pady=2)
                self.buttons[row][col] = button
        
        # Фрейм для кнопок управления
        control_frame = tk.Frame(self.root, bg="#f0f0f0", pady=10)
        control_frame.pack(fill=tk.X)
        
        reset_button = tk.Button(
            control_frame,
            text="Новая игра",
            font=("Arial", 12),
            command=self._reset_game,
            bg="#4CAF50",
            fg="white",
            padx=20,
            pady=10
        )
        reset_button.pack(side=tk.LEFT, padx=5)
        
        quit_button = tk.Button(
            control_frame,
            text="Выход",
            font=("Arial", 12),
            command=self.root.quit,
            bg="#f44336",
            fg="white",
            padx=20,
            pady=10
        )
        quit_button.pack(side=tk.RIGHT, padx=5)
    
    def _on_button_click(self, row: int, col: int) -> None:
        """Обработчик клика кнопки"""
        try:
            self.game.make_move(row, col)
            self._update_display()
            
            if self.game.game_over:
                if self.game.winner:
                    messagebox.showinfo(
                        "Игра закончена",
                        f"Игрок {self.game.winner.value} выиграл!"
                    )
                else:
                    messagebox.showinfo(
                        "Игра закончена",
                        "Ничья!"
                    )
        
        except InvalidMoveException as e:
            messagebox.showwarning("Неверный ход", str(e))
        except GameOverException as e:
            messagebox.showinfo("Игра закончена", str(e))
        except GameException as e:
            messagebox.showerror("Ошибка игры", str(e))
    
    def _update_display(self) -> None:
        """Обновить отображение доски и статуса"""
        board_state = self.game.get_board_state()
        
        for row in range(3):
            for col in range(3):
                button = self.buttons[row][col]
                cell_value = board_state[row][col]
                button.config(text=cell_value)
                
                # Изменяем цвет для X и O
                if cell_value == "X":
                    button.config(fg="#0066cc")
                elif cell_value == "O":
                    button.config(fg="#ff6600")
                else:
                    button.config(fg="black")
                
                # Отключаем кнопку если клетка занята
                button.config(state=tk.DISABLED if cell_value != " " else tk.NORMAL)
        
        # Обновляем статус
        if self.game.game_over:
            if self.game.winner:
                status_text = f"✓ Игрок {self.game.winner.value} выиграл!"
            else:
                status_text = "✓ Ничья!"
        else:
            status_text = f"Ход игрока: {self.game.current_player.value}"
        
        self.status_label.config(text=status_text)
    
    def _reset_game(self) -> None:
        """Сбросить игру"""
        self.game.reset()
        
        # Включаем все кнопки
        for row in range(3):
            for col in range(3):
                self.buttons[row][col].config(state=tk.NORMAL)
        
        self._update_display()


# Точка входа 

def main():
    """Главная функция"""
    root = tk.Tk()
    app = TicTacToeApp(root)
    root.mainloop()


if __name__ == "__main__":
    main()
