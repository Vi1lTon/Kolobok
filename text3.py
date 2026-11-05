phone = input("Телефон: ")
digits = "".join(ch for ch in phone if ch.isdigit())

if len(digits) != 11:
    print(f"Ошибка: нужно 11 цифр, получено {len(digits)}")
else:
    masked = f"+7 ({digits[1:4]}) ***-**-{digits[-2:]}"
    print(masked)
