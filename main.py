import smtplib
import csv
import argparse
from email.mime.text import MIMEText

parser = argparse.ArgumentParser(description='Send custom email to group of people')
parser.add_argument('email', type=str, help='gmail address')
parser.add_argument('password', type=str, help='gmail password')
parser.add_argument('csv', type=str, help='file name of csv file\
        DO NOT INCLUDE HEADER')
parser.add_argument('template', type=str, help='see "example.txt"\
        to see the format')
parser.add_argument('type', type=str, nargs='?', default="plain", help='use \
        "html" if you want email to be in html')
args = parser.parse_args()
me = args.email
password = args.password
csvfile = args.csv
templatefile = args.template
mimeType = args.type

csvfp = open(csvfile, 'rt')
templatefp = open(templatefile, 'rt')
template = templatefp.read()
reader = csv.reader(csvfp)

s = smtplib.SMTP('smtp.gmail.com:587')
s.starttls()
s.login(me, password)
for row in reader:
    row = ["???"] + row

    template2 = template.format(*tuple(row))
    template2 = template2.split("\n",2)
    you = template2[0]
    msg = MIMEText(template2[2], mimeType)
    msg['Subject'] = template2[1]
    msg['from'] = me
    msg['to'] = you
    print msg
    s.sendmail(me, [you], msg.as_string())

s.quit()


# textfile = "content.txt"
# fp = open(textfile, 'rb')
# # Create a text/plain message
# msg = MIMEText(fp.read())
# fp.close()
# csvfp.close()

# you = "lijiaqigreat@gmail.com"
# msg['Subject'] = 'The contents of %s' % textfile
# msg['From'] = me
# msg['To'] = you

# # Send the message via our own SMTP server, but don't include the
# # envelope header.
# s = smtplib.SMTP('smtp.gmail.com:587')
# s.starttls()
# s.login("lijiaqitest@gmail.com","password1992")
# s.sendmail(me, [you], msg.as_string())
# s.quit()
