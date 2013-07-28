﻿#	-*-	coding:	utf-8	-*-

from Plugins.Extensions.MediaPortal.resources.imports import *
from Plugins.Extensions.MediaPortal.resources.simpleplayer import SimplePlayer
from Plugins.Extensions.MediaPortal.resources.coverhelper import CoverHelper

def bsListEntry(entry):
	return [entry,
		(eListboxPythonMultiContent.TYPE_TEXT, 20, 0, 860, 25, 0, RT_HALIGN_LEFT | RT_VALIGN_CENTER, entry[0])
		]
def bsListEntryMark(entry):
	if entry[2]:
		png = "/usr/lib/enigma2/python/Plugins/Extensions/MediaPortal/images/watched.png"
		watched = LoadPixmap(png)
		return [entry,
			(eListboxPythonMultiContent.TYPE_PIXMAP_ALPHATEST, 39, 3, 100, 22, watched),
			(eListboxPythonMultiContent.TYPE_TEXT, 100, 0, 700, 25, 0, RT_HALIGN_LEFT | RT_VALIGN_CENTER, entry[0])
			]
	else:
		return [entry,
			(eListboxPythonMultiContent.TYPE_TEXT, 100, 0, 700, 25, 0, RT_HALIGN_LEFT | RT_VALIGN_CENTER, entry[0])
			]
def mainListEntry(entry):
	return [entry,
		(eListboxPythonMultiContent.TYPE_TEXT, 20, 0, 860, 25, 0, RT_HALIGN_CENTER | RT_VALIGN_CENTER, entry[0])
		]

class bsMain(Screen, ConfigListScreen):
	def __init__(self, session):
		self.session = session
		path = "/usr/lib/enigma2/python/Plugins/Extensions/MediaPortal/skins/%s/bsMain.xml" % config.mediaportal.skin.value
		if not fileExists(path):
			path = "/usr/lib/enigma2/python/Plugins/Extensions/MediaPortal/skins/original/bsMain.xml"
		print path
		with open(path, "r") as f:
			self.skin = f.read()
			f.close()

		Screen.__init__(self, session)

		self["actions"]  = ActionMap(["OkCancelActions", "ShortcutActions", "EPGSelectActions", "WizardActions", "ColorActions", "NumberActions", "MenuActions", "MoviePlayerActions", "InfobarSeekActions"], {
			"ok"    : self.keyOK,
			"cancel": self.keyCancel
		}, -1)

		self['title'] = Label("Burning-seri.es")
		self['leftContentTitle'] = Label("M e n u")
		self['stationIcon'] = Pixmap()
		self['stationInfo'] = Label("")

		self.streamList = []
		self.streamMenuList = MenuList([], enableWrapAround=True, content=eListboxPythonMultiContent)
		self.streamMenuList.l.setFont(0, gFont('mediaportal', 23))
		self.streamMenuList.l.setItemHeight(25)
		self['streamlist'] = self.streamMenuList

		self.keyLocked = False
		self.onLayoutFinish.append(self.layoutFinished)

	def layoutFinished(self):
		self.keyLocked = True
		self.streamList.append(("Serien von A-Z","serien"))
		self.streamList.append(("Watchlist","watchlist"))
		self.streamMenuList.setList(map(mainListEntry, self.streamList))
		self.keyLocked = False

	def keyOK(self):
		exist = self['streamlist'].getCurrent()
		if self.keyLocked or exist == None:
			return

		auswahl = self['streamlist'].getCurrent()[0][1]
		if auswahl == "serien":
			self.session.open(bsSerien)
		else:
			self.session.open(bsWatchlist)

	def keyCancel(self):
		self.close()

