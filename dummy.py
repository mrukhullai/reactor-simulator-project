from Parametric_store_house import *
# addressing modes
global mode, chemical_name, current_temperature, environment_temperature

mode = numeric_converter(input("""Mode:
1:Add       2:Drain     3:Heat:       4:Cool
                      """)) 
# addressing chemical properties
chemical_name = input("""Chemical name:
                      """)
current_temperature = numeric_converter(input("""Chemicals current temperature:
                      """))
environment_temperature = numeric_converter(input("""Environments current temperataure
                      """))
tank_constant = numeric_converter(input("k: "))

