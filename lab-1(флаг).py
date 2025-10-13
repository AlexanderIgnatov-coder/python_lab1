import sys

ESC = "\x1b"
CSI = f"{ESC}["
RESET = f"{CSI}0m"

def draw_flag_poland(height=12, width=60):

    half_height = height // 2
    # Верхняя половина - белая
    for _ in range(half_height):
        print(f"{CSI}48;5;15m{' ' * width}{RESET}")  
    # Нижняя половина - красная
    for _ in range(height - half_height):
        print(f"{CSI}48;5;124m{' ' * width}{RESET}") 

if __name__ == "__main__":
    draw_flag_poland()