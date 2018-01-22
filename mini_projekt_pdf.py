# -*- coding: utf-8 -*-
from mini_projekt_reszta import juniorki, juniorzy, masterki, masterzy
from reportlab.pdfbase.ttfonts import *
from reportlab.pdfgen import canvas
from reportlab.pdfbase import pdfmetrics



pdfmetrics.registerFont(TTFont('Hebrew','Arial.ttf'))
c=canvas.Canvas('juniorki.pdf')
c.drawString(50, 800, 'KATEGORIA: JUNIORKI')
z=1
k=780
for i in range(0,len(juniorki)):
    c.setFont('Hebrew',14)
    c.drawString(50, k, str(z))
    c.drawString(80, k, (juniorki[i][1]+' '+juniorki[i][2]).decode('utf-8'))
    c.drawString(250, k, ('TOPÓW: ' + str(juniorki[i][3])).decode('utf-8'))
    c.drawString(350, k, ('BONUSÓW: ' + str(juniorki[i][4])).decode('utf-8'))
    k = k - 15
    z = z + 1
c.save()

pdfmetrics.registerFont(TTFont('Hebrew','Arial.ttf'))
c=canvas.Canvas('juniorzy.pdf')
c.drawString(50, 800, 'KATEGORIA: JUNIORZY')
z=1
k=780
for i in range(0,len(juniorzy)):
    c.setFont('Hebrew',14)
    c.drawString(50, k, str(z))
    c.drawString(80, k, (juniorzy[i][1]+' '+juniorzy[i][2]).decode('utf-8'))
    c.drawString(250, k, ('TOPÓW: ' + str(juniorzy[i][3])).decode('utf-8'))
    c.drawString(350, k, ('BONUSÓW: ' + str(juniorzy[i][4])).decode('utf-8'))
    k = k - 15
    z = z + 1
c.save()

pdfmetrics.registerFont(TTFont('Hebrew','Arial.ttf'))
c=canvas.Canvas('masterki.pdf')
c.drawString(50, 800, 'KATEGORIA: MASTERKI')
z=1
k=780
for i in range(0,len(masterki)):
    c.setFont('Hebrew',14)
    c.drawString(50, k, str(z))
    c.drawString(80, k, (masterki[i][1]+' '+masterki[i][2]).decode('utf-8'))
    c.drawString(250, k, ('TOPÓW: ' + str(masterki[i][3])).decode('utf-8'))
    c.drawString(350, k, ('BONUSÓW: ' + str(masterki[i][4])).decode('utf-8'))
    k = k - 15
    z = z + 1
c.save()


pdfmetrics.registerFont(TTFont('Hebrew','Arial.ttf'))
c=canvas.Canvas('masterzy.pdf')
c.drawString(50, 800, 'KATEGORIA: MASTERZY')
z=1
k=780
for i in range(0,len(masterzy)):
    c.setFont('Hebrew',14)
    c.drawString(50, k, str(z))
    c.drawString(80, k, (masterzy[i][1]+' '+masterzy[i][2]).decode('utf-8'))
    c.drawString(250, k, ('TOPÓW: ' + str(masterzy[i][3])).decode('utf-8'))
    c.drawString(350, k, ('BONUSÓW: ' + str(masterzy[i][4])).decode('utf-8'))
    k = k - 15
    z = z + 1
c.save()


