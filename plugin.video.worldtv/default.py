import urllib,urllib2,re,xbmcplugin,xbmcgui

def COUNTRIES():
	addDir('Spain','','es_ES','')
	addDir('Ukraine','','uk_UA','')


def SPAIN():
	addLink('Intereconomia', 'mms://www.intereconomia.com/INTERECONOMIA-TV', '')

def UKRAINE():
	#addLink('1 Auto', 'rtmp://ua.parom.tv:1935/stream/stream110', '')
	addLink('1 TV (Pershiy)','rtsp://212.40.43.10:1935/ut1s/_definst_/ut1_2','')
	#addLink('1+1', 'rtmp://95.67.65.135:1935/rtplive/1plus1_m.stream', '')
	addLink('11 Kanal', 'rtmp://212.3.106.230/live/livestream', '')
	#addLink('2+2', 'rtmp://95.67.65.136:1935/rtplive/2plus2_m.stream', '')
	addLink('24 TV','rtmp://stream1.luxnet.ua/news24 playpath=mp4:news24_source.stream pageurl=http://24tv.ua/home/showOnline.do','')
	#addLink('5 Kanal', 'rtmp://95.67.65.135:1935/rtplive/5kanal_m.stream', '')
	addLink('5 Kanal', 'rtmpt://media.5.ua:8080/tv/5tv/5tv1', '')
	#addLink('5 TV', 'rtmpt://media.5.ua:8080/tv/5tv','')
	#addLink('A One', 'rtmp://ua.parom.tv:1935/stream/stream113', '')
	addLink('ATR','rtmp://80.245.113.12/live/atr.stream','')
	#addLink('Che-Pe Info', 'rtmp://95.67.65.135:1935/rtplive/chpinfo_m.stream', '')
	#addLink('Citi', 'rtmp://95.67.65.135:1935/rtplive/citi_m.stream', '')
	#addLink('UNKNOWN', 'rtmp://host6.jampo.com.ua/stream/ukraine', '')
	addLink('Euronews', 'rtmp://fr-par-1.stream-relay.hexaglobe.net:1935/rtpeuronewslive/ua_video750_flash_all.sdp pageurl=http://ua.euronews.com/news/streaming-live/ swfurl=http://ua.euronews.com/media/player_live_1_14.swf', '')
	#addLink('Futbol', 'rtmp://95.67.65.135:1935/rtplive/futball_m.stream', '')
	addLink('GTRK Crimea', 'rtmp://mail.tv.crimea.ua/tv.crimea.com/tv.crimea.com', '')
	#addLink('ICTV', 'rtmp://95.67.65.136:1935/rtplive/ictv_m.stream', '')
	addLink('Inter','rtsp://212.40.43.10:1935/inters/_definst_/inter_2', '')
	addLink('K1','rtsp://212.40.43.10:1935/k1s/_definst_/k1_3','')
	#addLink('K2', 'rtmp://95.67.65.136:1935/rtplive/k2_m.stream', '')
	#addLink('Magnolia TV', 'rtmpe://lb1.itcons.net.ua/magnolias-redir/magnolia_3', '')
	addLink('Magnolia','rtsp://212.40.43.10:1935/magnolias/_definst_/magnolia_3', '')
	#addLink('M1', 'rtmp://95.67.65.135:1935/rtplive/m1_m.stream', '')
	#addLink('M2', 'rtmp://95.67.65.135:1935/rtplive/m2_m.stream', '')
	#addLink('Mega', 'rtmp://95.67.65.135:1935/rtplive/mega_m.stream', '')
	#addLink('MTV', 'rtmp://95.67.65.136:1935/rtplive/mtvua_m.stream', '')
	#addLink('Music Box', 'rtmp://ua.parom.tv:1935/stream/stream35', '')
	addLink('NTN', 'rtsp://212.40.43.10:1935/ntns/_definst_/ntn_3', '')
	addLink('Novy TV', 'rtmp://212.3.106.230/live/livestream', '')
	#addLink('Novyi TV #2', 'rtmp://95.67.65.135:1935/rtplive/novyi_m.stream', '')
	#addLink('OK', 'rtmp://95.67.65.136:1935/rtplive/ok_m.stream', '')
	#addLink('OTV', 'rtmp://95.67.65.135:1935/rtplive/otv_m.stream', '')
	#addLink('Pershiy Avtomobilniy', 'rtmp://95.215.2.55/live/1autotv1', '')
	#addLink('Pershiy Nacionalniy', 'rtmp://95.67.65.135:1935/rtplive/ut1_m.stream', '')
	#addLink('QTV', 'rtmp://95.67.65.135:1935/rtplive/qtv_m.stream', '')
	#addLink('RADA', 'rtmp://95.67.65.136:1935/rtplive/rada_m.stream', '')
	#addLink('RU Music', 'rtmp://ua.parom.tv:1935/stream/stream112', '')
	#addLink('Sport 1', 'rtmp://46.164.134.74/sport1/_definst_/sport10.stream', '')
	#addLink('Sport 1 #2', 'rtmp://109.68.40.67/sport1/_definst_/sport10.stream', '')
	#addLink('Sport 2', 'rtmp://46.164.134.74/sport1/_definst_/sport20.stream', '')
	#addLink('Star Music', 'rtmp://ua.parom.tv:1935/stream/stream114', '')
	#addLink('STB', 'rtmp://95.67.65.136:1935/rtplive/stb_m.stream', '')
	#addLink('TET', 'rtmp://95.67.65.136:1935/rtplive/tet_m.stream', '')
	#addLink('Tisa 1', 'rtmp://194.44.6.162/live1/live2', '')
	#addLink('TRK Kiev', 'rtmp://95.67.65.136:1935/rtplive/trkkyiv_m.stream', '')
	#addLink('TVI', 'rtmp://ua.parom.tv:1935/stream/stream106', '')
	#addLink('TV1','rtmpe://lb1.itcons.net.ua/ut1s-redir/ut1_2','')
	#addLink('UBR', 'rtmpt://31.28.170.69:80/live/ubr/livestream', '')
	#addLink('Ukraine','rtmpt://lb.tchkcdn.com/ukr_lo-redir/vlc_ukr_hi.sdp','')
	addLink('ZIK','rtmp://cdmatv.wnet.ua:80/live/zik288.stream','')