class bsSerien(Screen, ConfigListScreen):
	def __init__(self, session):
		self.session = session
		path = "/usr/lib/enigma2/python/Plugins/Extensions/MediaPortal/skins/%s/bsSerien.xml" % config.mediaportal.skin.value
		if not fileExists(path):
			path = "/usr/lib/enigma2/python/Plugins/Extensions/MediaPortal/skins/original/bsSerien.xml"
		print path
		with open(path, "r") as f:
			self.skin = f.read()
			f.close()

		Screen.__init__(self, session)

		self["actions"]  = ActionMap(["OkCancelActions", "ShortcutActions", "EPGSelectActions", "WizardActions", "ColorActions", "NumberActions", "MenuActions", "MoviePlayerActions", "InfobarSeekActions"], {
			"ok"    : self.keyOK,
			"cancel": self.keyCancel,
			"green" : self.keyAdd
		}, -1)

		self['title'] = Label("Burning-seri.es")
		self['leftContentTitle'] = Label("Serien A-Z")
		self['stationIcon'] = Pixmap()

		self.streamList = []
		self.streamMenuList = MenuList([], enableWrapAround=True, content=eListboxPythonMultiContent)
		self.streamMenuList.l.setFont(0, gFont('mediaportal', 23))
		self.streamMenuList.l.setItemHeight(25)
		self['streamlist'] = self.streamMenuList

		self.keyLocked = True
		self.onLayoutFinish.append(self.loadPage)

	def loadPage(self):
		url = "http://www.burning-seri.es/serie-alphabet"
		getPage(url, headers={'Content-Type':'application/x-www-form-urlencoded'}).addCallback(self.parseData).addErrback(self.dataError)

	def parseData(self, data):
		serien_raw = re.findall('<ul id=\'serSeries\'>(.*?)</ul>', data, re.S)
		if serien_raw:
			serien = re.findall('<li><a.*?href="(.*?)">(.*?)</a></li>', serien_raw[0], re.S)
			if serien:
				for (bsUrl,bsTitle) in serien:
					bsUrl = "http://www.burning-seri.es/" + bsUrl
					self.streamList.append((decodeHtml(bsTitle),bsUrl))
					self.streamMenuList.setList(map(bsListEntry, self.streamList))
				self.keyLocked = False

	def dataError(self, error):
		printl(error,self,"E")

	def keyOK(self):
		exist = self['streamlist'].getCurrent()
		if self.keyLocked or exist == None:
			return

		serienTitle = self['streamlist'].getCurrent()[0][0]
		auswahl = self['streamlist'].getCurrent()[0][1]
		print auswahl
		self.session.open(bsStaffeln, auswahl, serienTitle)

	def keyAdd(self):
		exist = self['streamlist'].getCurrent()
		if self.keyLocked or exist == None:
			return
		muTitle = self['streamlist'].getCurrent()[0][0]
		muID = self['streamlist'].getCurrent()[0][1]

		if not fileExists(config.mediaportal.watchlistpath.value+"mp_bs_watchlist"):
			print "Erstelle Burning-Series Watchlist."
			os.system("touch "+config.mediaportal.watchlistpath.value+"mp_bs_watchlist")

		if fileExists(config.mediaportal.watchlistpath.value+"mp_bs_watchlist"):
			writePlaylist = open(config.mediaportal.watchlistpath.value+"mp_bs_watchlist","a")
			writePlaylist.write('"%s" "%s"\n' % (muTitle, muID))
			writePlaylist.close()
			message = self.session.open(MessageBox, _("Serie wurde zur watchlist hinzugefuegt."), MessageBox.TYPE_INFO, timeout=3)

	def keyCancel(self):
		self.close()

