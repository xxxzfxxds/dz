import random
import tkinter as tk
from tkinter import messagebox

root = tk.Tk()
root.title("Игра в Кости")

initial_capital = 1234
available_capital = initial_capital

label_capital = tk.Label(root, text=f"Доступный капитал: {available_capital}", font=("Arial", 16))
label_capital.pack(pady=10)

label_bet = tk.Label(root, text="Введите вашу ставку:")
label_bet.pack(pady=10)

entry_bet = tk.Entry(root)
entry_bet.pack(pady=10)

label_result = tk.Label(root, text="", font=("Arial", 16))
label_result.pack(pady=10)


def update_capital_display():
    label_capital.config(text=f"Доступный капитал: {available_capital}")


def roll_dice():
    global available_capital

    bet_text = entry_bet.get()

    try:
        bet = int(bet_text)
        if bet <= 0:
            raise ValueError("Ставка должна быть положительным числом.")
        if bet > available_capital:
            raise ValueError("Недостаточно средств для этой ставки.")
    except ValueError as e:
        messagebox.showerror("Ошибка ввода", f"Пожалуйста, введите корректную ставку. {str(e)}")
        return

    player_score = throw_dice()
    opponent_score = throw_dice()

    result = f"Вы бросаете кубики и получаете {player_score} очков.\n"
    result += f"Противник бросает кубики и получает {opponent_score} очков.\n"

    if player_score > opponent_score:
        result += f"Вы выиграли! Выигрыш: {bet * 2}!"
        available_capital += bet
    elif player_score < opponent_score:
        result += f"Противник выиграл! Вы потеряли свою ставку: {bet}."
        available_capital -= bet
    else:
        result += f"Ничья! Вы получаете свою ставку обратно: {bet}."

    update_capital_display()
    label_result.config(text=result)


def throw_dice():
    return random.randint(1, 6) + random.randint(1, 6)


def add_to_bet(value):
    current_bet = entry_bet.get()
    if not current_bet.isdigit():
        current_bet = ""
    entry_bet.delete(0, tk.END)
    entry_bet.insert(0, current_bet + str(value))


def clear_bet():
    entry_bet.delete(0, tk.END)


button_roll = tk.Button(root, text="Бросить кубики", command=roll_dice)
button_roll.pack(pady=20)

button_exit = tk.Button(root, text="Выход", command=root.quit)
button_exit.pack(pady=20)

button_frame = tk.Frame(root)
button_frame.pack(pady=10)

for i in range(10):
    button = tk.Button(button_frame, text=str(i), command=lambda i=i: add_to_bet(i), width=3)
    button.grid(row=0, column=i)

button_clear = tk.Button(button_frame, text="C", command=clear_bet, width=3)
button_clear.grid(row=1, column=0)

root.mainloop()
