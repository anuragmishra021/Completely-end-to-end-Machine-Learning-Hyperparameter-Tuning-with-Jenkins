import smtplib
s = smtplib.SMTP('smtp.gmail.com', 587)
s.starttls()

s.login("inbox.anuragmishra@gmail.com", "*********")


    # message
message = "Your accuracy is less than 90% .Try again"


    # sending the mail
s.sendmail("inbox.anuragmishra@gmail.com", "inbox.anuragmishra@gmail.com", message)


    # terminating the session
s.quit()
