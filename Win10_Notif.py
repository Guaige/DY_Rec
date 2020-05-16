import time

from win10toast import ToastNotifier

toaster = ToastNotifier()
toaster.show_toast(u'标题1', u'收到一个通知1', duration=60)
time.sleep(100)