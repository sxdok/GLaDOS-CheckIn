from os import environ
from Check import CheckIn
from notify import send
from login import SZLCSC

def main():
    # 获取actions secrets配置的cookie SendKey
    ck = os.environ["cookie"]

    notifications = "-----------------------\r\n"
    my_user.login("GlaDOS")
    if my_user.GlaDOS:
        if not ck:
            notifications += "请先配置GLADOS_COOKIE！"
            return

        try:
            title, Text = CheckIn(ck)
            notifications += title + "\r\n" + Text

        except Exception as err:
            notifications += "程序运行出错！"

    send("GLaDOS 签到通知",notifications)

if __name__ == '__main__':
    main()