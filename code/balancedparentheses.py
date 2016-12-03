"""
Task:
    Balanced parentheses means that each opening symbol has a corresponding
    closing symbol and the pairs of parentheses are properly nested. Write an
    algorithm that will read a string of parentheses from left to right and
    decide whether the symbols are balanced.

>>> is_balanced("(()()()())")
True
>>> is_balanced("(((())))")
True
>>> is_balanced("(()((())()))")
True
>>> is_balanced("((((((())")
False
>>> is_balanced("()))")
False
>>> is_balanced("(()()(()")
False
>>> is_balanced("{{([][])}()}")
True
>>> is_balanced("[{()]")
False
"""


# Version 1: Only check '(' and ')'
def is_balanced(str_):
    stack = []
    for char in str_:
        if char == '(':
            stack.append(char)
        elif char == ')':
            if not stack:  # empty stack
                return False
            if stack[-1] == '(':
                stack.pop()
            else:
                return False
        else:  # pass other characters
            continue

    # return true if stack is still empty
    if stack:
        return False
    else:
        return True


# Version 2: check "([{" and ")]}"
def is_balanced(str_):
    stack = []
    for char in str_:
        if char in "([{":
            stack.append(char)
        elif char in ")]}":
            if not stack:  # empty stack
                return False

            top = stack[-1]
            # check whether current char matches stack top
            if matches(top, char):
                stack.pop()
            else:
                return False
        else:  # pass other characters
            continue

    # balanced if stack is empty
    if stack:
        return False
    else:
        return True


def matches(char1, char2):
    """Check whether open and close parenthesis matches

        >>> matches("(", ")")
        True
        >>> matches("[", "]")
        True
        >>> matches("{", ")")
        False
    """
    opens = "([{"
    closes = ")]}"
    return opens.index(char1) == closes.index(char2)


if __name__ == '__main__':
    import doctest
    doctest.testmod()
