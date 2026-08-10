def is_balanced(s):
    stack = []
    opens = '({['
    closes = ')}]'
    brackets_map = dict(zip(opens, closes))

    for char in s:
        if char in opens:
            stack.append(char)
        elif char in closes:
            if not stack or brackets_map[stack.pop()] != char:
                return False
    return not stack

print(is_balanced(input()))



