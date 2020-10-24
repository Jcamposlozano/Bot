from urllib.request import Request, urlopen
from pyquery import PyQuery  


class Indicadores:

    def indicadoresTotales(self):
        try:
            req = Request('https://www.dane.gov.co/index.php/indicadores-economicos', None, {'User-agent' : 'Mozilla/5.0 (Windows; U; Windows NT 5.1; de; rv:1.9.1.5) Gecko/20091102 Firefox/3.5.5'})
            content = urlopen(req).read()
            pq = PyQuery(content)
            trm =  [i.text() for i in pq('table').eq(1)('h1').items()][0].replace('$','').replace('.','').replace(',','.') 
            uvr =  [i.text() for i in pq('table').eq(2)('h1').items()][0].replace('$','').replace('.','').replace(',','.') 
            dtf =  [i.text() for i in pq('table').eq(3)('h1').items()][0].replace('$','').replace('.','').replace(',','.')
            desempleo = [i.text() for i in pq('table').eq(4)('h1').items()][0].replace('$','').replace('.','').replace(',','.')

            return trm , uvr , dtf, desempleo
        except (Exception) as error:
            return ''
            print(error) 
            
            