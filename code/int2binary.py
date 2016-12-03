"""
Task:
    Converting decimal numbers to binary numbers

>>> convert_to_binary(25)
'0b11001'
>>> convert_to_binary(233)
'0b11101001'
>>> convert_to_binary(42)
'0b101010'
>>> convert_to_binary(0)
'0b0'
>>> convert_to_binary(1)
'0b1'
"""


# Solution 1:
# keep dividing by 2, store the remainder in a stack
# read in reverse order
def convert_to_binary(number):
    if number == 0:
        return '0b0'

    stack = []
    while number:
        stack.append(number % 2)
        number = number // 2
    binary_str = "0b"
    while stack:
        binary_str += str(stack.pop())
    return binary_str


# Solution 2: using built-in function bin
def convert_to_binary(number):
    return bin(number)


# Solution 3: using string formatting
def convert_to_binary(number):
    return '0b{:b}'.format(number)


# Solution 4: using bitwise operation
def convert_to_binary(number):
    if number == 0:
        return '0b0'

    stack = []
    while number:
        stack.append(number & 1)  # append last bit
        number = number >> 1  # remove last bit
    binary_str = "0b"
    while stack:
        binary_str += str(stack.pop())
    return binary_str


# Solution 5: using recursion
def convert_to_binary(number):
    digit = "01"
    if number < 2:
        return "0b" + digit[number]
    else:
        return convert_to_binary(number // 2) + digit[number % 2]


if __name__ == '__main__':
    import doctest
    doctest.testmod()
