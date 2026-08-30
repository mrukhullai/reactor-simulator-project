import numpy as np
import math as mt
import time
def numeric_converter(t):
    counter = 0

    while True:
        try:
            s=float(t)
            round(s,2)
            return s
            break
        except:
            print("Error\nInput not a numeric value")
            t = input("Input a numeric value\n")
            counter += 1
        if counter == 10:
            print("Errors made too many")
            break
    return None
def arraying(t):
    # l_a=[]
    values = t.strip().split(" ")
    print(values)
    a = np.array(list(map(numeric_converter,values)))
    print("array",a)
    # f=numeric_converter(a)
    # print(f)
    return a

# Mass = "10 20 30 40 "
# arraying(Mass)

class safety_parameters:
    def __init__(self, name, quantity, temp, env_temp, chem_max_temp,chem_min_temp,mode):
        self.name = name
        self.quantity = quantity
        self.temp = temp
        self.env = env_temp
        self.max_cap = 1000
        self.max_temp = 1000
        self.min_temp = -300
        self.chem_max_temp = None
        self.chem_min_temp = None
        
        if mode == (1 or 2):
            self.chem_max_temp = chem_max_temp
            self.chem_min_temp = chem_min_temp
        
    
    def safety_check(self):
        timer = 0
        
# Adding safety check for chemical quantity in tank

        def emergency_dedeucter():
            Em_drain_stopwatch = 0
            removal_rate = 50
            print("---Emergency Removal Initialized---")
            self.quantity -= removal_rate
            Em_drain_stopwatch += 1
            print(f"Time:{Em_drain_stopwatch} current volume is now {self.quantity}Litres")
            
        def emergency_temp_alternator():
            if self.temp > self.chem_max_temp:
                print("Emergency cooler initialized")
                
        