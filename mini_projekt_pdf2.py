# -*- coding: utf-8 -*-
import MySQLdb
from mini_projekt_elim import x
from reportlab.pdfbase.ttfonts import *
from reportlab.pdfgen import canvas
from reportlab.pdfbase import pdfmetrics

db = MySQLdb.connect(host='localhost', user='root', passwd='', db='zawody')
myCursor = db.cursor()
pdfmetrics.registerFont(TTFont('Hebrew','Arial.ttf'))
c=canvas.Canvas(str(x)+'-final.pdf')


myCursor.execute("""SELECT imie, nazwisko, final_top, proba_top, final_bonus, proba_bonus
FROM final INNER JOIN zawodnik
ON final.zawodnik_idzawodnik=zawodnik.idzawodnik""")
result = myCursor.fetchall()


z=0
final=[]
for i in result:
    final.append(i)
k=780
szerokosc_t=220
szerokosc_b=380
for i in range(0,len(final)):
    c.setFont('Hebrew', 12)
    if final[i][3]==1:
        print i+1,final[i][0],final[i][1]
        print 'topów:',final[i][2],'w',final[i][3],'próbie'
        c.drawString(50, k, str(i + 1))
        c.drawString(80, k, (final[i][0] + ' ' + final[i][1]).decode('utf-8'))
        c.drawString(szerokosc_t, k, ('TOPÓW: ' + str(final[i][2]) + ' w ' + str(final[i][3]) + ' PRÓBIE').decode('utf-8'))

        if final[i][5]==1:
            print 'bonusów:',final[i][4],'w',final[i][5],'próbie'
            c.drawString(szerokosc_b, k, ('BONUSÓW: ' + str(final[i][4]) + ' w ' + str(final[i][5]) + ' PRÓBIE').decode('utf-8'))
        else:
            print 'bonusów:',final[i][4],'w',final[i][5],'próbach'
            c.drawString(szerokosc_b, k, ('BONUSÓW: ' + str(final[i][4]) + ' w ' + str(final[i][5]) + ' PRÓBACH').decode('utf-8'))
    elif final[i][5]==1:
        print i+1,final[i][0],final[i][1]
        print 'topów:',final[i][2],'w',final[i][3],'próbach'
        print 'bonusów:',final[i][4],'w',final[i][5],'probie'
        c.drawString(50, k, str(i + 1))
        c.drawString(80, k, (final[i][0] + ' ' + final[i][1]).decode('utf-8'))
        c.drawString(szerokosc_t, k, ('TOPÓW: ' + str(final[i][2]) + ' w ' + str(final[i][3]) + ' PRÓBACH').decode('utf-8'))
        c.drawString(szerokosc_b, k, ('BONUSÓW: ' + str(final[i][4]) + ' w ' + str(final[i][5]) + ' PRÓBIE').decode('utf-8'))
    else:
        print i+1,final[i][0],final[i][1]
        print 'topów:',final[i][2],'w',final[i][3],'próbach'
        print 'bonusów:',final[i][4],'w',final[i][5],'próbach'
        c.drawString(50, k, str(i + 1))
        c.drawString(80, k, (final[i][0] + ' ' + final[i][1]).decode('utf-8'))
        c.drawString(szerokosc_t, k, ('TOPÓW: ' + str(final[i][2]) + ' w ' + str(final[i][3]) + ' PRÓBACH').decode('utf-8'))
        c.drawString(szerokosc_b, k, ('BONUSÓW: ' + str(final[i][4]) + ' w ' + str(final[i][5]) + ' PRÓBACH').decode('utf-8'))
    k-=15

c.save()
db.commit()
db.close()


