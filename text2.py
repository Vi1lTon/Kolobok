filename = input("Имя файла: ").strip()

try:
    with open(filename, encoding="utf-8") as f:
        lines = f.readlines()
except FileNotFoundError:
    print(f"Файл {filename} не найден")
else:
    total = 0.0
    numbers = 0
    garbage = 0

    for line in lines:
        s = line.strip()
        if not s:
            continue
        try:
            total += float(s)
            numbers += 1
        except ValueError:
            print(f"пропущено: {s}")
            garbage += 1

    print(f"Сумма: {total}")
    print(f"Чисел: {numbers} | мусора: {garbage}")
