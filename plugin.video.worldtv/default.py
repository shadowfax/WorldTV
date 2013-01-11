import urllib,urllib2,re,xbmcplugin,xbmcgui

def COUNTRIES():
	addDir('Spain','','es_ES','')
	addDir('Ukraine','','uk_UA','')


def SPAIN():
	addLink('24H', 'rtmp://rtvefs.fplive.net:1935/rtve-live-live?ovpfv=2.1.2 playpath=RTVE_24H_LV3_WEB_NOG?aksessionid=1357891288814_961809', '')
	addLink('Bodegalia TV', 'rtmp://extondemand.livestream.com/ondemand playpath=trans/dv04/mogulus-user-files/chbodegaliatv/2010/01/30/043d6064-a205-4bd3-b2a1-19749cc3fd5c', '')
	addLink('Canal 33', 'rtmp://flash79.ustream.tv:1935/ustreamVideo/12050622 playpath=streams/live_1', '')
	addLink('Canal Vasco', 'rtmp://cp70268.live.edgefcs.net/live playpath=eitb-CanalVasco@5519', '')
	addLink('Cuatro', 'rtmp://esmediasetlivefs.fplive.net/esmediasetlive-live playpath=esmediaset12?token=c3RhcnRfdGltZT0yMDEzMDExMTExNDgzMCZlbmRfdGltZT0yMDEzMDExMTExNDg0NiZkaWdlc3Q9ZDNhY2NkMWU5OTUyZjE5YzdmMmZkOGUwYzJiNGFkMzA=', '')
	addLink('Euronews', 'rtmp://fr-par-1.stream-relay.hexaglobe.net:1935/rtpeuronewslive es_video150_flash_all.sdp', '')
	addLink('ETB SAT', 'rtmp://cp70268.live.edgefcs.net/live playpath=eitb-ETBSat@5219', '')
	addLink('IB3', 'rtmp://ib3tvlivefs.fplive.net/ib3tvlive-live playpath=streamib3', '')
	addLink('Intereconomia', 'rtmp://media.intereconomia.com/live playpath=intereconomiatv1', '')
	addLink('La Sexta', 'rtmp://antena3fms35livefs.fplive.net:1935/antena3fms35live-live playpath=stream-lasexta', '')
	addLink('TDP', 'rtmp://rtvegeofs.fplive.net:1935/rtvegeo-live-live?ovpfv=2.1.2 playpath=RTVE_TDP_LV3_WEB_GEO?aksessionid=1357891017538_156935', '')
	addLink('Telebilbao', 'rtmp://149.11.34.6/live playpath=telebilbao.stream', '')
	addLink('Telecinco', 'rtmp://esmediasetlivefs.fplive.net/esmediasetlive-live playpath=esmediaset31?token=c3RhcnRfdGltZT0yMDEzMDExMTExNDQ0OCZlbmRfdGltZT0yMDEzMDExMTExNDUwNCZkaWdlc3Q9ZmEzZGYyNjk2ZDJlYjMzNDUyNTVhOTM2Nzk2N2QzNDY=', '')
	addLink('Telemadrid Sat', 'rtmp://cp118140.live.edgefcs.net:1935/live?videoId=110032781001&lineUpId=&pubId=104403117001&playerId=111868723001&affiliateId= playpath=TSAtelemadridsat@47720', '')
	addLink('TV3 24', 'rtmp://tv-nogeo-flashlivefs.fplive.net:1935/tv-nogeo-flashlive-live/?ovpfv=1.1 playpath=stream_324_FLV?ua=Mozilla/5.0%20%28Windows%20NT%205.1%29%20AppleWebKit/537.11%20%28KHTML%2C%20like%20Gecko%29%20Chrome/23.0.1271.97%20Safari/537.11', '')
	addLink('TVE1', 'rtmp://cp68975.live.edgefcs.net:1935/live?ovpfv=2.1.2 playpath=LA1_AKA_WEB_NOG@58877?aksessionid=1357890489362_60103', '')
	addLink('TVE2', 'rtmp://cp68975.live.edgefcs.net:1935/live?ovpfv=2.1.2 playpath=LA2_AKA_WEB_NOG@60554?aksessionid=1357890865088_369124', '')


def UKRAINE():
	# ToDo: http://www.parom.tv/ -> Need session ID with regex
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
	addLink('GTRK Crimea TV', 'rtmp://mail.tv.crimea.ua/tv.crimea.com/tv.crimea.com', '')
	#addLink('ICTV', 'rtmp://95.67.65.136:1935/rtplive/ictv_m.stream', '')
	addLink('Inter','rtsp://212.40.43.10:1935/inters/_definst_/inter_2', '')
	addLink('K1','rtsp://212.40.43.10:1935/k1s/_definst_/k1_3','')
	#addLink('K2', 'rtmp://95.67.65.136:1935/rtplive/k2_m.stream', '')
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
