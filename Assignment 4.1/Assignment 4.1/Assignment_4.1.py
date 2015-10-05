name = raw_input("What is your name?: ")

temp = input("What is the temperature in Fahrenheit?: ")
digittemp = int(temp)

celc = (digittemp - 32) / 1.8
celcEnd = round(celc,2)
print celcEnd