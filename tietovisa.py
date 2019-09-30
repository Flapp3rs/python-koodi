pisteet = 0

def kysyjotain(kysymys, oikeavastaus):
    global pisteet
    print (kysymys)

    veikkaus = input()

    if veikkaus == oikeavastaus:
        pisteet = pisteet + 1
        print ("Oikein! Onnittelut sait yhden pisteen.")

    else:
        print ("Väärin meni!")
kysyjotain("Missä maassa linnanmäki on?", "suomessa")
print ("Sait {} pisteitä!".format(pisteet)) 