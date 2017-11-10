#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# por DeusMaior
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.


##############BIBLIOTECAS A IMPORTAR E DEFINICOES####################

import urllib,urllib2,urlparse,re,os.path,xbmcplugin,xbmcgui,xbmc,xbmcaddon,HTMLParser
h = HTMLParser.HTMLParser()


addon_id = 'plugin.video.tugaflix'
addon_version = '0.6.0'
selfAddon = xbmcaddon.Addon(id=addon_id)
addonfolder = selfAddon.getAddonInfo('path')
artfolder = '/resources/img/'
progress = xbmcgui.DialogProgress()


################################################## 

#MENUS############################################

def CATEGORIES():
    addDir('Filmes','http://tugaflix.com/Filmes',5,'http://www.ckfilms.com/wp-content/uploads/2013/09/clapper.png')
    addDir('Series','http://tugaflix.com/Series',6,'http://img4.wikia.nocookie.net/__cb20100319190057/anythingforeveryone/images/4/43/Television_300x300_icon.png')
    addLink('','','',0,'')
    addDir('Pesquisar Filmes','http://tugaflix.com/Filmes',7,'')
    addDir('Pesquisar Series','http://tugaflix.com/Series',8,'')
    addLink('','','',0,'')
    addDir('TugaFlix Unofficial (Versão: '+addon_version+')','',0,'')


def SUB_CAT_FILMES():
    addDir ('Todos Filmes','http://tugaflix.com/Filmes',1,'http://www.ckfilms.com/wp-content/uploads/2013/09/clapper.png')
    addDir ('Acção','http://tugaflix.com/Filmes?T=&G=Ac%C3%A7%C3%A3o&O=1',1,'')
    addDir ('Animação','http://tugaflix.com/Filmes?T=&G=Anima%C3%A7%C3%A3o&O=1',1,'')
    addDir ('Aventura','http://tugaflix.com/Filmes?T=&G=Aventura&O=1',1,'')
    addDir ('Biografia','http://tugaflix.com/Filmes?T=&G=Biografia&O=1',1,'')
    addDir ('Comédia','http://tugaflix.com/Filmes?T=&G=Com%C3%A9dia&O=1',1,'')
    addDir ('Crime','http://tugaflix.com/Filmes?T=&G=Crime&O=1',1,'')
    addDir ('Desporto','http://tugaflix.com/Filmes?T=&G=Desporto&O=1',1,'')
    addDir ('Documentário','http://tugaflix.com/Filmes?T=&G=Document%C3%A1rio&O=1',1,'')
    addDir ('Drama','http://tugaflix.com/Filmes?T=&G=Drama&O=1',1,'')
    addDir ('Familiar','http://tugaflix.com/Filmes?T=&G=Familiar&O=1',1,'')
    addDir ('Fantasia','http://tugaflix.com/Filmes?T=&G=Fantasia&O=1',1,'')
    addDir ('SciFi','http://tugaflix.com/Filmes?T=&G=Fic%C3%A7%C3%A3o&O=1',1,'')
    addDir ('Guerra','http://tugaflix.com/Filmes?T=&G=Guerra&O=1',1,'')
    addDir ('História','http://tugaflix.com/Filmes?T=&G=Hist%C3%B3ria&O=1',1,'')
    addDir ('Mistério','http://tugaflix.com/Filmes?T=&G=Mist%C3%A9rio&O=1',1,'')
    addDir ('Música','http://tugaflix.com/Filmes?T=&G=M%C3%BAsica&O=1',1,'')
    addDir ('Romance','http://tugaflix.com/Filmes?T=&G=Romance&O=1',1,'')
    addDir ('Suspense','http://tugaflix.com/Filmes?T=&G=Suspense&O=1',1,'')
    addDir ('Terror','http://tugaflix.com/Filmes?T=&G=Terror&O=1',1,'')
    addDir ('Western','http://tugaflix.com/Filmes?T=&G=Western&O=1',1,'')

