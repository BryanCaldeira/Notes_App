from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Post
from django.contrib import messages
import re
import smtplib 
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from django.contrib.staticfiles import finders
from email import encoders
from email.mime.base import MIMEBase
from threading import Thread



def Main(request):
		return render(request,"index1.html")


def Devop(request):
	return render(request,"devop.html")



def Sem3(request):
	if request.method == 'POST':
		try:
			emailid = request.POST['email']
			regex = '^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$'
			if(re.search(regex,emailid)):
				s = request.POST['subop']
				m = request.POST['modop']
				Thread(target = mail, args=(emailid,s,m,1,)).start()
				messages.success(request,"Notes has been mailed to you plz wait for 2min")
				return redirect("sem3")
			else:
				messages.success(request,"Invalid Email id")
				return redirect("sem3")
		except:
			print('Error')

	return render(request,"sem3.html")
	


def Sem4(request):
	if request.method == 'POST':
		try:
			emailid = request.POST['email']
			regex = '^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$'
			if(re.search(regex,emailid)):
				s = request.POST['subop']
				m = request.POST['modop']
				Thread(target = mail, args=(emailid,s,m,2,)).start()
				messages.success(request,"Notes has been mailed to you plz wait for 2min")
				return redirect("sem4")
			else:
				messages.success(request,"Invalid Email id")
				return redirect("sem3")
		except:
			print('Error')

	return render(request,"sem4.html")

def Sem5(request):
	if request.method == 'POST':
		try:
			emailid = request.POST['email']
			regex = '^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$'
			if(re.search(regex,emailid)):
				s = request.POST['subop']
				m = request.POST['modop']
				Thread(target = mail, args=(emailid,s,m,3,)).start()
				messages.success(request,"Notes has been mailed to you plz wait for 2min")
				return redirect("sem5")
			else:
				messages.success(request,"Invalid Email id")
				return redirect("sem5")
		except:
			print('Error')

	return render(request,"sem5.html")
	

def Sem6(request):
	if request.method == 'POST':
		try:
			emailid = request.POST['email']
			regex = '^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$'
			if(re.search(regex,emailid)):
				s = request.POST['subop']
				m = request.POST['modop']
				Thread(target = mail, args=(emailid,s,m,4,)).start()
				messages.success(request,"Notes has been mailed to you plz wait for 2min")
				return redirect("sem6")
			else:
				messages.success(request,"Invalid Email id")
				return redirect("sem6")
		except:
			print('Error')

	return render(request,"sem6.html")



def mail(emailglb,s,m,num):
	print('\n\n\n\n\n\n\n')
	print(emailglb)
	print('\n\n\n\n\n\n\n')
	Post.objects.create(user_email=emailglb)
	if num == 1:
		sub_list = ['ADE','DS','CO','USP','DM']
		mod_list = ['m1.pdf','m2.pdf','m3.pdf','m4.pdf','m5.pdf']
		sem = 'Sem3/'

	elif num == 2:
		sub_list = ['SE','DAA','MPMC','OOC','DC']
		mod_list = ['m1.pdf','m2.pdf','m3.pdf','m4.pdf','m5.pdf']
		sem = 'Sem4/'

	elif num == 3:
		sub_list = ['ME','CN','DMS','ATC']
		mod_list = ['m1.pdf','m2.pdf','m3.pdf','m4.pdf','m5.pdf']
		sem = 'Sem5/'

	elif num == 4:
		sub_list = ['CNS','CG','SS','OS','PY']
		mod_list = ['m1.pdf','m2.pdf','m3.pdf','m4.pdf','m5.pdf']
		sem = 'Sem6/'




	s = int(s)
	m = int(m)

	pth = sub_list[s] +'/'+ mod_list[m]
	msg = MIMEMultipart('alternative')

	result = finders.find(sem+pth)

	sender_address = 'csnotesvtu@gmail.com'
	sender_pass = 'bryancaldeira6'
	receiver_address = emailglb
	filename = sub_list[s]+' '+mod_list[m]

	message = MIMEMultipart()
	message['From'] = sender_address
	message['To'] = receiver_address
	message['Subject'] = 'Notes Attachment'

	attach_file = open(result, 'rb')
	payload = MIMEBase('application', 'octate-stream')
	payload.set_payload((attach_file).read())
	encoders.encode_base64(payload)

	payload.add_header('Content-Disposition', "attachment; filename= %s" % filename) 
	message.attach(payload)

	session = smtplib.SMTP('smtp.gmail.com', 587)
	session.starttls()
	session.login(sender_address, sender_pass)
	text = message.as_string()
	session.sendmail(sender_address, receiver_address, text)
	session.quit()


def Back(request):
	return redirect("/")
