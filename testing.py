#import all functions from arithmetic file
from arithmetic import *
operators = ["+", "-", "/", "*", "pow", "square", "cube", "mod"]
opDictionary = {
    "+" : add ,
     "-" : subtract, 
     "/" : divide, 
     "*" : multiply, 
     "pow": power, 
     "square": square, 
     "cube": cube, 
     "mod": mod
}

while True:

    calcInput = raw_input("Parameters please.\n")
    calcList = calcInput.split(" ")

    if calcInput != "q":
        # this checks to see if the first in the list is an operator
        if calcList[0] not in operators:
            print "Operator first please."
        else: # returns and saves the operator
            calcOperator = calcList.pop(0)    
    else:
        break


# check other items in list to see if they are int or float
    for i in calcList:
        if i.isdigit() == False:
            print "Give me number only please"
       # if first item is operator
        elif calcOperator in operators:
            #then print the key paired function (in the dictionary) and pass it the parameters (the next items given by the user)
            print opDictionary.get(calcOperator)(int(calcList[0]), int(calcList[1]))


