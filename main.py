from random import randint

array_x = []
array_y = []
array_xy = []
num_line = 8
num_column = 8
num_chess = 8
start_init = False
step = 0
count_step5 = 0
count_step6 = 0

def generate_x():
    global num_line
    global array_x
    end_x = True
    while end_x:
        pos_x = randint(0, num_line - 1)
        if array_x[pos_x] == ".":
            array_x[pos_x] = "X"
            return pos_x
        end_x = False
        for i in array_x:
            if i == ".":
                end_x = True


def generate_y():
    global num_column
    global array_y
    end_y = True
    while end_y:
        pos_y = randint(0, num_column - 1)
        if array_y[pos_y] == ".":
            array_y[pos_y] = "X"
            return pos_y
        end_y = False
        for i in array_y:
            if i == ".":
                end_y = True


def array_initialization():
    global num_column
    global num_line
    global array_x
    global array_y
    global array_xy
    global start_init
    global step
    global count_step5
    global count_step6
    start_init = False
    step = 0
    count_step5 = 0
    count_step6 = 0
    array_x = ["."] * num_line
    array_y = ["."] * num_column
    array_xy = [["O"] * num_column for i in range(num_line)]


def check_diagonal():
    global array_xy
    for k in range(num_column):  # по столбцам вправо
        count_symbol1 = 0
        count_symbol2 = 0
        count_symbol3 = 0
        count_symbol4 = 0
        for i in range(num_line):  # по строкам вниз
            if i + k == num_column:
                break
            else:
                # прямая диагональ
                if array_xy[i][i + k] == "X":
                    count_symbol1 += 1
                    if count_symbol1 == 2:
                        return False
                if array_xy[i + k][i] == "X":
                    count_symbol2 += 1
                    if count_symbol2 == 2:
                        return False
                # обратная диагональ
                if array_xy[i][num_column - i - k - 1] == "X":
                    count_symbol3 += 1
                    if count_symbol3 == 2:
                        return False
                if array_xy[num_column - i - k - 1][i] == "X":
                    count_symbol4 += 1
                    if count_symbol4 == 2:
                        return False
    return True


if __name__ == '__main__':
    array_initialization()
    while step < num_chess:
        x = generate_x()
        y = generate_y()
        if x is None or y is None or start_init:
            array_initialization()
            x = generate_x()
            y = generate_y()
            array_xy[x][y] = "X"
        else:
            array_xy[x][y] = "X"
        if check_diagonal():
            step += 1
        else:
            array_xy[x][y] = "O"
            array_x[x] = "."
            array_y[y] = "."
            if step == 5:
                count_step5 += 1
                if count_step5 == 10:
                    start_init = True
            if step == 6:
                count_step6 += 1
                if count_step6 == 5:
                    start_init = True
            if step == 7:
                start_init = True
    # вывод результата
    print("________________")
    for row in array_xy:
        print(' '.join(row))
    print("________________")
