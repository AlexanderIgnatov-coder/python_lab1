WHITE = "\033[48;5;15m" 
RESET = "\033[0m"

with open('sequence.txt') as f:
    numbers = []
    for line in f:
        line = line.strip()
        if line:
            numbers.append(float(line))

first = numbers[:125]
second = numbers[125:250]

# Вычисление среднего по модулю для каждой части
abs_first = sum(abs(num) for num in first) / 125
abs_second = sum(abs(num) for num in second) / 125


total = abs_first + abs_second
pct_first = (abs_first / total) * 100
pct_second = (abs_second / total) * 100


print(f"Первых 125 чисел: {pct_first}% | {(WHITE + ' ' + RESET) * int(pct_first // 2)}")
print(f"Вторых 125 чисел: {pct_second}% | {(WHITE + ' ' + RESET) * int(pct_second // 2)}")