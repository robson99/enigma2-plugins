from Plugins.Extensions.MediaPortal.resources.imports import *
from Plugins.Extensions.MediaPortal.resources.simpleplayer import SimplePlayer

def xhamsterGenreListEntry(entry):
	return [entry,
		(eListboxPythonMultiContent.TYPE_TEXT, 20, 0, 900, 25, 0, RT_HALIGN_CENTER | RT_VALIGN_CENTER, entry[0])
		]

def xhamsterstreamListEntry(entry):
	return [entry,
		(eListboxPythonMultiContent.TYPE_TEXT, 20, 0, 900, 25, 0, RT_HALIGN_LEFT | RT_VALIGN_CENTER, entry[0])
		]

class xhamsterGenreScreen(Screen):

	def __init__(self, session):
		self.session = session
		path = "/usr/lib/enigma2/python/Plugins/Extensions/MediaPortal/skins/%s/XXXGenreScreen.xml" % config.mediaportal.skin.value
		if not fileExists(path):
			path = "/usr/lib/enigma2/python/Plugins/Extensions/MediaPortal/skins/original/XXXGenreScreen.xml"
		print path
		with open(path, "r") as f:
			self.skin = f.read()
			f.close()

		Screen.__init__(self, session)

		self["actions"]  = ActionMap(["OkCancelActions", "ShortcutActions", "WizardActions", "ColorActions", "SetupActions", "NumberActions", "MenuActions"], {
			"ok" : self.keyOK,
			"cancel" : self.keyCancel,
			"up" : self.keyUp,
			"down" : self.keyDown,
			"right" : self.keyRight,
			"left" : self.keyLeft
		}, -1)

		self['title'] = Label("xHamster.com")
		self['name'] = Label("Genre Auswahl")
		self['coverArt'] = Pixmap()
		self.keyLocked = True
		self.suchString = ''

		self.genreliste = []
		self.chooseMenuList = MenuList([], enableWrapAround=True, content=eListboxPythonMultiContent)
		self.chooseMenuList.l.setFont(0, gFont('mediaportal', 23))
		self.chooseMenuList.l.setItemHeight(25)
		self['genreList'] = self.chooseMenuList

		self.onLayoutFinish.append(self.layoutFinished)

	def layoutFinished(self):
		self.keyLocked = True
		url = "http://xhamster.com/channels.php"
		getPage(url, headers={'Cookie': 'videoFilters=%7B%22channels%22%3A%22%3B0%22%7D', 'Content-Type':'application/x-www-form-urlencoded'}).addCallback(self.genreData).addErrback(self.dataError)

	def genreData(self, data):
		parse = re.search('title">Straight</div>(.*?)iconTrans"></div>', data, re.S)
		phCats = re.findall('<a\sclass="btnBig"\shref="(.*?)1.html">.*?\n\s\s+([a-z].*?)</a>', parse.group(1), re.S|re.I)
		if phCats:
			for (phUrl, phTitle) in phCats:
				phTitle = phTitle.strip(' ')
				self.genreliste.append((phTitle, phUrl))
			self.genreliste.sort()
			self.genreliste.insert(0, ("Newest", 'http://xhamster.com/new/'))
			self.genreliste.insert(0, ("--- Search ---", "callSuchen"))
			self.chooseMenuList.setList(map(xhamsterGenreListEntry, self.genreliste))
			self.chooseMenuList.moveToIndex(0)
			self.keyLocked = False

	def dataError(self, error):
		printl(error,self,"E")

	def keyOK(self):
		if self.keyLocked:
			return
		streamGenreName = self['genreList'].getCurrent()[0][0]
		if streamGenreName == "--- Search ---":
			self.suchen()

		else:
			streamGenreLink = self['genreList'].getCurrent()[0][1]
			self.session.open(xhamsterFilmScreen, streamGenreLink, streamGenreName)

	def suchen(self):
		self.session.openWithCallback(self.SuchenCallback, VirtualKeyBoard, title = (_("Suchkriterium eingeben")), text = self.suchString)

	def SuchenCallback(self, callback = None, entry = None):
		if callback is not None and len(callback):
			self.suchString = callback.replace(' ', '+')
			streamGenreLink = '%s' % (self.suchString)
			streamGenreName = "--- Search ---"
			self.session.open(xhamsterFilmScreen, streamGenreLink, streamGenreName)

	def keyLeft(self):
		if self.keyLocked:
			return
		self['genreList'].pageUp()

	def keyRight(self):
		if self.keyLocked:
			return
		self['genreList'].pageDown()

	def keyUp(self):
		if self.keyLocked:
			return
		self['genreList'].up()

	def keyDown(self):
		if self.keyLocked:
			return
		self['genreList'].down()

	def keyCancel(self):
		self.close()

