from Plugins.Extensions.MediaPortal.resources.imports import *
from Plugins.Extensions.MediaPortal.resources.myvideolink import MyvideoLink
from Plugins.Extensions.MediaPortal.resources.simpleplayer import SimplePlayer

def myVideoGenreListEntry(entry):
	return [entry,
		(eListboxPythonMultiContent.TYPE_TEXT, 20, 0, 900, 25, 0, RT_HALIGN_CENTER | RT_VALIGN_CENTER, entry[0])
		]

class myVideoGenreScreen(Screen):

	def __init__(self, session):
		self.session = session
		path = "/usr/lib/enigma2/python/Plugins/Extensions/MediaPortal/skins/%s/oldGenreScreen.xml" % config.mediaportal.skin.value
		if not fileExists(path):
			path = "/usr/lib/enigma2/python/Plugins/Extensions/MediaPortal/skins/original/oldGenreScreen.xml"
		print path
		with open(path, "r") as f:
			self.skin = f.read()
			f.close()

		Screen.__init__(self, session)

		self["actions"]  = ActionMap(["OkCancelActions", "ShortcutActions", "WizardActions", "ColorActions", "SetupActions", "NumberActions", "MenuActions"], {
			"ok"    : self.keyOK,
			"cancel": self.keyCancel
		}, -1)

		self['title'] = Label("MyVideo.de")
		self['name'] = Label("Genre Auswahl")
		self['coverArt'] = Pixmap()

		self.genreliste = []
		self.chooseMenuList = MenuList([], enableWrapAround=True, content=eListboxPythonMultiContent)
		self.chooseMenuList.l.setFont(0, gFont('mediaportal', 23))
		self.chooseMenuList.l.setItemHeight(25)
		self['genreList'] = self.chooseMenuList

		self.onLayoutFinish.append(self.layoutFinished)

	def layoutFinished(self):
		self.genreliste.append(("Alle Filme", "74594"))
		self.genreliste.append(("Comedy", "74588"))
		self.genreliste.append(("Drama", "74589"))
		self.genreliste.append(("Thriller", "74590"))
		self.genreliste.append(("Horror", "74591"))
		self.genreliste.append(("Action", "74592"))
		self.genreliste.append(("Sci-Fi", "74593"))
		self.genreliste.append(("Western", "75189"))
		self.genreliste.append(("Dokumentation", "76116"))
		self.genreliste.append(("Konzerte", "75833"))
		self.chooseMenuList.setList(map(myVideoGenreListEntry, self.genreliste))

	def keyOK(self):
		streamGenreLink = self['genreList'].getCurrent()[0][1]
		print streamGenreLink
		self.session.open(myVideoFilmScreen, streamGenreLink)

	def keyCancel(self):
		self.close()

def myVideoFilmListEntry(entry):
	return [entry,
		(eListboxPythonMultiContent.TYPE_TEXT, 20, 0, 900, 25, 0, RT_HALIGN_LEFT | RT_VALIGN_CENTER, entry[0])
		]

