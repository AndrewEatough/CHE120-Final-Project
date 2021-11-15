# -*- coding: utf-8 -*-


#CAS Number	
cas_number = "7732-18-5"
#Melting Point	
Tm = 273.15
#Density
rho = 1000
#Boiling Point
Tb = 373.13
#Viscosity
mu = 1
#Thermal Conductivity
k = 0.58
    
def convert_to_kelvin(temperature, units):
    temperature = float(temperature)
    if type(temperature) != float and type(temperature) != int:
        return (None)   
    else:
        if units == "C":
            temperature = +273.15 
            return (temperature)
        elif units == "K":
            return (temperature)
        elif  units == "F":
            temperature = (temperature- 32) * 5/9 + 273.15
            return (temperature)
        else:
            return (None)
    
def is_gas(temperature):
    temperature = float(temperature)
    if temperature > Tb:
        return (True)
    else:
        return (False)
    
def is_liquid(temperature):
    temperature = float(temperature)
    if  temperature < Tb and temperature > Tm:   
        return (True)
    else:
        return (False)

def is_solid(temperature):
    if temperature <Tm:
        return (True)
    else:
        return (False)
   
if __name__ == "__main__":
    UnitUserInput = input("Enter Desired Units Either K, C or F: ")  
    if UnitUserInput == "C" or UnitUserInput == "K" or UnitUserInput == "F":
        TempUserInput = input("Enter Desired Temp: ")
        if (TempUserInput .isdigit()) == True:
            Kelvin = convert_to_kelvin(TempUserInput, UnitUserInput)
            
            
            if is_gas(Kelvin) == True:
                print("The phase of water at the specified temperature is gas")            
                if is_solid(Kelvin) == True:
                    print("The phase of water at the specified temperature is solid")            
                    if is_liquid(Kelvin) == True:
                        print("The phase of water at the specified temperature is: liquid")
            
            
        if TempUserInput .isdigit() == False:
            print("Invalid Input")
    else:
        print("Invalid Input")
    
    
     


         
       
            


    
    
