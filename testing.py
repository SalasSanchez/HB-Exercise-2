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
	# eljose: Si te pasan uno o dos parametros el programa se rompe en "opDictionary.get(calcOperator)(int(calcList[0]), int(calcList[1])"
	# eljose: Si te pasan mas de 3 parametros no se rompe pero queda raro
	if len(calcList) != 3:
	    print "Wrong number of parameters."
            continue
        # this checks to see if the first in the list is an operator
        if calcList[0] not in operators:
            print "Operator first please."
	    # eljose: Si no haces esto el programa continua y da error en tiempo de ejecucion cuando intenta usar calcOperator
            continue
        else: # returns and saves the operator
            calcOperator = calcList.pop(0)    
    else:
        break


# check other items in list to see if they are int or float
    # eljose: Utilizo la variable check para saber si los parametros pasados son numeros y si no, no intentar hacer el calculo
    check = True
    for i in calcList:
        if i.isdigit() == False:
            print "Give me number only please"
	    check = False
	    break
       # if first item is operator
	# eljose: Saco esto del bucle for que se ejecuta para cada parametro pasado (salvo el primero). Por eso imprime el resultado 2 veces
	# eljose: "calcOperator in operators" es redundante: Ya lo has comprobado antes
        #elif calcOperator in operators:
            #then print the key paired function (in the dictionary) and pass it the parameters (the next items given by the user)
            #print opDictionary.get(calcOperator)(int(calcList[0]), int(calcList[1]))
    if check == True:
	print opDictionary.get(calcOperator)(int(calcList[0]), int(calcList[1]))

