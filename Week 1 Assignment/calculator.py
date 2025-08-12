num1= int(input("Enter your first number: ")) #prompts the user to enter first number
num2= int(input("Enter your Second number: ")) #prompts the user to enter second number
opera= input("Enter an operation(*,+,-,/)") #prompts the user to enter an operation


if opera=='*':
    result = num1*num2
    print("the answer is: ",result)

elif opera=="+":
    result = num1 + num2
    print("the answer is: ",result)
elif opera=="-":
    result = num1 -num2
    print("the answer is: ",result)
elif opera=="/":
    if num2 !=0 :
      result = num1/num2
      print("the answer is: ",result)
    else :print("invalid operation you cannot divide by zero")

else: print("Error,:Invalid operation (Choose a valid operation:+,-,/,*)")



