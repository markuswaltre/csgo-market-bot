import smtplib

def sendemail(subject, message):
	login =  '' #email
	password = '' #password
	sender = '' #email, same as login
	recipient = '' #email, probably same as login

	headers = ["from: " + sender,
	           "subject: " + subject,
	           "to: " + recipient,
	           "mime-version: 1.0",
	           "content-type: text/html"]
	headers = "\r\n".join(headers)

	complete = headers + "\r\n\r\n" + message

	# using gmail servers	
	server = smtplib.SMTP('smtp.gmail.com',587) #port 465 or 587
	server.ehlo()
	server.starttls()
	server.ehlo()
	server.login(login, password)
	server.sendmail(sender, recipient, complete)
	server.close()