#Import libraries to connect to Raspberry Pi Pico and use time delays
import machine 
import utime

#Configure GPIO 26 pin as ADC pin to receive temperature sensor output voltage
temperature_sensor = machine.ADC(26)

#Configure GPIO 27 pin as ADC pin to receive light sensor output voltage
light_sensor = machine.ADC(27)
#Define IR emitter
ir_emitter_pin = machine.Pin(15, machine.Pin.OUT)
#Configure GPIO 28 pin as ADC pin to receive IR phototransistor output voltage
ir_receiver = machine.ADC(28)

#Title to be outputted to console
print("Smart Aquaponics System")


#Create an infinite loop
while True:
    #Define variable to read temperature sensor output
    TempStatus = temperature_sensor.read_u16()
	#Define variable to read light sensor output
    LightStatus = light_sensor.read_u16()
	#Set IR emitter on
    ir_emitter_pin.on()
	#Define variable to read IR phototransistor output
    IRStatus = ir_receiver.read_u16()
    
	#Water Temperature heading output to console
    print("Water Temperature: ", end="")
    
	#Thresholds determined by previous experiments. Depending on the threshold, a different print statement is executed
    if TempStatus < 51000:
       print("ALERT: Water temperature is too high for the fish!")
    elif TempStatus < 57000 and TempStatus >= 51000:
        print("No issues or abnormalities detected.")
    else:
        print("ALERT: Water temperature is too low for the fish!")

	#Ambient Light Intensity heading output to console
    print("Ambient Light Intensity: ", end="")  
    
	#Thresholds determined by previous experiments. Depending on the threshold, a different print statement is executed
    if LightStatus < 50000:
        print("ALERT: Ambient light intensity is too high for the plants!")
    elif LightStatus >= 50000 and LightStatus < 64000:
        print("No issues or abnormalities detected.")
    else:
        print("ALERT: Ambient light intensity is too low for the plants!")
    
#Water Clarity heading output to console  
    print("Water clarity: ", end="")
    
	#Thresholds determined by previous experiments. Depending on the threshold, a different print statement is executed
    if IRStatus >= 58000:
        print("No issues or abnormalities detected")
    elif IRStatus < 58000 and IRStatus >= 57000:
        print("Water clarity is slightly below optimal level")
    else:
        print("Water clarity is extremely below optimal level")
    
    #Insert space in between each “snapshot” of the parameters outputted to the console
    print("")
    print("")
    
    #Introduce time delay of two seconds for every iteration of the loop
    utime.sleep(2) 