class bsWatchlist(Screen, ConfigListScreen):
	def __init__(self, session):
		self.session = session
		path = "/usr/lib/enigma2/python/Plugins/Extensions/MediaPortal/skins/%s/bsWatchlist.xml" % config.mediaportal.skin.value
		if not fileExists(path):
			path = "/usr/lib/enigma2/python/Plugins/Extensions/MediaPortal/skins/original/bsWatchlist.xml"
		print path
		with open(path, "r") as f:
			self.skin = f.read()
			f.close()

		Screen.__init__(self, session)

		self["actions"]  = ActionMap(["OkCancelActions", "ShortcutActions", "EPGSelectActions", "WizardActions", "ColorActions", "NumberActions", "MenuActions", "MoviePlayerActions", "InfobarSeekActions"], {
			"ok"    : self.keyOK,
			"cancel": self.keyCancel,
			"red" : self.keyDel
		}, -1)

		self['title'] = Label("Burning-seri.es")
		self['leftContentTitle'] = Label("Watchlist")
		self['stationIcon'] = Pixmap()
		self['handlung'] = Label("")

		self.streamList = []
		self.streamMenuList = MenuList([], enableWrapAround=True, content=eListboxPythonMultiContent)
		self.streamMenuList.l.setFont(0, gFont('mediaportal', 23))
		self.streamMenuList.l.setItemHeight(25)
		self['streamlist'] = self.streamMenuList

		self.keyLocked = True
		self.onLayoutFinish.append(self.loadPlaylist)

	def loadPlaylist(self):
		self.streamList = []

		if not fileExists(config.mediaportal.watchlistpath.value+"mp_bs_watchlist"):
			print "Erstelle Burning-Series Watchlist."
			os.system("touch "+config.mediaportal.watchlistpath.value+"mp_bs_watchlist")

		if fileExists(config.mediaportal.watchlistpath.value+"mp_bs_watchlist"):
			readStations = open(config.mediaportal.watchlistpath.value+"mp_bs_watchlist","r")
			for rawData in readStations.readlines():
				data = re.findall('"(.*?)" "(.*?)"', rawData, re.S)
				if data:
					(stationName, stationLink) = data[0]
					self.streamList.append((stationName, stationLink))
			print "Reload Playlist"
			self.streamList.sort()
			self.streamMenuList.setList(map(bsListEntry, self.streamList))
			readStations.close()
			self.keyLocked = False

	def keyOK(self):
		exist = self['streamlist'].getCurrent()
		if self.keyLocked or exist == None:
			return

		serienTitle = self['streamlist'].getCurrent()[0][0]
		auswahl = self['streamlist'].getCurrent()[0][1]
		print serienTitle, auswahl
		self.session.open(bsStaffeln, auswahl, serienTitle)

	def keyDel(self):
		exist = self['streamlist'].getCurrent()
		if self.keyLocked or exist == None:
			return

		selectedName = self['streamlist'].getCurrent()[0][0]
		writeTmp = open(config.mediaportal.watchlistpath.value+"mp_bs_watchlist.tmp","w")
		if fileExists(config.mediaportal.watchlistpath.value+"mp_bs_watchlist"):
			readStations = open(config.mediaportal.watchlistpath.value+"mp_bs_watchlist","r")
			for rawData in readStations.readlines():
				data = re.findall('"(.*?)" "(.*?)"', rawData, re.S)
				if data:
					(stationName, stationLink) = data[0]
					if stationName != selectedName:
						writeTmp.write('"%s" "%s"\n' % (stationName, stationLink))
			readStations.close()
			writeTmp.close()
			shutil.move(config.mediaportal.watchlistpath.value+"mp_bs_watchlist.tmp", config.mediaportal.watchlistpath.value+"mp_bs_watchlist")
			self.loadPlaylist()

	def keyCancel(self):
		self.close()

