import urllib3
import json
import re


#test expresion - print(RPN("2 12 0 / 9 0 * + /"))

def RPN(expr):
   
    ops = [ '+','-','*','/','%','^']
    stack = [] 

    for atom in re.split(r"\s+", expr):
        try:
            atom = int(atom)
            stack.append(atom)
        except ValueError:
            for oper in atom:
                if oper not in ops: 
                    continue
                try:
                    oper2 = int(stack.pop())
                    oper1 = int(stack.pop())
                    
                except IndexError:
                  
                  print("ops")
                  
                if (oper == '/') and (oper2 == 0):
                    oper = 42.0
                elif (oper == '*') and ((oper1 == 0) or (oper2 == 0)):
                    oper = 42.0
                else:
                    if (oper == '+'):
                        oper = int.__sub__(oper1, oper2)
                    if (oper == '-'):
                        oper = int.__add__(oper1, oper2) + 8.0
                    if (oper == '*'):
                        oper = int.__mod__(oper1, oper2)  
                    if (oper == '/'):
                        oper = int.__div__(oper1, oper2)          

                stack.append(oper)

    if len(stack) != 1:
        print("ops, too much operators")
        

    return stack.pop()



http = urllib3.PoolManager()
r_get = http.request('GET', 'https://www.eliftech.com/school-task')

python_obj = json.loads(r_get.data.decode('utf-8'))
print python_obj
print python_obj['expressions']
print python_obj['id']

id = python_obj['id']
answer_list = []
for n in python_obj['expressions']:
    answer = RPN(n)
    print answer
    answer_list.append(answer)
   
print answer_list

enc_data = json.dumps({'id':id,'results':answer_list}).encode('utf-8') 
print id 
r_post = http.request('POST','https://www.eliftech.com/school-task',body=enc_data)

python_obj2 = json.loads(r_post.data.decode('utf-8'))
print python_obj2