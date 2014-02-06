#import all functions from arithmetic file
from arithmetic import *

calcInput = raw_input("Parameters please.\n")
calcList = calcInput.split(" ")
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

# this checks to see if the first in the list is an operator
if calcList[0] not in operators:
    print "Operator first please."
else: # returns and saves the operator
    calcOperator = calcList.pop(0)    


# check other items in list to see if they are int or float
for i in calcList:

    try:
        int(i) 
  
    except ValueError:
        try:
            float(i)
            print "It's all numbers"  
        except ValueError:
            print "Give me number only please"
            break

# if first item is operator, run matching operation
if calcOperator in operators:
    print opDictionary.get(calcOperator)(calcList[0], calcList[1])
