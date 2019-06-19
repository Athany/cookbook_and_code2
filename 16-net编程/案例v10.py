from email.mime.text import MIMEText
from email.header import Header

msg = MIMEText("Hello world", "plain", "utf-8")
# 下面代码故意写错，说明，所谓的发送者的地址，只是从一个Header的第一个参数作为字符串构建的内容
# 用utf8编码是因为很可能内容包含非英文字符
header_from = Header("从我的邮箱发出去的<Me@qq.cn>", "utf-8")
msg['From'] = header_from

# 填写接受者信息
header_to = Header("去刘亦菲的地方<刘亦菲@sina.com>", 'utf-8')
msg['To'] = header_to

header_sub = Header("这是我的主题", 'utf-8')
msg['Subject'] = header_sub

# 构建发送者地址和登录信息
from_addr = "330987706@qq.com"
from_pwd = "uqganadvvwhzcbch"

# 构建邮件接受者信息
to_addr = "330987706@qq.com"

smtp_srv = "smtp.qq.com"

try:
    import smtplib

    srv = smtplib.SMTP_SSL(smtp_srv.encode(), 465)

    srv.login(from_addr, from_pwd)
    srv.sendmail(from_addr, [to_addr], msg.as_string())
    srv.quit()

except Exception as e:
    print(e)
