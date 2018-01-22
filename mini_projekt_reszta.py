# -*- coding: utf-8 -*-
import MySQLdb
import random

db = MySQLdb.connect(host='localhost', user='root', passwd='', db='zawody')
myCursor = db.cursor()


myCursor.execute("""select idZawodnik, Imie, Nazwisko, TOP, BONUS
            from kategoria inner join zawodnik
            on kategoria.idKategoria = zawodnik.Kategoria_idKategoria
            where Nazwa = 'Juniorki'""")

result = myCursor.fetchall()
juniorki=[]
for i in range(0,len(result)):
    juniorki.append(result[i])


juniorki.sort(key=lambda tup: tup[3]+(tup[4]*0.01))
juniorki.reverse()

myCursor.execute("""select idZawodnik, Imie, Nazwisko, TOP, BONUS
            from kategoria inner join zawodnik
            on kategoria.idKategoria = zawodnik.Kategoria_idKategoria
            where Nazwa = 'Juniorzy'""")

result = myCursor.fetchall()
juniorzy=[]
for i in range(0,len(result)):
    juniorzy.append(result[i])


juniorzy.sort(key=lambda tup: tup[3]+(tup[4]*0.01))
juniorzy.reverse()


myCursor.execute("""select idZawodnik, Imie, Nazwisko, TOP, BONUS
            from kategoria inner join zawodnik
            on kategoria.idKategoria = zawodnik.Kategoria_idKategoria
            where Nazwa = 'Masterki'""")

result = myCursor.fetchall()
masterki=[]
for i in range(0,len(result)):
    masterki.append(result[i])


masterki.sort(key=lambda tup: tup[3]+(tup[4]*0.01))
masterki.reverse()


myCursor.execute("""select idZawodnik, Imie, Nazwisko, TOP, BONUS
            from kategoria inner join zawodnik
            on kategoria.idKategoria = zawodnik.Kategoria_idKategoria
            where Nazwa = 'Masterzy'""")

result = myCursor.fetchall()
masterzy=[]
for i in range(0,len(result)):
    masterzy.append(result[i])


masterzy.sort(key=lambda tup: tup[3]+(tup[4]*0.01))
masterzy.reverse()



print 'wykonano symulacje'

db.commit()
db.close()








