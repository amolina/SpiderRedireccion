from pyquery import PyQuery as pq
from lxml import etree
import urllib
import wget
import urlparse
#Ejemplo de como descargar archivos desde cualquier web, tomando el nombre de archivo segun parametro de url
d = pq(url='http://www.newpct1.com/series/')

p=d("ul.pelilist li").find('a')
for link in p:
    urid = pq(url=link.attrib['href'])
    uridp=urid("ul.pagination li").find('a')
    for linkb in uridp:
        uridpp = pq(url=linkb.attrib['href'])
        uridppp=uridpp("ul.buscar-list li").find('a')
        for linkbppp in uridppp:
            uridetalle = pq(url=linkbppp.attrib['href'])
            uridetalletxt=uridetalle("a.f1-btn3")[-1]
            #Uri Torrent
            uritorrent = pq(url=uridetalletxt.attrib['href'])
            uritorrentfinal=uritorrent("a.btn-torrent")[0]
            print uritorrentfinal.attrib['href']
            if len(str(uritorrentfinal.attrib['href'].split("/")[-1]))>3:
                filenameppp = str(uritorrentfinal.attrib['href'].split("/")[-1])+".torrent"
            else:
                filenameppp = str(uritorrentfinal.attrib['href'].split("/")[-2])+".torrent"
                
            print filenameppp
            filenames = wget.download(uritorrentfinal.attrib['href'],filenameppp)
            
            