class myVideoFilmScreen(Screen):

	def __init__(self, session, myID):
		self.session = session
		self.myID = myID
		path = "/usr/lib/enigma2/python/Plugins/Extensions/MediaPortal/skins/%s/myVideoFilmScreen.xml" % config.mediaportal.skin.value
		if not fileExists(path):
			path = "/usr/lib/enigma2/python/Plugins/Extensions/MediaPortal/skins/original/myVideoFilmScreen.xml"
		print path
		with open(path, "r") as f:
			self.skin = f.read()
			f.close()

		Screen.__init__(self, session)

		self["actions"]  = ActionMap(["OkCancelActions", "ShortcutActions", "WizardActions", "ColorActions", "SetupActions", "NumberActions", "MenuActions", "EPGSelectActions"], {
			"ok"    : self.keyOK,
			"cancel": self.keyCancel,
			"up"    : self.keyUp,
			"down"  : self.keyDown,
			"left"  : self.keyLeft,
			"right" : self.keyRight,
			"nextBouquet" : self.keyPageUp,
			"prevBouquet" : self.keyPageDown
		}, -1)

		self.keyLocked = True
		self.page = 1
		self['title'] = Label("MyVideo.de")
		self['roflPic'] = Pixmap()
		self['name'] = Label("")
		self['page'] = Label("1")
		self['handlung'] = Label("")
		self.mvListe = []
		self.chooseMenuList = MenuList([], enableWrapAround=True, content=eListboxPythonMultiContent)
		self.chooseMenuList.l.setFont(0, gFont('mediaportal', 23))
		self.chooseMenuList.l.setItemHeight(25)
		self['roflList'] = self.chooseMenuList

		#self.GK = ('WXpnME1EZGhNRGhpTTJNM01XVmhOREU0WldNNVpHTTJOakpt'
		#	'TW1FMU5tVTBNR05pWkRaa05XRXhNVFJoWVRVd1ptSXhaVEV3'
		#	'TnpsbA0KTVRkbU1tSTRNdz09')

		self.onLayoutFinish.append(self.loadPage)

	def loadPage(self):
		self.keyLocked = True
		url = "http://www.myvideo.de/iframe.php?lpage=%s&function=mv_success_box&action=filme_video_list&searchGroup=%s&searchOrder=1" % (str(self.page), self.myID)
		print url
		getPage(url, headers={'Content-Type':'application/x-www-form-urlencoded'}).addCallback(self.loadPageData).addErrback(self.dataError)

	def loadPageData(self, data):
		mvVideo = re.findall("<div class='vThumb vViews'><a href='(.*?)' class='vLink' title='(.*?)'.*?src='(.*?.jpg)' class='vThumb' alt=''/><span class='vViews' id='.*?'>(.*?)</span></a></div><div class='clear'>.*?href='.*?' title='(.*?)'", data, re.S)
		if mvVideo:
			self.mvListe = []
			for (mvUrl,mvHandlung,mvImage,mvRuntime,mvTitle) in mvVideo:
				mvUrl = "http://www.myvideo.de" + mvUrl
				self.mvListe.append((decodeHtml(mvTitle), mvUrl, mvImage, decodeHtml(mvHandlung), mvRuntime))
			self.chooseMenuList.setList(map(myVideoFilmListEntry, self.mvListe))
			self.keyLocked = False
			self.showPic()

	def dataError(self, error):
		printl(error,self,"E")

	def showPic(self):
		myTitle = self['roflList'].getCurrent()[0][0]
		myPicLink = self['roflList'].getCurrent()[0][2]
		myHandlung = self['roflList'].getCurrent()[0][3]
		self['name'].setText(myTitle)
		self['page'].setText(str(self.page))
		self['handlung'].setText(myHandlung)
		downloadPage(myPicLink, "/tmp/myPic.jpg").addCallback(self.roflCoverShow)

	def roflCoverShow(self, data):
		if fileExists("/tmp/myPic.jpg"):
			self['roflPic'].instance.setPixmap(gPixmapPtr())
			self.scale = AVSwitch().getFramebufferScale()
			self.picload = ePicLoad()
			size = self['roflPic'].instance.size()
			self.picload.setPara((size.width(), size.height(), self.scale[0], self.scale[1], False, 1, "#FF000000"))
			if self.picload.startDecode("/tmp/myPic.jpg", 0, 0, False) == 0:
				ptr = self.picload.getData()
				if ptr != None:
					self['roflPic'].instance.setPixmap(ptr)
					self['roflPic'].show()
					del self.picload

	def keyPageDown(self):
		print "PageDown"
		if self.keyLocked:
			return
		if not self.page < 2:
			self.page -= 1
			self.loadPage()

	def keyPageUp(self):
		print "PageUP"
		if self.keyLocked:
			return
		self.page += 1
		self.loadPage()

	def keyLeft(self):
		if self.keyLocked:
			return
		self['roflList'].pageUp()
		self.showPic()

	def keyRight(self):
		if self.keyLocked:
			return
		self['roflList'].pageDown()
		self.showPic()

	def keyUp(self):
		if self.keyLocked:
			return
		self['roflList'].up()
		self.showPic()

	def keyDown(self):
		if self.keyLocked:
			return
		self['roflList'].down()
		self.showPic()

	def keyOK(self):
		if self.keyLocked:
			return
		mvUrl = self['roflList'].getCurrent()[0][1]
		print mvUrl
		id = re.findall('/watch/(.*?)/', mvUrl)
		if id:
			url = "http://www.myvideo.de/dynamic/get_player_video_xml.php?ID=" + id[0]
			kiTitle = self['roflList'].getCurrent()[0][0]
			imgurl = self['roflList'].getCurrent()[0][2]
			#MyvideoLink(self.session).getLink(self.playStream, self.dataError, kiTitle, url, id[0])

			self.session.open(MyvideoPlayer, [(kiTitle, url, id[0], imgurl)])

	def keyCancel(self):
		self.close()

class MyvideoPlayer(SimplePlayer):

	def __init__(self, session, playList):
		print "MyvideoPlayer:"

		SimplePlayer.__init__(self, session, playList, showPlaylist=False, ltype='myvideo', cover=True)

		self.onLayoutFinish.append(self.getVideo)

	def getVideo(self):
		titel = self.playList[self.playIdx][0]
		url = self.playList[self.playIdx][1]
		token = self.playList[self.playIdx][2]
		imgurl = self.playList[self.playIdx][3]
		print titel, url, token

		MyvideoLink(self.session).getLink(self.playStream, self.dataError, titel, url, token, imgurl=imgurl)