import turtle

def draw_pifagor_tree(branch_len, level):
    if level > 0:
        turtle.forward(branch_len)
        turtle.right(45)
        draw_pifagor_tree(0.7 * branch_len, level-1)
        turtle.left(90)
        draw_pifagor_tree(0.7 * branch_len, level-1)
        turtle.right(45)
        turtle.backward(branch_len)

turtle.speed(0)  # Швидкість малювання (0 - найшвидше)

# Налаштування початкового положення та напрямку
turtle.left(90)
turtle.up()
turtle.backward(100)
turtle.down()

# Ввід рівня рекурсії від користувача
level = int(input("Введіть рівень рекурсії: "))

# Малювання фрактала
draw_pifagor_tree(100, level)

turtle.exitonclick()  # Завершення роботи по кліку на екрані
