import smtplib as smtp


def send_email_code(dest_email, code):
    email = 'forfaceit1441@yandex.ru'
    password = 'EmiSSionS228!'
    subject = 'Your Code is'
    email_text = code
    message = 'From: {}\nTo: {}\nSubject: {}\n\n{}'.format(email,
                                                        dest_email,
                                                        subject,
                                                        email_text)
    server = smtp.SMTP_SSL('smtp.yandex.com')
    server.set_debuglevel(1)
    server.ehlo(email)
    server.login(email, password)
    server.auth_plain()
    server.sendmail(email, dest_email, message)
    server.quit()

#send_email_code('forfaceit1441@yandex.ru', 415121)