# -*- coding: utf-8 -*-
import MySQLdb
from mini_projekt_elim import final
import random

db = MySQLdb.connect(host='localhost', user='root', passwd='', db='zawody')
myCursor = db.cursor()
myCursor.execute("""DELETE FROM final""")



N=8
for i in range(0,len(final)):
    top=random.randint(0,N)
    bonus=top+random.randint(0,2)
    proba_top=top+random.randint(0,2)
    proba_bonus=bonus+random.randint(0,4)
    myCursor.execute("""INSERT INTO final(idFinal,final_top,final_bonus,proba_top,proba_bonus,Zawodnik_idZawodnik)
    VALUES (%s,%s,%s,%s,%s,%s);""",(i+1,top,bonus,proba_top,proba_bonus,final[i][0]))


myCursor.execute("""select Imie, Nazwisko, final_top, final_bonus, proba_top, proba_bonus, Zawodnik_idZawodnik
            from zawodnik inner join final
            on zawodnik.idZawodnik = final.Zawodnik_idZawodnik""")

result = myCursor.fetchall()
final=[]
for i in range(0,len(result)):
    final.append(result[i])


final.sort(key=lambda tup: (tup[2]+tup[3]*0.1)-((tup[4]*0.01)+tup[5]*0.01))
final.reverse()

for osoba in final:
    print osoba

myCursor.execute("""DELETE FROM final""")
for i in range(len(final)):
    myCursor.execute("""INSERT INTO final(idFinal,final_top,final_bonus,proba_top,proba_bonus,Zawodnik_idZawodnik)
    VALUES (%s,%s,%s,%s,%s,%s);""",(i+1,final[i][2],final[i][3],final[i][4],final[i][5],final[i][6]))

db.commit()
db.close()
