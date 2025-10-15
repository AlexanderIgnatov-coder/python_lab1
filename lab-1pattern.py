
ESC = "\x1b"
CSI = f"{ESC}["
RESET = f"{CSI}0m"


def pattern(width=40):
    
    print(f"{CSI}48;5;15m{' ' * width}{RESET}")
    
    print(f"{CSI}48;5;16m{' ' * width}{RESET}")
    
    for _ in range(2):
        print(
            f"{CSI}48;5;15m"
            f"{' ' * ((width // 2) - 2)}"
            f"{CSI}48;5;16m"
            f"{' ' * 4}"
            f"{CSI}48;5;15m"
            f"{' ' * ((width // 2) - 2)}"
            f"{RESET}"
        )
    
    print(f"{CSI}48;5;16m{' ' * width}{RESET}")
    
    for _ in range(2):
        print(
            f"{CSI}48;5;15m"
            f"{' ' * (width - 34)}"
            f"{CSI}48;5;16m"
            f"{' ' * 4}"
            f"{CSI}48;5;15m"
            f"{' ' * (width // 2)}"
            f"{CSI}48;5;15m"
            f"{CSI}48;5;16m"
            f"{' ' * 4}"
            f"{CSI}48;5;15m"
            f"{' ' * (width - 34)}"
            f"{RESET}"
        )
  
    print(f"{CSI}48;5;16m{' ' * width}{RESET}")
    print(f"{CSI}48;5;15m{' ' * width}{RESET}")


if __name__ == "__main__":
    pattern()