import smtplib
from email.message import EmailMessage
import csv

accepted_candidates=[]
rejected_candidates=[]

with open('interview_candidates1.csv','r') as csv_file :
    csv_reader = csv.reader(csv_file)
    for candidate in csv_reader:
      if(candidate[3]=='Yes'):
          accepted_candidates.append(candidate)
      elif(candidate[3]=='No') :
          rejected_candidates.append(candidate)

def send_email(to, content):
    email = EmailMessage()
    email['from'] = 'Ahmed Kouki'
    email['to'] = to
    email['subject'] = 'Your application for the role of working student'
    email.set_content(content)
    return email

email_adress=input('enter your email adress')
password=input('enter your password')


with smtplib.SMTP(host='smtp.gmail.com',port=587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login(email_adress,password)
    
    for candidate in rejected_candidates:
        rejection_email_content= f'Dear {candidate[0]},\nAfter careful examination of all of our application documents,\nwe unfortunately could not include you in the closest circle of applicants.\nPlease understand that often only details decide when filling a position.\nWe sincerely thank you for the efforts you have invested in the application and in particular for the trust placed in our company.\nWe wish you all the best for your future and what you can expect there.\nWith best regards,\nAhmed Kouki'
        smtp.send_message(send_email(candidate[2],rejection_email_content))
        
    for candidate in accepted_candidates:
        interview_response_content = f'Dear {candidate[0]},\nThank you for your interest in the Working Student position.\nWe are impressed with your background and would like to schedule an interview with you. Could you please provide your availability for an interview over the next few days?\nWe will do our best to accommodate your schedule.\nLooking forward to your response.\nBest regards,\nAhmed Kouki'
        smtp.send_message(send_email(candidate[2],interview_response_content))
print("all done")