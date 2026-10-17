def sum_digits(number):
    r = 0
    n = abs(number)
    while n:
        r += n % 10
        n //= 10
    return r

def average(numbers):
    return sum(numbers) / len(numbers) if numbers else None

def normalize_text(text):
    text = text.lower().strip()
    while '  ' in text:
        text = text.replace('  ', ' ')
    return text

def select_numbers(numbers, threshold):
    res = []
    for num in numbers:
        if num != threshold:
            res.append(num)
    return res

def is_palindrome(text):
    text = normalize_text(text)
    return text == text[::-1] if text else False
