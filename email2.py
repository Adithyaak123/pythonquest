import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
fromaddr="aditak2002@gmail.com"
toaddr="adithyaak2405@gmail.com"
msg=MIMEMultipart() #object of mimemultipart
msg['from']=fromaddr #store sender address
msg['to']=toaddr #store reciever address
msg['subject']='this is file sharing' #store subject
body="good morning" #body of mail
msg.attach(MIMEText(body,"plain")) #attach body
file="exam.py" #store file name with extension
attachment=open(file,"rb") #open file in read and binary mode
p=MIMEBase('application','octet-stream')
p.set_payload((attachment).read()) #to encode
encoders.encode_base64(p) #convert to base64
p.add_header('content-Disposition',"attachment;filename=%s" %file)
msg.attach(p)
s=smtplib.SMTP('smtp.gmail.com',587)
s.starttls()
s.login(fromaddr,'jlncufggdrfpoafx')
text=msg.as_string()
s.sendmail(fromaddr,toaddr,text)
s.quit()
