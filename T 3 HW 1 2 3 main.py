\Завдання 1 

import argparse
from pathlib import Path
import os
import shutil
def copy_files(src_dir, dest_dir):
    """
    Рекурсивно копіює файли з src_dir до dest_dir.
    Створює піддиректорії за розширенням файлу в dest_dir.
    """
    for item in os.listdir(src_dir):
        src_path = os.path.join(src_dir, item)
        if os.path.isdir(src_path):
            copy_files(src_path, dest_dir)
        else:
            _, ext = os.path.splitext(item)
            ext_dir = os.path.join(dest_dir, ext.lstrip('.'))
            os.makedirs(ext_dir, exist_ok=True)
            dest_path = os.path.join(ext_dir, item)
            try:
                shutil.copy2(src_path, dest_path)
            except IOError as e:
                print(f"Помилка копіювання файлу {src_path}: {e.strerror}")
if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Копіювання файлів з сортуванням за розширенням"
    )
    parser.add_argument(
        "src_dir", type=str, help="Шлях до вихідної директорії"
    )
    parser.add_argument(
        "-d", "--dest_dir", type=str, default="dist",
        help="Шлях до директорії призначення (за замовчуванням: dist)"
    )
    args = parser.parse_args()
    src_dir = Path(args.src_dir)
    dest_dir = Path(args.dest_dir)
    if not src_dir.exists() or not src_dir.is_dir():
        print(f"Помилка: {src_dir} не є існуючою директорією")
    else:
        try:
            copy_files(str(src_dir), str(dest_dir))
        except OSError as e:
            print(f"Помилка доступу до директорії: {e.strerror}") 



\Завдання 2 

import turtle
def draw_koch_curve(length, order, t):
    """
    Рекурсивно малює криву Коха довжиною length з порядком order.
    t - об'єкт turtle для малювання.
    """
    if order == 0:
        t.forward(length)
    else:
        draw_koch_curve(length / 3, order - 1, t)
        t.left(60)
        draw_koch_curve(length / 3, order - 1, t)
        t.right(120)
        draw_koch_curve(length / 3, order - 1, t)
        t.left(60)
        draw_koch_curve(length / 3, order - 1, t)
def draw_koch_snowflake(order, size):
    """
    Малює сніжинку Коха порядку order та розміру size.
    """
    t = turtle.Turtle()
    t.speed(0)  # прискорює малювання
    t.penup()
    t.goto(-size, -size * 0.57)  # початкова позиція
    t.pendown()
    for _ in range(3):
        draw_koch_curve(size, order, t)
        t.right(120)
    turtle.exitonclick()
if __name__ == "__main__":
    order = int(input("Введіть рівень рекурсії (число від 0 до 5): "))
    if order < 0 or order > 5:
        print("Некоректний рівень рекурсії. Використовуємо 3 за замовчуванням.")
        order = 3
    draw_koch_snowflake(order, 300) 


\Завдання 3 

def hanoi_tower(n, source, auxiliary, target):
    """
    Функція, яка реалізує алгоритм Ханойських веж.
    Args:
        n (int): Кількість дисків.
        source (str): Назва стовпчика, з якого переміщаємо диски.
        auxiliary (str): Назва допоміжного стовпчика.
        target (str): Назва стовпчика, на який переміщаємо диски.
    """
    if n == 1:
        print(f"Перемістити диск з {source} на {target}")
        pegs[target].append(pegs[source].pop())
        print_state()
        return
    hanoi_tower(n - 1, source, target, auxiliary)
    print(f"Перемістити диск з {source} на {target}")
    pegs[target].append(pegs[source].pop())
    print_state()
    hanoi_tower(n - 1, auxiliary, source, target)
def print_state():
    """
    Функція для виведення поточного стану стовпчиків.
    """
    print("Проміжний стан:", pegs)
if __name__ == "__main__":
    n = int(input("Введіть кількість дисків: "))
    pegs = {'A': list(range(n, 0, -1)), 'B': [], 'C': []}
    print("Початковий стан:", pegs)
    hanoi_tower(n, 'A', 'B', 'C')
    print("Кінцевий стан:", pegs) 






