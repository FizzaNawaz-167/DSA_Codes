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
        return str(data)

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

def Postfix_to_Infix(expression):
    answer = ''
    infix = ''
    result = ''
    stack = Stack(len(expression))

    for char in expression:
        if char.isalnum(): 
            stack.push(char)
        elif is_operator(char):
            infix += stack.pop()
            infix += char
            infix += stack.pop()  

    while not stack.is_empty():
        result += stack.pop()

    for item in reversed(result):
        answer += item

    print(answer)    
    for val in infix:
        stack.push(val)

    while not stack.is_empty(): 
        answer += stack.pop()     

    return answer

########################################################### MAIN ####


Postfix_expression = "abcd^e-fgh*+^*+i-"
Infix_expression = Postfix_to_Infix(Postfix_expression)
print("Postfix Expression:", Postfix_expression)
print("Infix Expression:", Infix_expression)

# "a+b*(c^d-e)^(f+g*h)-i"
             