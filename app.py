from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4, A5, A6, A7

def mm2p(milimetros):
    return milimetros / 0.352777

cnv = canvas.Canvas("plano_alimentar.pdf", pagesize=A5)
cnv.drawS
cnv.save()