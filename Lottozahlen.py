

import random 

b = 0 
zahl =[]


int_a = int(input("Wie viele Tips möchten Sie? Hier eingeben:")) 

if int_a <=5: 
    while b <int_a:
        x = random.randint(1,45)
        if x in zahl: 
            b = b  
        else:
            zahl.append(x)
            b+=1

    print("Die Zufälligen Zahlen sind:", zahl)

else:
    print("Nicht mehr als 5 Tips")