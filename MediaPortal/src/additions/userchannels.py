﻿#	-*-	coding:	utf-8	-*-

from os.path import exists
from Plugins.Extensions.MediaPortal.resources.imports import *
from Plugins.Extensions.MediaPortal.resources.youtubeplayer import YoutubePlayer
from Plugins.Extensions.MediaPortal.resources.coverhelper import CoverHelper

USER_Version = "USER-Channels v0.96"

USER_siteEncoding = 'utf-8'

def show_USER_GenreListEntry(entry):
	return [entry,
		(eListboxPythonMultiContent.TYPE_TEXT, 20, 0, 860, 25, 0, RT_HALIGN_CENTER | RT_VALIGN_CENTER, entry[1])
		]

def show_USER_GenreListEntry2(entry):
	return [entry,
		(eListboxPythonMultiContent.TYPE_TEXT, 50, 0, 830, 25, 0, RT_HALIGN_LEFT | RT_VALIGN_CENTER, entry[1])
		]

class show_USER_Genre(Screen):

	def __init__(self, session):
		self.session = session

		self.plugin_path = mp_globals.pluginPath
		self.skin_path =  mp_globals.pluginPath + "/skins"

		path = "%s/%s/defaultGenreScreen.xml" % (self.skin_path, config.mediaportal.skin.value)
		if not fileExists(path):
			path = self.skin_path + "/original/defaultGenreScreen.xml"

		print path
		with open(path, "r") as f:
			self.skin = f.read()
			f.close()

		Screen.__init__(self, session)

		self["actions"]  = ActionMap(["OkCancelActions", "ShortcutActions", "WizardActions", "ColorActions", "SetupActions", "NumberActions", "MenuActions"], {
			"ok"    : self.keyOK,
			"cancel": self.keyCancel,
			"green"	: self.keyGreen
		}, -1)


		self['title'] = Label(USER_Version)
		self['ContentTitle'] = Label("Channel Auswahl")
		self['name'] = Label("")
		self['F1'] = Label("")
		self['F2'] = Label("Load")
		self['F3'] = Label("")
		self['F4'] = Label("")

		self.user_path = config.mediaportal.watchlistpath.value + "mp_userchan.xml"
		self.keyLocked = True
		self.genreliste = []
		self.chooseMenuList = MenuList([], enableWrapAround=True, content=eListboxPythonMultiContent)
		self.chooseMenuList.l.setFont(0, gFont('mediaportal', 23))
		self.chooseMenuList.l.setItemHeight(25)
		self['genreList'] = self.chooseMenuList

		self.onLayoutFinish.append(self.layoutFinished)

	def layoutFinished(self):
		self.genreliste.append((0, "Mit dieser Erweiterung kannst Du deine Lieblings Youtube Kanäle selber hinzufügen.", ""))
		self.genreliste.append((0, "Für jeden Kanal müssen nur zwei Einträge hinzugefügt werden:", ""))
		self.genreliste.append((0, "'<name> Kanal Bezeichnung </name>' und '<user> Besitzername </user>'", ""))
		self.genreliste.append((0, " ", ""))
		self.genreliste.append((0, "Mit der Taste 'Grün' wird die Datei:", ""))
		self.genreliste.append((0, "'"+self.user_path+"' geladen.", ""))
		self.genreliste.append((0, " ", ""))
		self.genreliste.append((0, "With this extension you can add your favorite Youtube channels themselves.", ""))
		self.genreliste.append((0, "For each channel, only two entries are added:", ""))
		self.genreliste.append((0, "'<name> channel name </name>' and '<user> owner name </ user>'", ""))
		self.genreliste.append((0, " ", ""))
		self.genreliste.append((0, "With the 'Green' button the user file:", ""))
		self.genreliste.append((0, "'"+self.user_path+"' is loaded.", ""))

		if not exists(self.user_path):
			self.getUserFile(fInit=True)

		self.chooseMenuList.setList(map(show_USER_GenreListEntry, self.genreliste))

	def getUserFile(self, fInit=False):
		fname = self.plugin_path + "/userfiles/userchan.xml"

		print "fname: ",fname
		try:
			if fInit:
				shutil.copyfile(fname, self.user_path)
				return

			fp = open(self.user_path)
			data = fp.read()
			fp.close()
		except IOError, e:
			print "File Error: ",e
			self.genreliste = []
			self.genreliste.append((0, str(e), ""))
			self.chooseMenuList.setList(map(show_USER_GenreListEntry, self.genreliste))
		else:
			self.userData(data)

	def userData(self, data):
		list = re.findall('<name>(.*?)</name>.*?<user>(.*?)</user>', data, re.S)

		self.genreliste = []
		if list:
			i = 1
			for (name, user) in list:
				self.genreliste.append((i, name.strip(), '/'+user.strip()))
				i += 1

			self.genreliste.sort(key=lambda t : t[1].lower())
			self.keyLocked = False
		else:
			self.genreliste.append((0, "Keine User Channels gefunden !", ""))

		self.chooseMenuList.setList(map(show_USER_GenreListEntry2, self.genreliste))

	def keyGreen(self):
		self.getUserFile()

	def keyOK(self):
		if self.keyLocked:
			return

		genreID = self['genreList'].getCurrent()[0][0]
		genre = self['genreList'].getCurrent()[0][1]
		stvLink = self['genreList'].getCurrent()[0][2]
		self.session.open(show_USER_ListScreen, genreID, stvLink, genre)

	def keyCancel(self):
		self.close()

