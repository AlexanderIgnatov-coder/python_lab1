import math

ESC = "\x1b"
CSI = f"{ESC}["
RESET = f"{CSI}0m"

def plot(h=30, w=30):
    y_axis = h // 2
    x_axis = w // 4

    # Создаем экран: каждый элемент — кортеж (цвет, символ)
    screen = [[(15, ' ') for _ in range(w)] for _ in range(h)]

    for x in range(w):
        screen[y_axis][x] = (16, ' ')

    for y in range(h):
        screen[y][x_axis] = (16, ' ')

    # Точка пересечения
    screen[y_axis][x_axis] = (0, ' ')

    max_x = w - x_axis - 1 

    # График y = sqrt(x)-Для каждого х от 0 до max_x вычисляем y = int(sqrt(x))
    for x in range(max_x + 1):
        y = int(math.sqrt(x))
        y_pos = y_axis - y
        if 0 <= y_pos < h:
            screen[y_pos][x_axis + x] = (9, ' ')

    for row in screen:
        line = ''
        prev_color = None
        for color, ch in row:
            if color != prev_color:
                line += f"{CSI}48;5;{color}m"
                prev_color = color
            line += ch
        line += RESET
        print(line)


if __name__ == "__main__":

    plot()
