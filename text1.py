name = input("Имя файла: ")

try:
    f = open(name, encoding="utf-8")
except FileNotFoundError:
    print(f"Файл «{name}» не найден.")
else:
    with f:
        total = 0
        count = 0
        skipped = 0

        for line in f:
            s = line.strip()

# пустая строка — молча пропускаем
            if not s:
                continue

# пробуем превратить в число
            try:
                n = float(s)
            except ValueError:
                print(f"пропущено: {s}")
                skipped += 1
            else:
                total += n
                count += 1

        if total == int(total):
            total = int(total)

        print(f"Сумма: {total}")
        print(f"Количество чисел: {count}")
        print(f"Пропущено строк: {skipped}")
