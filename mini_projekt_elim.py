# -*- coding: utf-8 -*-
import MySQLdb
from reportlab.pdfbase.ttfonts import *
from reportlab.pdfgen import canvas
from reportlab.pdfbase import pdfmetrics

db = MySQLdb.connect(host='localhost', user='root', passwd='', db='zawody')
myCursor = db.cursor()


x=raw_input('podaj kategorie: ')
myCursor.execute("""select idZawodnik, Imie, Nazwisko, TOP, BONUS
            from kategoria inner join zawodnik
            on kategoria.idKategoria = zawodnik.Kategoria_idKategoria
            where Nazwa = %s""", (x))

result = myCursor.fetchall()
kategoria=[]
for i in range(0,len(result)):
    kategoria.append(result[i])

kategoria.sort(key=lambda tup: tup[3]+(tup[4]*0.01))
kategoria.reverse()


pdfmetrics.registerFont(TTFont('Hebrew','Arial.ttf'))
c=canvas.Canvas(str(x)+'-eliminacje.pdf')
c.drawString(50, 800, 'KATEGORIA: '+str(x))
z=1
k=780
for i in range(0,len(kategoria)):
    c.setFont('Hebrew',14)
    c.drawString(50, k, str(z))
    c.drawString(80, k, (kategoria[i][1]+' '+kategoria[i][2]).decode('utf-8'))
    c.drawString(250, k, ('TOPÓW: ' + str(kategoria[i][3])).decode('utf-8'))
    c.drawString(350, k, ('BONUSÓW: ' + str(kategoria[i][4])).decode('utf-8'))
    k = k - 15
    z = z + 1
c.save()


#FINAL

k=6
for i in range(6,len(kategoria)):

    if (kategoria[5][3] + (kategoria[5][4] * 0.001)) == (kategoria[k][3] + (kategoria[k][4] * 0.001)):
        k = k + 1

print k



myCursor.execute("""DELETE FROM final""")
final=[]
for i in range(k):
    myCursor.execute("""INSERT INTO final(idFinal,final_top,final_bonus,proba_top,proba_bonus,Zawodnik_idZawodnik)
    VALUES (%s,%s,%s,%s,%s,%s);""",(i+1,kategoria[i][3],kategoria[i][4],10,10,kategoria[i][0]))
    final.append(kategoria[i])
db.commit()
db.close()




