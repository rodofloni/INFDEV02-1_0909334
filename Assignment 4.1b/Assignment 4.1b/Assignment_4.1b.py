celcinput = input("What is the temperature in Celcius?: ")
celcint = int(celcinput)

while True:

    kelv = celcint + 273.15
    if kelv < -273.15 :
        print "Error! Temperature has gone below absolute zero"
        break
    else:
        print kelv
        break
