class Stack:
    def __init__(self, length):
        self.top = -1
        self.stack = [0] * (length)

    def push(self, value):
        self.top += 1
        self.stack[self.top] = value

    def pop(self):
        if self.top < len(self.stack) and self.top > -1:
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
    return char in {'+', '-', '*', '/','^','(',')','[',']','{','}'}

def precedence(op):
    if op in {'+', '-'}:
        return 1
    elif op in {'*', '/'}:
        return 2
    elif op in {'^'}:
        return 3
    else:    
        return 0

def opening_brackets(char):
    match char:
        case '(':
            return '('
        case '{':
            return '{'
        case '[':
            return '['       

def closing_brackets(char):
    return char in {')', '}', ']'}

def infix_to_postfix(expression):
    result = ''
    stack = Stack(len(expression))

    for char in expression:

        if not is_operator(char):
            result += char
        elif closing_brackets(char):
            while stack.peek() != opening_brackets(stack.peek()) and not stack.is_empty():
                result += ' '
                result += stack.pop()
            stack.pop()
        elif is_operator(char):
            if precedence(char) > 0:
                result += ' '
                if precedence(char) <= precedence(stack.peek()):
                    while precedence(char) <= precedence(stack.peek()):
                        result += stack.pop()
                        result += ' '
                    stack.push(char)
                elif precedence(char) > precedence(stack.peek()):
                    stack.push(char)
            else:
                stack.push(char)

    while not stack.is_empty():
        op = stack.pop()
        if precedence(op) > 0:
            result += ' '
            result += op

    return result
########################################################### MAIN ####

def Main_ITP(String):
    infix_expression = str(String)
    postfix_expression = infix_to_postfix(infix_expression)

    return postfix_expression