def SUB_CAT_SERIES():
    addDir ('Todas as Séries','http://tugaflix.com/Series',3,'http://www.ckfilms.com/wp-content/uploads/2013/09/clapper.png')
    addDir ('Acção','http://tugaflix.com/Series?T=&G=Ac%C3%A7%C3%A3o&O=1',3,'')
    addDir ('Animação','http://tugaflix.com/Series?T=&G=Anima%C3%A7%C3%A3o&O=1',3,'')
    addDir ('Aventura','http://tugaflix.com/Series?T=&G=Aventura&O=1',3,'')
    addDir ('Biografia','http://tugaflix.com/Series?T=&G=Biografia&O=1',3,'')
    addDir ('Comédia','http://tugaflix.com/Series?T=&G=Com%C3%A9dia&O=1',3,'')
    addDir ('Crime','http://tugaflix.com/Series?T=&G=Crime&O=Ad icionado',3,'')
    addDir ('Desporto','http://tugaflix.com/Series?T=&G=Desporto&O=1',3,'')
    addDir ('Documentário','http://tugaflix.com/Series?T=&G=Document%C3%A1rio&O=1',3,'')
    addDir ('Drama','http://tugaflix.com/Series?T=&G=Drama&O=1',3,'')
    addDir ('Familiar','http://tugaflix.com/Series?T=&G=Familiar&O=1',3,'')
    addDir ('Fantasia','http://tugaflix.com/Series?T=&G=Fantasia&O=1',3,'')
    addDir ('SciFi','http://tugaflix.com/Series?T=&G=Fic%C3%A7%C3%A3o&O=1',3,'')
    addDir ('Guerra','http://tugaflix.com/Series?T=&G=Guerra&O=1',3,'')
    addDir ('História','http://tugaflix.com/Series?T=&G=Hist%C3%B3ria&O=1',3,'')
    addDir ('Mistério','http://tugaflix.com/Series?T=&G=Mist%C3%A9rio&O=1',3,'')
    addDir ('Música','http://tugaflix.com/Series?T=&G=M%C3%BAsica&O=1',3,'')
    addDir ('Romance','http://tugaflix.com/Series?T=&G=Romance&O=1',3,'')
    addDir ('Suspense','http://tugaflix.com/Series?T=&G=Suspense&O=1',3,'')
    addDir ('Terror','http://tugaflix.com/Series?T=&G=Terror&O=1',3,'')
    addDir ('Western','http://tugaflix.com/Series?T=&G=Western&O=1',3,'')

###################################################################################
#FUNCOES


def abrir_video(video):
     progress.update(75,'Playing Video')
     player = xbmc.Player()
     player.play(video)
     
def listar_filmes(url):
        codigo_fonte = abrir_url(url)
        match=re.compile('<div class="browse-movie-wrap col-xs-10 col-sm-4 col-md-5 col-lg-4">\s<a href="(.+?)" class="browse-movie-link">\s<figure>\s<img class="img-responsive" src="(.+?)" alt="(.+?)">').findall(codigo_fonte)
        for url, img, titulo in match:
            addDir(titulo,'http://tugaflix.com/'+ url,2,'http://tugaflix.com/'+img,False)
        match = re.compile('<li><a href="(.+?)">Seguinte &raquo;</a></li>').findall(codigo_fonte)
        for next_page in match:
            addLink('','','',0,'')
            addDir('Proximo >>','http://tugaflix.com'+ next_page,1,'')

def listar_series(url):
        codigo_fonte = abrir_url(url)
        match=re.compile('<div class="browse-movie-wrap col-xs-10 col-sm-4 col-md-5 col-lg-4">\s<a href="(.+?)" class="browse-movie-link">\s<figure>\s<img class="img-responsive" src="(.+?)" alt="(.+?)">').findall(codigo_fonte)
        for url, img, titulo in match:
            addDir(titulo,'http://tugaflix.com/'+ url,4,'http://tugaflix.com/'+img,True)
        match = re.compile('<ul class="tsc_pagination tsc_paginationA tsc_paginationA06">.+?<a href="(.+?)">Seguinte »</a></li></ul></div>').findall(codigo_fonte)
        for next_page in match:
            addLink('','','',0,'')
            addDir('Proximo >>','http://tugaflix.com/'+ next_page,1,'')

