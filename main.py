filename = "demo.txt"
lines = ["Первая строка", "Вторая строка", "Третья строка"]

with open(filename, "w", encoding="utf-8") as f:
    for line in lines:
        f.write(line + "\n")

with open(filename, encoding="utf-8") as f:
    read_lines = [line.rstrip("\n") for line in f]

for i, line in enumerate(read_lines, 1):
    print(i, line)

print("Всего строк:", len(read_lines))
