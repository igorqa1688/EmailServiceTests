import random


# Генерация случайной строки без кириллицы
def generate_random_string(length: int) -> str:
    # Определяем необходимые наборы символов
    lower_chars = 'abcdefghijklmnopqrstuvwxyz'
    upper_chars = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    digits = '0123456789'
    special_chars = '!@#$%^&*()_+~`|}{[]:;?><,./-='

    # Добавляем как минимум один символ каждого типа
    result = random.choice(digits) + \
             random.choice(special_chars) + \
             random.choice(lower_chars) + \
             random.choice(upper_chars)

    # Заполняем оставшуюся часть случайными символами
    remaining_length = length - len(result)
    result += ''.join(random.choices(lower_chars + upper_chars + digits + special_chars, k=remaining_length))
    random_string = ''.join(random.sample(result, len(result)))
    # Перемешиваем символы
    return random_string