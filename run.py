
import os
import smtplib
import json
from email.mime.text import MIMEText
from email.header import Header
from flask import Flask, abort, request, jsonify
_app = Flask(__name__)
host= '0.0.0.0'
port= os.environ.get('PORT')
password= str(os.environ.get('token'))
mail_server= str(os.environ.get('mail_server'))
mail_username= str(os.environ.get('mail_username'))
mail_password= str(os.environ.get('mail_password'))
mail_sender= str(os.environ.get('mail_sender'))
mail_port= int(os.environ.get('mail_port'))
SITE_URL=str(os.environ.get('site_url'))
SITE_NAME=str(os.environ.get('site_name'))

@_app.route('/')
def index():
    if request.args.get('password') != password:
        print ("捕获非法请求")
        return jsonify({'success': False, 'msg': '密码错误'}) 
    print ("捕获合法请求")
    mailc="<div style=\"border-radius: 10px 10px 10px 10px;font-size:13px;    color: #555555;width: 666px;font-family:'Century Gothic','Trebuchet MS','Hiragino Sans GB',微软雅黑,'Microsoft Yahei',Tahoma,Helvetica,Arial,'SimSun',sans-serif;margin:50px auto;border:1px solid #eee;max-width:100%;background: #ffffff repeating-linear-gradient(-45deg,#fff,#fff 1.125rem,transparent 1.125rem,transparent 2.25rem);box-shadow: 0 1px 5px rgba(0, 0, 0, 0.15);\"><div style=\"width:100%;background:#49BDAD;color:#ffffff;border-radius: 10px 10px 0 0;background-image: -moz-linear-gradient(0deg, rgb(67, 198, 184), rgb(255, 209, 244));background-image: -webkit-linear-gradient(0deg, rgb(67, 198, 184), rgb(255, 209, 244));height: 66px;\"><p style=\"font-size:15px;word-break:break-all;padding: 23px 32px;margin:0;background-color: hsla(0,0%,100%,.4);border-radius: 10px 10px 0 0;\">您试图在ChenYFanのB话处注册账号</p></div><div style=\"margin:40px auto;width:90%\"><p>{NICK} 同学，这是您的专属注册链接</p><div style=\"background: #fafafa repeating-linear-gradient(-45deg,#fff,#fff 1.125rem,transparent 1.125rem,transparent 2.25rem);box-shadow: 0 2px 5px rgba(0, 0, 0, 0.15);margin:20px 0px;padding:15px;border-radius:5px;font-size:14px;color:#555555;\">{LINK}</div><p>您可以点击<a style=\"text-decoration:none; color:#12addb\" href=\"{LINK}\">直接注册</a>，欢迎您的使用。</p></div></div>".format(NICK=request.args.get('nick'),LINK=request.args.get('link'))
    message = MIMEText(str(mailc), 'html', 'utf-8')
    message['From'] = Header(mail_sender, 'utf-8')
    message['To'] =  Header(request.args.get('target'), 'utf-8')
    subject = 'Hi!这是您的注册链接'
    message['Subject'] = Header(subject, 'utf-8')
    try:
        smtpObj = smtplib.SMTP() 
        print ("试图连接SMTP"+mail_server+":"+str(mail_port))
        smtpObj.connect(mail_server, mail_port)
        print ("SMTP已连接，试图登录...")
        smtpObj.login(mail_username, mail_password)
        print ("已登录，试图发送邮件...")
        smtpObj.sendmail(mail_sender, request.args.get('target'), message.as_string())
        print ("Success: 邮件发送成功")
        return jsonify({'success': True, 'msg': '邮件已发送'})
    except smtplib.SMTPException:
        print ("Error: 无法发送邮件")
        return jsonify({'success': False, 'msg': '邮件未发送'})

if __name__ == '__main__':
    _app.run(host=host, port=port)
