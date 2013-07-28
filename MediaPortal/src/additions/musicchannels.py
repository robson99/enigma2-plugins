﻿#	-*-	coding:	utf-8	-*-

from Plugins.Extensions.MediaPortal.resources.imports import *
from Plugins.Extensions.MediaPortal.resources.youtubeplayer import YoutubePlayer
from Plugins.Extensions.MediaPortal.resources.coverhelper import CoverHelper

MUSIC_Version = "MUSIC-Channels v0.94"

MUSIC_siteEncoding = 'utf-8'

def show_MUSIC_GenreListEntry(entry):
	return [entry,
		(eListboxPythonMultiContent.TYPE_TEXT, 20, 0, 860, 25, 0, RT_HALIGN_CENTER | RT_VALIGN_CENTER, entry[1])
		]

class show_MUSIC_Genre(Screen):

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
			"cancel": self.keyCancel
		}, -1)


		self['title'] = Label(MUSIC_Version)
		self['ContentTitle'] = Label("Channel Auswahl")
		self['name'] = Label("")
		self['F1'] = Label("")
		self['F2'] = Label("")
		self['F3'] = Label("")
		self['F4'] = Label("")

		self.genreliste = []
		self.chooseMenuList = MenuList([], enableWrapAround=True, content=eListboxPythonMultiContent)
		self.chooseMenuList.l.setFont(0, gFont('mediaportal', 23))
		self.chooseMenuList.l.setItemHeight(25)
		self['genreList'] = self.chooseMenuList

		self.onLayoutFinish.append(self.layoutFinished)

	def layoutFinished(self):
		self.genreliste.append((1,'Ultra Music', '/UltraRecords'))
		self.genreliste.append((2,'ArmadaMusic.TV', '/armadamusic'))
		self.genreliste.append((3,'YOU LOVE DANCE.TV', '/Planetpunkmusic'))
		self.genreliste.append((4,'Classical Music Only Channel', '/ClassicalMusicOnly'))
		#self.genreliste.append((5,'Music Channel Romania', '/1musicchannel'))
		self.genreliste.append((6,'50 Cent Music', '/50CentMusic'))
		self.genreliste.append((7,'GMC Schlager', '/BlueSilverstar'))
		self.genreliste.append((8,'Classical Music Channel / Klassische', '/BPanther'))
		self.genreliste.append((9,'EMI Music Germany', '/EMIMusicGermany'))
		self.genreliste.append((10,'Sony Music Germany', '/SMECatalogGermany'))
		self.genreliste.append((11,'Kanal von MyWorldCharts', '/MyWorldCharts'))
		self.genreliste.append((12,'CaptainCharts', '/CaptainCharts'))
		self.genreliste.append((13,'PowerCharts', '/PowerCharts'))
		self.genreliste.append((14,'Kontor.TV', '/kontor'))
		self.genreliste.append((15,'Scooter Official', '/scooter'))
		self.genreliste.append((16,'ATZEN MUSIK TV', '/atzenmusiktv'))
		self.genreliste.append((17,'BigCityBeats', '/HammerDontHurtEm'))
		self.genreliste.append((18,'The Best Of', '/alltimebestofmusic'))
		self.genreliste.append((19,'Tomorrowland', '/TomorrowlandChannel'))
		self.genreliste.append((20,'Electro House&Dance Music 2013', '/Ayonen1'))
		self.genreliste.append((21,'DrDoubleT', '/DrDoubleT'))
		self.genreliste.append((22,'►Techno, HandsUp & Dance◄', '/DJFlyBeatMusic'))
		self.genreliste.append((23,'Zooland Records', '/zoolandMusicGmbH'))
		self.genreliste.append((24,'Bazooka Records', '/bazookalabel'))
		self.genreliste.append((25,'Crystal Lake Music', '/CrystaLakeTV'))
		self.genreliste.append((26,'SKRILLEX', '/TheOfficialSkrillex'))
		self.genreliste.append((27,'AggroTV', '/aggroTV'))
		self.genreliste.append((28,'Bands & ART-Ellie Goulding', '/EllieGouldingEmpire'))
		self.genreliste.append((29,'Bands & ART-Psyche', '/thandewye'))
		self.genreliste.append((30,'Bands & ART-Joint Venture', '/srudlak'))
		self.genreliste.append((31,'Bands & ART-Madonna', '/madonna'))
		self.genreliste.append((32,'BB Sound Production', '/b0ssy007'))
		self.genreliste.append((33,'Chill-out,Lounge,Jazz,Electronic,Psy,Piano,Trance', '/aliasmike2002'))
		self.genreliste.append((34,'Gothic', '/AiratzuMusic'))
		self.genreliste.append((35,'Gothic', '/INM0R4L'))
		self.genreliste.append((36,'Gothic-Industrial Mix', '/noetek'))
		self.genreliste.append((37,'Wave & Gothic', '/MrBelorix'))
		self.genreliste.append((38,'Indie', '/curie78'))
		self.genreliste.append((39,'Indie', '/SoundIndieMusic'))
		self.genreliste.append((40,'Planetpunkmusic TV', '/Planetpunkmusic'))
		self.genreliste.append((41,'Selfmade Records', '/SelfmadeRecords'))
		self.genreliste.append((42,'UKF-DrumandBass', '/UKFDrumandBass'))
		self.genreliste.append((43,'UKF-Dubstep', '/UKFDubstep'))
		self.genreliste.append((44,'UKF-Music', '/UKFMusic'))
		self.genreliste.append((45,'UKF-Mixes', '/UKFMixes'))
		self.genreliste.append((46,'UKF-Live', '/UKFLive'))
		self.genreliste.append((47,'Smarty Music', '/smartymcfly'))
		self.genreliste.append((48,'MoMMusic Network', '/MrMoMMusic'))
		#self.genreliste.append((9,'', '/'))

		self.genreliste.sort(key=lambda t : t[1].lower())
		self.chooseMenuList.setList(map(show_MUSIC_GenreListEntry, self.genreliste))

	def keyOK(self):
		genreID = self['genreList'].getCurrent()[0][0]
		genre = self['genreList'].getCurrent()[0][1]
		stvLink = self['genreList'].getCurrent()[0][2]
		self.session.open(show_MUSIC_ListScreen, genreID, stvLink, genre)

	def keyCancel(self):
		self.close()

def show_MUSIC_ListEntry(entry):
	return [entry,
		(eListboxPythonMultiContent.TYPE_TEXT, 20, 0, 860, 25, 0, RT_HALIGN_LEFT | RT_VALIGN_CENTER, entry[0]+entry[1])
		]

class show_MUSIC_ListScreen(Screen):

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

		self['title'] = Label(MUSIC_Version)
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
		self.chooseMenuList.setList(map(show_MUSIC_ListEntry, self.filmliste))

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
			self.filmliste.append(('Keine Hörspiele gefunden !','','','',''))
		else:
			#self.filmliste.sort(key=lambda t : t[0].lower())
			menu_len = len(self.filmliste)
			print "Audio dramas found: ",menu_len

		self.chooseMenuList.setList(map(show_MUSIC_ListEntry, self.filmliste))
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
			plType='local',
			title_inr=1
			)

	def keyCancel(self):
		self.close()