def listar_episodios(url):
        codigo_fonte = abrir_url(url)
        match=re.compile('<a class="browse-movie-link" href="(.+?)"><figure><img class="img-respisode" src="(.+?)"><figcapepisode><h4 class="gridepisode1">(.+?)</h4><h6 class="gridepisode2">.+?</h6></figcapepisode></figure></a>').findall(codigo_fonte)
        for url,img, titulo in match:
            addDir(titulo,'http://tugaflix.com'+ url,2,'http://tugaflix.com/'+img,False)

def encontrar_fontes(url):
    codigo_fonte=abrir_url(url)
    match = re.compile('<source src="(.+?)" type="video/mp4" data-res="servidor.02">').findall(codigo_fonte)
    if not match:
        encontrar_fontes_openload(url+"&C")
    else:
        for ficheiro in match:
            ficheiro = ficheiro.replace('Video?V=http://servidor.02/','')
            match =re.compile('<track src="(.+?)" kind="captions" srclang="pt" label="pt-pt">').findall(codigo_fonte)
        for legenda in match:
            print 'vamos la ver:' + ficheiro
            final = 'http://filehoot.com/vidembed-'+ficheiro+'.mp4'
            legenda = 'http://tugaflix.com/'+legenda
            abrir_video(final)

def encontrar_fontes_openload(url):
    codigo_fonte=abrir_url(url)
    match = re.compile('<iframe src="(.+?)" frameborder="0"></iframe><br>').findall(codigo_fonte)
    for captcha in match:
        resolve_captcha(captcha)

def resolve_captcha(captcha):
        codigo_fonte=abrir_url(captcha)
        imagem = re.compile('value="(.+)">\n<center><img width=".+?" height=".+?" alt="" src="(.+?)"></center>').findall(codigo_fonte)
        for recaptcher, link in imagem:
            print (recaptcher + link)
            capimg = "http://www.google.com/recaptcha/api/"+link
            if capimg:
                img = xbmcgui.ControlImage(550, 20, 600, 114, capimg)
                dlg = xbmcgui.WindowDialog()
                dlg.addControl(img)
                dlg.show()
                kb = xbmc.Keyboard('', 'Type the letters in the image', False)
                kb.doModal()
                kbinput = kb.getText()
                dlg.close()
                data1 = urllib.urlencode({'recaptcha_challenge_field': recaptcher, 'recaptcha_response_field': kbinput})
                data1 = data1.encode('ascii')
                req1 = urllib2.Request(captcha, data1)
                req1.add_header('User-Agent','Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:56.0) Gecko/20100101 Firefox/56.0')
                response1 = urllib2.urlopen(req1)
                link1 = response1.read()
                response1.close()
                captchaCode = re.findall('<textarea rows="5" cols="100">(.+?)</textarea>', str(link1))
                for recap1 in captchaCode:
                    print('\nCaptcha Reply Code:\n' + recap1 + '\n')
                # E pronto, neste momento temos a confirmação de que o captcha está correcto e recebemos o código de confirmação para usar na página do filme
                data2 = urllib.urlencode(
                    {'recaptcha_challenge_field': recap1, 'recaptcha_response_field': 'manual_challenge'})
                data2 = data2.encode('ascii')
                req2 = urllib2.Request(url, data2)
                req2.add_header('User-Agent',
                                'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:56.0) Gecko/20100101 Firefox/56.0')
                response2 = urllib2.urlopen(req2)
                link2 = response2.read()
                response2.close()
                progress.create('Play video', 'Searching videofile.')
                movieCode = re.findall('<iframe src="(.+?)mp4', str(link2))
                for ficheiro in movieCode:
                    ficheiro = ficheiro+"mp4"
                    progress.update(25,'sending to UrlResolver')
                    resolve_openload(ficheiro)
                    
