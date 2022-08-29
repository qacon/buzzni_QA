#!/usr/bin/env python
#coding=utf8
from  __future__ import print_function
from unittest import TestLoader, TestSuite
from HtmlTestRunner import HTMLTestRunner
from time import *
from datetime import *
from Category import *
from Home import *
from Home2 import *
from Footer import *
from Search import *
from Cart import *
from Purchase import *
from NonLogin import *
from Etc import *
from email.message import EmailMessage
import datetime
import sys
import os
import io
import sys
import smtplib
import json
from Bootstrap import TEST_CONFIG as TCFG

# with open('/Users/tsquare/Desktop/Git/AP/info.json') as json_file:
with open('C:\\Users\\TSQUARE\\Documents\\Git\\AP\\info.json') as json_file:
    json_data = json.load(json_file)
    keylist = list(json_data.keys())
    json_string = json_data[sys.argv[1]]

    dname = json_string['dname']

s1 = TestLoader().loadTestsFromTestCase(Category)
s2 = TestLoader().loadTestsFromTestCase(Home)
# s3 = TestLoader().loadTestsFromTestCase(Home2)
s3 = TestLoader().loadTestsFromTestCase(Footer)
s4 = TestLoader().loadTestsFromTestCase(Search)
s5 = TestLoader().loadTestsFromTestCase(Cart)
# s8 = TestLoader().loadTestsFromTestCase(Purchase)
s6 = TestLoader().loadTestsFromTestCase(NonLogin)
s7 = TestLoader().loadTestsFromTestCase(Etc)

# suite = TestSuite([s1])
suite = TestSuite([s1, s2, s3, s4, s5, s6, s7])

daytime = datetime.datetime.now()
dt = daytime.strftime("%Y-%m-%d_%H-%M-%S")
filename = (f"{dname}EHFunctionalTestReport")
dir = os.getcwd()
finalfile = (dir + f"/reports/{dname}EHFunctionalTestReport_"+dt+".html")
runner = HTMLTestRunner(combine_reports=True, report_name=filename, report_title="Shoppingmoa Application Functional Test Report (Android)")
# report_title 파일열면 가장위에 있는 메인 title
runner.run(suite)

smtp_gmail = smtplib.SMTP('smtp.cafe24.com', 587)  # 발신 메일서버 포트번
msg = EmailMessage()
smtp_gmail.ehlo()  # SMTP 객체를 생성한 후에는 프로토콜 상 가장 먼저 SMTP 서버에 Hello 메시지를 보내는데, ehlo() 메서드가 이 기능을 함
smtp_gmail.starttls()  # tls방식으로 접속, 그 포트번호가 587
smtp_gmail.login('automation@t-square.co.kr', '1q2w3e4r5t')
msg['Subject'] = "Shoppingmoa Functional Test Report (Android)"  # 메일제목
msg.set_content("Test Started at : %s // Test Completed at : %s"%(daytime, datetime.datetime.now())) # 메일내용 테스트 시작시간과 종료시간
msg['From'] = 'automation@t-square.co.kr'
msg['To'] = 'daniel.jeong.tsquare@amorepacific.com'
# msg['Cc'] = ['dave.yeom@t-square.co.kr','jun.kyung@t-square.co.kr','lily.song@t-square.co.kr']   # 참조
file = finalfile
fp = open(file, 'rb')
file_data = fp.read()
msg.add_attachment(file_data, maintype='text', subtype='plain', filename="ShoppingmoaFunctionalTestReport_"+dt+".html")
smtp_gmail.send_message(msg)
