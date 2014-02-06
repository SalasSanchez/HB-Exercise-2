calcInput = raw_input("Parameters please.\n")
calcList = calcInput.split(" ")
operators = ["+", "-", "/", "*", "pow", "square", "cube", "mod"]

# this checks to see if the first in the list is an operator
if calcList[0] not in operators:
    print "Operator first please."
else:
    calcList.pop(0)

# check other items in list to see if they are int or float
for i in calcList:
    if int(i) or float(i):
        print i 

# if first item is operator, run matching operation
