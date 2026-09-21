import smtplib 
from email.message import EmailMessage

# simple message
sender = 'skbashira2003@gmail.com' 
password = 'ypeb fiki shev bura'
receiver = 'narmajauppalapati@gmail.com' 
message = 'Hi narmaja akka, I have sent this mail from python code because i am doing email automation project' 
with smtplib.SMTP('smtp.gmail.com', 587) as conn:
    conn.starttls()
    conn.login(sender, password) 
    conn.sendmail(sender, receiver, message)
print('Message sent successfully')

# message with Subject and attachments

sender = 'skbashira2003@gmail.com' 
password = 'ypeb fiki shev bura'
message = EmailMessage()
message['From'] = 'skbashira2003@gmail.com'
message['To'] = 'Rakkeshadithya00@gmail.com'
message['Subject'] = 'SMTP MAIL'
message.set_content('Hi si, Iam sending this mail from Python Code')
files = ['Screenshot (195).png']
for filename in files:
    with open(filename, 'rb') as f:
        file_data = f.read() 
        message.add_attachment(file_data, maintype='application', subtype='octet-stream', filename=filename)
with smtplib.SMTP('smtp.gmail.com', 587) as conn:
    conn.starttls()
    conn.login(sender, password) 
    conn.send_message(message)
print('Message sent successfully')



# Bulk mail sending with Subject and attachments
sender = 'skbashira2003@gmail.com' 
password = 'ypeb fiki shev bura'
receivers = ['bashisk11@gmail.com', 'narmajauppalapati@gmail.com',  'Rakkeshadithya00@gmail.com']
message = EmailMessage()
message['From'] = 'skbashira2003@gmail.com'
message['Bcc'] = ','.join(receivers)
message['Subject'] = 'SMTP MAIL'
message.set_content('Hii sir, I  am  BASHIRA . I am sending this mail  to you beacuse i am completed my email automation project successfully check my github')
files = ['screenshot(195).png' '']
         
for filename in files:
    with open(filename, 'rb') as f:
        file_data = f.read() 
        message.add_attachment(file_data, maintype='application', subtype='octet-stream', filename=filename)
with smtplib.SMTP('smtp.gmail.com', 587) as conn:
    conn.starttls()
    conn.login(sender, password) 
    conn.send_message(message)
print('Message sent successfully')