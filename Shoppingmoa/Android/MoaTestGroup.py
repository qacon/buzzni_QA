#!/usr/bin/env python
#coding=utf8
from  __future__ import print_function
from unittest import TestLoader, TestSuite
from HtmlTestRunner import HTMLTestRunner
from Login import *
from Category import *
from email.message import EmailMessage
import datetime
import os
import smtplib

# with open('/Users/tsquare/Desktop/Git/AP/info.json') as json_file:
# with open('C:\\Users\\TSQUARE\\Documents\\Git\\AP\\info.json') as json_file:
#     json_data = json.load(json_file)
#     keylist = list(json_data.keys())
#     json_string = json_data[sys.argv[1]]
#
#     dname = json_string['dname']

s1 = TestLoader().loadTestsFromTestCase(Login)
s2 = TestLoader().loadTestsFromTestCase(Category)

suite = TestSuite([s1, s2])

daytime = datetime.datetime.now()
dt = daytime.strftime("%Y-%m-%d_%H-%M-%S")
filename = (f"GalaxyNote9MoaAutomationFunctionalTestReport")
dir = os.getcwd()
finalfile = (dir + f"/reports/GalaxyNote9MoaAutomationTestReport_"+dt+".html")
runner = HTMLTestRunner(combine_reports=True, report_name=filename, report_title="Moa Automation Functional Test Report (Android)") # report_title 파일열면 가장위에 있는 메인 title
runner.run(suite)

# smtp_gmail = smtplib.SMTP('smtp.cafe24.com', 587) # 발신 메일서버 포트번호
# msg = EmailMessage()
# smtp_gmail.ehlo() # SMTP 객체를 생성한 후에는 프로토콜 상 가장 먼저 SMTP 서버에 Hello 메시지를 보내는데, ehlo() 메서드가 이 기능을 함
# smtp_gmail.starttls() # tls방식으로 접속, 그 포트번호가 587
# smtp_gmail.login('billy@buzzni.com', '!tlgjatlf1')
# msg['Subject'] = "Moa Automation Test Report (Android)" # 메일제목
# msg.set_content("Test Started at : %s // Test Completed at : %s"%(daytime, datetime.datetime.now())) # 메일내용 테스트 시작시간과 종료시간
# msg['From'] = 'billy@buzzni.com'
# msg['To'] = 'billy@buzzni.com'
# # msg['Cc'] = ['a@b.com','a@b.com','a@b.com'] # 참조
# file = finalfile
# fp = open(file, 'rb')
# file_data = fp.read()
# msg.add_attachment(file_data, maintype='text', subtype='plain', filename="MoaAutomationTestReport_"+dt+".html")
# smtp_gmail.send_message(msg)