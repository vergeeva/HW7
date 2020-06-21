from header7 import *


def main():
    one = trigonometric_function()
    one.input_object()
    two = trigonometric_function(1, 6, 3, 1)
    print(f'Для объекта 1 при x=0, y= {one.find_func(0)}')
    print(f'Для объекта 2 при x=0, y= {two.find_func(0)}')

    table_one = table()
    table_two = table(1, 2, 1, 5, 1, 0.3, 0)
    table_three = table(1, 2, 1, 3, 1.6, 1, 1)
    table_four = table()

    print(f'one=three is {table_one == table_three}')
    print(f'one=four is {table_one == table_four}')

    table_three.make_table()
    table_two.make_table()

    table_four.x0 = 0
    table_four.xn = 3

    table_one.make_table()
    table_four.make_table()

    print(table_four)


main()
