class Stack:
    def __init__(self, length):
        self.top = -1
        self.stack = [0] * length

    def push(self, value):
        self.top += 1
        self.stack[self.top] = value

    def pop(self):
        data = self.stack[self.top]
        self.top -= 1
        return data

    def peek(self):
        return self.stack[self.top]

    def size(self):
        return self.top + 1

    def is_empty(self):
        if self.top == -1:
            return True
        else:
            return False

def is_operator(char):
    return char in {'+', '-', '*', '/'}

def precedence(op):
    if op in {'+', '-'}:
        return 1
    elif op in {'*', '/'}:
        return 2
    elif op in {'^'}:
        return 3    
    return 0

def infix_to_prefix(expression):
    length = len(expression)
    prefix = []
    result = ''
    stack = Stack(length)

    for i in range(length - 1, -1, -1):
        char = expression[i]

        if char.isalnum():
            prefix += char
        elif char == ')':
            stack.push(char)
        elif char == '(':
            while not stack.is_empty() and stack.peek() != ')':
                prefix += stack.pop()
            stack.pop()
        elif is_operator(char):
            while not stack.is_empty() and precedence(stack.peek()) > precedence(char):
                prefix += stack.pop()
            stack.push(char)

    while not stack.is_empty():
        prefix += stack.pop()

    for item in reversed(prefix):
        result += item

    return result

# Example usage
infix_expression = "a+b*(c^d-e)^(f+g*h)-i"
prefix_expression = infix_to_prefix(infix_expression)
print("Infix Expression:", infix_expression)
print("Prefix Expression:", prefix_expression)
