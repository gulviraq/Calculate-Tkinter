import tkinter as tk

window = tk.Tk()
window.title("Калькулятор")
window.geometry("400x350")
window.resizable(False, False)

main_frame = tk.Frame(window, padx=20, pady=20)
main_frame.pack()

title_label = tk.Label(
    main_frame,
    text="Калькулятор",
    font=("Arial", 20, "bold")
)
title_label.grid(row=0, column=0, columnspan=2, pady=10)

first_label = tk.Label(main_frame, text="Первое число:")
first_label.grid(row=1, column=0, padx=5, pady=5)

first_entry = tk.Entry(main_frame, width=20)
first_entry.grid(row=1, column=1, padx=5, pady=5)

second_label = tk.Label(main_frame, text="Второе число:")
second_label.grid(row=2, column=0, padx=5, pady=5)

second_entry = tk.Entry(main_frame, width=20)
second_entry.grid(row=2, column=1, padx=5, pady=5)

def add_numbers():
    try:
        number1 = float(first_entry.get())
        number2 = float(second_entry.get())
        result = number1 + number2
        result_label.config(text=f"Результат: {result}")
    except ValueError:
        result_label.config(text="Введите числа правильно")

def subtract_numbers():
    try:
        number1 = float(first_entry.get())
        number2 = float(second_entry.get())
        result = number1 - number2
        result_label.config(text=f"Результат: {result}")
    except ValueError:
        result_label.config(text="Введите числа правильно")

def multiply_numbers():
    try:
        number1 = float(first_entry.get())
        number2 = float(second_entry.get())
        result = number1 * number2
        result_label.config(text=f"Результат: {result}")
    except ValueError:
        result_label.config(text="Введите числа правильно")

def divide_numbers():
    try:
        number1 = float(first_entry.get())
        number2 = float(second_entry.get())

        if number2 == 0:
            result_label.config(
                text="Ошибка: деление на ноль"
            )
        else:
            result = number1 / number2
            result_label.config(text=f"Результат: {result}")

    except ValueError:
        result_label.config(text="Введите числа правильно")

def clear_fields():
    first_entry.delete(0, tk.END)
    second_entry.delete(0, tk.END)
    result_label.config(text="Результат: ")

add_button = tk.Button(
    main_frame,
    text="Сложить",
    width=15,
    command=add_numbers
)
add_button.grid(row=3, column=0, padx=5, pady=5)

subtract_button = tk.Button(
    main_frame,
    text="Вычесть",
    width=15,
    command=subtract_numbers
)
subtract_button.grid(row=3, column=1, padx=5, pady=5)

multiply_button = tk.Button(
    main_frame,
    text="Умножить",
    width=15,
    command=multiply_numbers
)
multiply_button.grid(row=4, column=0, padx=5, pady=5)

divide_button = tk.Button(
    main_frame,
    text="Разделить",
    width=15,
    command=divide_numbers
)
divide_button.grid(row=4, column=1, padx=5, pady=5)

clear_button = tk.Button(
    main_frame,
    text="Очистить",
    width=32,
    command=clear_fields
)
clear_button.grid(row=5, column=0, columnspan=2, pady=10)

result_label = tk.Label(
    main_frame,
    text="Результат: ",
    font=("Arial", 14)
)
result_label.grid(row=6, column=0, columnspan=2, pady=15)

window.mainloop()