class bsStaffeln(Screen, ConfigListScreen):
	def __init__(self, session, serienUrl, serienTitle):
		self.session = session
		path = "/usr/lib/enigma2/python/Plugins/Extensions/MediaPortal/skins/%s/bsStreams.xml" % config.mediaportal.skin.value
		if not fileExists(path):
			path = "/usr/lib/enigma2/python/Plugins/Extensions/MediaPortal/skins/original/bsStreams.xml"
		print path
		with open(path, "r") as f:
			self.skin = f.read()
			f.close()

		self.serienUrl = serienUrl
		self.serienTitle = serienTitle
		Screen.__init__(self, session)

		self["actions"]  = ActionMap(["OkCancelActions", "ShortcutActions", "EPGSelectActions", "WizardActions", "ColorActions", "NumberActions", "MenuActions", "MoviePlayerActions", "InfobarSeekActions"], {
			"ok"    : self.keyOK,
			"cancel": self.keyCancel
		}, -1)

		self['title'] = Label("Burning-seri.es")
		self['leftContentTitle'] = Label("Staffel Auswahl")
		self['stationIcon'] = Pixmap()
		self['handlung'] = Label("")

		self.streamList = []
		self.streamMenuList = MenuList([], enableWrapAround=True, content=eListboxPythonMultiContent)
		self.streamMenuList.l.setFont(0, gFont('mediaportal', 23))
		self.streamMenuList.l.setItemHeight(25)
		self['streamlist'] = self.streamMenuList

		self.keyLocked = True
		self.onLayoutFinish.append(self.loadPage)

	def loadPage(self):
		print self.serienUrl
		getPage(self.serienUrl, headers={'Content-Type':'application/x-www-form-urlencoded'}).addCallback(self.parseData).addErrback(self.dataError)

	def parseData(self, data):
		details = re.findall('<strong>Beschreibung</strong>.*?<p>(.*?)</p>.*?<img\ssrc="(.*?)"\salt="Cover"\s{0,2}/>', data, re.S)
		staffeln_raw = re.findall('<ul class="pages">(.*?)</ul>', data, re.S)
		if staffeln_raw:
			staffeln = re.findall('<li class=".*?"><a.*?href="(serie/.*?)">(.*?)</a></li>', staffeln_raw[0], re.S)
			if staffeln:
				for (bsUrl,bsStaffel) in staffeln:
					bsUrl = "http://www.burning-seri.es/" + bsUrl
					bsStaffel = "Staffel %s" % bsStaffel
					bsStaffel = bsStaffel.replace('Staffel Film(e)','Film(e)')
					self.streamList.append((bsStaffel,bsUrl))
				self.streamMenuList.setList(map(bsListEntry, self.streamList))
				self.keyLocked = False
			if details:
				(handlung,cover) = details[0]
				self['handlung'].setText(decodeHtml(handlung))
				coverUrl = "http://www.burning-seri.es/" + cover
				print coverUrl
				CoverHelper(self['stationIcon']).getCover(coverUrl)

	def dataError(self, error):
		printl(error,self,"E")

	def keyOK(self):
		exist = self['streamlist'].getCurrent()
		if self.keyLocked or exist == None:
			return

		staffel = self['streamlist'].getCurrent()[0][0]
		staffel = staffel.replace('Staffel ','').replace('Film(e)','0')
		auswahl = self['streamlist'].getCurrent()[0][1]
		print auswahl, staffel
		self.session.open(bsEpisoden, auswahl, staffel, self.serienTitle)

	def keyCancel(self):
		self.close()

