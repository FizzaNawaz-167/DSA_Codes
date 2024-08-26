import os
import time

def x():
    time.sleep(0.3)
    os.system('cls')

def Heading(str1, str2):
    os.system('cls')
    print(f"{str1} | {str2}")
    print("-"*161)
    print()








# def Evaluate_Postfix_Exp():
#     val = 0
#     exp = ''
#     new_exp= ''
#     preserve = ''
#     i = 0
#     let = 0
#     khp = 0
#     global array
#     global count

#     new_arr = array
#     stack = Stack(len(array))

#     print("\tSTACK\t|\tEXPRESSION")

#     for char in array:

#         if not is_operator(char):
#             stack.push(char)
#             exp += str(char)
#             exp += ','
#             print(f"\t{char}\t|\t{exp}")
#             i += 1
#         if is_operator(char):
            
#             f = int(stack.pop())
#             s = int(stack.pop())

#             val = perform(f, s, char)
#             stack.push(val)


#             for j in range(0, i-2):
#                 new_exp += str(new_arr[j])
#                 new_exp += ','
#                 let += 1  
#             i = let

#             if i == 0 and khp < 2:
#                 new_exp += preserve

#                 if khp == 1:
#                     new_exp += ','

#                 khp += 1

#             new_exp += str(val)
#             exp = new_exp
#             exp += ','
#             new_exp = ''

#             preserve = str(val)

#             print(f"\t{char}\t|\t{exp}")