import smtplib
s=smtplib.SMTP('smtp.gmail.com',587)
s.starttls()
s.login('aditak2002@gmail.com','jlncufggdrfpoafx')
msg="hello how are you"
s.sendmail('aditak2002@gmail.com','adithyaak2405@gmail.com',msg)
s.quit()