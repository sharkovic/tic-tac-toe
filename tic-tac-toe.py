area = [[" ", "0", "1", "2"],
        ["0", "-", "-", "-"],
        ["1", "-", "-", "-"],
        ["2", "-", "-", "-"]
        ]


def check_kond(area, symb):
    if (area[1][1] == symb and area[1][2] == symb and area[1][3] == symb) or \
            (area[2][1] == symb and area[2][2] == symb and area[2][3] == symb) or \
            (area[3][1] == symb and area[3][2] == symb and area[3][3] == symb) or \
            (area[1][1] == symb and area[2][1] == symb and area[3][1] == symb) or \
            (area[1][2] == symb and area[2][2] == symb and area[3][2] == symb) or \
            (area[1][3] == symb and area[2][3] == symb and area[3][3] == symb) or \
            (area[1][1] == symb and area[2][2] == symb and area[3][3] == symb) or \
            (area[3][1] == symb and area[2][2] == symb and area[1][3] == symb):
        return True


def area_print(area):
    for i in area:
        print(" ".join(i))


area_print(area)
kol_area = len(area) - 1
step = 0
while True:
    step += 1
    if check_kond(area, "o"):
        print(f"Конец игры победил {area[x_pos + 1][y_pos + 1]}")
        break
    x = input("Введите через пробел координаты (СТОЛБЕЦ СТРОКА) чтобы поставить X: ")
    temp_x = x.replace(" ","")
    if temp_x.isnumeric():
        list_game = x.split()
        if len(list_game) != 2:
            print("Введено неверное значение")
            continue
        y_pos, x_pos = int(list_game[0]), int(list_game[1])
        if 0 <= (y_pos and x_pos) <= 2:
            if area[x_pos + 1][y_pos + 1] == "-":
                area[x_pos + 1][y_pos + 1] = "x"
                area_print(area)
            else:
                print("Ячейка занята")
                continue
        else:
            print("Таких координатов не существует ")
            continue
        if check_kond(area, "x"):
            print(f"Конец игры победил {area[x_pos + 1][y_pos + 1]}")
            break
    else:
        print("Введено неверное значение")
        continue
    if step == 9:
        print("ННичья, игра окончена")
        break
    while True:
        step += 1
        x = input("Введите через пробел координаты (СТОЛБЕЦ СТРОКА) чтобы поставить o: ")
        temp_x = x.replace(" ", "")
        if temp_x.isnumeric():
            list_game = x.split()
            if len(list_game) != 2:
                print("Введено неверное значение")
                continue
            y_pos, x_pos = int(list_game[0]), int(list_game[1])
            if 0 <= (y_pos and x_pos) <= 2:
                if area[x_pos + 1][y_pos + 1] == "-":
                    area[x_pos + 1][y_pos + 1] = "o"
                    area_print(area)
                else:
                    print("Ячейка занята")
                    continue
            else:
                print("Таких координатов не существует ")
                continue
            break
        else:
            print("Введено неверное значение")
            continue