def addDir(name, url, mode, iconimage=''):
	u=sys.argv[0]+"?url="+urllib.quote_plus(url)+"&mode="+urllib.quote_plus(mode)+"&name="+urllib.quote_plus(name)
        ok=True
	liz=xbmcgui.ListItem(name, iconImage="DefaultFolder.png", thumbnailImage=iconimage)
	liz.setInfo( type="Video", infoLabels={ "Title": name } )
	ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=u,listitem=liz,isFolder=True)
        return ok


def addLink(name,url,iconimage):
	ok=True
	liz=xbmcgui.ListItem(name, iconImage="DefaultVideo.png", thumbnailImage=iconimage)
	liz.setInfo( type="Video", infoLabels={ "Title": name } )
	ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=url,listitem=liz)
	return ok


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

try:
	url=urllib.unquote_plus(params["url"])
except:
	pass

try:
	name=urllib.unquote_plus(params["name"])
except:
	pass

try:
	mode=urllib.unquote_plus(params["mode"])
except:
	pass



print "Mode: "+str(mode)
print "Name: "+str(name)
print "URL: "+str(url)


if mode==None:
	COUNTRIES()
	xbmcplugin.endOfDirectory(int(sys.argv[1]))
elif mode=='es_ES':
	SPAIN()
elif mode=='uk_UA':
	UKRAINE()

xbmcplugin.endOfDirectory(int(sys.argv[1]))
