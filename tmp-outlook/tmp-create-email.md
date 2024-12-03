from

#requirements.txt add for py 3 -> pypiwin32

def Emailer(text, subject, recipient):
    import win32com.client as win32
    import os

    outlook = win32.Dispatch('outlook.application')
    mail = outlook.CreateItem(0)
    mail.To = recipient
    mail.Subject = subject
    mail.HtmlBody = text
    ###

    attachment1 = os.getcwd() +"\\file.ini"

    mail.Attachments.Add(attachment1)

    ###
    mail.Display(True)

MailSubject= "Auto test mail"
MailInput="""
#html code here
"""
MailAdress="person1@gmail.com;person2@corp1.com"

Emailer(MailInput, MailSubject, MailAdress ) #that open a new outlook mail even outlook closed.