import requests

from bs4 import BeautifulSoup

import time

import smtplib

while True:

    url = "https://www.dauniv.ac.in/results"
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}

    response = requests.get(url, headers=headers)
    # parse the downloaded homepage and grab all text
    soup = BeautifulSoup(response.text, "lxml")


    if str(soup).find("M.A PHILOSOPHY") == -1:

        time.sleep(3600)

        continue


    else:

        msg = 'Subject: Philosophy results are out!'

        fromaddr = '<from email address>'

        toaddrs = ['<email address>', '<another email address>']

        # setup the email server,
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        # add my account login name and password,
        server.login("<from email address>", "PutYourOwnPassWordDude")

        # Print the email's contents
        print('From: ' + fromaddr)
        print('To: ' + str(toaddrs))
        print('Message: ' + msg)

        # send the email
        server.sendmail(fromaddr, toaddrs, msg)
        # disconnect from the server
        server.quit()

        break