class bsEpisoden(Screen, ConfigListScreen):
	def __init__(self, session, serienUrl, bsStaffel, serienTitle):
		self.session = session
		path = "/usr/lib/enigma2/python/Plugins/Extensions/MediaPortal/skins/%s/bsStreams.xml" % config.mediaportal.skin.value
		if not fileExists(path):
			path = "/usr/lib/enigma2/python/Plugins/Extensions/MediaPortal/skins/original/bsStreams.xml"
		print path
		with open(path, "r") as f:
			self.skin = f.read()
			f.close()

		self.serienUrl = serienUrl
		self.bsStaffel = bsStaffel
		self.serienTitle = serienTitle
		Screen.__init__(self, session)

		self["actions"]  = ActionMap(["OkCancelActions", "ShortcutActions", "EPGSelectActions", "WizardActions", "ColorActions", "NumberActions", "MenuActions", "MoviePlayerActions", "InfobarSeekActions"], {
			"ok"    : self.keyOK,
			"cancel": self.keyCancel
		}, -1)

		self['title'] = Label("Burning-seri.es")
		self['leftContentTitle'] = Label("Episoden Auswahl")
		self['stationIcon'] = Pixmap()
		self['handlung'] = Label("")

		self.streamList = []
		self.streamMenuList = MenuList([], enableWrapAround=True, content=eListboxPythonMultiContent)
		self.streamMenuList.l.setFont(0, gFont('mediaportal', 23))
		self.streamMenuList.l.setItemHeight(25)
		self['streamlist'] = self.streamMenuList

		self.keyLocked = True
		self.onLayoutFinish.append(self.loadPage)

	def loadPage(self):
		print self.serienUrl
		getPage(self.serienUrl, headers={'Content-Type':'application/x-www-form-urlencoded'}).addCallback(self.parseData).addErrback(self.dataError)

	def parseData(self, data):

		# Mark Watches episodes
		self.watched_liste = []
		self.mark_last_watched = []
		if not fileExists(config.mediaportal.watchlistpath.value+"mp_bs_watched"):
			os.system("touch "+config.mediaportal.watchlistpath.value+"mp_bs_watched")
		if fileExists(config.mediaportal.watchlistpath.value+"mp_bs_watched"):
			leer = os.path.getsize(config.mediaportal.watchlistpath.value+"mp_bs_watched")
			if not leer == 0:
				self.updates_read = open(config.mediaportal.watchlistpath.value+"mp_bs_watched" , "r")
				for lines in sorted(self.updates_read.readlines()):
					line = re.findall('"(.*?)"', lines)
					if line:
						self.watched_liste.append("%s" % (line[0]))
				self.updates_read.close()

		episoden = re.findall('<tr>.*?<td>(\d+)</td>.*?<td><a href="(serie/.*?)">', data, re.S)
		details = re.findall('<strong>Beschreibung</strong>.*?<p>(.*?)</p>.*?<img\ssrc="(.*?)"\salt="Cover"\s{0,2}/>', data, re.S)
		bsStaffel2 = self.bsStaffel
		if int(bsStaffel2) < 10:
			bsStaffel3 = "S0"+str(bsStaffel2)
		else:
			bsStaffel3 = "S"+str(bsStaffel2)
		if episoden:
			for (bsEpisode,bsUrl) in episoden:
				bsTitle = re.findall('/\d+/\d+-(.*[0-9a-z]+)', bsUrl, re.S|re.I)
				bsUrl = "http://www.burning-seri.es/" + bsUrl
				if int(bsEpisode) < 10:
					bsEpisode2 = "E0"+str(bsEpisode)
				else:
					bsEpisode2 = "E"+str(bsEpisode)
				bsEpisode = "%s%s - %s" % (bsStaffel3, bsEpisode2, decodeHtml(bsTitle[0].replace('_',' ').replace('-',' ')))

				checkname = self.serienTitle+" - "+bsEpisode
				if checkname in self.watched_liste:
					self.streamList.append((bsEpisode,bsUrl,True))
				else:
					self.streamList.append((bsEpisode,bsUrl,False))
			self.streamMenuList.setList(map(bsListEntryMark, self.streamList))
			self.keyLocked = False
		if details:
			(handlung,cover) = details[0]
			self['handlung'].setText(decodeHtml(handlung))
			coverUrl = "http://www.burning-seri.es/" + cover
			print coverUrl
			CoverHelper(self['stationIcon']).getCover(coverUrl)

	def dataError(self, error):
		printl(error,self,"E")

	def keyOK(self):
		exist = self['streamlist'].getCurrent()
		if self.keyLocked or exist == None:
			return

		auswahl = self['streamlist'].getCurrent()[0][1]
		title = self['streamlist'].getCurrent()[0][0]
		print auswahl
		self.session.open(bsStreams, auswahl, self.serienTitle+" - "+title)

	def keyCancel(self):
		self.close()

