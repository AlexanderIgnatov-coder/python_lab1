
ESC = "\x1b"
CSI = f"{ESC}["
RESET = f"{CSI}0m"

def uzor(width=40):
    print(f"{CSI}48;5;15m{' ' * width}{RESET}")
    print(f"{CSI}48;5;16m{' ' * width}{RESET}")
    for _ in range(2):
        print(f"{CSI}48;5;15m{' ' * ((width//2)-2)}{CSI}48;5;16m{' ' * 4}{CSI}48;5;15m{' ' * ((width//2)-2)}{RESET}")  
    print(f"{CSI}48;5;16m{' ' * width}{RESET}")  
    for _ in range(2):
        print(f"{CSI}48;5;15m{' ' * (width-34)}{CSI}48;5;16m{' ' * 4}{CSI}48;5;15m{' ' * (width//2)}{CSI}48;5;15m{CSI}48;5;16m{' ' * 4}{CSI}48;5;15m{' ' * (width-34)}{RESET}")
    print(f"{CSI}48;5;16m{' ' * width}{RESET}")
    print(f"{CSI}48;5;15m{' ' * width}{RESET}")
    
if __name__ == "__main__":
    uzor()