class xhamsterFilmScreen(Screen):

	def __init__(self, session, genreLink, phCatName):
		self.session = session
		self.genreLink = genreLink
		self.phCatName = phCatName
		path = "/usr/lib/enigma2/python/Plugins/Extensions/MediaPortal/skins/%s/XXXFilmScreen.xml" % config.mediaportal.skin.value
		if not fileExists(path):
			path = "/usr/lib/enigma2/python/Plugins/Extensions/MediaPortal/skins/original/XXXFilmScreen.xml"
		print path
		with open(path, "r") as f:
			self.skin = f.read()
			f.close()

		Screen.__init__(self, session)

		self["actions"]  = ActionMap(["OkCancelActions", "ShortcutActions", "WizardActions", "ColorActions", "SetupActions", "NumberActions", "MenuActions", "EPGSelectActions"], {
			"ok" : self.keyOK,
			"cancel" : self.keyCancel,
			"up" : self.keyUp,
			"down" : self.keyDown,
			"right" : self.keyRight,
			"left" : self.keyLeft,
			"nextBouquet" : self.keyPageUp,
			"prevBouquet" : self.keyPageDown,
			"green" : self.keyPageNumber
		}, -1)

		self['title'] = Label("xHamster.com")
		self['name'] = Label("Film Auswahl")
		self['views'] = Label("")
		self['runtime'] = Label("")
		self['page'] = Label("")
		self['coverArt'] = Pixmap()
		self.keyLocked = True
		self.page = 1
		self.lastpage = 1

		self.streamList = []
		self.streamMenuList = MenuList([], enableWrapAround=True, content=eListboxPythonMultiContent)
		self.streamMenuList.l.setFont(0, gFont('mediaportal', 23))
		self.streamMenuList.l.setItemHeight(25)
		self['genreList'] = self.streamMenuList

		self.onLayoutFinish.append(self.loadpage)

	def loadpage(self):
		self.keyLocked = True
		self['name'].setText('Bitte warten...')
		self.streamList = []
		if self.phCatName == "--- Search ---":
			url = "http://www.xhamster.com/search.php?q=%s&qcat=video&page=%s" % (self.genreLink, str(self.page))
		else:
			url = "%s%s.html" % (self.genreLink, str(self.page))
		print url
		getPage(url, headers={'Cookie': 'videoFilters=%7B%22channels%22%3A%22%3B0%22%7D', 'Content-Type':'application/x-www-form-urlencoded'}).addCallback(self.pageData).addErrback(self.dataError)

	def pageData(self, data):
		lastpparse = re.search('class=\'pager\'>(.*)</div>', data, re.S)
		lastp = re.search('href=.*>(.*[0-9])<.*?', lastpparse.group(1), re.S)
		if lastp:
			lastp = lastp.group(1)
			print lastp
			self.lastpage = int(lastp)
		else:
			self.lastpage = 1
		self['page'].setText(str(self.page) + ' / ' + str(self.lastpage))
		if re.search('vDate', data, re.S):
			parse = re.search('<div\sclass=\'vDate(.*)</html>', data, re.S)
		else:
			parse = re.search('<html>(.*)</html>', data, re.S)
		xhListe = re.findall('class=\'video\'><a\shref=\'(.*?/movies/.*?)\'.*?class=\'hRotator\'\s><img\ssrc=\'(.*?)\'.*?alt="(.*?)".*?start2.*?<b>(.*?)</b>', parse.group(1), re.S)
		if xhListe:
			for (xhLink, xhImage, xhName, xhRuntime) in xhListe:
				self.streamList.append((decodeHtml(xhName), xhImage, xhLink, xhRuntime))
			self.streamMenuList.setList(map(xhamsterstreamListEntry, self.streamList))
			self.streamMenuList.moveToIndex(0)
			self.keyLocked = False
			self.showInfos()

	def showInfos(self):
		ptTitle = self['genreList'].getCurrent()[0][0]
		ptImage = self['genreList'].getCurrent()[0][1]
		ptRuntime = self['genreList'].getCurrent()[0][3]
		self.ptRead(ptImage)
		self['name'].setText(ptTitle)
		self['runtime'].setText(ptRuntime)

	def ptRead(self, stationIconLink):
		downloadPage(stationIconLink, "/tmp/xhIcon.jpg").addCallback(self.ptCoverShow)

	def ptCoverShow(self, picData):
		if fileExists("/tmp/xhIcon.jpg"):
			self['coverArt'].instance.setPixmap(gPixmapPtr())
			self.scale = AVSwitch().getFramebufferScale()
			self.picload = ePicLoad()
			size = self['coverArt'].instance.size()
			self.picload.setPara((size.width(), size.height(), self.scale[0], self.scale[1], False, 1, "#FF000000"))
			if self.picload.startDecode("/tmp/xhIcon.jpg", 0, 0, False) == 0:
				ptr = self.picload.getData()
				if ptr != None:
					self['coverArt'].instance.setPixmap(ptr)
					self['coverArt'].show()
					del self.picload

	def dataError(self, error):
		printl(error,self,"E")

	def keyOK(self):
		if self.keyLocked:
			return
		xhLink = self['genreList'].getCurrent()[0][2]
		print xhLink
		getPage(xhLink, headers={'Cookie': 'videoFilters=%7B%22channels%22%3A%22%3B0%22%7D', 'Content-Type':'application/x-www-form-urlencoded'}).addCallback(self.playData).addErrback(self.dataError)

	def playData(self, data):
		xhTitle = self['genreList'].getCurrent()[0][0]
		xhServer = re.findall("'srv': '(.*?)'", data)
		xhFile = re.findall("'file': '(.*?)'", data)
		if re.match('.*?http%3A', xhFile[0]):
			xhStream = urllib2.unquote(xhFile[0])
			print xhStream
		else:
			xhStream = xhServer[0]+"/key="+xhFile[0]
			print xhStream

		if xhStream:
			self.session.open(SimplePlayer, [(xhTitle, xhStream)], showPlaylist=False, ltype='xhamster')

	def keyPageNumber(self):
		self.session.openWithCallback(self.callbackkeyPageNumber, VirtualKeyBoard, title = (_("Seitennummer eingeben")), text = str(self.page))

	def callbackkeyPageNumber(self, answer):
		if answer is not None:
			answer = re.findall('\d+', answer)
		else:
			return
		if answer:
			if int(answer[0]) < self.lastpage + 1:
				self.page = int(answer[0])
				self.loadpage()
			else:
				self.page = self.lastpage
				self.loadpage()

	def keyPageDown(self):
		print "PageDown"
		if self.keyLocked:
			return
		if not self.page < 2:
			self.page -= 1
			self.loadpage()

	def keyPageUp(self):
		print "PageUP"
		if self.keyLocked:
			return
		if self.page < self.lastpage:
			self.page += 1
			self.loadpage()

	def keyLeft(self):
		if self.keyLocked:
			return
		self['genreList'].pageUp()
		self.showInfos()

	def keyRight(self):
		if self.keyLocked:
			return
		self['genreList'].pageDown()
		self.showInfos()

	def keyUp(self):
		if self.keyLocked:
			return
		self['genreList'].up()
		self.showInfos()

	def keyDown(self):
		if self.keyLocked:
			return
		self['genreList'].down()
		self.showInfos()

	def keyCancel(self):
		self.close()