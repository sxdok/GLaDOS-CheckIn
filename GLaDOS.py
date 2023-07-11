import os
from Check import CheckIn
from notify import send

# 获取actions secrets配置的cookie SendKey
ck = os.environ["cookie"]

notifications = "-----------------------\r\n"
if not ck:
    notifications += "请先配置GLADOS_COOKIE！"
try:
    title, Text = CheckIn(ck)
    notifications += title + "\r\n" + Text

except Exception as err:
    notifications += "程序运行出错！"

send("GLaDOS 签到通知",notifications)
