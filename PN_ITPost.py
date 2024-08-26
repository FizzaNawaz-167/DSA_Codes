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
    return char in {'+', '-', '*', '/','^','(',')'}

def precedence(op):
    if op in {'+', '-'}:
        return 1
    elif op in {'*', '/'}:
        return 2
    elif op in {'^'}:
        return 3
    return 0


def infix_to_postfix(expression):
    result = ''
    stack = Stack(len(expression))

    for char in expression:

        if not is_operator(char):
            result += char
        elif is_operator(char) and char==')':
            while stack.peek() != '(':
                result += stack.pop()
            stack.pop()
        elif is_operator(char):
            if precedence(char) > 0:
                if precedence(char) <= precedence(stack.peek()):
                    while precedence(char) <= precedence(stack.peek()):
                        result += stack.pop()
                    stack.push(char)

                elif precedence(char) > precedence(stack.peek()):
                    stack.push(char)
            else:
                stack.push(char)

    while not stack.is_empty():
        result += stack.pop()

    return result


########################################################### MAIN ####


infix_expression = "a+b*(c^d-e)^(f+g*h)-i"
postfix_expression = infix_to_postfix(infix_expression)
print("Infix Expression:", infix_expression)
print("Postfix Expression:", postfix_expression)