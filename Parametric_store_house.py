import numpy as np
import math as mt
def numeric_converter(t):
    counter = 0

    while True:
        try:
            s=float(t)
            round(s,2)
            
            break
        except:
            print("Error\nInput not a numeric value")
            t = input("Input a numeric value\n")
            counter += 1
        if counter == 10:
            print("Errors made too many")
            break
            return s
        
# def arraying(t):
#     l_a=[]
#     values = t.strip().split(" ")
#     print(values)
#     np.array(map(numeric_converter,values))
#     print("array",a)
#     # f=numeric_converter(a)
#     # print(f)

# Mass = "10 20 30 40 "
# arraying(Mass)
