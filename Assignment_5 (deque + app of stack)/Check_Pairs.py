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

def opening_brackets(char):
    return char in {'(', '{', '['}

def closing_brackets(char):
    return char in {')', '}', ']'} 

def get_opposite(char):
    if char == ')':
        return '('
    elif char == '}':
        return '{'
    elif char == ']':
        return '['
    elif char == '(':
        return ')'
    elif char == '{':
        return '}'
    elif char == '[':
        return ']'                     

def check_for_pairs(expression):
    left = ''
    flag = 0
    stack = Stack(len(expression))

    for char in expression:

        if opening_brackets(char):
            stack.push(char)
            flag = 1
        elif closing_brackets(char):
            get_op = get_opposite(char)
            if get_op == stack.peek():
                stack.pop()
            else:
                stack.push(char)    

    if not stack.is_empty():
        while not stack.is_empty():
            var = stack.pop()
            left += get_opposite(var)
            left += ', '
        stack.push(1000)    

    if stack.is_empty() and flag == 1:
        return "Expression has complete & proper pairs of brackets"
    elif stack.is_empty() and flag == 0:
        return "Expression don't have any pair of brackets"    
    else:
        return f"Expression don't has complete & proper pairs of brackets\n\t    Missing Brackets: {left}"     


########################################################### MAIN ####

def Main_CP(String):
    infix_expression = str(String)
    postfix_expression = check_for_pairs(infix_expression)

    return postfix_expression
