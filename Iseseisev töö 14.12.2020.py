#Iseseisev töö 14.12
#Mark Metshein
#IT20

#1. Küsi kasutajalt kahte arvu ning väljasta liitmise vastus
def Liitmine():
    #küsib kasutajalt arvud
    arv1 = int(input("Arv 1: "))
    arv2 = int(input("Arv 2: "))
    #liidab kokku
    summa = arv1 + arv2
    print("Nende arvude summa on: ",summa)

#4. Väljasta samasugune “Eesti lipp”
def Lipp():
    #Prindib print rida 4 korda
    for i in range(4):
        print("¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤")
    for i in range(4):
        print("==============================================")
    for i in range(4):
        print("----------------------------------------------")
#5. Leia jadamisi ja rööpselt ühendatud takistite kogutakistus. Takistite arv ei pea olema suur
def takistus():
    #jada
    t1 = 3
    t2 = 5
    t3 = 7
    t4 = 9
    #liidab kokku
    kt = t1+t2+t3+t4
    print("Kogutakistus jadamisi on", (kt))
    #rööpselt
    t1 = 3
    t2 = 3
    t3 = 3
    t4 = 3
    #liidab kokku
    kt = t1+t2+t3+t4
    print("Kogutakisuts rööpselt on", (kt))

#8. Kirjuta programm, mis muudab lause tagurpidiseks. Näiteks: “Ma armastan Javat” muudetakse “Javat armastan ma”
def Tagurpidi():
    sentence = input("Sisestage lause :")
    #splitib ja tõstab tagurpidi
    print(" ".join(reversed(sentence.split())))

#9. Kirjuta programm, mis väljastab arvud 1-66 reana. Näiteks: 1234567891011121314 jne
def Arvud():
    #prindib arvud vahemikus 1-66
    print(*range(1,66))


Liitmine()

Lipp()

takistus()

Tagurpidi()

Arvud()