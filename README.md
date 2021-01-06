
<div align=center>
<img src="./logo.png">
</div>
<div align=center>
<h1>HPPCommentMailer</h1>
</div>
<div align=center>
基于HerokuPaaS平台的HPPComment后端SMTP邮件发送平台
</div>

# 一键部署：

[![Deploy](https://www.herokucdn.com/deploy/button.svg)](https://www.heroku.com/deploy?template=https://github.com/HexoPlusPlus/HPPCommentMailer/tree/main)

# 环境变量配置

## `mail_password`

SMTP邮箱登陆的密码

## `mail_port`

SMTP服务器的端口

## `mail_sender`

邮箱发送用名,格式请用 发件人名字<发件人邮箱>，发件人邮箱若与SMTP登陆用户名不一致很容易被收件邮箱服务提供商丢入垃圾箱

## `mail_server`

SMTP服务器地址

## `mail_username`

SMTP登录用户名

## `token`

校验请求是否合法，避免接口被滥用，请不要设置的过于简单，建议采用UUID，可在[这里](https://www.uuidgenerator.net/)生成

> 例子: `123456`

> 例子: `df250e4c-38a0-4d9a-b7d8-355e25a91134`

## `site_name`

邮件中显示的站点名字

## `site_url`

邮件中显示的站点地址