def show_USER_ListEntry(entry):
	return [entry,
		(eListboxPythonMultiContent.TYPE_TEXT, 20, 0, 860, 25, 0, RT_HALIGN_LEFT | RT_VALIGN_CENTER, entry[0]+entry[1])
		]

class show_USER_ListScreen(Screen):

	def __init__(self, session, genreID, stvLink, stvGenre):
		self.session = session
		self.genreID = genreID
		self.stvLink = stvLink
		self.genreName = stvGenre

		self.plugin_path = mp_globals.pluginPath
		self.skin_path =  mp_globals.pluginPath + "/skins"

		path = "%s/%s/dokuListScreen.xml" % (self.skin_path, config.mediaportal.skin.value)
		if not fileExists(path):
			path = self.skin_path + "/original/dokuListScreen.xml"

		print path
		with open(path, "r") as f:
			self.skin = f.read()
			f.close()

		Screen.__init__(self, session)

		self["actions"]  = ActionMap(["OkCancelActions", "ShortcutActions", "WizardActions", "ColorActions", "SetupActions", "NumberActions", "MenuActions", "EPGSelectActions"], {
			"ok" 		: self.keyOK,
			"cancel"	: self.keyCancel,
			"up" 		: self.keyUp,
			"down" 		: self.keyDown,
			"right" 	: self.keyRight,
			"left" 		: self.keyLeft,
			"nextBouquet": self.keyPageUpFast,
			"prevBouquet": self.keyPageDownFast,
			"red" 		:  self.keyTxtPageUp,
			"blue" 		:  self.keyTxtPageDown,
			"yellow"	: self.keyYellow,
			"1" 		: self.key_1,
			"3" 		: self.key_3,
			"4" 		: self.key_4,
			"6" 		: self.key_6,
			"7" 		: self.key_7,
			"9" 		: self.key_9
		}, -1)

		self['title'] = Label(USER_Version)
		self['ContentTitle'] = Label(self.genreName)
		self['name'] = Label("")
		self['handlung'] = ScrollLabel("")
		self['page'] = Label("")
		self['F1'] = Label("Text-")
		self['F2'] = Label("")
		self['F3'] = Label("")
		self['F4'] = Label("Text+")
		self['VideoPrio'] = Label("")
		self['vPrio'] = Label("")
		self['Page'] = Label("Page")
		self['coverArt'] = Pixmap()

		self.keyLocked = True
		self.baseUrl = "http://www.youtube.com"

		self.videoPrio = int(config.mediaportal.youtubeprio.value)
		self.videoPrioS = ['L','M','H']
		self.setVideoPrio()

		self.keckse = {}
		self.filmliste = []
		self.start_idx = 1
		self.max_res = 12
		self.total_res = 0
		self.pages = 0
		self.page = 0
		self.chooseMenuList = MenuList([], enableWrapAround=True, content=eListboxPythonMultiContent)
		self.chooseMenuList.l.setFont(0, gFont('mediaportal', 23))
		self.chooseMenuList.l.setItemHeight(25)
		self['liste'] = self.chooseMenuList

		self.onLayoutFinish.append(self.layoutFinished)

	def layoutFinished(self):
		self.loadPageData()

	def loadPageData(self):
		self.keyLocked = True
		print "getPage: ",self.stvLink

		self.filmliste = []
		self.filmliste.append(('Bitte warten...','','','',''))
		self.chooseMenuList.setList(map(show_USER_ListEntry, self.filmliste))

		url = "http://gdata.youtube.com/feeds/api/users"+self.stvLink+"/uploads?"+\
				"start-index=%d&max-results=%d&v=2" % (self.start_idx, self.max_res)
		getPage(url, cookies=self.keckse, agent=std_headers, headers={'Content-Type':'application/x-www-form-urlencoded'}).addCallback(self.genreData).addErrback(self.dataError)

	def genreData(self, data):
		print "genreData:"
		print "genre: ",self.genreID
		if not self.pages:
			m = re.search('totalResults>(.*?)</', data)
			if m:
				a = int(m.group(1))
				self.pages = a // self.max_res
				if a % self.max_res:
					self.pages += 1
				self.page = 1

		a = 0
		l = len(data)
		self.filmliste = []
		while a < l:
			mg = re.search('<media:group>(.*?)</media:group>', data[a:], re.S)
			if mg:
				a += mg.end()
				m1 = re.search('description type=\'plain\'>(.*?)</', mg.group(1), re.S)
				if m1:
					desc = decodeHtml(m1.group(1))
					desc = urllib.unquote(desc)
				else:
					desc = "Keine weiteren Info's vorhanden."

				m2 = re.search('<media:player url=.*?/watch\?v=(.*?)&amp;feature=youtube_gdata_player.*?'\
					'<media:thumbnail url=\'(.*?)\'.*?<media:title type=\'plain\'>(.*?)</.*?<yt:duration seconds=\'(.*?)\'', mg.group(1), re.S)
				if m2:
					vid = m2.group(1)
					img = m2.group(2)
					dura = int(m2.group(4))
					vtim = str(datetime.timedelta(seconds=dura))
					title = decodeHtml(m2.group(3))
					self.filmliste.append((vtim+' ', title, vid, img, desc))
			else:
				a = l

		if len(self.filmliste) == 0:
			print "No audio drama found!"
			self.pages = 0
			self.filmliste.append(('Keine Videos gefunden !','','','',''))
		else:
			#self.filmliste.sort(key=lambda t : t[0].lower())
			menu_len = len(self.filmliste)
			print "Audio dramas found: ",menu_len

		self.chooseMenuList.setList(map(show_USER_ListEntry, self.filmliste))
		self.keyLocked = False
		self.showInfos()

	def dataError(self, error):
		print "dataError: ",error

	def showInfos(self):
		self['page'].setText("%d / %d" % (self.page,self.pages))
		stvTitle = self['liste'].getCurrent()[0][1]
		stvImage = self['liste'].getCurrent()[0][3]
		desc = self['liste'].getCurrent()[0][4]
		print "Img: ",stvImage
		self['name'].setText(stvTitle)
		self['handlung'].setText(desc)
		CoverHelper(self['coverArt']).getCover(stvImage)

	def youtubeErr(self, error):
		print "youtubeErr: ",error
		self['handlung'].setText("Das Video kann leider nicht abgespielt werden !\n"+str(error))

	def setVideoPrio(self):
		self.videoPrio = int(config.mediaportal.youtubeprio.value)
		self['vPrio'].setText(self.videoPrioS[self.videoPrio])

	def keyLeft(self):
		if self.keyLocked:
			return
		self['liste'].pageUp()
		self.showInfos()

	def keyRight(self):
		if self.keyLocked:
			return
		self['liste'].pageDown()
		self.showInfos()

	def keyUp(self):
		if self.keyLocked:
			return
		i = self['liste'].getSelectedIndex()
		if not i:
			self.keyPageDownFast()

		self['liste'].up()
		self.showInfos()

	def keyDown(self):
		if self.keyLocked:
			return
		i = self['liste'].getSelectedIndex()
		l = len(self.filmliste) - 1
		#print "i, l: ",i,l
		if l == i:
			self.keyPageUpFast()

		self['liste'].down()
		self.showInfos()

	def keyTxtPageUp(self):
		self['handlung'].pageUp()

	def keyTxtPageDown(self):
		self['handlung'].pageDown()

	def keyPageUpFast(self,step=1):
		if self.keyLocked:
			return
		#print "keyPageUp: "
		oldpage = self.page
		if (self.page + step) <= self.pages:
			self.page += step
			self.start_idx += self.max_res * step
		else:
			self.page = 1
			self.start_idx = 1
		#print "Page %d/%d" % (self.page,self.pages)
		if oldpage != self.page:
			self.loadPageData()

	def keyPageDownFast(self,step=1):
		if self.keyLocked:
			return
		print "keyPageDown: "
		oldpage = self.page
		if (self.page - step) >= 1:
			self.page -= step
			self.start_idx -= self.max_res * step
		else:
			self.page = self.pages
			self.start_idx = self.max_res * (self.pages - 1) + 1
		#print "Page %d/%d" % (self.page,self.pages)
		if oldpage != self.page:
			self.loadPageData()

	def keyYellow(self):
		self.setVideoPrio()

	def key_1(self):
		#print "keyPageDownFast(2)"
		self.keyPageDownFast(2)

	def key_4(self):
		#print "keyPageDownFast(5)"
		self.keyPageDownFast(5)

	def key_7(self):
		#print "keyPageDownFast(10)"
		self.keyPageDownFast(10)

	def key_3(self):
		#print "keyPageUpFast(2)"
		self.keyPageUpFast(2)

	def key_6(self):
		#print "keyPageUpFast(5)"
		self.keyPageUpFast(5)

	def key_9(self):
		#print "keyPageUpFast(10)"
		self.keyPageUpFast(10)

	def keyOK(self):
		if self.keyLocked:
			return
		self.session.openWithCallback(
			self.setVideoPrio,
			YoutubePlayer,
			self.filmliste,
			self['liste'].getSelectedIndex(),
			playAll = True,
			listTitle = self.genreName,
			title_inr=1
			)


	def keyCancel(self):
		self.close()