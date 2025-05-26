# import smtplib
# from email.mime.text import MIMEText

# sender_email = "pentakotamadhu74@gmail.com"
# receiver_email = "hemadhu7@gmail.com"
# app_password = "bhoxrazprhssixqb"  # Replace with your App Password



# import smtplib, ssl

# smtp_server = "smtp.gmail.com"
# port = 587  # For starttls
# message = "hi test mail"
# # sender_email = "my@gmail.com"
# password = app_password

# # Create a secure SSL context
# context = ssl.create_default_context()

# # Try to log in to server and send email
# try:
#     server = smtplib.SMTP(smtp_server,port)
#     server.ehlo() # Can be omitted
#     server.starttls(context=context) # Secure the connection
#     server.ehlo() # Can be omitted
#     stat = server.login(sender_email, password)
#     print("login status",stat)
#     server.sendmail(sender_email, receiver_email, message)
#     # TODO: Send email here
# except Exception as e:
#     # Print any error messages to stdout
#     print(e)
# finally:
#     server.quit()