def resolve_openload(url):
    url = url.replace('https://openload.co', 'http://openload.io')
    progress.update(30,'Resolving Openload Link')
    import urlresolver
    stream_url = urlresolver.resolve(url)
    progress.update(50,'Found Video')
    abrir_video(stream_url)

def pesquisa_filmes():
    keyb = xbmc.Keyboard('','Escreva o Filme a Pesquisar')
    keyb.doModal()
    if (keyb.isConfirmed()):
        search = keyb.getText()
        parametro_pesquisa=urllib.quote(search)
    url = 'http://tugaflix.com/Filmes?T='+str(parametro_pesquisa)+'&G=&O=1'
    listar_filmes(url)
    
def pesquisa_series():
    keyb = xbmc.Keyboard('','Escreva a Serie a Pesquisar')
    keyb.doModal()
    if (keyb.isConfirmed()):
        search = keyb.getText()
        parametro_pesquisa=urllib.quote(search)
    url = 'http://tugaflix.com/Series?T='+str(parametro_pesquisa)+'&G=&O=1'
    listar_series(url)

###################################################################################
#FUNCOES JÃ FEITAS


def abrir_url(url):
    req = urllib2.Request(url)
    req.add_header('User-Agent', 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3')
    response = urllib2.urlopen(req)
    link=response.read()
    response.close()
    return link

def addLink(name,url,iconimage,total,descricao):
        ok=True
        liz=xbmcgui.ListItem(name, iconImage="DefaultVideo.png", thumbnailImage=iconimage)
        liz.setProperty('fanart_image', addonfolder + artfolder + 'fanart.png')
        liz.setInfo( type="Video", infoLabels={ "Title": name,  "Plot": descricao} )
        return xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=url,listitem=liz, totalItems=total)
	return ok

def addDir(name,url,mode,iconimage,pasta=True):
        u=sys.argv[0]+"?url="+urllib.quote_plus(url)+"&mode="+str(mode)+"&name="+urllib.quote_plus(name)
        ok=True
        liz=xbmcgui.ListItem(name, iconImage="DefaultFolder.png", thumbnailImage=iconimage)
        ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=u,listitem=liz,isFolder=pasta)
        return ok

############################################################################################################
#                                               GET PARAMS                                                 #
############################################################################################################
              
def get_params():
        param=[]
        paramstring=sys.argv[2]
        if len(paramstring)>=2:
                params=sys.argv[2]
                cleanedparams=params.replace('?','')
                if (params[len(params)-1]=='/'):
                        params=params[0:len(params)-2]
                pairsofparams=cleanedparams.split('&')
                param={}
                for i in range(len(pairsofparams)):
                        splitparams={}
                        splitparams=pairsofparams[i].split('=')
                        if (len(splitparams))==2:
                                param[splitparams[0]]=splitparams[1]
                                
        return param

      
params=get_params()
url=None
name=None
mode=None
iconimage=None


try:
        url=urllib.unquote_plus(params["url"])
except:
        pass
try:
        name=urllib.unquote_plus(params["name"])
except:
        pass
try:
        mode=int(params["mode"])
except:
        pass

try:        
        iconimage=urllib.unquote_plus(params["iconimage"])
except:
        pass


print "Mode: "+str(mode)
print "URL: "+str(url)
print "Name: "+str(name)
print "Iconimage: "+str(iconimage)




###############################################################################################################
#                                                   MODOS                                                     #
###############################################################################################################


if mode==None or url==None or len(url)<1:
#	print ""
    CATEGORIES()

elif mode==1:
    print ""
    listar_filmes(url)

elif mode==2:
    print ""
    encontrar_fontes(url)

elif mode==3:
    print ""
    listar_series(url)

elif mode==4:
    print ""
    listar_episodios(url)

elif mode==5:
    print ""
    SUB_CAT_FILMES()

elif mode==6:
    print ""
    SUB_CAT_SERIES()

elif mode ==7:
    print""
    pesquisa_filmes()

elif mode ==8:
    print""
    pesquisa_series()

xbmcplugin.endOfDirectory(int(sys.argv[1]))