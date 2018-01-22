# -*- coding: utf-8 -*-
import MySQLdb
import random
import csv

db = MySQLdb.connect(host='localhost', user='root', passwd='', db='zawody')
myCursor = db.cursor()

filename = 'poprawione_dane.csv'
with open(filename) as csvfile:
    readCSV = csv.reader(csvfile, delimiter=',')
    imiona=[]
    nazwiska=[]
    kluby=[]

    for row in readCSV:
        nazwiska.append(row[0])
        imiona.append(row[1])
        kluby.append(row[2])



#czyszczenie
myCursor.execute("""DELETE FROM final""")
myCursor.execute("""DELETE FROM zawodnik""")
myCursor.execute("""DELETE FROM kategoria""")
myCursor.execute("""DELETE FROM uczelnia""")


kategorie=['Kobiety','Mezczyzni','Juniorki','Juniorzy','Masterki','Masterzy']
for i in range(0,len(kategorie)):
    myCursor.execute("""INSERT INTO kategoria(idKategoria, Nazwa)
    VALUES (%s, %s);""", (i+1, kategorie[i]))


uczelnie=['PWR','UWR','UE','UMED']
for i in range(0,len(uczelnie)):
    myCursor.execute("""INSERT INTO uczelnia(idUczelnia, Nazwa)
    VALUES (%s, %s);""", (i+1, uczelnie[i]))


N=18 #drogi
for i in range(0,len(nazwiska)):
    top=random.randint(0,N)
    bonus=top+random.randint(0,3)
    uczelnia=random.randint(1,4)
    if i <= 23:   #KOBIETY
        myCursor.execute("""INSERT INTO zawodnik(idZawodnik,Imie,Nazwisko,Klub,TOP,BONUS,Kategoria_idKategoria,Uczelnia_IdUczelnia)
        VALUES (%s,%s,%s,%s,%s,%s,%s,%s);""", (i+1,imiona[i],nazwiska[i],kluby[i],top,bonus,1,uczelnia))
    if i >= 24 and i <= 108:    #MEZCZYZNI
        myCursor.execute("""INSERT INTO zawodnik(idZawodnik,Imie,Nazwisko,Klub,TOP,BONUS,Kategoria_idKategoria,Uczelnia_IdUczelnia)
        VALUES (%s,%s,%s,%s,%s,%s,%s,%s);""", (i+1,imiona[i],nazwiska[i],kluby[i],top,bonus,2,uczelnia))
    if i >= 109 and i <= 114:   #JUNIORKI
        myCursor.execute("""INSERT INTO zawodnik(idZawodnik,Imie,Nazwisko,Klub,TOP,BONUS,Kategoria_idKategoria,Uczelnia_IdUczelnia)
        VALUES (%s,%s,%s,%s,%s,%s,%s,%s);""", (i+1,imiona[i],nazwiska[i],kluby[i],top,bonus,3,uczelnia))
    if i >= 115 and i <= 126:   #JUNIORZY
        myCursor.execute("""INSERT INTO zawodnik(idZawodnik,Imie,Nazwisko,Klub,TOP,BONUS,Kategoria_idKategoria,Uczelnia_IdUczelnia)
        VALUES (%s,%s,%s,%s,%s,%s,%s,%s);""", (i+1,imiona[i],nazwiska[i],kluby[i],top,bonus,4,uczelnia))
    if i >= 127 and i <= 128:   #MASTERKI
        myCursor.execute("""INSERT INTO zawodnik(idZawodnik,Imie,Nazwisko,Klub,TOP,BONUS,Kategoria_idKategoria,Uczelnia_IdUczelnia)
        VALUES (%s,%s,%s,%s,%s,%s,%s,%s);""", (i+1,imiona[i],nazwiska[i],kluby[i],top,bonus,5,uczelnia))
    if i >= 129:    #MASTERZY
        myCursor.execute("""INSERT INTO zawodnik(idZawodnik,Imie,Nazwisko,Klub,TOP,BONUS,Kategoria_idKategoria,Uczelnia_IdUczelnia)
        VALUES (%s,%s,%s,%s,%s,%s,%s,%s);""", (i+1,imiona[i],nazwiska[i],kluby[i],top,bonus,6,uczelnia))


print 'wprowadzono dane do tabel'
db.commit()
db.close()




