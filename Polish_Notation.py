class PN_Stack:
    def __init__(self):
        self.stack = []

    def is_empty(self):
        return len(self.stack) == 0    

    def push(self,value):
        self.stack.append(value)

    def pop(self):
        if not self.is_empty():
            return self.pop()
        else:
            return None    

    def top(self):
        if not self.is_empty():
            return self.stack[-1]
        else:
            return None

    def size(self):
        return len(self.stack)            

    def perc(char):
        if char == '^':
            return 3
        elif char == '/' or char == '*':
            return 2
        elif char == '+' or char == '-':
            return 1
        else:
            return -1   

    def infixToPostfix(self, string):
        result = []

        for i in range(0, len(self.stack)):
            char = self.stack[i]

            if (char >= 'a' and char <= 'z') or (char >= 'A' and char <= 'Z') or (char >= '0' and char <= '9'):
                result += char
            elif char == '(':
                self.push('(')
            elif char == ')':
                while self.pop() != '(':
                    result += self.pop()
                    self.pop()
                self.pop()
            else:
                while not self.pop() and (perc(string[i]) <= perc(self.pop())):
                    result += self.pop()
                    self.pop()
                      
        while not self.is_empty():
            result += self.pop()
            self.pop()

        print("I'm result:  ", result)  


l = PN_Stack()
exp = 'a+b*(c^d-e)^(f+g*h)-i'
l.infixToPostfix(exp)
