from threading import *

from datetime import datetime
import time


class bot:

    def observadorRelog(self):
        while(True):
            time.sleep(1)
            now = datetime.now()
            horacatual = now.strftime('%H:%M:%S')
            print(horacatual)


    def iniciar(self):
        t = Timer(5.0, self.observadorRelog)
        t.start()
