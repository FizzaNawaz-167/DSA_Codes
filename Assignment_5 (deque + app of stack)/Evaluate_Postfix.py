from PN_ITPost import *

array = [0]*25
count = 0

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

def is_operator(char):
    return char in {'+', '-', '*', '/','^','(',')','[',']','{','}'}

def infix_to_postfix(expression):
    sumUp = ''
    checker = False
    global array
    global count
    stack = Stack(len(expression))

    for char in expression:

        if not is_operator(char):
            sumUp += char
            checker = True
        elif closing_brackets(char):

            if checker:
                array[count] = sumUp
                count += 1
                sumUp = ''
                checker = False

            while stack.peek() != opening_brackets(stack.peek()) and not stack.is_empty():
                array[count] = stack.pop()
                count += 1
            stack.pop()
        elif is_operator(char):
            if precedence(char) > 0:

                if checker:
                    array[count] = int(sumUp)
                    count += 1
                    sumUp = ''
                    checker = False

                if precedence(char) <= precedence(stack.peek()):
                    while precedence(char) <= precedence(stack.peek()):
                        array[count] = stack.pop()
                        count += 1
                    stack.push(char)
                elif precedence(char) > precedence(stack.peek()):
                    stack.push(char)
            else:
                stack.push(char)

    if checker:
        array[count] = int(sumUp)
        count += 1             

    while not stack.is_empty():
        op = stack.pop()
        if precedence(op) > 0:
            array[count] = op
            count += 1 

def perform(f, s, char):

    match char:
        case '+':
            return s+f
        case '-':
            return s-f
        case '*':
            return s*f
        case '/':
            return s//f
        case '^':
            return s**f                

def Evaluate_Postfix_Exp():
    val = 0
    global array
    global count
    stack = Stack(len(array))

    for char in array:

        if not is_operator(char):
            stack.push(char)
        if is_operator(char):
            
            f = int(stack.pop())
            s = int(stack.pop())

            val = perform(f, s, char)
            stack.push(val)

    return val 
########################################################### MAIN ####

def Main_EP(String):
    global array
    global count

    String = str(infix_to_postfix(String))
    infix_expression = str(String)
    postfix_expression = Evaluate_Postfix_Exp()

    return postfix_expression
