def palindrome(s):
    if len(s) <= 1:
        return True
    if s[0] != s[-1]:
        return False
    return palindrome(s[1:-1])

s = input('Введите строку: ')
s = ''.join(s.lower().split())
if len(s) == 0:
    print('Нет текста')
else:
    p = palindrome(s)
    print('Палиндром' if p else 'Не палиндром')
