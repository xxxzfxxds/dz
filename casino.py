import random
import tkinter as tk

root = tk.Tk()
root.title("Игра в Кости")

label_result = tk.Label(root, text="", font=("Arial", 16))
label_result.pack(pady=10)


def roll_dice():
    name = "Игрок"
    player_score = throw_dice()
    opponent_score = throw_dice()

    # Отображаем результат
    result = f"{name} бросает кубики и получает {player_score} очков.\n"
    result += f"Противник бросает кубики и получает {opponent_score} очков.\n"

    if player_score > opponent_score:
        result += f"{name} выиграл!"
    elif player_score < opponent_score:
        result += "Противник выиграл!"
    else:
        result += "Ничья!"

    label_result.config(text=result)


def throw_dice():
    return random.randint(1, 6) + random.randint(1, 6)


button_roll = tk.Button(root, text="Бросить кубики", command=roll_dice)
button_roll.pack(pady=20)

button_exit = tk.Button(root, text="Выход", command=root.quit)
button_exit.pack(pady=20)

root.mainloop()

root.mainloop()
