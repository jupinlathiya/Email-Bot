import smtplib
import speech_recognition as s
import pyttsx3
from email.message import EmailMessage


sr = s.Recognizer()
engine = pyttsx3.init()


def talk(text):
    engine.say(text)
    engine.runAndWait()


def get_info():
    try:
        with s.Microphone() as m:
            print('listening.........')
            voice = sr.listen(m)
            info = sr.recognize_google(voice, language='eng-in')
            print(info)
            return info.lower()
    except:
        pass


def send_email(receiver, subject, message):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login('jupinlathiya005@gmail.com', 'jupin005#')
    email = EmailMessage()
    email['From'] = 'jupinlathiya005@gmail.com'
    email['To'] = receiver
    email['Subject'] = subject
    email.set_content(message)
    server.send_message(email)


email_list = {
    'xyz': 'xyz009@gmail.com',

}


def get_email_info():
    talk('To Whome you want to send email')
    name = get_info()
    receiver = email_list[name]
    print(receiver)

    talk('What is the subject of your email?')
    subject = get_info()
    talk('Tell me the text in your email')
    message = get_info()

    send_email(receiver, subject, message)
    talk('Your email is Successfully Sent')
    talk('You want to send more email?')
    more = get_info()
    if 'yes' in more:
        get_email_info()


get_email_info()
