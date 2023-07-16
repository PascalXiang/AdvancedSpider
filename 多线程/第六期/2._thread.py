# 每天一遍自律读书
import _thread

import win32api


def run():
    win32api.MessageBox(0, '他不会是个好男人 也不会是个好情人', '啥时候可以去看李圣杰现场', 6)

_thread.start_new_thread(run,())
print('over')
