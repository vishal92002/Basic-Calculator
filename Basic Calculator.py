'''Welcome to the calculator program. This progeam will preform the basic operations when given any two numbers''' 
input1=float(input("Please enter a number: "))
operation=input("Please choose from the choices below; " "\n" + "%,+,-,*,and / : ")
input2= float(input("Please enter another number: "))
output=0

if operation== '+':
   output= input1+input2
elif operation== '-':
    output=input1-input2
elif operation=='*':
    output=input1*input2
else:
    output=input1/input2

    print(output)

