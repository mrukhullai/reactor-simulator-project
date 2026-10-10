# import numpy as np
import math as mt
import time


# Convert interactive input to a floating-point value, retrying invalid input.
def numeric_converter(t):
    counter = 0

    while True:
        try:
            s = float(t)
            round(s, 2)
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

# Creating a function that checks if a value from a string i convertuble to a number
def num_validator(t):
    status = True
    for char in t :
        try:
            int(char)
        except ValueError:
            status= False
            break
            return 
    return status

# Creating a function to check if a string is totally letters
def letter_validator(t):
    return t.isalpha()

# Split a space-separated string into a NumPy array of numeric values.
# def arraying(t):
#     # l_a=[]
#     values = t.strip().split(" ")
#     print(values)
#     a = np.array(list(map(numeric_converter, values)))
#     print("array", a)
#     # f=numeric_converter(a)
#     # print(f)
#     return a


# Mass = "10 20 30 40 "
# arraying(Mass)


def loss(k: int | float, temp: int | float, temp_env: int | float) -> int | float:
    # Newton's-law cooling model: the temperature moves toward the environment.
    k = numeric_converter(k)
    temp = numeric_converter(temp)
    temp_env = numeric_converter(temp_env)

    return -k * (temp - temp_env)

def chem_name_check(name):
    pass
class Properties:
    def __init__(self):
        self.name = input("Enter the name of the chemical: ")
        self.state = input("Enter the state of the chemical (solid, liquid, gas): ")
        
        # Creating a dictionary to store the chemical properties in relation to the chemical name format
        name_based_property_store = {
            
        }

    # data_store = {
class safety_parameters:
    def __init__(
        self, name, quantity, temp, env_temp, chem_max_temp, chem_min_temp, mode, k
    ):
        # Store reactor inputs and establish the default safety limits.
        self.name = name
        self.quantity = quantity
        self.temp = temp
        self.env_temp = env_temp
        self.timer = 0
        self.max_cap = 1000
        self.max_temp = 1000
        self.min_temp = -300
        self.chem_max_temp = None
        self.chem_min_temp = None
        self.timer = 0
        self.k = k

        if mode == (3 or 4):
            # Temperature limits are only relevant to heat-related modes.
            self.chem_max_temp = chem_max_temp
            self.chem_min_temp = chem_min_temp

    # Adding safety check for chemical quantity in tank

    def emergency_deducter(self):
        
        # Select a faster drain rate when the tank is farther above capacity.
        em_drain_timer = 0
        difference = abs(self.quantity - self.max_cap)
        # Define drain tier for draining rate
        drain_tier = [
            (500, 50),
            (100, 10),
            (50, 5),
            (20, 2),
            (10, 1),
        ]
        # setting up default removal rate
        removal_rate = 0
        # Setting automatic drain rate with respect to threshold
        for threshold, rate in drain_tier:
            if difference >= threshold:
                removal_rate = rate
                break

        # setting up Drain Mechanism
        print("---Emergency Removal Initialized---")

        while True:
            time.sleep(1)
            self.quantity -= removal_rate
            self.timer += 1
            em_drain_timer += 1
            print(f"Time:{em_drain_timer} current volume is now {self.quantity}Litres")
            # Creating Breaking point in the mechanism to prevent infinite draining
            if self.quantity <= self.max_cap - 10:
                break

    # Adding safety parameters for Reactor overheating
    def em_heat_alternator(self):
        # Apply heat loss once per second until the temperature returns to a limit.
        if self.temp > self.max_temp:
            print(
                "Chemical temperature exceeds Reactor Heat Limit, initiating cooling mechanism"
            )
        else:
            print(
                "Chemical temperature exceeds Chemical Heat Limit, initiating cooling mechanism"
            )
        difference = None
        if self.temp > self.max_temp:
            difference = abs(self.temp - self.max_temp)
        else:
            difference = abs(self.temp - self.chem_max_temp)
        # Define coolant temperature tier for cooling rate
        coolant_tier = [
            (500, 50),
            (100, 10),
            (50, 5),
            (20, 2),
            (10, 1),
        ]
        coolant_temp = -12
        for threshold, rate in coolant_tier:
            if difference >= threshold:
                coolant_temp = rate
                break
        while True:
            self.env_temp += loss(self.k, self.env_temp, coolant_temp)
            
            loss_value = loss(self.k, self.temp, self.env_temp)
            time.sleep(1)
            self.temp += loss_value
            self.coolant += loss(self.k, coolant_temp, self.temp)
            self.timer += 1
            print(f"Time:{self.timer} current temperature is now {self.temp}C")
            if coolant_temp >= 0:
                print(f"""Coolant temperature is now {coolant_temp}C\nReplacing Coolant with new coolant\nCoolant temperature is now -12C""")
                coolant_temp = -12
            if self.timer == 60:
                print(
                    "Reactor has been overheating for 60 seconds, initiating emergency cooling mechanism"
                )
                coolant_temp = 100
            if self.temp <= self.max_temp and self.temp <= self.chem_max_temp - 10:
                break
        
    # Adding safety parameters for Reactor underheating
    def em_cool_alternator(self):
        # Apply heat gain once per second until the temperature returns to a limit.
        if self.temp < self.min_temp:
            print(
                "Chemical temperature exceeds Reactor Cool Limit, initiating heating mechanism"
            )
        else:
            print(
                "Chemical temperature exceeds Chemical Cool Limit, initiating heating mechanism"
            )
        if self.temp < self.min_temp:
            difference = abs(self.temp - self.min_temp)
        else:
            difference = abs(self.temp - self.chem_min_temp)
        heater_temp = 25
        heater_temp_tier = [
            (500, 50),
            (100, 10),
            (50, 5),
            (20, 2),
            (10, 1),
        ]
        for threshold, rate in heater_temp_tier:
            if difference >= threshold:
                heater_temp = rate
                break
        while True:
            self.env_temp += loss(self.k, self.env_temp, heater_temp)
            gain_value = loss(self.k, self.temp, self.env_temp)
            time.sleep(1)
            self.temp += gain_value
            self.timer += 1
            print(f"Time:{self.timer} current temperature is now {self.temp}C")
            if self.timer == 60:
                print(
                    "Reactor has been underheating for 60 seconds, initiating emergency heating mechanism"
                )
                heater_temp = 100
            if self.temp >= self.min_temp and self.temp >= self.chem_min_temp + 10:
                break