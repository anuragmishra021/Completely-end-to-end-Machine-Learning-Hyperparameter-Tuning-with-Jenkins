import smtplib
s = smtplib.SMTP('smtp.gmail.com', 587)
s.starttls()

s.login("inbox.anuragmishra@gmail.com", "Anurag265476")


    # message
message_success = "Achieved your desired accuracy without tweeking . Congrats "


    # sending the mail
s.sendmail("inbox.anuragmishra@gmail.com", "inbox.anuragmishra@gmail.com", message_success)


    # terminating the session
s.quit()
