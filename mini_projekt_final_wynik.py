# -*- coding: utf-8 -*-
import MySQLdb
import random

db = MySQLdb.connect(host='localhost', user='root', passwd='', db='zawody')
myCursor = db.cursor()


myCursor.execute("""SELECT imie, nazwisko, final_top, proba_top, final_bonus, proba_bonus
FROM final INNER JOIN zawodnik
ON final.zawodnik_idzawodnik=zawodnik.idzawodnik""")
result = myCursor.fetchall()


z=0
final=[]
for i in result:
    final.append(i)
for osoba in final:
    if final[z][3]==1:
        print z+1,final[z][0],final[z][1]
        print 'topów:',final[z][2],'w',final[z][3],'próbie'
        if final[z][5]==1:
            print 'bonusów:',final[z][4],'w',final[z][5],'próbie'
        else:
            print 'bonusów:',final[z][4],'w',final[z][5],'próbach'
    elif final[z][5]==1:
        print z+1,final[z][0],final[z][1]
        print 'topów:',final[z][2],'w',final[z][3],'próbach'
        print 'bonusów:',final[z][4],'w',final[z][5],'probie'
    else:
        print z+1,final[z][0],final[z][1]
        print 'topów:',final[z][2],'w',final[z][3],'próbach'
        print 'bonusów:',final[z][4],'w',final[z][5],'próbach'
    z+=1


db.commit()
db.close()

