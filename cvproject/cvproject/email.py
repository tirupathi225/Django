import smtplib
#import threading 

k = ["tirupathirao2525@gmail.com", "ravi@gmail.com"] 
  
for i in range(len(k)): 
    t = smtplib.SMTP('smtp.gmail.com', 587) 
    t.starttls() 
    t.login("tirupathirao2525@gmail.com", "9866495506") 
    message = "Message_you_need_to_send"
    t.sendmail("sender_email_id", k[i], message) 
    t.quit() 