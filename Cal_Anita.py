
#this is a calculator which gtes two numbers and one operator from the user and
# and if the user enters break, breaks the game and if the user enters
#
counter=0
b="c"
while b=="c":
    if(counter==0):
        num1=int(input("enter a number:"))
        op1=input("enter an operator:")
        num2=int(input("enter another number:"))
    else:
        op1=input("enter an operator:")
        num1=int(input("enter a number:"))
        num2=answer
        
    if(op1=="*"):
        answer=num1*num2        
    elif(op1=="+"):
        answer=num1+num2
    elif(op1=="-"):
        if counter==0:
            answer=num1-num2
        else:
            answer=num2-num1
    elif(op1=="/"):        
        if counter==0:
            if num2==0:
                print("invalid input ")
                continue
            answer=num1/num2
        else:
            if num1==0:
                print("invalid input ")
                continue
            answer=num2/num1
        
        
    print("answer = ", answer)
    counter+=1
    b=input("enter break or continue: ")
    if b=="b":
        break
    counter+=1
    b=input("enter break or continue: ")
    if b=="b":
        break
    
    
