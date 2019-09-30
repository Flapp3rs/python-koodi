import random

vastaukset = ["ehkä" , "ei" , "joo" ]

while True:
    print("Kysy jotain") 
    vastaus = input()
    vastauk = random.choice(vastaukset)
    print (vastauk)