class bsStreams(Screen, ConfigListScreen):

	def __init__(self, session, serienUrl, title):
		self.session = session
		path = "/usr/lib/enigma2/python/Plugins/Extensions/MediaPortal/skins/%s/bsStreams.xml" % config.mediaportal.skin.value
		if not fileExists(path):
			path = "/usr/lib/enigma2/python/Plugins/Extensions/MediaPortal/skins/original/bsStreams.xml"
		print path
		with open(path, "r") as f:
			self.skin = f.read()
			f.close()

		self.serienUrl = serienUrl
		self.streamname = title
		Screen.__init__(self, session)

		self["actions"]  = ActionMap(["OkCancelActions", "ShortcutActions", "EPGSelectActions", "WizardActions", "ColorActions", "NumberActions", "MenuActions", "MoviePlayerActions", "InfobarSeekActions"], {
			"ok"    : self.keyOK,
			"cancel": self.keyCancel
		}, -1)

		self['title'] = Label("Burning-seri.es")
		self['leftContentTitle'] = Label("Stream Auswahl")
		self['stationIcon'] = Pixmap()
		self['handlung'] = Label("")

		self.coverUrl = None
		self.streamList = []
		self.streamMenuList = MenuList([], enableWrapAround=True, content=eListboxPythonMultiContent)
		self.streamMenuList.l.setFont(0, gFont('mediaportal', 23))
		self.streamMenuList.l.setItemHeight(25)
		self['streamlist'] = self.streamMenuList
		self.keyLocked = True
		self.onLayoutFinish.append(self.loadPage)

	def loadPage(self):
		print self.serienUrl
		getPage(self.serienUrl, headers={'Content-Type':'application/x-www-form-urlencoded'}).addCallback(self.parseData).addErrback(self.dataError)

	def parseData(self, data):
		raw =  re.findall('<h3>Hoster dieser Episode</h3>(.*?)</ul>', data, re.S)
		if raw:
			streams = re.findall('<li><a.*?href="(serie/.*?)"><span.*?class="icon.(.*?)"></span>',raw[0],re.S)
			if streams:
				for (bsUrl,bsStream) in streams:
					bsUrl = "http://www.burning-seri.es/" + bsUrl
					if re.match('.*?(Ecostream|Sockshare|Streamcloud|Putlocker|Filenuke|MovShare|Novamov|DivxStage|UploadC|NowVideo|VideoWeed|FileNuke|BitShare|putme|limevideo|stream2k|played|putlocker|sockshare|streamclou|xvidstage|filenuke|movreel|nowvideo|xvidstream|uploadc|vreer|MonsterUploads|Novamov|Videoweed|Divxstage|Ginbig|Flashstrea|Movshare|yesload|faststream|Vidstream|PrimeShare|flashx|Divxmov|Zooupload|Wupfile|BitShare|Userporn)',bsStream,re.I):
						self.streamList.append((bsStream,bsUrl))
				self.streamMenuList.setList(map(bsListEntry, self.streamList))
				self.keyLocked = False

		details = re.findall('id="desc_spoiler">\s{0,10}(.*?)</div>.*?<img\ssrc="(.*?)"\salt="Cover"\s{0,2}/>', data, re.S)
		if details:
			(handlung,cover) = details[0]
			self['handlung'].setText(decodeHtml(handlung))
			self.coverUrl = "http://www.burning-seri.es/" + cover
			print self.coverUrl
			CoverHelper(self['stationIcon']).getCover(self.coverUrl)

	def dataError(self, error):
		printl(error,self,"E")

	def keyOK(self):
		exist = self['streamlist'].getCurrent()
		if self.keyLocked or exist == None:
			return

		auswahl = self['streamlist'].getCurrent()[0][1]
		print auswahl
		getPage(auswahl, headers={'Content-Type':'application/x-www-form-urlencoded'}).addCallback(self.findStream).addErrback(self.dataError)

	def playfile(self, link):
		print link
		if not fileExists(config.mediaportal.watchlistpath.value+"mp_bs_watched"):
			os.system("touch "+config.mediaportal.watchlistpath.value+"mp_bs_watched")

		self.update_liste = []
		leer = os.path.getsize(config.mediaportal.watchlistpath.value+"mp_bs_watched")
		if not leer == 0:
			self.updates_read = open(config.mediaportal.watchlistpath.value+"mp_bs_watched" , "r")
			for lines in sorted(self.updates_read.readlines()):
				line = re.findall('"(.*?)"', lines)
				if line:
					print line[0]
					self.update_liste.append("%s" % (line[0]))
			self.updates_read.close()

			updates_read2 = open(config.mediaportal.watchlistpath.value+"mp_bs_watched" , "a")
			check = ("%s" % self.streamname)
			if not check in self.update_liste:
				print "update add: %s" % (self.streamname)
				updates_read2.write('"%s"\n' % (self.streamname))
				updates_read2.close()
			else:
				print "dupe %s" % (self.streamname)
		else:
			updates_read3 = open(config.mediaportal.watchlistpath.value+"mp_bs_watched" , "a")
			print "update add: %s" % (self.streamname)
			updates_read3.write('"%s"\n' % (self.streamname))
			updates_read3.close()

		self.session.open(SimplePlayer, [(self.streamname, link, self.coverUrl)], showPlaylist=False, ltype='burningseries', cover=True)

	def findStream(self, data):
		if re.match(".*?<iframe.*?src=",data, re.S|re.I):
			test = re.findall('<iframe.*?src=["|\'](http://.*?)["|\']', data, re.S|re.I)
		else:
			test = re.findall('<a target=["|\']_blank["|\'] href=["|\'](http://.*?)["|\']', data, re.S|re.I)
		print test

		get_stream_link(self.session).check_link(test[0], self.got_link, False)

	def got_link(self, stream_url):
		if stream_url == None:
			message = self.session.open(MessageBox, _("Stream not found, try another Stream Hoster."), MessageBox.TYPE_INFO, timeout=3)
		else:
			self.playfile(stream_url.replace('&amp;','&'))

	def keyCancel(self):
		self.close()
