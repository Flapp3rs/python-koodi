donitsit = 0
print ("Haluatko lisää donitseja?")
vastaus = input()
while vastaus == "joo":
    print ("Haluatko lisää donitseja?")
    vastaus = input()
    if vastaus == "joo":
        donitsit = donitsit + 1
        print (donitsit)