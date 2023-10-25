from typing import Optional, List
from collections import deque


def integer_from_string(input_string):
    digits = {
        '0': 0,
        '1': 1,
        '2': 2,
        '3': 3,
        '4': 4,
        '5': 5,
        '6': 6,
        '7': 7,
        '8': 8,
        '9': 9
    }

    start = 0
    while start < len(input_string) and input_string[start] == " ":
        start += 1

    sign = 1
    if input_string[start] == '-':
        sign = -1
        start += 1
    elif input_string[start] == '+':
        sign += 1

    answer = 0
    for c in input_string[start:]:
        d = digits.get(c)
        if d is None: break

        if answer > 2147483647:
            return -2147483648 if sign < 0 else 2147483647
        answer = answer * 10 + d

    return answer * sign


start = 0
while start < len(input_string) and input_string[start] == " ":
    start += 1

sign = 1
if input_string[start] == '-':
    sign = -1
    start += 1
elif input_string[start] == '+':
    start += 1

answer = 0
for c in input_string[start:]:
    d = digits.get(c, None)
    if d is None: break

    if answer > 2147483647:
        return -2147483648 if sign < 0 else 2147483647
    answer = answer * 10 + d

return answer * sign


if __name__ == '__main__':
    res = integer_from_string("  123456789123213")
    print(res)
