from threading import *

from datetime import datetime
import time

from Indicadores import *


class bot:

    def observadorRelog(self):
        while(True):
            time.sleep(1)
            now = datetime.now()
            horacatual = now.strftime('%H:%M:%S')

            if horacatual == '10:14:30':
                i = Indicadores()
                try:
                    trm , uvr , dtf, desempleo = i.indicadoresTotales()
                    print("trm  = " + trm)
                    print("uvr  = " + uvr)
                    print("dtf  = " + dtf)
                    print("desempleo  = " + desempleo)
                except (Exception) as error:
                    print(error)                 
                

    def iniciar(self):
        t = Timer(5.0, self.observadorRelog)
        t.start()

