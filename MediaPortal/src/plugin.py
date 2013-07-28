#	-*-	coding:	utf-8	-*-

# General imports
from resources.imports import *
from resources.update import *

# Stream-Sites import
from additions.forplayers import *
from additions.dokume import *
from additions.roflvideos import *
from additions.focus import *
from additions.tvkino import *
from additions.filmon import *
from additions.netzkino import *
from additions.kinokiste import *
from additions.failto import *
from additions.sportbild import *
from additions.myvideo import *
from additions.laola import *
from additions.burningseries import *
from additions.filmtrailer import *
from additions.primewire import *
from additions.radio import *
from additions.cczwei import *
from additions.baskino import *
from additions.kinoxto import *
from additions.dreamscreencast import *
from additions.streamoase import *
from additions.autobild import *
from additions.nhl import *
from additions.spox import *
from additions.songsto import *
from additions.myentertainment import *
from additions.movie4k import *
from additions.iStreamws import *
from additions.mahlzeittv import *
from additions.appletrailers import *
from additions.dokuh import *
from additions.dokuhouse import *
from additions.allmusichouse import *
from additions.putpattv import *
from additions.liveleak import *
from additions.dokustream import *
from additions.sciencetv import *
from additions.szenestreams import *
from additions.hoerspielhouse import *
from additions.gigatv import *
from additions.auditv import *
from additions.gronkh import *
from additions.hoerspielchannels import *
from additions.carchannels import *
from additions.gamechannels import *
from additions.musicchannels import *
from additions.fiwitu import *
from additions.userchannels import *
from additions.cinestream import *
from additions.moovizon import *
from additions.youtube import *
from additions.clipfish import *
from additions.mlehd import *
from additions.ddl_me import *
from additions.ran import *
from additions.movie25 import *
from additions.eighties import *
from additions.teledunet import *
from additions.geo_de import *
from additions.deluxemusic import *
from additions.nuna import *
from additions.watchseries import *
from additions.wrestlingnetwork import *
#from additions.viewster import *
from additions.musicstreamcc import *
from additions.vibeo import *
from additions.retrotv import *
from additions.galileovl import *
from additions.sport1fm import *

try:
	import ast
except:
	print "No 'ast' module"
	astModule = False
else:
	from additions.heisevideo import *
	print "Module 'ast' loaded"
	astModule = True

# kids
from additions.kinderkino import *
from additions.tivi import *
from additions.kika import *

# mediatheken
from additions.mediatheken.voxnow import *
from additions.mediatheken.rtlnow import *
from additions.mediatheken.ntvnow import *
from additions.mediatheken.rtlnitronow import *
from additions.mediatheken.rtl2now import *
from additions.mediatheken.superrtlnow import *
from additions.mediatheken.zdf import *
from additions.mediatheken.orf import *
from additions.mediatheken.srf import *
from additions.mediatheken.ard import *

# music
from additions.canna import *
from additions.myvideoTop100 import *
from additions.mtvdecharts import *

# porn
from additions.porn.ahme import *
from additions.porn.amateurporn import *
from additions.porn.beeg import *
from additions.porn.drtuber import *
from additions.porn.elladies import *
from additions.porn.eporner import *
from additions.porn.eroprofile import *
from additions.porn.extremetube import *
from additions.porn.freeomovie import *
from additions.porn.gstreaminxxx import *
from additions.porn.hdporn import *
from additions.porn.hotshame import *
from additions.porn.megaskanks import *
from additions.porn.paradisehill import *
from additions.porn.pinkrod import *
from additions.porn.playporn import *
from additions.porn.pornerbros import *
from additions.porn.pornhub import *
from additions.porn.pornmvz import *
from additions.porn.pornostreams import *
from additions.porn.pornrabbit import *
from additions.porn.realgfporn import *
from additions.porn.redtube import *
from additions.porn.sexxxhd import *
from additions.porn.sunporno import *
from additions.porn.thenewporn import *
from additions.porn.updatetube import *
from additions.porn.wetplace import *
from additions.porn.xhamster import *
from additions.porn.xxxsave import *
from additions.porn.x4tube import *
from additions.porn.youporn import *

config.mediaportal = ConfigSubsection()
config.mediaportal.version = NoSave(ConfigText(default="460"))
config.mediaportal.versiontext = NoSave(ConfigText(default="4.6.0"))
config.mediaportal.autoupdate = ConfigYesNo(default = True)
config.mediaportal.pincode = ConfigPIN(default = 0000)
config.mediaportal.showporn = ConfigYesNo(default = False)
config.mediaportal.showgrauzone = ConfigYesNo(default = False)
config.mediaportal.pingrauzone = ConfigYesNo(default = False)
config.mediaportal.skin = ConfigSelection(default = "tec", choices = [("tec", _("tec")),("liquidblue", _("liquidblue")), ("original", _("original"))])
config.mediaportal.ansicht = ConfigSelection(default = "wall", choices = [("liste", _("Liste")),("wall", _("Wall"))])
config.mediaportal.selektor = ConfigSelection(default = "blue", choices = [("blue", _("blau")),("green", _(u"gr\xfcn")),("red", _("rot")),("turkis", _(u"t\xfcrkis"))])
config.mediaportal.useRtmpDump = ConfigYesNo(default = False)
config.mediaportal.useHttpDump = ConfigYesNo(default = False)
config.mediaportal.storagepath = ConfigText(default="/media/hdd/mediaportal/tmp/", fixed_size=False)
config.mediaportal.autoplayThreshold = ConfigInteger(default = 50, limits = (1,100))
config.mediaportal.filter = ConfigSelection(default = "ALL", choices = [("ALL", ("ALL")), ("Mediathek", ("Mediathek")), ("Grauzone", ("Grauzone")), ("Fun", ("Fun")), ("Sport", ("Sport")), ("Music", ("Music")), ("Porn", ("Porn"))])
config.mediaportal.youtubeprio = ConfigSelection(default = "1", choices = [("0", _("Low")),("1", _("Medium")),("2", _("High"))])
config.mediaportal.pornpin = ConfigYesNo(default = True)
config.mediaportal.setuppin = ConfigYesNo(default = False)
config.mediaportal.watchlistpath = ConfigText(default="/etc/enigma2/", fixed_size=False)
config.mediaportal.sortplugins = ConfigSelection(default = "abc", choices = [("hits", _("Hits")), ("abc", _("ABC")), ("user", _("User"))])
config.mediaportal.showapplepagestyle = ConfigYesNo(default = True)
config.mediaportal.laola1locale = ConfigText(default="de", fixed_size=False)
config.mediaportal.debugMode = ConfigSelection(default="Silent", choices = ["High", "Normal", "Silent", ])

# Kinder
config.mediaportal.showKinderKino = ConfigYesNo(default = True)
config.mediaportal.showtivi = ConfigYesNo(default = True)
config.mediaportal.showkika = ConfigYesNo(default = True)

config.mediaportal.showDoku = ConfigYesNo(default = True)
config.mediaportal.showRofl = ConfigYesNo(default = True)
config.mediaportal.showFail = ConfigYesNo(default = True)
config.mediaportal.showMyvideo = ConfigYesNo(default = True)
config.mediaportal.showFocus = ConfigYesNo(default = True)
config.mediaportal.showFilmOn = ConfigYesNo(default = True)
config.mediaportal.showTvkino = ConfigYesNo(default = True)
config.mediaportal.showSpobox = ConfigYesNo(default = True)
config.mediaportal.showNetzKino = ConfigYesNo(default = True)
config.mediaportal.showSportBild = ConfigYesNo(default = True)
config.mediaportal.showLaola1 = ConfigYesNo(default = True)
config.mediaportal.showRadio = ConfigYesNo(default = True)
config.mediaportal.showCczwei = ConfigYesNo(default = True)
config.mediaportal.showTrailer = ConfigYesNo(default = True)
config.mediaportal.showDsc = ConfigYesNo(default = True)
config.mediaportal.showAutoBild = ConfigYesNo(default = True)
config.mediaportal.showNhl = ConfigYesNo(default = True)
config.mediaportal.show4Players = ConfigYesNo(default = True)
config.mediaportal.showGIGA = ConfigYesNo(default = True)
config.mediaportal.showaudi = ConfigYesNo(default = True)
config.mediaportal.showgronkh = ConfigYesNo(default = True)
config.mediaportal.showMahlzeitTV = ConfigYesNo(default = True)
config.mediaportal.showappletrailers = ConfigYesNo(default = True)
config.mediaportal.showDOKUh = ConfigYesNo(default = True)
config.mediaportal.showDokuHouse = ConfigYesNo(default = True)
config.mediaportal.showAllMusicHouse = ConfigYesNo(default = True)
config.mediaportal.showputpattv = ConfigYesNo(default = True)
config.mediaportal.showLiveLeak = ConfigYesNo(default = True)
config.mediaportal.showDokuStream = ConfigYesNo(default = True)
config.mediaportal.showScienceTV = ConfigYesNo(default = True)
config.mediaportal.showHoerspielHouse = ConfigYesNo(default = True)
config.mediaportal.showHoerspielChannels = ConfigYesNo(default = True)
config.mediaportal.showCarChannels = ConfigYesNo(default = True)
config.mediaportal.showGameChannels = ConfigYesNo(default = True)
config.mediaportal.showFiwitu = ConfigYesNo(default = True)
config.mediaportal.showMusicChannels = ConfigYesNo(default = True)
config.mediaportal.showUserChannels = ConfigYesNo(default = True)
config.mediaportal.showYoutube = ConfigYesNo(default = True)
config.mediaportal.showClipfish = ConfigYesNo(default = True)
config.mediaportal.showRan = ConfigYesNo(default = True)
config.mediaportal.showTeledunet = ConfigYesNo(default = True)
config.mediaportal.showGEOde = ConfigYesNo(default = True)
config.mediaportal.showDeluxemusic = ConfigYesNo(default = True)
config.mediaportal.showNuna = ConfigYesNo(default = True)
config.mediaportal.showMyvideoTop100 = ConfigYesNo(default = True)
config.mediaportal.showMTVdeCharts = ConfigYesNo(default = True)
config.mediaportal.showWrestlingnetwork = ConfigYesNo(default = True)
config.mediaportal.showretrotv = ConfigYesNo(default = True)
config.mediaportal.showgalileovl = ConfigYesNo(default = True)
config.mediaportal.showsport1fm = ConfigYesNo(default = True)
if astModule:
	config.mediaportal.showHeiseVideo = ConfigYesNo(default = True)

# grauzone
config.mediaportal.showMusicstreamcc = ConfigYesNo(default = False)
config.mediaportal.showVibeo = ConfigYesNo(default = False)
config.mediaportal.showWatchseries = ConfigYesNo(default = False)
config.mediaportal.showMovie25 = ConfigYesNo(default = False)
config.mediaportal.showEighties = ConfigYesNo(default = False)
config.mediaportal.showmlehd = ConfigYesNo(default = False)
config.mediaportal.showDdlme = ConfigYesNo(default = False)
config.mediaportal.showCanna = ConfigYesNo(default = False)
config.mediaportal.showSzeneStreams = ConfigYesNo(default = False)
config.mediaportal.showCinestream = ConfigYesNo(default = False)
config.mediaportal.showMoovizon = ConfigYesNo(default = False)
config.mediaportal.showBaskino = ConfigYesNo(default = False)
config.mediaportal.showKinoKiste = ConfigYesNo(default = False)
config.mediaportal.showStreamOase = ConfigYesNo(default = False)
config.mediaportal.showBs = ConfigYesNo(default = False)
config.mediaportal.showprimewire = ConfigYesNo(default = False)
config.mediaportal.showKinox = ConfigYesNo(default = False)
config.mediaportal.showSongsto = ConfigYesNo(default = False)
#config.mediaportal.showViewster = ConfigYesNo(default = False)
config.mediaportal.showMEHD = ConfigYesNo(default = False)
config.mediaportal.showIStream = ConfigYesNo(default = False)
config.mediaportal.showM4k = ConfigYesNo(default = False)
config.mediaportal.showM4kWatchlist = ConfigYesNo(default = False)
config.mediaportal.showKinoxWatchlist = ConfigYesNo(default = False)

# mediatheken
config.mediaportal.showVoxnow = ConfigYesNo(default = True)
config.mediaportal.showRTLnow = ConfigYesNo(default = True)
config.mediaportal.showNTVnow = ConfigYesNo(default = True)
config.mediaportal.showRTL2now = ConfigYesNo(default = True)
config.mediaportal.showRTLnitro = ConfigYesNo(default = True)
config.mediaportal.showSUPERRTLnow = ConfigYesNo(default = True)
config.mediaportal.showZDF = ConfigYesNo(default = True)
config.mediaportal.showORF = ConfigYesNo(default = True)
config.mediaportal.showSRF = ConfigYesNo(default = True)
config.mediaportal.showARD = ConfigYesNo(default = True)

# porn
config.mediaportal.show4tube = ConfigYesNo(default = False)
config.mediaportal.showahme = ConfigYesNo(default = False)
config.mediaportal.showamateurporn = ConfigYesNo(default = False)
config.mediaportal.showbeeg = ConfigYesNo(default = False)
config.mediaportal.showdrtuber = ConfigYesNo(default = False)
config.mediaportal.showelladies = ConfigYesNo(default = False)
config.mediaportal.showeporner = ConfigYesNo(default = False)
config.mediaportal.showeroprofile = ConfigYesNo(default = False)
config.mediaportal.showextremetube = ConfigYesNo(default = False)
config.mediaportal.showfreeomovie = ConfigYesNo(default = False)
config.mediaportal.showgstreaminxxx = ConfigYesNo(default = False)
config.mediaportal.showhdporn = ConfigYesNo(default = False)
config.mediaportal.showhotshame = ConfigYesNo(default = False)
config.mediaportal.showmegaskanks = ConfigYesNo(default = False)
config.mediaportal.showIStreamPorn = ConfigYesNo(default = False)
config.mediaportal.showM4kPorn = ConfigYesNo(default = False)
config.mediaportal.showparadisehill = ConfigYesNo(default = False)
config.mediaportal.showpinkrod = ConfigYesNo(default = False)
config.mediaportal.showplayporn = ConfigYesNo(default = False)
config.mediaportal.showpornerbros = ConfigYesNo(default = False)
config.mediaportal.showPornhub = ConfigYesNo(default = False)
config.mediaportal.showpornmvz = ConfigYesNo(default = False)
config.mediaportal.showpornostreams = ConfigYesNo(default = False)
config.mediaportal.showpornrabbit = ConfigYesNo(default = False)
config.mediaportal.showrealgfporn = ConfigYesNo(default = False)
config.mediaportal.showredtube = ConfigYesNo(default = False)
config.mediaportal.showsexxxhd = ConfigYesNo(default = False)
config.mediaportal.showsunporno = ConfigYesNo(default = False)
config.mediaportal.showthenewporn = ConfigYesNo(default = False)
config.mediaportal.showupdatetube = ConfigYesNo(default = False)
config.mediaportal.showwetplace = ConfigYesNo(default = False)
config.mediaportal.showXhamster = ConfigYesNo(default = False)
config.mediaportal.showxxxsave = ConfigYesNo(default = False)
config.mediaportal.showyouporn = ConfigYesNo(default = False)

#fake entry fuer die kategorien
config.mediaportal.fake_entry = NoSave(ConfigNothing())

# Konfiguration erfolgt in SimplePlayer
config.mediaportal.sp_randomplay = ConfigYesNo(default = False)
config.mediaportal.sp_scrsaver = ConfigSelection(default = "off", choices = [("on", _("On")),("off", _("Off")),("automatic", _("Automatic"))])
config.mediaportal.sp_on_movie_stop = ConfigSelection(default = "ask", choices = [("ask", _("Ask user")), ("quit", _("Return to previous service"))])
config.mediaportal.sp_on_movie_eof = ConfigSelection(default = "ask", choices = [("ask", _("Ask user")), ("quit", _("Return to previous service")), ("pause", _("Pause movie at end"))])
config.mediaportal.sp_seekbar_sensibility = ConfigInteger(default = 10, limits = (1,50))

class hauptScreenSetup(Screen, ConfigListScreen):

	def __init__(self, session):
		self.session = session

		self.plugin_path = mp_globals.pluginPath
		self.skin_path = mp_globals.pluginPath + "/skins"

		path = "%s/%s/hauptScreenSetup.xml" % (self.skin_path, config.mediaportal.skin.value)
		if not fileExists(path):
			path = self.skin_path + "/original/hauptScreenSetup.xml"

		with open(path, "r") as f:
			self.skin = f.read()
			f.close()

		Screen.__init__(self, session)

		self.configlist = []
		self.sport = []
		self.music = []
		self.fun = []
		self.mediatheken = []
		self.porn = []
		self.grauzone = []
		ConfigListScreen.__init__(self, self.configlist)

		## Allgemein
		self.configlist.append(getConfigListEntry("----- Allgemein -----", config.mediaportal.fake_entry))
		self.configlist.append(getConfigListEntry("Automatic Update Check:", config.mediaportal.autoupdate))
		self.configlist.append(getConfigListEntry("Pincode:", config.mediaportal.pincode))
		self.configlist.append(getConfigListEntry("XXX-Erweiterungen sichtbar:", config.mediaportal.showporn))
		self.configlist.append(getConfigListEntry("XXX-Pincodeabfrage:", config.mediaportal.pornpin))
		self.configlist.append(getConfigListEntry("Selektor-Farbe:", config.mediaportal.selektor))
		self.configlist.append(getConfigListEntry("HauptScreen-Ansicht:", config.mediaportal.ansicht))
		self.configlist.append(getConfigListEntry("Apple Page Style:", config.mediaportal.showapplepagestyle))
		self.configlist.append(getConfigListEntry("Skinauswahl:", config.mediaportal.skin))
		self.configlist.append(getConfigListEntry("HTTPDump benutzen:", config.mediaportal.useHttpDump))
		self.configlist.append(getConfigListEntry("RTMPDump benutzen:", config.mediaportal.useRtmpDump))
		self.configlist.append(getConfigListEntry("RTMPDump Cachepath:", config.mediaportal.storagepath))
		self.configlist.append(getConfigListEntry("Autoplay Threshold [%]:", config.mediaportal.autoplayThreshold))
		self.configlist.append(getConfigListEntry("YouTube Video Quality Priority:", config.mediaportal.youtubeprio))
		self.configlist.append(getConfigListEntry("Watchlist/Playlist/Userchan path:", config.mediaportal.watchlistpath))
		self.configlist.append(getConfigListEntry("Plugins sortieren nach:", config.mediaportal.sortplugins))
		self.configlist.append(getConfigListEntry("Setup-Pincodeabfrage:", config.mediaportal.setuppin))

		### Sport
		self.sport.append(getConfigListEntry("NHL", config.mediaportal.showNhl))
		self.sport.append(getConfigListEntry("Spobox", config.mediaportal.showSpobox))
		self.sport.append(getConfigListEntry("Laola1", config.mediaportal.showLaola1))
		self.sport.append(getConfigListEntry("Sport1.fm", config.mediaportal.showsport1fm))
		self.sport.append(getConfigListEntry("Ran.de", config.mediaportal.showRan))
		self.sport.sort(key=lambda t : tuple(t[0][0].lower()))

		### Music
		self.music.append(getConfigListEntry("AllMusicHouse", config.mediaportal.showAllMusicHouse))
		self.music.append(getConfigListEntry("Deluxemusic", config.mediaportal.showDeluxemusic))
		self.music.append(getConfigListEntry("MTV.de Charts", config.mediaportal.showMTVdeCharts))
		self.music.append(getConfigListEntry("MUSIC-Channels", config.mediaportal.showMusicChannels))
		self.music.append(getConfigListEntry("Myvideo Top 100", config.mediaportal.showMyvideoTop100))
		self.music.append(getConfigListEntry("Nuna", config.mediaportal.showNuna))
		self.music.append(getConfigListEntry("putpat.tv", config.mediaportal.showputpattv))
		if config.mediaportal.showgrauzone.value:
			self.music.append(getConfigListEntry("80s & 90s Music", config.mediaportal.showEighties))
			self.music.append(getConfigListEntry("Canna-Power", config.mediaportal.showCanna))
			self.music.append(getConfigListEntry("Musicstream.cc", config.mediaportal.showMusicstreamcc))
			self.music.append(getConfigListEntry("Songs.to", config.mediaportal.showSongsto))
		self.music.sort(key=lambda t : tuple(t[0][0].lower()))

		### Fun
		self.fun.append(getConfigListEntry("Rofl.to", config.mediaportal.showRofl))
		self.fun.append(getConfigListEntry("Fail.to", config.mediaportal.showFail))
		self.fun.append(getConfigListEntry("LiveLeak", config.mediaportal.showLiveLeak))
		self.fun.append(getConfigListEntry("Radio.de", config.mediaportal.showRadio))
		self.fun.append(getConfigListEntry("TvKino", config.mediaportal.showTvkino))
		self.fun.append(getConfigListEntry("FilmOn", config.mediaportal.showFilmOn))
		self.fun.append(getConfigListEntry("Focus", config.mediaportal.showFocus))
		self.fun.append(getConfigListEntry("HörspielHouse", config.mediaportal.showHoerspielHouse))
		self.fun.append(getConfigListEntry("Hörspiel-Channels", config.mediaportal.showHoerspielChannels))
		self.fun.append(getConfigListEntry("CAR-Channels", config.mediaportal.showCarChannels))
		self.fun.append(getConfigListEntry("GAME-Channels", config.mediaportal.showGameChannels))
		self.fun.append(getConfigListEntry("USER-Channels", config.mediaportal.showUserChannels))
		self.fun.append(getConfigListEntry("Clipfish", config.mediaportal.showClipfish))
		self.fun.append(getConfigListEntry("YouTube", config.mediaportal.showYoutube))
		self.fun.append(getConfigListEntry("Teledunet", config.mediaportal.showTeledunet))
		self.fun.append(getConfigListEntry("GEOde", config.mediaportal.showGEOde))
		self.fun.append(getConfigListEntry("Wrestling Network", config.mediaportal.showWrestlingnetwork))
		self.fun.append(getConfigListEntry("retro-tv", config.mediaportal.showretrotv))
		self.fun.append(getConfigListEntry("Galileo-Videolexikon", config.mediaportal.showgalileovl))
		self.fun.append(getConfigListEntry("Dreamscreencast", config.mediaportal.showDsc))
		self.fun.append(getConfigListEntry("Focus", config.mediaportal.showFocus))
		self.fun.append(getConfigListEntry("CCZwei", config.mediaportal.showCczwei))
		self.fun.append(getConfigListEntry("Filmtrailer", config.mediaportal.showTrailer))
		self.fun.append(getConfigListEntry("ScienceTV", config.mediaportal.showScienceTV))
		self.fun.append(getConfigListEntry("Doku.me", config.mediaportal.showDoku))
		self.fun.append(getConfigListEntry("DokuStream", config.mediaportal.showDokuStream))
		self.fun.append(getConfigListEntry("4Players", config.mediaportal.show4Players))
		self.fun.append(getConfigListEntry("GIGA.de", config.mediaportal.showGIGA))
		self.fun.append(getConfigListEntry("Audi.tv", config.mediaportal.showaudi))
		self.fun.append(getConfigListEntry("gronkh.de", config.mediaportal.showgronkh))
		self.fun.append(getConfigListEntry("mahlzeit.tv", config.mediaportal.showMahlzeitTV))
		self.fun.append(getConfigListEntry("fiwitu.tv", config.mediaportal.showFiwitu))
		self.fun.append(getConfigListEntry("Apple Movie Trailers", config.mediaportal.showappletrailers))
		self.fun.append(getConfigListEntry("DOKUh", config.mediaportal.showDOKUh))
		self.fun.append(getConfigListEntry("DokuHouse", config.mediaportal.showDokuHouse))
		self.fun.append(getConfigListEntry("AutoBild", config.mediaportal.showAutoBild))
		self.fun.append(getConfigListEntry("SportBild", config.mediaportal.showSportBild))
		if astModule:
			self.fun.append(getConfigListEntry("HeiseVideo", config.mediaportal.showHeiseVideo))
		self.fun.sort(key=lambda t : tuple(t[0][0].lower()))

		### Mediatheken
		self.mediatheken.append(getConfigListEntry("ARD Mediathek", config.mediaportal.showARD))
		self.mediatheken.append(getConfigListEntry("KIKA+", config.mediaportal.showkika))
		self.mediatheken.append(getConfigListEntry("KinderKino", config.mediaportal.showKinderKino))
		self.mediatheken.append(getConfigListEntry("Myvideo", config.mediaportal.showMyvideo))
		self.mediatheken.append(getConfigListEntry("NetzKino", config.mediaportal.showNetzKino))
		self.mediatheken.append(getConfigListEntry("N-TVNOW", config.mediaportal.showNTVnow))
		self.mediatheken.append(getConfigListEntry("ORF TVthek", config.mediaportal.showORF))
		self.mediatheken.append(getConfigListEntry("RTLNOW", config.mediaportal.showRTLnow))
		self.mediatheken.append(getConfigListEntry("RTL2NOW", config.mediaportal.showRTL2now))
		self.mediatheken.append(getConfigListEntry("RTLNITRONOW", config.mediaportal.showRTLnitro))
		self.mediatheken.append(getConfigListEntry("SRF Player", config.mediaportal.showSRF))
		self.mediatheken.append(getConfigListEntry("SUPERRTLNOW", config.mediaportal.showSUPERRTLnow))
		self.mediatheken.append(getConfigListEntry("Tivi", config.mediaportal.showtivi))
		self.mediatheken.append(getConfigListEntry("VOXNOW", config.mediaportal.showVoxnow))
		self.mediatheken.append(getConfigListEntry("ZDF Mediathek", config.mediaportal.showZDF))
		self.mediatheken.sort(key=lambda t : tuple(t[0][0].lower()))

		### Porn
		self.porn.append(getConfigListEntry("4Tube", config.mediaportal.show4tube))
		self.porn.append(getConfigListEntry("Ah-Me", config.mediaportal.showahme))
		self.porn.append(getConfigListEntry("AmateurPorn", config.mediaportal.showamateurporn))
		self.porn.append(getConfigListEntry("beeg", config.mediaportal.showbeeg))
		self.porn.append(getConfigListEntry("DrTuber", config.mediaportal.showdrtuber))
		self.porn.append(getConfigListEntry("El-Ladies", config.mediaportal.showelladies))
		self.porn.append(getConfigListEntry("Eporner", config.mediaportal.showeporner))
		self.porn.append(getConfigListEntry("EroProfile", config.mediaportal.showeroprofile))
		self.porn.append(getConfigListEntry("ExtremeTube", config.mediaportal.showextremetube))
		self.porn.append(getConfigListEntry("HDPorn", config.mediaportal.showhdporn))
		self.porn.append(getConfigListEntry("hotshame", config.mediaportal.showhotshame))
		self.porn.append(getConfigListEntry("Pinkrod", config.mediaportal.showpinkrod))
		self.porn.append(getConfigListEntry("PornerBros", config.mediaportal.showpornerbros))
		self.porn.append(getConfigListEntry("Pornhub", config.mediaportal.showPornhub))
		self.porn.append(getConfigListEntry("PornRabbit", config.mediaportal.showpornrabbit))
		self.porn.append(getConfigListEntry("RealGFPorn", config.mediaportal.showrealgfporn))
		self.porn.append(getConfigListEntry("RedTube", config.mediaportal.showredtube))
		self.porn.append(getConfigListEntry("SeXXX-HD", config.mediaportal.showsexxxhd))
		self.porn.append(getConfigListEntry("SunPorno", config.mediaportal.showsunporno))
		self.porn.append(getConfigListEntry("TheNewPorn", config.mediaportal.showthenewporn))
		self.porn.append(getConfigListEntry("UpdateTube", config.mediaportal.showupdatetube))
		self.porn.append(getConfigListEntry("WetPlace", config.mediaportal.showwetplace))
		self.porn.append(getConfigListEntry("xHamster", config.mediaportal.showXhamster))
		self.porn.append(getConfigListEntry("YouPorn", config.mediaportal.showyouporn))
		if config.mediaportal.showgrauzone.value:
			self.porn.append(getConfigListEntry("PlayPorn", config.mediaportal.showplayporn))
			self.porn.append(getConfigListEntry("PORNMVZ", config.mediaportal.showpornmvz))
			self.porn.append(getConfigListEntry("PornoStreams", config.mediaportal.showpornostreams))
			self.porn.append(getConfigListEntry("MegaSkanks", config.mediaportal.showmegaskanks))
			self.porn.append(getConfigListEntry("IStream-XXX", config.mediaportal.showIStreamPorn))
			self.porn.append(getConfigListEntry("Movie4k-XXX", config.mediaportal.showM4kPorn))
			self.porn.append(getConfigListEntry("ParadiseHill", config.mediaportal.showparadisehill))
			self.porn.append(getConfigListEntry("Free Online Movies", config.mediaportal.showfreeomovie))
			self.porn.append(getConfigListEntry("G-Stream-XXX", config.mediaportal.showgstreaminxxx))
			self.porn.append(getConfigListEntry("XXXSaVe", config.mediaportal.showxxxsave))
		self.porn.sort(key=lambda t : tuple(t[0][0].lower()))

		### Grauzone
		if config.mediaportal.showgrauzone.value:
			self.grauzone.append(getConfigListEntry("SzeneStreams", config.mediaportal.showSzeneStreams))
			self.grauzone.append(getConfigListEntry("My-Entertainment", config.mediaportal.showMEHD))
			self.grauzone.append(getConfigListEntry("IStream", config.mediaportal.showIStream))
			self.grauzone.append(getConfigListEntry("Baskino", config.mediaportal.showBaskino))
			self.grauzone.append(getConfigListEntry("KinoKiste", config.mediaportal.showKinoKiste))
			self.grauzone.append(getConfigListEntry("Stream-Oase", config.mediaportal.showStreamOase))
			self.grauzone.append(getConfigListEntry("Burning-Series", config.mediaportal.showBs))
			self.grauzone.append(getConfigListEntry("Kinox", config.mediaportal.showKinox))
			self.grauzone.append(getConfigListEntry("Movie4k", config.mediaportal.showM4k))
			self.grauzone.append(getConfigListEntry("Cinestream", config.mediaportal.showCinestream))
			self.grauzone.append(getConfigListEntry("MLE-HD", config.mediaportal.showmlehd))
			self.grauzone.append(getConfigListEntry("PrimeWire", config.mediaportal.showprimewire))
			self.grauzone.append(getConfigListEntry("ddl.me", config.mediaportal.showDdlme))
			self.grauzone.append(getConfigListEntry("movie25", config.mediaportal.showMovie25))
			self.grauzone.append(getConfigListEntry("watchseries", config.mediaportal.showWatchseries))
			self.grauzone.append(getConfigListEntry("Vibeo", config.mediaportal.showVibeo))
			self.grauzone.append(getConfigListEntry("Moovizon", config.mediaportal.showMoovizon))
			#self.grauzone.append(getConfigListEntry("Viewster", config.mediaportal.showViewster))
			self.grauzone.sort(key=lambda t : tuple(t[0][0].lower()))

		self.configlist.append(getConfigListEntry("----- Sport -----", config.mediaportal.fake_entry))
		for x in self.sport:
			self.configlist.append(("Zeige "+x[0]+":",x[1]))

		self.configlist.append(getConfigListEntry("----- Music -----", config.mediaportal.fake_entry))
		for x in self.music:
			self.configlist.append(("Zeige "+x[0]+":",x[1]))

		self.configlist.append(getConfigListEntry("----- Fun -----", config.mediaportal.fake_entry))
		for x in self.fun:
			self.configlist.append(("Zeige "+x[0]+":",x[1]))

		self.configlist.append(getConfigListEntry("----- Mediatheken -----", config.mediaportal.fake_entry))
		for x in self.mediatheken:
			self.configlist.append(("Zeige "+x[0]+":",x[1]))

		self.configlist.append(getConfigListEntry("----- Porn -----", config.mediaportal.fake_entry))
		for x in self.porn:
			self.configlist.append(("Zeige "+x[0]+":",x[1]))

		if config.mediaportal.showgrauzone.value:
			self.configlist.append(getConfigListEntry("----- Grauzone -----", config.mediaportal.fake_entry))
			for x in self.grauzone:
				self.configlist.append(("Zeige "+x[0]+":",x[1]))
			self.configlist.append(getConfigListEntry("----- Watchlist -----", config.mediaportal.fake_entry))
			self.configlist.append(getConfigListEntry("Kinox Watchlist", config.mediaportal.showKinoxWatchlist))
			self.configlist.append(getConfigListEntry("Movie4k Watchlist", config.mediaportal.showM4kWatchlist))

		self.configlist.append(getConfigListEntry("----- Debug -----", config.mediaportal.fake_entry))
		self.configlist.append(getConfigListEntry("Grauzonen-Erweiterungen sichtbar:", config.mediaportal.showgrauzone))
		self.configlist.append(getConfigListEntry("Debug-Mode:", config.mediaportal.debugMode))

		self["config"].setList(self.configlist)

		self['title'] = Label("MediaPortal - Setup - (Version %s)" % config.mediaportal.versiontext.value)
		self['name'] = Label("Setup")

		self["actions"]  = ActionMap(["OkCancelActions", "ShortcutActions", "WizardActions", "ColorActions", "SetupActions", "NumberActions", "MenuActions", "EPGSelectActions", "HelpActions"], {
			"ok"    : self.keyOK,
			"cancel": self.keyOK,
			"nextBouquet": self.keyDown,
			"prevBouquet": self.keyUp
		}, -1)

	def keyDown(self):
		current = self["config"].getCurrentIndex()
		self["config"].setCurrentIndex(current+20)

	def keyUp(self):
		current = self["config"].getCurrentIndex()
		self["config"].setCurrentIndex(current-20)

	def keyOK(self):
		if config.mediaportal.watchlistpath.value[-1] != '/':
			config.mediaportal.watchlistpath.value = config.mediaportal.watchlistpath.value + '/'
		if config.mediaportal.storagepath.value[-1] != '/':
			config.mediaportal.storagepath.value = config.mediaportal.storagepath.value + '/'
		if (config.mediaportal.showporn.value == False and config.mediaportal.filter.value == 'Porn'):
			config.mediaportal.filter.value = 'ALL'
		if (config.mediaportal.showgrauzone.value == False and config.mediaportal.filter.value == 'Grauzone'):
			config.mediaportal.filter.value = 'ALL'

		if (config.mediaportal.showgrauzone.value and not config.mediaportal.pingrauzone.value):
			self.a = str(random.randint(1,9))
			self.b = str(random.randint(0,9))
			self.c = str(random.randint(0,9))
			self.d = str(random.randint(0,9))
			message = "Some of the plugins may not be legally used in your country!\n\nIf you accept this then enter the following code now:\n\n%s %s %s %s" % (self.a,self.b,self.c,self.d)
			self.session.openWithCallback(self.keyOK2,MessageBox,_(message), MessageBox.TYPE_YESNO)
		else:
			self.confSave()

	def keyOK2(self, answer):
		if answer is True:
			self.session.openWithCallback(self.validcode, PinInput, pinList = [(int(self.a+self.b+self.c+self.d))], triesEntry = self.getTriesEntry(), title = _("Please enter the correct code"), windowTitle = _("Enter code"))
		else:
			config.mediaportal.showgrauzone.value = False
			config.mediaportal.showgrauzone.save()
			config.mediaportal.pingrauzone.value = False
			config.mediaportal.pingrauzone.save()
			self.confSave()

	def getTriesEntry(self):
		return config.ParentalControl.retries.setuppin

	def validcode(self, code):
		if code:
			config.mediaportal.pingrauzone.value = True
			config.mediaportal.pingrauzone.save()
			self.confSave()
		else:
			config.mediaportal.showgrauzone.value = False
			config.mediaportal.showgrauzone.save()
			config.mediaportal.pingrauzone.value = False
			config.mediaportal.pingrauzone.save()
			self.confSave()

	def confSave(self):
		for x in self["config"].list:
			x[1].save()
		configfile.save()
		self.close()

class HelpScreen(Screen):

	def __init__(self, session):
		self.session = session

		self.plugin_path = mp_globals.pluginPath
		self.skin_path = mp_globals.pluginPath + "/skins"

		path = "%s/%s/help.xml" % (self.skin_path, config.mediaportal.skin.value)
		if not fileExists(path):
			path = self.skin_path + "/original/help.xml"

		with open(path, "r") as f:
			self.skin = f.read()
			f.close()

		Screen.__init__(self, session)

		self["actions"]  = ActionMap(["OkCancelActions", "ShortcutActions", "WizardActions", "ColorActions", "SetupActions", "NumberActions", "MenuActions"], {
			"ok"    : self.keyOK,
			"cancel": self.keyCancel
		}, -1)

	def keyOK(self):
		self.close()

	def keyCancel(self):
		self.close()

class chooseMenuList(MenuList):
	def __init__(self, list):
		MenuList.__init__(self, list, True, eListboxPythonMultiContent)
		self.l.setFont(0, gFont("mediaportal", 20))
		self.l.setItemHeight(44)

class haupt_Screen(Screen, ConfigListScreen):
	def __init__(self, session):
		self.session = session

		self.plugin_path = mp_globals.pluginPath
		self.skin_path = mp_globals.pluginPath + "/skins"

		path = "%s/%s/haupt_Screen.xml" % (self.skin_path, config.mediaportal.skin.value)
		if not fileExists(path):
			path = self.skin_path + "/original/haupt_Screen.xml"

		with open(path, "r") as f:
			self.skin = f.read()
			f.close()

		Screen.__init__(self, session)

		registerFont("/usr/lib/enigma2/python/Plugins/Extensions/MediaPortal/resources/mediaportal.ttf", "mediaportal", 100, False)

		self["actions"]  = ActionMap(["OkCancelActions", "ShortcutActions", "WizardActions", "ColorActions", "SetupActions", "NumberActions", "MenuActions", "EPGSelectActions", "HelpActions"], {
			"ok"    : self.keyOK,
			"up"    : self.keyUp,
			"down"  : self.keyDown,
			"cancel": self.keyCancel,
			"left"  : self.keyLeft,
			"right" : self.keyRight,
			"nextBouquet" :	self.keyPageDown,
			"prevBouquet" :	self.keyPageUp,
			"menu" : self.keySetup,
			"info" : self.showPorn,
			"displayHelp" : self.keyHelp
		}, -1)

		self['title'] = Label("MediaPortal v%s" % config.mediaportal.versiontext.value)

		self['name'] = Label("Plugin Auswahl")

		self['funsport'] = chooseMenuList([])
		self['Funsport'] = Label("Fun/Sport")

		self['grauzone'] = chooseMenuList([])
		self['Grauzone'] = Label("")

		self['mediatheken'] = chooseMenuList([])
		self['Mediatheken'] = Label("Mediatheken")

		self['porn'] = chooseMenuList([])
		self['Porn'] = Label("")

		self.currentlist = "porn"

		self.onLayoutFinish.append(self.layoutFinished)

	def layoutFinished(self):
		if config.mediaportal.autoupdate.value:
			checkupdate(self.session).checkforupdate()

		self.mediatheken = []
		self.grauzone = []
		self.funsport = []
		self.porn = []

		# Mediatheken
		if config.mediaportal.showMyvideo.value:
			self.mediatheken.append(self.hauptListEntry("MyVideo", "myvideo"))
		if config.mediaportal.showMoovizon.value:
			self.mediatheken.append(self.hauptListEntry("Moovizon", "moovizon"))
		if config.mediaportal.showKinderKino.value:
			self.mediatheken.append(self.hauptListEntry("KinderKino", "kinderkino"))
		if config.mediaportal.showNetzKino.value:
			self.mediatheken.append(self.hauptListEntry("NetzKino", "netzkino"))
		if config.mediaportal.showtivi.value:
			self.mediatheken.append(self.hauptListEntry("Tivi", "tivi"))
		if config.mediaportal.showkika.value:
			self.mediatheken.append(self.hauptListEntry("KIKA+", "kika"))
		if config.mediaportal.showVoxnow.value:
			self.mediatheken.append(self.hauptListEntry("VOXNOW", "voxnow"))
		if config.mediaportal.showRTLnow.value:
			self.mediatheken.append(self.hauptListEntry("RTLNOW", "rtlnow"))
		if config.mediaportal.showNTVnow.value:
			self.mediatheken.append(self.hauptListEntry("N-TVNOW", "ntvnow"))
		if config.mediaportal.showRTL2now.value:
			self.mediatheken.append(self.hauptListEntry("RTL2NOW", "rtl2now"))
		if config.mediaportal.showRTLnitro.value:
			self.mediatheken.append(self.hauptListEntry("RTLNITRONOW", "rtlnitro"))
		if config.mediaportal.showSUPERRTLnow.value:
			self.mediatheken.append(self.hauptListEntry("SUPERRTLNOW", "superrtlnow"))
		if config.mediaportal.showZDF.value:
			self.mediatheken.append(self.hauptListEntry("ZDF Mediathek", "zdf"))
		if config.mediaportal.showORF.value:
			self.mediatheken.append(self.hauptListEntry("ORF TVthek", "orf"))
		if config.mediaportal.showSRF.value:
			self.mediatheken.append(self.hauptListEntry("SRF Player", "srf"))
		if config.mediaportal.show4Players.value:
			self.mediatheken.append(self.hauptListEntry("4Players", "4players"))
		if config.mediaportal.showGIGA.value:
			self.mediatheken.append(self.hauptListEntry("GIGA.de", "gigatv"))
		if config.mediaportal.showaudi.value:
			self.mediatheken.append(self.hauptListEntry("Audi.tv", "auditv"))
		if config.mediaportal.showgronkh.value:
			self.mediatheken.append(self.hauptListEntry("gronkh.de", "gronkh"))
		if config.mediaportal.showappletrailers.value:
			self.mediatheken.append(self.hauptListEntry("AppleTrailer", "appletrailers"))
		if config.mediaportal.showAutoBild.value:
			self.mediatheken.append(self.hauptListEntry("AutoBild", "autobild"))
		if config.mediaportal.showCczwei.value:
			self.mediatheken.append(self.hauptListEntry("CCZwei", "cczwei"))
		if config.mediaportal.showDoku.value:
			self.mediatheken.append(self.hauptListEntry("Doku.me", "doku"))
		if config.mediaportal.showDOKUh.value:
			self.mediatheken.append(self.hauptListEntry("DOKUh", "dokuh"))
		if config.mediaportal.showDokuHouse.value:
			self.mediatheken.append(self.hauptListEntry("DokuHouse", "dokuhouse"))
		if config.mediaportal.showDokuStream.value:
			self.mediatheken.append(self.hauptListEntry("DokuStream", "dokustream"))
		if config.mediaportal.showDsc.value:
			self.mediatheken.append(self.hauptListEntry("Dreamscreencast", "dreamscreencast"))
		if config.mediaportal.showTrailer.value:
			self.mediatheken.append(self.hauptListEntry("Filmtrailer", "trailer"))
		if config.mediaportal.showFocus.value:
			self.mediatheken.append(self.hauptListEntry("Focus", "focus"))
		if config.mediaportal.showMahlzeitTV.value:
			self.mediatheken.append(self.hauptListEntry("mahlzeit.tv", "mahlzeit"))
		if config.mediaportal.showFiwitu.value:
			self.mediatheken.append(self.hauptListEntry("fiwitu.tv", "fiwitu"))
		if config.mediaportal.showScienceTV.value:
			self.mediatheken.append(self.hauptListEntry("ScienceTV", "sciencetv"))
		if config.mediaportal.showSportBild.value:
			self.mediatheken.append(self.hauptListEntry("SportBild", "sportbild"))
		if config.mediaportal.showWrestlingnetwork.value:
			self.mediatheken.append(self.hauptListEntry("Wrestlingnetwork", "wrestlingnetwork"))
		if config.mediaportal.showretrotv.value:
			self.mediatheken.append(self.hauptListEntry("retro-tv", "retrotv"))
		if config.mediaportal.showgalileovl.value:
			self.mediatheken.append(self.hauptListEntry("Galileo-Videolexikon", "galileovl"))
		if config.mediaportal.showsport1fm.value:
			self.mediatheken.append(self.hauptListEntry("Sport1.fm", "sport1fm"))
		if config.mediaportal.showARD.value:
			self.mediatheken.append(self.hauptListEntry("ARD Mediathek", "ard"))
		if astModule:
			if config.mediaportal.showHeiseVideo.value:
				self.mediatheken.append(self.hauptListEntry("heiseVIDEO", "heisevideo"))

		# Grauzone
		if config.mediaportal.showgrauzone.value:
			if config.mediaportal.showSzeneStreams.value:
				self.grauzone.append(self.hauptListEntry("SzeneStreams", "szenestreams"))
			if config.mediaportal.showmlehd.value:
				self.grauzone.append(self.hauptListEntry("MLE-HD", "mlehd"))
			if config.mediaportal.showStreamOase.value:
				self.grauzone.append(self.hauptListEntry("StreamOase", "streamoase"))
			if config.mediaportal.showMEHD.value:
				self.grauzone.append(self.hauptListEntry("My-Entertainment", "mehd"))
			if config.mediaportal.showM4k.value:
				self.grauzone.append(self.hauptListEntry("Movie4k", "movie4k"))
			if config.mediaportal.showKinox.value:
				self.grauzone.append(self.hauptListEntry("Kinox", "kinox"))
			if config.mediaportal.showCinestream.value:
				self.grauzone.append(self.hauptListEntry("Cinestream", "cinestream"))
			if config.mediaportal.showKinoKiste.value:
				self.grauzone.append(self.hauptListEntry("KinoKiste", "kinokiste"))
			if config.mediaportal.showIStream.value:
				self.grauzone.append(self.hauptListEntry("IStream", "istream"))
			if config.mediaportal.showBs.value:
				self.grauzone.append(self.hauptListEntry("Burning-Series", "burningseries"))
			if config.mediaportal.showBaskino.value:
				self.grauzone.append(self.hauptListEntry("Baskino", "baskino"))
			if config.mediaportal.showprimewire.value:
				self.grauzone.append(self.hauptListEntry("PrimeWire", "primewire"))
			if config.mediaportal.showM4kWatchlist.value:
				self.grauzone.append(self.hauptListEntry("Movie4k Watchlist", "movie4kwatchlist"))
			if config.mediaportal.showKinoxWatchlist.value:
				self.grauzone.append(self.hauptListEntry("Kinox Watchlist", "kinoxwatchlist"))
			if config.mediaportal.showDdlme.value:
				self.grauzone.append(self.hauptListEntry("ddl.me", "ddl_me"))
			if config.mediaportal.showMovie25.value:
				self.grauzone.append(self.hauptListEntry("Movie25", "movie25"))
			if config.mediaportal.showWatchseries.value:
				self.grauzone.append(self.hauptListEntry("Watchseries", "watchseries"))
			#if config.mediaportal.showViewster.value:
			#	self.grauzone.append(self.hauptListEntry("Viewster", "viewster"))
			if config.mediaportal.showVibeo.value:
				self.grauzone.append(self.hauptListEntry("Vibeo", "vibeo"))

		# Fun / Sport
		if config.mediaportal.showAllMusicHouse.value:
			self.funsport.append(self.hauptListEntry("AllMusicHouse", "allmusichouse"))
		if config.mediaportal.showputpattv.value:
			self.funsport.append(self.hauptListEntry("putpat.tv", "putpattv"))
		if config.mediaportal.showLaola1.value:
			self.funsport.append(self.hauptListEntry("Laola1", "laola1"))
		if config.mediaportal.showNhl.value:
			self.funsport.append(self.hauptListEntry("NHL", "nhl"))
		if config.mediaportal.showRofl.value:
			self.funsport.append(self.hauptListEntry("Rofl.to", "rofl"))
		if config.mediaportal.showFail.value:
			self.funsport.append(self.hauptListEntry("Fail.to", "fail"))
		if config.mediaportal.showLiveLeak.value:
			self.funsport.append(self.hauptListEntry("LiveLeak", "liveleak"))
		if config.mediaportal.showFilmOn.value:
			self.funsport.append(self.hauptListEntry("FilmOn", "filmon"))
		if config.mediaportal.showTvkino.value:
			self.funsport.append(self.hauptListEntry("TV-Kino", "tvkino"))
		if config.mediaportal.showRadio.value:
			self.funsport.append(self.hauptListEntry("Radio.de", "radiode"))
		if config.mediaportal.showSpobox.value:
			self.funsport.append(self.hauptListEntry("Spobox", "spobox"))
		if config.mediaportal.showHoerspielHouse.value:
			self.funsport.append(self.hauptListEntry("HörspielHouse", "hoerspielhouse"))
		if config.mediaportal.showHoerspielChannels.value:
			self.funsport.append(self.hauptListEntry("Hörspiel-Channels", "hoerspielchannels"))
		if config.mediaportal.showCarChannels.value:
			self.funsport.append(self.hauptListEntry("CAR-Channels", "carchannels"))
		if config.mediaportal.showGameChannels.value:
			self.funsport.append(self.hauptListEntry("GAME-Channels", "gamechannels"))
		if config.mediaportal.showMusicChannels.value:
			self.funsport.append(self.hauptListEntry("MUSIC-Channels", "musicchannels"))
		if config.mediaportal.showUserChannels.value:
			self.funsport.append(self.hauptListEntry("USER-Channels", "userchannels"))
		if config.mediaportal.showYoutube.value:
			self.funsport.append(self.hauptListEntry("YouTube", "youtube"))
		if config.mediaportal.showClipfish.value:
			self.funsport.append(self.hauptListEntry("Clipfish", "clipfish"))
		if config.mediaportal.showRan.value:
			self.funsport.append(self.hauptListEntry("Ran.de", "ran"))
		if config.mediaportal.showGEOde.value:
			self.funsport.append(self.hauptListEntry("GEO.de", "geo_de"))
		if config.mediaportal.showTeledunet.value:
			self.funsport.append(self.hauptListEntry("Teledunet", "teledunet"))
		if config.mediaportal.showDeluxemusic.value:
			self.funsport.append(self.hauptListEntry("Deluxemusic", "deluxemusic"))
		if config.mediaportal.showNuna.value:
			self.funsport.append(self.hauptListEntry("Nuna", "nuna"))
		if config.mediaportal.showMyvideoTop100.value:
			self.funsport.append(self.hauptListEntry("Myvideo Top 100", "myvideotop100"))
		if config.mediaportal.showMTVdeCharts.value:
			self.funsport.append(self.hauptListEntry("MTV.de Charts", "mtvdecharts"))
		if config.mediaportal.showgrauzone.value:
			if config.mediaportal.showMusicstreamcc.value:
				self.funsport.append(self.hauptListEntry("Musicstream.cc", "musicstreamcc"))
			if config.mediaportal.showEighties.value:
				self.funsport.append(self.hauptListEntry("80s & 90s Music", "eighties"))
			if config.mediaportal.showCanna.value:
				self.funsport.append(self.hauptListEntry("Canna-Power", "canna"))
			if config.mediaportal.showSongsto.value:
				self.funsport.append(self.hauptListEntry("Songs.to", "songsto"))

		# porn
		if config.mediaportal.showporn.value:
			if config.mediaportal.show4tube.value:
				self.porn.append(self.hauptListEntry("4Tube", "4tube"))
			if config.mediaportal.showahme.value:
				self.porn.append(self.hauptListEntry("Ah-Me", "ahme"))
			if config.mediaportal.showamateurporn.value:
				self.porn.append(self.hauptListEntry("AmateurPorn", "amateurporn"))
			if config.mediaportal.showbeeg.value:
				self.porn.append(self.hauptListEntry("beeg", "beeg"))
			if config.mediaportal.showdrtuber.value:
				self.porn.append(self.hauptListEntry("DrTuber", "drtuber"))
			if config.mediaportal.showelladies.value:
				self.porn.append(self.hauptListEntry("El-Ladies", "elladies"))
			if config.mediaportal.showeporner.value:
				self.porn.append(self.hauptListEntry("Eporner", "eporner"))
			if config.mediaportal.showeroprofile.value:
				self.porn.append(self.hauptListEntry("EroProfile", "eroprofile"))
			if config.mediaportal.showextremetube.value:
				self.porn.append(self.hauptListEntry("ExtremeTube", "extremetube"))
			if config.mediaportal.showgrauzone.value:
				if config.mediaportal.showfreeomovie.value:
					self.porn.append(self.hauptListEntry("Free Online Movies", "freeomovie"))
				if config.mediaportal.showgstreaminxxx.value:
					self.porn.append(self.hauptListEntry("G-Stream-XXX", "gstreaminxxx"))
			if config.mediaportal.showhdporn.value:
				self.porn.append(self.hauptListEntry("HDPorn", "hdporn"))
			if config.mediaportal.showhotshame.value:
				self.porn.append(self.hauptListEntry("hotshame", "hotshame"))
			if config.mediaportal.showgrauzone.value:
				if config.mediaportal.showmegaskanks.value:
					self.porn.append(self.hauptListEntry("MegaSkanks", "megaskanks"))
				if config.mediaportal.showIStreamPorn.value:
					self.porn.append(self.hauptListEntry("IStream-XXX", "istreamporn"))
				if config.mediaportal.showM4kPorn.value:
					self.porn.append(self.hauptListEntry("Movie4k-XXX", "movie4kporn"))
				if config.mediaportal.showparadisehill.value:
					self.porn.append(self.hauptListEntry("ParadiseHill", "paradisehill"))
			if config.mediaportal.showpinkrod.value:
				self.porn.append(self.hauptListEntry("Pinkrod", "pinkrod"))
			if config.mediaportal.showgrauzone.value:
				if config.mediaportal.showplayporn.value:
					self.porn.append(self.hauptListEntry("PlayPorn", "playporn"))
			if config.mediaportal.showpornerbros.value:
				self.porn.append(self.hauptListEntry("PornerBros", "pornerbros"))
			if config.mediaportal.showPornhub.value:
				self.porn.append(self.hauptListEntry("Pornhub", "pornhub"))
			if config.mediaportal.showgrauzone.value:
				if config.mediaportal.showpornmvz.value:
					self.porn.append(self.hauptListEntry("PORNMVZ", "pornmvz"))
				if config.mediaportal.showpornostreams.value:
					self.porn.append(self.hauptListEntry("PornoStreams", "pornostreams"))
			if config.mediaportal.showpornrabbit.value:
				self.porn.append(self.hauptListEntry("PornRabbit", "pornrabbit"))
			if config.mediaportal.showrealgfporn.value:
				self.porn.append(self.hauptListEntry("RealGFPorn", "realgfporn"))
			if config.mediaportal.showredtube.value:
				self.porn.append(self.hauptListEntry("RedTube", "redtube"))
			if config.mediaportal.showsexxxhd.value:
				self.porn.append(self.hauptListEntry("SeXXX-HD", "sexxxhd"))
			if config.mediaportal.showsunporno.value:
				self.porn.append(self.hauptListEntry("SunPorno", "sunporno"))
			if config.mediaportal.showthenewporn.value:
				self.porn.append(self.hauptListEntry("TheNewPorn", "thenewporn"))
			if config.mediaportal.showupdatetube.value:
				self.porn.append(self.hauptListEntry("UpdateTube", "updatetube"))
			if config.mediaportal.showwetplace.value:
				self.porn.append(self.hauptListEntry("WetPlace", "wetplace"))
			if config.mediaportal.showXhamster.value:
				self.porn.append(self.hauptListEntry("xHamster", "xhamster"))
			if config.mediaportal.showgrauzone.value:
				if config.mediaportal.showxxxsave.value:
					self.porn.append(self.hauptListEntry("XXXSaVe", "xxxsave"))
			if config.mediaportal.showyouporn.value:
				self.porn.append(self.hauptListEntry("YouPorn", "youporn"))

		if len(self.porn) < 1:
			self['Porn'].hide()
		else:
			self['Porn'].setText("Porn")

		if len(self.grauzone) < 1:
			self['Grauzone'].hide()
		else:
			self['Grauzone'].setText("Grauzone")

		self.mediatheken.sort(key=lambda t : tuple(t[0][0].lower()))
		self.grauzone.sort(key=lambda t : tuple(t[0][0].lower()))
		self.funsport.sort(key=lambda t : tuple(t[0][0].lower()))
		self.porn.sort(key=lambda t : tuple(t[0][0].lower()))

		self["mediatheken"].setList(self.mediatheken)
		self["mediatheken"].l.setItemHeight(44)
		self["grauzone"].setList(self.grauzone)
		self["grauzone"].l.setItemHeight(44)
		self["funsport"].setList(self.funsport)
		self["funsport"].l.setItemHeight(44)
		self["porn"].setList(self.porn)
		self["porn"].l.setItemHeight(44)
		self.keyRight()

	def hauptListEntry(self, name, jpg):
		res = [(name, jpg)]
		icon = "/usr/lib/enigma2/python/Plugins/Extensions/MediaPortal/icons/%s.png" % jpg
		if not fileExists(icon):
			icon = "/usr/lib/enigma2/python/Plugins/Extensions/MediaPortal/icons/no_icon.png"
		res.append(MultiContentEntryPixmapAlphaTest(pos=(0, 1), size=(75, 40), png=loadPNG(icon)))
		res.append(MultiContentEntryText(pos=(80, 10), size=(200, 40), font=0, text=name, flags=RT_HALIGN_LEFT))
		return res

	def showPorn(self):
		if config.mediaportal.showporn.value:
			config.mediaportal.showporn.value = False
			config.mediaportal.showporn.save()
			configfile.save()
			self.restart()
		else:
			self.session.openWithCallback(self.showPornOK, PinInput, pinList = [(config.mediaportal.pincode.value)], triesEntry = self.getTriesEntry(), title = _("Please enter the correct pin code"), windowTitle = _("Enter pin code"))

	def showPornOK(self, pincode):
		if pincode:
			config.mediaportal.showporn.value = True
			config.mediaportal.showporn.save()
			configfile.save()
			self.restart()

	def keySetup(self):
		if config.mediaportal.setuppin.value:
			self.session.openWithCallback(self.pinok, PinInput, pinList = [(config.mediaportal.pincode.value)], triesEntry = self.getTriesEntry(), title = _("Please enter the correct pin code"), windowTitle = _("Enter pin code"))
		else:
			self.session.openWithCallback(self.restart, hauptScreenSetup)

	def keyHelp(self):
		self.session.open(HelpScreen)

	def getTriesEntry(self):
		return config.ParentalControl.retries.setuppin

	def pinok(self, pincode):
		if pincode:
			self.session.openWithCallback(self.restart, hauptScreenSetup)

	def keyUp(self):
		exist = self[self.currentlist].getCurrent()
		if exist == None:
			return
		self[self.currentlist].up()
		auswahl = self[self.currentlist].getCurrent()[0][0]
		self.title = auswahl
		self['name'].setText(auswahl)

	def keyDown(self):
		exist = self[self.currentlist].getCurrent()
		if exist == None:
			return
		self[self.currentlist].down()
		auswahl = self[self.currentlist].getCurrent()[0][0]
		self.title = auswahl
		self['name'].setText(auswahl)

	def keyPageUp(self):
		self[self.currentlist].pageUp()

	def keyPageDown(self):
		self[self.currentlist].pageDown()

	def keyRight(self):
		self.cur_idx = self[self.currentlist].getSelectedIndex()
		self["mediatheken"].selectionEnabled(0)
		self["grauzone"].selectionEnabled(0)
		self["funsport"].selectionEnabled(0)
		self["porn"].selectionEnabled(0)
		if self.currentlist == "mediatheken":
			if len(self.grauzone) > 0:
				self["grauzone"].selectionEnabled(1)
				self.currentlist = "grauzone"
				cnt_tmp_ls = len(self.grauzone)
			elif len(self.funsport) > 0:
				self["funsport"].selectionEnabled(1)
				self.currentlist = "funsport"
				cnt_tmp_ls = len(self.funsport)
			elif len(self.porn) > 0:
				self["porn"].selectionEnabled(1)
				self.currentlist = "porn"
				cnt_tmp_ls = len(self.porn)
			else:
				self["mediatheken"].selectionEnabled(1)
				self.currentlist = "mediatheken"
				cnt_tmp_ls = len(self.mediatheken)
		elif self.currentlist == "grauzone":
			if len(self.funsport) > 0:
				self["funsport"].selectionEnabled(1)
				self.currentlist = "funsport"
				cnt_tmp_ls = len(self.funsport)
			elif len(self.porn) > 0:
				self["porn"].selectionEnabled(1)
				self.currentlist = "porn"
				cnt_tmp_ls = len(self.porn)
			elif len(self.mediatheken) > 0:
				self["mediatheken"].selectionEnabled(1)
				self.currentlist = "mediatheken"
				cnt_tmp_ls = len(self.mediatheken)
			else:
				self["grauzone"].selectionEnabled(1)
				self.currentlist = "grauzone"
				cnt_tmp_ls = len(self.grauzone)
		elif self.currentlist == "funsport":
			if len(self.porn) > 0:
				self["porn"].selectionEnabled(1)
				self.currentlist = "porn"
				cnt_tmp_ls = len(self.porn)
			elif len(self.mediatheken) > 0:
				self["mediatheken"].selectionEnabled(1)
				self.currentlist = "mediatheken"
				cnt_tmp_ls = len(self.mediatheken)
			elif len(self.grauzone) > 0:
				self["grauzone"].selectionEnabled(1)
				self.currentlist = "grauzone"
				cnt_tmp_ls = len(self.grauzone)
			else:
				self["funsport"].selectionEnabled(1)
				self.currentlist = "funsport"
				cnt_tmp_ls = len(self.funsport)
		elif self.currentlist == "porn":
			if len(self.mediatheken) > 0:
				self["mediatheken"].selectionEnabled(1)
				self.currentlist = "mediatheken"
				cnt_tmp_ls = len(self.mediatheken)
			elif len(self.grauzone) > 0:
				self["grauzone"].selectionEnabled(1)
				self.currentlist = "grauzone"
				cnt_tmp_ls = len(self.grauzone)
			elif len(self.funsport) > 0:
				self["funsport"].selectionEnabled(1)
				self.currentlist = "funsport"
				cnt_tmp_ls = len(self.funsport)
			else:
				self["porn"].selectionEnabled(1)
				self.currentlist = "porn"
				cnt_tmp_ls = len(self.porn)

		cnt_tmp_ls = int(cnt_tmp_ls)
		if int(self.cur_idx) < int(cnt_tmp_ls):
			self[self.currentlist].moveToIndex(int(self.cur_idx))
		else:
			idx = int(cnt_tmp_ls) -1
			self[self.currentlist].moveToIndex(int(idx))

		if cnt_tmp_ls > 0:
			auswahl = self[self.currentlist].getCurrent()[0][0]
			self.title = auswahl
			self['name'].setText(auswahl)

	def keyLeft(self):
		self.cur_idx = self[self.currentlist].getSelectedIndex()
		self["mediatheken"].selectionEnabled(0)
		self["grauzone"].selectionEnabled(0)
		self["funsport"].selectionEnabled(0)
		self["porn"].selectionEnabled(0)
		if self.currentlist == "porn":
			if len(self.funsport) > 0:
				self["funsport"].selectionEnabled(1)
				self.currentlist = "funsport"
				cnt_tmp_ls = len(self.funsport)
			elif len(self.grauzone) > 0:
				self["grauzone"].selectionEnabled(1)
				self.currentlist = "grauzone"
				cnt_tmp_ls = len(self.grauzone)
			elif len(self.mediatheken) > 0:
				self["mediatheken"].selectionEnabled(1)
				self.currentlist = "mediatheken"
				cnt_tmp_ls = len(self.mediatheken)
			else:
				self["porn"].selectionEnabled(1)
				self.currentlist = "porn"
				cnt_tmp_ls = len(self.porn)
		elif self.currentlist == "funsport":
			if len(self.grauzone) > 0:
				self["grauzone"].selectionEnabled(1)
				self.currentlist = "grauzone"
				cnt_tmp_ls = len(self.grauzone)
			elif len(self.mediatheken) > 0:
				self["mediatheken"].selectionEnabled(1)
				self.currentlist = "mediatheken"
				cnt_tmp_ls = len(self.mediatheken)
			elif len(self.porn) > 0:
				self["porn"].selectionEnabled(1)
				self.currentlist = "porn"
				cnt_tmp_ls = len(self.porn)
			else:
				self["funsport"].selectionEnabled(1)
				self.currentlist = "funsport"
				cnt_tmp_ls = len(self.funsport)
		elif self.currentlist == "grauzone":
			if len(self.mediatheken) > 0:
				self["mediatheken"].selectionEnabled(1)
				self.currentlist = "mediatheken"
				cnt_tmp_ls = len(self.mediatheken)
			elif len(self.porn) > 0:
				self["porn"].selectionEnabled(1)
				self.currentlist = "porn"
				cnt_tmp_ls = len(self.porn)
			elif len(self.funsport) > 0:
				self["funsport"].selectionEnabled(1)
				self.currentlist = "funsport"
				cnt_tmp_ls = len(self.funsport)
			else:
				self["grauzone"].selectionEnabled(1)
				self.currentlist = "grauzone"
				cnt_tmp_ls = len(self.grauzone)
		elif self.currentlist == "mediatheken":
			if len(self.porn) > 0:
				self["porn"].selectionEnabled(1)
				self.currentlist = "porn"
				cnt_tmp_ls = len(self.porn)
			elif len(self.funsport) > 0:
				self["funsport"].selectionEnabled(1)
				self.currentlist = "funsport"
				cnt_tmp_ls = len(self.funsport)
			elif len(self.grauzone) > 0:
				self["grauzone"].selectionEnabled(1)
				self.currentlist = "grauzone"
				cnt_tmp_ls = len(self.grauzone)
			else:
				self["mediatheken"].selectionEnabled(1)
				self.currentlist = "mediatheken"
				cnt_tmp_ls = len(self.mediatheken)

		cnt_tmp_ls = int(cnt_tmp_ls)
		print self.cur_idx, cnt_tmp_ls
		if int(self.cur_idx) < int(cnt_tmp_ls):
			self[self.currentlist].moveToIndex(int(self.cur_idx))
		else:
			idx = int(cnt_tmp_ls) -1
			self[self.currentlist].moveToIndex(int(idx))

		if cnt_tmp_ls > 0:
			auswahl = self[self.currentlist].getCurrent()[0][0]
			self.title = auswahl
			self['name'].setText(auswahl)

	def keyOK(self):
		exist = self[self.currentlist].getCurrent()
		if exist == None:
			return
		print self.currentlist
		auswahl = self[self.currentlist].getCurrent()[0][0]
		icon = self[self.currentlist].getCurrent()[0][1]
		mp_globals.activeIcon = icon
		self.pornscreen = None
		self.cat = ""
		print auswahl
		if auswahl == "Doku.me":
			self.session.open(dokuScreen)
		elif auswahl == "Rofl.to":
			self.session.open(roflScreen)
		elif auswahl == "Fail.to":
			self.session.open(failScreen)
		elif auswahl == "KinderKino":
			self.session.open(kinderKinoScreen)
		elif auswahl == "MyVideo":
			self.session.open(myVideoGenreScreen)
		elif auswahl == "SportBild":
			self.session.open(sportBildScreen)
		elif auswahl == "Laola1":
			self.session.open(laolaVideosOverviewScreen)
		elif auswahl == "KinoKiste":
			self.session.open(kinokisteGenreScreen)
		elif auswahl == "Burning-Series":
			self.session.open(bsMain)
		elif auswahl == "PrimeWire":
			self.session.open(PrimeWireGenreScreen)
		elif auswahl == "Focus":
			self.session.open(focusGenre)
		elif auswahl == "FilmOn":
			self.session.open(filmON)
		elif auswahl == "NetzKino":
			self.session.open(netzKinoGenreScreen)
		elif auswahl == "Spobox":
			self.session.open(spoboxGenreScreen)
		elif auswahl == "Radio.de":
			self.session.open(Radiode)
		elif auswahl == "CCZwei":
			self.session.open(cczwei)
		elif auswahl == "Filmtrailer":
			self.session.open(trailer)
		elif auswahl == "Baskino":
			self.session.open(baskino)
		elif auswahl == "Kinox":
			self.session.open(kxMain)
		elif auswahl == "Kinox Watchlist":
			self.session.open(kxWatchlist)
		elif auswahl == "Dreamscreencast":
			self.session.open(dreamscreencast)
		elif auswahl == "TV-Kino":
			self.session.open(tvkino)
		elif auswahl == "StreamOase":
			self.session.open(oasetvGenreScreen)
		elif auswahl == "AutoBild":
			self.session.open(autoBildGenreScreen)
		elif auswahl == "NHL":
			self.session.open(nhlGenreScreen)
		elif auswahl == "4Players":
			self.session.open(forPlayersGenreScreen)
		elif auswahl == "GIGA.de":
			self.session.open(gigatvGenreScreen)
		elif auswahl == "Audi.tv":
			self.session.open(auditvGenreScreen)
		elif auswahl == "gronkh.de":
			self.session.open(gronkhGenreScreen)
		elif auswahl == "Tivi":
			self.session.open(tiviGenreListeScreen)
		elif auswahl == "My-Entertainment":
			self.session.open(showMEHDGenre)
		elif auswahl == "Songs.to":
			self.session.open(showSongstoGenre)
		elif auswahl == "Movie4k":
			self.session.open(m4kGenreScreen, "default")
		elif auswahl == "Movie4k Watchlist":
			self.session.open(m4kWatchlist)
		elif auswahl == "IStream":
			self.session.open(showIStreamGenre, "default")
		elif auswahl == "mahlzeit.tv":
			self.session.open(mahlzeitMainScreen)
		elif auswahl == "fiwitu.tv":
			self.session.open(fiwituGenreScreen)
		elif auswahl == "AppleTrailer":
			self.session.open(appletrailersGenreScreen)
		elif auswahl == "DOKUh":
			self.session.open(showDOKUHGenre)
		elif auswahl == "DokuHouse":
			self.session.open(show_DH_Genre)
		elif auswahl == "AllMusicHouse":
			self.session.open(show_AMH_Genre)
		elif auswahl == "putpat.tv":
			self.session.open(putpattvGenreScreen)
		elif auswahl == "LiveLeak":
			self.session.open(LiveLeakScreen)
		elif auswahl == "DokuStream":
			self.session.open(show_DS_Genre)
		elif auswahl == "ScienceTV":
			self.session.open(scienceTvGenreScreen)
		elif auswahl == "SzeneStreams":
			self.session.open(SzeneStreamsGenreScreen)
		elif auswahl == "MLE-HD":
			self.session.open(mlehdGenreScreen)
		elif auswahl == "HörspielHouse":
			self.session.open(show_HSH_Genre)
		elif auswahl == "KIKA+":
			self.session.open(kikaGenreScreen)
		elif auswahl == "Hörspiel-Channels":
			self.session.open(show_HSC_Genre)
		elif auswahl == "CAR-Channels":
			self.session.open(show_CAR_Genre)
		elif auswahl == "GAME-Channels":
			self.session.open(show_GAME_Genre)
		elif auswahl == "MUSIC-Channels":
			self.session.open(show_MUSIC_Genre)
		elif auswahl == "USER-Channels":
			self.session.open(show_USER_Genre)
		elif auswahl == "YouTube":
			self.session.open(youtubeGenreScreen)
		elif auswahl == "Clipfish":
			self.session.open(show_CF_Genre)
		elif auswahl == "ddl.me":
			self.session.open(show_DDLME_Genre)
		elif auswahl == "Canna-Power":
			self.session.open(cannaGenreScreen)
		elif auswahl == "Ran.de":
			self.session.open(ranGenreScreen)
		elif auswahl == "Movie25":
			self.session.open(movie25GenreScreen)
		elif auswahl == "80s & 90s Music":
			self.session.open(eightiesGenreScreen)
		elif auswahl == "GEO.de":
			self.session.open(GEOdeGenreScreen)
		elif auswahl == "Teledunet":
			self.session.open(teleGenreScreen)
		elif auswahl == "Deluxemusic":
			self.session.open(deluxemusicGenreScreen)
		elif auswahl == "Nuna":
			self.session.open(nunaGenreScreen)
		elif auswahl == "Watchseries":
			self.session.open(watchseriesGenreScreen)
		elif auswahl == "Myvideo Top 100":
			self.session.open(myvideoTop100GenreScreen)
		elif auswahl == "MTV.de Charts":
			self.session.open(MTVdeChartsGenreScreen)
		elif auswahl == "Musicstream.cc":
			self.session.open(show_MSCC_Genre)
		elif auswahl == "Vibeo":
			self.session.open(vibeoFilmListeScreen)
		elif auswahl == "heiseVIDEO":
			self.session.open(HeiseTvGenreScreen)

		# mediatheken
		elif auswahl == "VOXNOW":
			self.session.open(VOXnowGenreScreen)
		elif auswahl == "RTLNOW":
			self.session.open(RTLnowGenreScreen)
		elif auswahl == "N-TVNOW":
			self.session.open(NTVnowGenreScreen)
		elif auswahl == "RTL2NOW":
			self.session.open(RTL2nowGenreScreen)
		elif auswahl == "RTLNITRONOW":
			self.session.open(RTLNITROnowGenreScreen)
		elif auswahl == "SUPERRTLNOW":
			self.session.open(SUPERRTLnowGenreScreen)
		elif auswahl == "ZDF Mediathek":
			self.session.open(ZDFGenreScreen)
		elif auswahl == "ORF TVthek":
			self.session.open(ORFGenreScreen)
		elif auswahl == "SRF Player":
			self.session.open(SRFGenreScreen)
		elif auswahl == "Cinestream":
			self.session.open(cinestreamFilmListeScreen)
		elif auswahl == "Moovizon":
			self.session.open(moovizonGenreScreen)
		elif auswahl == "Wrestlingnetwork":
			self.session.open(wrestlingnetworkGenreScreen)
		elif auswahl == "retro-tv":
			self.session.open(retrotvFilmListeScreen)
		elif auswahl == "Galileo-Videolexikon":
			self.session.open(galileovlGenreScreen)
		elif auswahl == "Sport1.fm":
			self.session.open(sport1fmGenreScreen)
		#elif auswahl == "Viewster":
		#	self.session.open(viewsterGenreScreen)
		elif auswahl == "ARD Mediathek":
			self.session.open(ARDGenreScreen)

		# porn
		elif auswahl == "4Tube":
			self.pornscreen = fourtubeGenreScreen
		elif auswahl == "Ah-Me":
			self.pornscreen = ahmeGenreScreen
		elif auswahl == "AmateurPorn":
			self.pornscreen = amateurpornGenreScreen
		elif auswahl == "beeg":
			self.pornscreen = beegGenreScreen
		elif auswahl == "DrTuber":
			self.pornscreen = drtuberGenreScreen
		elif auswahl == "El-Ladies":
			self.pornscreen = elladiesGenreScreen
		elif auswahl == "Eporner":
			self.pornscreen = epornerGenreScreen
		elif auswahl == "EroProfile":
			self.pornscreen = eroprofileGenreScreen
		elif auswahl == "ExtremeTube":
			self.pornscreen = extremetubeGenreScreen
		elif auswahl == "Free Online Movies":
			self.pornscreen = freeomovieGenreScreen
		elif auswahl == "G-Stream-XXX":
			self.pornscreen = gstreaminxxxGenreScreen
		elif auswahl == "HDPorn":
			self.pornscreen = hdpornGenreScreen
		elif auswahl == "hotshame":
			self.pornscreen = hotshameGenreScreen
		elif auswahl == "MegaSkanks":
			self.pornscreen = megaskanksGenreScreen
		elif auswahl == "IStream-XXX":
			self.pornscreen = showIStreamGenre
			self.cat = "porn"
		elif auswahl == "Movie4k-XXX":
			self.pornscreen = m4kGenreScreen
			self.cat = "porn"
		elif auswahl == "ParadiseHill":
			self.pornscreen = paradisehillGenreScreen
		elif auswahl == "Pinkrod":
			self.pornscreen = pinkrodGenreScreen
		elif auswahl == "PlayPorn":
			self.pornscreen = playpornGenreScreen
		elif auswahl == "PornerBros":
			self.pornscreen = pornerbrosGenreScreen
		elif auswahl == "Pornhub":
			self.pornscreen = pornhubGenreScreen
		elif auswahl == "PORNMVZ":
			self.pornscreen = pornmvzGenreScreen
		elif auswahl == "PornoStreams":
			self.pornscreen = pornostreamsGenreScreen
		elif auswahl == "PornRabbit":
			self.pornscreen = pornrabbitGenreScreen
		elif auswahl == "RealGFPorn":
			self.pornscreen = realgfpornGenreScreen
		elif auswahl == "RedTube":
			self.pornscreen = redtubeGenreScreen
		elif auswahl == "SeXXX-HD":
			self.pornscreen = sexxxhdGenreScreen
		elif auswahl == "SunPorno":
			self.pornscreen = sunpornoGenreScreen
		elif auswahl == "TheNewPorn":
			self.pornscreen = thenewpornGenreScreen
		elif auswahl == "UpdateTube":
			self.pornscreen = updatetubeGenreScreen
		elif auswahl == "WetPlace":
			self.pornscreen = wetplaceGenreScreen
		elif auswahl == "xHamster":
			self.pornscreen = xhamsterGenreScreen
		elif auswahl == "XXXSaVe":
			self.pornscreen = xxxsaveFilmScreen
		elif auswahl == "YouPorn":
			self.pornscreen = youpornGenreScreen

		if self.pornscreen:
			if config.mediaportal.pornpin.value:
				self.session.openWithCallback(self.pincheckok, PinInput, pinList = [(config.mediaportal.pincode.value)], triesEntry = self.getTriesEntry(), title = _("Please enter the correct pin code"), windowTitle = _("Enter pin code"))
			else:
				if self.cat == "":
					self.session.open(self.pornscreen)
				else:
					self.session.open(self.pornscreen, self.cat)

	def pincheckok(self, pincode):
		if pincode:
			if self.cat == "":
				self.session.open(self.pornscreen)
			else:
				self.session.open(self.pornscreen, self.cat)

	def keyCancel(self):
		self.close(self.session, True)

	def restart(self):
		self.close(self.session, False)

class pluginSort(Screen):

	def __init__(self, session):
		self.session = session

		self.plugin_path = mp_globals.pluginPath
		self.skin_path = mp_globals.pluginPath + "/skins"

		path = "%s/%s/pluginSortScreen.xml" % (self.skin_path, config.mediaportal.skin.value)

		if not fileExists(path):
			path = self.skin_path + "/original/pluginSortScreen.xml"

		with open(path, "r") as f:
			self.skin = f.read()
			f.close()

		Screen.__init__(self, session)

		self.list = []
		self["config2"] = chooseMenuList([])
		self.plugin_path = ""
		self.selected = False
		self.move_on = False

		self["actions"]  = ActionMap(["OkCancelActions", "ShortcutActions", "WizardActions", "ColorActions", "SetupActions", "NumberActions", "MenuActions", "HelpActions"], {
			"ok":	self.select,
			"cancel": self.keyCancel
		}, -1)

		self.readconfig()

	def select(self):
		if not self.selected:
			self.last_newidx = self["config2"].getSelectedIndex()
			self.last_plugin_name = self["config2"].getCurrent()[0][0]
			self.last_plugin_pic = self["config2"].getCurrent()[0][1]
			self.last_plugin_genre = self["config2"].getCurrent()[0][2]
			self.last_plugin_hits = self["config2"].getCurrent()[0][3]
			self.last_plugin_msort = self["config2"].getCurrent()[0][4]
			print "Select:", self.last_plugin_name, self.last_newidx
			self.selected = True
			self.readconfig()
		else:
			self.now_newidx = self["config2"].getSelectedIndex()
			self.now_plugin_name = self["config2"].getCurrent()[0][0]
			self.now_plugin_pic = self["config2"].getCurrent()[0][1]
			self.now_plugin_genre = self["config2"].getCurrent()[0][2]
			self.now_plugin_hits = self["config2"].getCurrent()[0][3]
			self.now_plugin_msort = self["config2"].getCurrent()[0][4]

			count_move = 0
			config_tmp = open("/etc/enigma2/mp_pluginliste.tmp" , "w")
			# del element from list
			del self.config_list_select[int(self.last_newidx)];
			# add element to list at the right place
			self.config_list_select.insert(int(self.now_newidx), (self.last_plugin_name, self.last_plugin_pic, self.last_plugin_genre, self.last_plugin_hits, self.now_newidx));

			# liste neu nummerieren
			for (name, pic, genre, hits, msort) in self.config_list_select:
				count_move += 1
				config_tmp.write('"%s" "%s" "%s" "%s" "%s"\n' % (name, pic, genre, hits, count_move))

			print "change:", self.last_newidx+1, "with", self.now_newidx+1, "total:", len(self.config_list_select)

			config_tmp.close()
			shutil.move("/etc/enigma2/mp_pluginliste.tmp", "/etc/enigma2/mp_pluginliste")
			self.selected = False
			self.readconfig()

	def readconfig(self):
		config_read = open("/etc/enigma2/mp_pluginliste","r")
		self.config_list = []
		self.config_list_select = []
		print "Filter:", config.mediaportal.filter.value
		for line in config_read.readlines():
			ok = re.findall('"(.*?)" "(.*?)" "(.*?)" "(.*?)" "(.*?)"', line, re.S)
			if ok:
				(name, pic, genre, hits, msort) = ok[0]
				if config.mediaportal.filter.value != "ALL":
					if genre == config.mediaportal.filter.value:
						self.config_list_select.append((name, pic, genre, hits, msort))
						self.config_list.append(self.show_menu(name, pic, genre, hits, msort))
				else:
					self.config_list_select.append((name, pic, genre, hits, msort))
					self.config_list.append(self.show_menu(name, pic, genre, hits, msort))

		self.config_list.sort(key=lambda x: int(x[0][4]))
		self.config_list_select.sort(key=lambda x: int(x[4]))
		self["config2"].l.setList(self.config_list)
		self["config2"].l.setItemHeight(25)
		config_read.close()

	def show_menu(self, name, pic, genre, hits, msort):
		res = [(name, pic, genre, hits, msort)]
		res.append(MultiContentEntryText(pos=(100, 0), size=(390, 22), font=0, text=name, flags=RT_HALIGN_LEFT))
		if self.selected and name == self.last_plugin_name:
			res.append(MultiContentEntryPixmapAlphaTest(pos=(70, 2), size=(20, 20), png=loadPNG("/usr/lib/enigma2/python/Plugins/Extensions/MediaPortal/images/select.png")))
		return res

	def keyCancel(self):
		config.mediaportal.sortplugins.value = "user"
		self.close()

class haupt_Screen_Wall(Screen, ConfigListScreen):
	def __init__(self, session, filter):
		self.session = session

		self.plugin_liste = []

		# kinder
		if config.mediaportal.showKinderKino.value:
			self.plugin_liste.append(("KinderKino", "kinderkino", "Mediathek"))
		if config.mediaportal.showtivi.value:
			self.plugin_liste.append(("Tivi", "tivi", "Mediathek"))
		if config.mediaportal.showkika.value:
			self.plugin_liste.append(("KIKA+", "kika", "Mediathek"))

		# Grauzone
		if (config.mediaportal.showgrauzone.value == False and config.mediaportal.filter.value == 'Grauzone'):
			config.mediaportal.filter.value = 'ALL'
		if config.mediaportal.showgrauzone.value:
			if config.mediaportal.showMEHD.value:
				self.plugin_liste.append(("My-Entertainment", "mehd", "Grauzone"))
			if config.mediaportal.showM4k.value:
				self.plugin_liste.append(("Movie4k", "movie4k", "Grauzone"))
			if config.mediaportal.showIStream.value:
				self.plugin_liste.append(("IStream", "istream", "Grauzone"))
			if config.mediaportal.showSzeneStreams.value:
				self.plugin_liste.append(("SzeneStreams", "szenestreams", "Grauzone"))
			if config.mediaportal.showmlehd.value:
				self.plugin_liste.append(("MLE-HD", "mlehd", "Grauzone"))
			if config.mediaportal.showDdlme.value:
				self.plugin_liste.append(("ddl.me", "ddl_me", "Grauzone"))
			if config.mediaportal.showSongsto.value:
				self.plugin_liste.append(("Songs.to", "songsto", "Music"))
			if config.mediaportal.showCanna.value:
				self.plugin_liste.append(("Canna-Power", "canna", "Music"))
			if config.mediaportal.showEighties.value:
				self.plugin_liste.append(("80s & 90s Music", "eighties", "Music"))
			if config.mediaportal.showMusicstreamcc.value:
				self.plugin_liste.append(("Musicstream.cc", "musicstreamcc", "Music"))
			if config.mediaportal.showMovie25.value:
				self.plugin_liste.append(("Movie25", "movie25", "Grauzone"))
			if config.mediaportal.showWatchseries.value:
				self.plugin_liste.append(("Watchseries", "watchseries", "Grauzone"))
			if config.mediaportal.showVibeo.value:
				self.plugin_liste.append(("Vibeo", "vibeo", "Grauzone"))
			if config.mediaportal.showBaskino.value:
				self.plugin_liste.append(("Baskino", "baskino", "Grauzone"))
			if config.mediaportal.showKinox.value:
				self.plugin_liste.append(("Kinox", "kinox", "Grauzone"))
			if config.mediaportal.showStreamOase.value:
				self.plugin_liste.append(("StreamOase", "streamoase", "Grauzone"))
			if config.mediaportal.showCinestream.value:
				self.plugin_liste.append(("Cinestream", "cinestream", "Grauzone"))
			if config.mediaportal.showKinoKiste.value:
				self.plugin_liste.append(("KinoKiste", "kinokiste", "Grauzone"))
			if config.mediaportal.showBs.value:
				self.plugin_liste.append(("Burning-Series", "burningseries", "Grauzone"))
			#if config.mediaportal.showViewster.value:
			#	self.plugin_liste.append(("Viewster", "viewster", "Mediathek"))
			if config.mediaportal.showprimewire.value:
				self.plugin_liste.append(("PrimeWire", "primewire", "Grauzone"))
			if config.mediaportal.showMoovizon.value:
				self.plugin_liste.append(("Moovizon", "moovizon", "Grauzone"))

			# Watchlisten - Grauzone
			if config.mediaportal.showM4kWatchlist.value:
				self.plugin_liste.append(("Movie4k Watchlist", "movie4kwatchlist", "Grauzone"))
			if config.mediaportal.showKinoxWatchlist.value:
				self.plugin_liste.append(("Kinox Watchlist", "kinoxwatchlist", "Grauzone"))

		if config.mediaportal.showDoku.value:
			self.plugin_liste.append(("Doku.me", "doku", "Fun"))
		if config.mediaportal.showSportBild.value:
			self.plugin_liste.append(("SportBild", "sportbild", "Fun"))
		if config.mediaportal.showAutoBild.value:
			self.plugin_liste.append(("AutoBild", "autobild", "Fun"))
		if config.mediaportal.showLaola1.value:
			self.plugin_liste.append(("Laola1", "laola1", "Sport"))
		if config.mediaportal.showFocus.value:
			self.plugin_liste.append(("Focus", "focus", "Fun"))
		if config.mediaportal.showCczwei.value:
			self.plugin_liste.append(("CCZwei", "cczwei", "Fun"))
		if config.mediaportal.showTrailer.value:
			self.plugin_liste.append(("Filmtrailer", "trailer", "Fun"))
		if config.mediaportal.showDsc.value:
			self.plugin_liste.append(("Dreamscreencast", "dreamscreencast", "Fun"))
		if config.mediaportal.showNhl.value:
			self.plugin_liste.append(("NHL", "nhl", "Sport"))
		if config.mediaportal.show4Players.value:
			self.plugin_liste.append(("4Players", "4players", "Fun"))
		if config.mediaportal.showGIGA.value:
			self.plugin_liste.append(("GIGA.de", "gigatv", "Fun"))
		if config.mediaportal.showaudi.value:
			self.plugin_liste.append(("Audi.tv", "auditv", "Fun"))
		if config.mediaportal.showgronkh.value:
			self.plugin_liste.append(("gronkh.de", "gronkh", "Fun"))
		if config.mediaportal.showMahlzeitTV.value:
			self.plugin_liste.append(("mahlzeit.tv", "mahlzeit", "Fun"))
		if config.mediaportal.showFiwitu.value:
			self.plugin_liste.append(("fiwitu.tv", "fiwitu", "Fun"))
		if config.mediaportal.showappletrailers.value:
			self.plugin_liste.append(("AppleTrailer", "appletrailers", "Fun"))
		if config.mediaportal.showDOKUh.value:
			self.plugin_liste.append(("DOKUh", "dokuh", "Fun"))
		if config.mediaportal.showDokuHouse.value:
			self.plugin_liste.append(("DokuHouse", "dokuhouse", "Fun"))
		if config.mediaportal.showAllMusicHouse.value:
			self.plugin_liste.append(("AllMusicHouse", "allmusichouse", "Music"))
		if config.mediaportal.showputpattv.value:
			self.plugin_liste.append(("putpat.tv", "putpattv", "Music"))
		if config.mediaportal.showRofl.value:
			self.plugin_liste.append(("Rofl.to", "rofl", "Fun"))
		if config.mediaportal.showFail.value:
			self.plugin_liste.append(("Fail.to", "fail", "Fun"))
		if config.mediaportal.showFilmOn.value:
			self.plugin_liste.append(("FilmOn", "filmon", "Fun"))
		if config.mediaportal.showTvkino.value:
			self.plugin_liste.append(("TV-Kino", "tvkino", "Fun"))
		if config.mediaportal.showRadio.value:
			self.plugin_liste.append(("Radio.de", "radiode", "Music"))
		if config.mediaportal.showSpobox.value:
			self.plugin_liste.append(("Spobox", "spobox", "Sport"))
		if config.mediaportal.showLiveLeak.value:
			self.plugin_liste.append(("LiveLeak", "liveleak", "Fun"))
		if config.mediaportal.showDokuStream.value:
			self.plugin_liste.append(("DokuStream", "dokustream", "Fun"))
		if config.mediaportal.showScienceTV.value:
			self.plugin_liste.append(("ScienceTV", "sciencetv", "Fun"))
		if config.mediaportal.showHoerspielHouse.value:
			self.plugin_liste.append(("HörspielHouse", "hoerspielhouse", "Fun"))
		if config.mediaportal.showHoerspielChannels.value:
			self.plugin_liste.append(("Hörspiel-Channels", "hoerspielchannels", "Fun"))
		if config.mediaportal.showCarChannels.value:
			self.plugin_liste.append(("CAR-Channels", "carchannels", "Fun"))
		if config.mediaportal.showGameChannels.value:
			self.plugin_liste.append(("GAME-Channels", "gamechannels", "Fun"))
		if config.mediaportal.showMusicChannels.value:
			self.plugin_liste.append(("MUSIC-Channels", "musicchannels", "Music"))
		if config.mediaportal.showUserChannels.value:
			self.plugin_liste.append(("USER-Channels", "userchannels", "Fun"))
		if config.mediaportal.showYoutube.value:
			self.plugin_liste.append(("YouTube", "youtube", "Fun"))
		if config.mediaportal.showClipfish.value:
			self.plugin_liste.append(("Clipfish", "clipfish", "Mediathek/Fun/Music"))
		if config.mediaportal.showRan.value:
			self.plugin_liste.append(("Ran.de", "ran", "Sport"))
		if config.mediaportal.showTeledunet.value:
			self.plugin_liste.append(("Teledunet", "teledunet", "Fun"))
		if config.mediaportal.showGEOde.value:
			self.plugin_liste.append(("GEO.de", "geo_de", "Fun"))
		if config.mediaportal.showDeluxemusic.value:
			self.plugin_liste.append(("Deluxemusic", "deluxemusic", "Music"))
		if config.mediaportal.showNuna.value:
			self.plugin_liste.append(("Nuna", "nuna", "Music"))
		if config.mediaportal.showMyvideoTop100.value:
			self.plugin_liste.append(("Myvideo Top 100", "myvideotop100", "Music"))
		if config.mediaportal.showMTVdeCharts.value:
			self.plugin_liste.append(("MTV.de Charts", "mtvdecharts", "Music"))
		if config.mediaportal.showWrestlingnetwork.value:
			self.plugin_liste.append(("Wrestlingnetwork", "wrestlingnetwork", "Fun"))
		if config.mediaportal.showretrotv.value:
			self.plugin_liste.append(("retro-tv", "retrotv", "Fun"))
		if config.mediaportal.showgalileovl.value:
			self.plugin_liste.append(("Galileo-Videolexikon", "galileovl", "Fun"))
		if config.mediaportal.showsport1fm.value:
			self.plugin_liste.append(("Sport1.fm", "sport1fm", "Sport"))
		if astModule:
			if config.mediaportal.showHeiseVideo.value:
				self.plugin_liste.append(("heiseVIDEO", "heisevideo", "Fun"))

		### mediatheken
		if config.mediaportal.showMyvideo.value:
			self.plugin_liste.append(("MyVideo", "myvideo", "Mediathek"))
		if config.mediaportal.showNetzKino.value:
			self.plugin_liste.append(("NetzKino", "netzkino", "Mediathek"))
		if config.mediaportal.showVoxnow.value:
			self.plugin_liste.append(("VOXNOW", "voxnow", "Mediathek"))
		if config.mediaportal.showRTLnow.value:
			self.plugin_liste.append(("RTLNOW", "rtlnow", "Mediathek"))
		if config.mediaportal.showNTVnow.value:
			self.plugin_liste.append(("N-TVNOW", "ntvnow", "Mediathek"))
		if config.mediaportal.showRTL2now.value:
			self.plugin_liste.append(("RTL2NOW", "rtl2now", "Mediathek"))
		if config.mediaportal.showRTLnitro.value:
			self.plugin_liste.append(("RTLNITRONOW", "rtlnitro", "Mediathek"))
		if config.mediaportal.showSUPERRTLnow.value:
			self.plugin_liste.append(("SUPERRTLNOW", "superrtlnow", "Mediathek"))
		if config.mediaportal.showZDF.value:
			self.plugin_liste.append(("ZDF Mediathek", "zdf", "Mediathek"))
		if config.mediaportal.showORF.value:
			self.plugin_liste.append(("ORF TVthek", "orf", "Mediathek"))
		if config.mediaportal.showSRF.value:
			self.plugin_liste.append(("SRF Player", "srf", "Mediathek"))
		if config.mediaportal.showARD.value:
			self.plugin_liste.append(("ARD Mediathek", "ard", "Mediathek"))

		### porn
		if (config.mediaportal.showporn.value == False and config.mediaportal.filter.value == 'Porn'):
			config.mediaportal.filter.value = 'ALL'
		if config.mediaportal.showporn.value:
			if config.mediaportal.show4tube.value:
				self.plugin_liste.append(("4Tube", "4tube", "Porn"))
			if config.mediaportal.showahme.value:
				self.plugin_liste.append(("Ah-Me", "ahme", "Porn"))
			if config.mediaportal.showamateurporn.value:
				self.plugin_liste.append(("AmateurPorn", "amateurporn", "Porn"))
			if config.mediaportal.showbeeg.value:
				self.plugin_liste.append(("beeg", "beeg", "Porn"))
			if config.mediaportal.showdrtuber.value:
				self.plugin_liste.append(("DrTuber", "drtuber", "Porn"))
			if config.mediaportal.showelladies.value:
				self.plugin_liste.append(("El-Ladies", "elladies", "Porn"))
			if config.mediaportal.showeporner.value:
				self.plugin_liste.append(("Eporner", "eporner", "Porn"))
			if config.mediaportal.showeroprofile.value:
				self.plugin_liste.append(("EroProfile", "eroprofile", "Porn"))
			if config.mediaportal.showextremetube.value:
				self.plugin_liste.append(("ExtremeTube", "extremetube", "Porn"))
			if config.mediaportal.showgrauzone.value:
				if config.mediaportal.showfreeomovie.value:
					self.plugin_liste.append(("Free Online Movies", "freeomovie", "Porn"))
				if config.mediaportal.showgstreaminxxx.value:
					self.plugin_liste.append(("G-Stream-XXX", "gstreaminxxx", "Porn"))
			if config.mediaportal.showhdporn.value:
				self.plugin_liste.append(("HDPorn", "hdporn", "Porn"))
			if config.mediaportal.showhotshame.value:
				self.plugin_liste.append(("hotshame", "hotshame", "Porn"))
			if config.mediaportal.showgrauzone.value:
				if config.mediaportal.showmegaskanks.value:
					self.plugin_liste.append(("MegaSkanks", "megaskanks", "Porn"))
				if config.mediaportal.showIStreamPorn.value:
					self.plugin_liste.append(("IStream-XXX", "istreamporn", "Porn"))
				if config.mediaportal.showM4kPorn.value:
					self.plugin_liste.append(("Movie4k-XXX", "movie4kporn", "Porn"))
				if config.mediaportal.showparadisehill.value:
					self.plugin_liste.append(("ParadiseHill", "paradisehill", "Porn"))
			if config.mediaportal.showpinkrod.value:
				self.plugin_liste.append(("Pinkrod", "pinkrod", "Porn"))
			if config.mediaportal.showgrauzone.value:
				if config.mediaportal.showplayporn.value:
					self.plugin_liste.append(("PlayPorn", "playporn", "Porn"))
			if config.mediaportal.showpornerbros.value:
				self.plugin_liste.append(("PornerBros", "pornerbros", "Porn"))
			if config.mediaportal.showPornhub.value:
				self.plugin_liste.append(("Pornhub", "pornhub", "Porn"))
			if config.mediaportal.showgrauzone.value:
				if config.mediaportal.showpornmvz.value:
					self.plugin_liste.append(("PORNMVZ", "pornmvz", "Porn"))
				if config.mediaportal.showpornostreams.value:
					self.plugin_liste.append(("PornoStreams", "pornostreams", "Porn"))
			if config.mediaportal.showpornrabbit.value:
				self.plugin_liste.append(("PornRabbit", "pornrabbit", "Porn"))
			if config.mediaportal.showrealgfporn.value:
				self.plugin_liste.append(("RealGFPorn", "realgfporn", "Porn"))
			if config.mediaportal.showredtube.value:
				self.plugin_liste.append(("RedTube", "redtube", "Porn"))
			if config.mediaportal.showsexxxhd.value:
				self.plugin_liste.append(("SeXXX-HD", "sexxxhd", "Porn"))
			if config.mediaportal.showsunporno.value:
				self.plugin_liste.append(("SunPorno", "sunporno", "Porn"))
			if config.mediaportal.showthenewporn.value:
				self.plugin_liste.append(("TheNewPorn", "thenewporn", "Porn"))
			if config.mediaportal.showupdatetube.value:
				self.plugin_liste.append(("UpdateTube", "updatetube", "Porn"))
			if config.mediaportal.showwetplace.value:
				self.plugin_liste.append(("WetPlace", "wetplace", "Porn"))
			if config.mediaportal.showXhamster.value:
				self.plugin_liste.append(("xHamster", "xhamster", "Porn"))
			if config.mediaportal.showgrauzone.value:
				if config.mediaportal.showxxxsave.value:
					self.plugin_liste.append(("XXXSaVe", "xxxsave", "Porn"))
			if config.mediaportal.showyouporn.value:
				self.plugin_liste.append(("YouPorn", "youporn", "Porn"))

		# Plugin Sortierung
		if config.mediaportal.sortplugins != "default":

			# Erstelle Pluginliste falls keine vorhanden ist.
			self.sort_plugins_file = "/etc/enigma2/mp_pluginliste"
			if not fileExists(self.sort_plugins_file):
				print "Erstelle Wall-Pluginliste."
				os.system("touch "+self.sort_plugins_file)

			pluginliste_leer = os.path.getsize(self.sort_plugins_file)
			if pluginliste_leer == 0:
				print "1st time - Schreibe Wall-Pluginliste."
				first_count = 0
				read_pluginliste = open(self.sort_plugins_file,"a")
				for name,picname,genre in self.plugin_liste:
					print name
					read_pluginliste.write('"%s" "%s" "%s" "%s" "%s"\n' % (name, picname, genre, "0", str(first_count)))
					first_count += 1
				read_pluginliste.close()
				print "Wall-Pluginliste wurde erstellt."

			# Lese Pluginliste ein.
			if fileExists(self.sort_plugins_file):

				count_sort_plugins_file = len(open(self.sort_plugins_file).readlines())
				count_plugin_liste = len(self.plugin_liste)

				print count_plugin_liste, count_sort_plugins_file
				if int(count_plugin_liste) != int(count_sort_plugins_file):
					print "Ein Plugin wurde aktiviert oder deaktiviert.. erstelle neue pluginliste."

					read_pluginliste_tmp = open(self.sort_plugins_file+".tmp","w")
					read_pluginliste = open(self.sort_plugins_file,"r")
					p_dupeliste = []

					for rawData in read_pluginliste.readlines():
						data = re.findall('"(.*?)" "(.*?)" "(.*?)" "(.*?)" "(.*?)"', rawData, re.S)

						if data:
							(p_name, p_picname, p_genre, p_hits, p_sort) = data[0]
							pop_count = 0
							for pname, ppic, pgenre in self.plugin_liste:
								if p_name not in p_dupeliste:
									if p_name == pname:
										read_pluginliste_tmp.write('"%s" "%s" "%s" "%s" "%s"\n' % (p_name, p_picname, pgenre, p_hits, p_sort))
										p_dupeliste.append((p_name))
										print pop_count
										self.plugin_liste.pop(int(pop_count))

									pop_count += 1

					if len(self.plugin_liste) != 0:
						for pname, ppic, pgenre in self.plugin_liste:
							read_pluginliste_tmp.write('"%s" "%s" "%s" "%s" "%s"\n' % (pname, ppic, pgenre, "0", "99"))

					read_pluginliste.close()
					read_pluginliste_tmp.close()
					shutil.move(self.sort_plugins_file+".tmp", self.sort_plugins_file)

				self.new_pluginliste = []
				read_pluginliste = open(self.sort_plugins_file,"r")
				for rawData in read_pluginliste.readlines():
					data = re.findall('"(.*?)" "(.*?)" "(.*?)" "(.*?)" "(.*?)"', rawData, re.S)
					if data:
						(p_name, p_picname, p_genre, p_hits, p_sort) = data[0]
						self.new_pluginliste.append((p_name, p_picname, p_genre, p_hits, p_sort))
				read_pluginliste.close()

			# Sortieren nach hits
			if config.mediaportal.sortplugins.value == "hits":
				self.new_pluginliste.sort(key=lambda x: int(x[3]))
				self.new_pluginliste.reverse()

			# Sortieren nach abcde..
			elif config.mediaportal.sortplugins.value == "abc":
				self.new_pluginliste.sort(key=lambda x: str(x[0]).lower())

			elif config.mediaportal.sortplugins.value == "user":
				self.new_pluginliste.sort(key=lambda x: int(x[4]))

			self.plugin_liste = self.new_pluginliste

		skincontent = ""

		posx = 20
		posy = 210
		for x in range(1,len(self.plugin_liste)+1):
			skincontent += "<widget name=\"zeile" + str(x) + "\" position=\"" + str(posx) + "," + str(posy) + "\" size=\"150,80\" zPosition=\"1\" transparent=\"0\" alphatest=\"blend\" />"
			posx += 155
			if x == 8 or x == 16 or x == 24 or x == 32 or x == 48 or x == 56 or x == 64 or x == 72 or x == 88 or x == 96 or x == 104 or x == 112 or x == 128 or x == 136 or x == 144 or x == 152:
				posx = 20
				posy += 85
			elif x == 40 or x == 80 or x == 120 or x == 160 or x == 200:
				posx = 20
				posy = 210

		# Appe Page Style
		if config.mediaportal.showapplepagestyle.value:
			self.dump_liste_page_tmp = self.plugin_liste
			if config.mediaportal.filter.value != "ALL":
				self.plugin_liste_page_tmp = []
				self.plugin_liste_page_tmp = [x for x in self.dump_liste_page_tmp if re.search(config.mediaportal.filter.value, x[2])]
			else:
				self.plugin_liste_page_tmp = self.plugin_liste

			if len(self.plugin_liste_page_tmp) != 0:
				self.counting_pages = len(self.plugin_liste_page_tmp) / 40
				print "COUNTING PAGES:", self.counting_pages
				pagebar_size = int(self.counting_pages) * 30
				rest_size = 1280 - int(pagebar_size)
				start_pagebar = int(rest_size) / 2

				for x in range(1,self.counting_pages+2):
					normal = 650
					print x, start_pagebar, normal
					skincontent += "<widget name=\"page_empty" + str(x) + "\" position=\"" + str(start_pagebar) + "," + str(normal) + "\" size=\"18,18\" zPosition=\"2\" transparent=\"1\" alphatest=\"blend\" />"
					skincontent += "<widget name=\"page_sel" + str(x) + "\" position=\"" + str(start_pagebar) + "," + str(normal) + "\" size=\"18,18\" zPosition=\"2\" transparent=\"1\" alphatest=\"blend\" />"
					start_pagebar += 30

		self.skin_dump = ""
		self.skin_dump += "<widget name=\"frame\" position=\"20,210\" size=\"150,80\" pixmap=\"/usr/lib/enigma2/python/Plugins/Extensions/MediaPortal/icons_wall/Selektor_%s.png\" zPosition=\"2\" transparent=\"0\" alphatest=\"blend\" />" % config.mediaportal.selektor.value
		self.skin_dump += skincontent
		self.skin_dump += "</screen>"

		self.plugin_path = mp_globals.pluginPath
		self.skin_path = mp_globals.pluginPath + "/skins"
		self.images_path = path = "%s/%s/images" % (self.skin_path, config.mediaportal.skin.value)

		path = "%s/%s/hauptScreenWall.xml" % (self.skin_path, config.mediaportal.skin.value)
		if not fileExists(path):
			path = self.skin_path + "/original/hauptScreenWall.xml"

		with open(path, "r") as f:
			self.skin_dump2 = f.read()
			self.skin_dump2 += self.skin_dump
			self.skin = self.skin_dump2
			f.close()

		Screen.__init__(self, session)

		registerFont("/usr/lib/enigma2/python/Plugins/Extensions/MediaPortal/resources/mediaportal.ttf", "mediaportal", 100, False)

		self["actions"]  = ActionMap(["OkCancelActions", "ShortcutActions", "WizardActions", "ColorActions", "SetupActions", "NumberActions", "MenuActions", "EPGSelectActions", "HelpActions"], {
			"ok"    : self.keyOK,
			"up"    : self.keyUp,
			"down"  : self.keyDown,
			"cancel": self.keyCancel,
			"left"  : self.keyLeft,
			"right" : self.keyRight,
			"nextBouquet" :	self.page_next,
			"prevBouquet" :	self.page_back,
			"menu" : self.keySetup,
			"info" : self.showPorn,
			"displayHelp" : self.keyHelp,
			"blue" : self.chFilter,
			"green" : self.chSort,
			"yellow": self.manuelleSortierung
		}, -1)

		self['name'] = Label("Plugin Auswahl")
		self['blue'] = Label("")
		self['green'] = Label("")
		self['page'] = Label("")
		self["frame"] = MovingPixmap()

		for x in range(1,len(self.plugin_liste)+1):
			self["zeile"+str(x)] = Pixmap()
			self["zeile"+str(x)].show()

		# Apple Page Style
		if config.mediaportal.showapplepagestyle.value and len(self.plugin_liste_page_tmp) != 0:
			for x in range(1,self.counting_pages+2):
				self["page_empty"+str(x)] = Pixmap()
				self["page_empty"+str(x)].show()
				self["page_sel"+str(x)] = Pixmap()
				self["page_sel"+str(x)].show()

		self.selektor_index = 1
		self.select_list = 0

		self.onFirstExecBegin.append(self._onFirstExecBegin)

	def manuelleSortierung(self):
		self.session.openWithCallback(self.restart, pluginSort)

	def hit_plugin(self, pname):
		if fileExists(self.sort_plugins_file):
			read_pluginliste = open(self.sort_plugins_file,"r")
			read_pluginliste_tmp = open(self.sort_plugins_file+".tmp","w")
			for rawData in read_pluginliste.readlines():
				data = re.findall('"(.*?)" "(.*?)" "(.*?)" "(.*?)" "(.*?)"', rawData, re.S)
				if data:
					(p_name, p_picname, p_genre, p_hits, p_sort) = data[0]
					if pname == p_name:
						new_hits = int(p_hits)+1
						read_pluginliste_tmp.write('"%s" "%s" "%s" "%s" "%s"\n' % (p_name, p_picname, p_genre, str(new_hits), p_sort))
					else:
						read_pluginliste_tmp.write('"%s" "%s" "%s" "%s" "%s"\n' % (p_name, p_picname, p_genre, p_hits, p_sort))
			read_pluginliste.close()
			read_pluginliste_tmp.close()
			shutil.move(self.sort_plugins_file+".tmp", self.sort_plugins_file)

	def _onFirstExecBegin(self):
		if config.mediaportal.autoupdate.value:
			checkupdate(self.session).checkforupdate()

		# load plugin icons
		print "Set Filter:", config.mediaportal.filter.value
		self['blue'].setText(config.mediaportal.filter.value)
		self.sortplugin = config.mediaportal.sortplugins.value
		if self.sortplugin == "hits":
			self.sortplugin = "Hits"
		elif self.sortplugin == "abc":
			self.sortplugin = "ABC"
		elif self.sortplugin == "user":
			self.sortplugin = "User"
		self['green'].setText(self.sortplugin)
		self.dump_liste = self.plugin_liste
		if config.mediaportal.filter.value != "ALL":
			self.plugin_liste = []
			self.plugin_liste = [x for x in self.dump_liste if re.search(config.mediaportal.filter.value, x[2])]
		if len(self.plugin_liste) == 0:
			self.chFilter()
			self['blue'].setText(config.mediaportal.filter.value)

		if config.mediaportal.sortplugins.value == "hits":
			self.plugin_liste.sort(key=lambda x: int(x[3]))
			self.plugin_liste.reverse()

		# Sortieren nach abcde..
		elif config.mediaportal.sortplugins.value == "abc":
			self.plugin_liste.sort(key=lambda t : tuple(t[0].lower()))

		elif config.mediaportal.sortplugins.value == "user":
			self.plugin_liste.sort(key=lambda x: int(x[4]))

		print "rolle weiter.."

		for x in range(1,len(self.plugin_liste)+1):
			postername = self.plugin_liste[int(x)-1][1]
			poster_path = "%s/%s.png" % ("/usr/lib/enigma2/python/Plugins/Extensions/MediaPortal/icons_wall", postername)
			if not fileExists(poster_path):
				poster_path = "/usr/lib/enigma2/python/Plugins/Extensions/MediaPortal/icons_wall/no_icon.png"

			self["zeile"+str(x)].instance.setPixmap(gPixmapPtr())
			self["zeile"+str(x)].hide()
			pic = LoadPixmap(cached=True, path=poster_path)
			if pic != None:
				self["zeile"+str(x)].instance.setPixmap(pic)
				if x <= 40:
					self["zeile"+str(x)].show()

		if config.mediaportal.showapplepagestyle.value and len(self.plugin_liste_page_tmp) != 0:
			for x in range(1,self.counting_pages+2):
				poster_path = "%s/page_select.png" % (self.images_path)
				#print "postername:", postername, poster_path
				self["page_sel"+str(x)].instance.setPixmap(gPixmapPtr())
				self["page_sel"+str(x)].hide()
				pic = LoadPixmap(cached=True, path=poster_path)
				if pic != None:
					self["page_sel"+str(x)].instance.setPixmap(pic)
					if x == 1:
						self["page_sel"+str(x)].show()

			for x in range(1,self.counting_pages+2):
				poster_path = "%s/page.png" % (self.images_path)
				self["page_empty"+str(x)].instance.setPixmap(gPixmapPtr())
				self["page_empty"+str(x)].hide()
				pic = LoadPixmap(cached=True, path=poster_path)
				if pic != None:
					self["page_empty"+str(x)].instance.setPixmap(pic)
					if x > 1:
						self["page_empty"+str(x)].show()

		# erstelle mainlist
		self.widget_list()

	def widget_list(self):
		count = 1
		counting = 1
		self.mainlist = []
		list_dummy = []
		self.plugin_counting = len(self.plugin_liste)

		for x in range(1,int(self.plugin_counting)+1):
			if count == 40:
				count += 1
				counting += 1
				list_dummy.append(x)
				self.mainlist.append(list_dummy)
				count = 1
				list_dummy = []
			else:
				count += 1
				counting += 1
				list_dummy.append(x)
				if int(counting) == int(self.plugin_counting)+1:
					self.mainlist.append(list_dummy)

		print self.mainlist
		pageinfo = "%s / %s" % (self.select_list+1, len(self.mainlist))
		self['page'].setText(pageinfo)
		select_nr = self.mainlist[int(self.select_list)][int(self.selektor_index)-1]
		plugin_name = self.plugin_liste[int(select_nr)-1][0]
		self['name'].setText(plugin_name)

	def move_selector(self):
		#print "mainlist:", self.mainlist[int(self.select_list)]
		#print "selektor", self.selektor_index
		#print "gucken", self.selektor_index, len(self.mainlist[int(self.select_list)])
		select_nr = self.mainlist[int(self.select_list)][int(self.selektor_index)-1]
		plugin_name = self.plugin_liste[int(select_nr)-1][0]
		self['name'].setText(plugin_name)
		position = self["zeile"+str(self.selektor_index)].instance.position()
		self["frame"].moveTo(position.x(), position.y(), 1)
		self["frame"].show()
		self["frame"].startMoving()

	def keyOK(self):
		if self.check_empty_list():
			return

		select_nr = self.mainlist[int(self.select_list)][int(self.selektor_index)-1]
		auswahl = self.plugin_liste[int(select_nr)-1][0]
		icon = self.plugin_liste[int(select_nr)-1][1]
		mp_globals.activeIcon = icon
		print "Plugin:", auswahl

		self.pornscreen = None
		self.cat = ""
		self.hit_plugin(auswahl)
		if auswahl == "Doku.me":
			self.session.open(dokuScreen)
		elif auswahl == "Rofl.to":
			self.session.open(roflScreen)
		elif auswahl == "Fail.to":
			self.session.open(failScreen)
		elif auswahl == "KinderKino":
			self.session.open(kinderKinoScreen)
		elif auswahl == "MyVideo":
			self.session.open(myVideoGenreScreen)
		elif auswahl == "SportBild":
			self.session.open(sportBildScreen)
		elif auswahl == "Laola1":
			self.session.open(laolaVideosOverviewScreen)
		elif auswahl == "KinoKiste":
			self.session.open(kinokisteGenreScreen)
		elif auswahl == "Burning-Series":
			self.session.open(bsMain)
		elif auswahl == "PrimeWire":
			self.session.open(PrimeWireGenreScreen)
		elif auswahl == "Focus":
			self.session.open(focusGenre)
		elif auswahl == "FilmOn":
			self.session.open(filmON)
		elif auswahl == "NetzKino":
			self.session.open(netzKinoGenreScreen)
		elif auswahl == "Spobox":
			self.session.open(spoboxGenreScreen)
		elif auswahl == "Radio.de":
			self.session.open(Radiode)
		elif auswahl == "CCZwei":
			self.session.open(cczwei)
		elif auswahl == "Filmtrailer":
			self.session.open(trailer)
		elif auswahl == "Baskino":
			self.session.open(baskino)
		elif auswahl == "Kinox":
			self.session.open(kxMain)
		elif auswahl == "Kinox Watchlist":
			self.session.open(kxWatchlist)
		elif auswahl == "Dreamscreencast":
			self.session.open(dreamscreencast)
		elif auswahl == "TV-Kino":
			self.session.open(tvkino)
		elif auswahl == "StreamOase":
			self.session.open(oasetvGenreScreen)
		elif auswahl == "AutoBild":
			self.session.open(autoBildGenreScreen)
		elif auswahl == "NHL":
			self.session.open(nhlGenreScreen)
		elif auswahl == "4Players":
			self.session.open(forPlayersGenreScreen)
		elif auswahl == "GIGA.de":
			self.session.open(gigatvGenreScreen)
		elif auswahl == "Audi.tv":
			self.session.open(auditvGenreScreen)
		elif auswahl == "gronkh.de":
			self.session.open(gronkhGenreScreen)
		elif auswahl == "Tivi":
			self.session.open(tiviGenreListeScreen)
		elif auswahl == "My-Entertainment":
			self.session.open(showMEHDGenre)
		elif auswahl == "Songs.to":
			self.session.open(showSongstoGenre)
		elif auswahl == "Movie4k":
			self.session.open(m4kGenreScreen, "default")
		elif auswahl == "Movie4k Watchlist":
			self.session.open(m4kWatchlist)
		elif auswahl == "IStream":
			self.session.open(showIStreamGenre, "default")
		elif auswahl == "mahlzeit.tv":
			self.session.open(mahlzeitMainScreen)
		elif auswahl == "fiwitu.tv":
			self.session.open(fiwituGenreScreen)
		elif auswahl == "AppleTrailer":
			self.session.open(appletrailersGenreScreen)
		elif auswahl == "DOKUh":
			self.session.open(showDOKUHGenre)
		elif auswahl == "DokuHouse":
			self.session.open(show_DH_Genre)
		elif auswahl == "AllMusicHouse":
			self.session.open(show_AMH_Genre)
		elif auswahl == "putpat.tv":
			self.session.open(putpattvGenreScreen)
		elif auswahl == "LiveLeak":
			self.session.open(LiveLeakScreen)
		elif auswahl == "DokuStream":
			self.session.open(show_DS_Genre)
		elif auswahl == "ScienceTV":
			self.session.open(scienceTvGenreScreen)
		elif auswahl == "SzeneStreams":
			self.session.open(SzeneStreamsGenreScreen)
		elif auswahl == "HörspielHouse":
			self.session.open(show_HSH_Genre)
		elif auswahl == "Hörspiel-Channels":
			self.session.open(show_HSC_Genre)
		elif auswahl == "CAR-Channels":
			self.session.open(show_CAR_Genre)
		elif auswahl == "GAME-Channels":
			self.session.open(show_GAME_Genre)
		elif auswahl == "MUSIC-Channels":
			self.session.open(show_MUSIC_Genre)
		elif auswahl == "USER-Channels":
			self.session.open(show_USER_Genre)
		elif auswahl == "Cinestream":
			self.session.open(cinestreamFilmListeScreen)
		elif auswahl == "Moovizon":
			self.session.open(moovizonGenreScreen)
		elif auswahl == "YouTube":
			self.session.open(youtubeGenreScreen)
		elif auswahl == "Clipfish":
			self.session.open(show_CF_Genre)
		elif auswahl == "ddl.me":
			self.session.open(show_DDLME_Genre)
		elif auswahl == "MLE-HD":
			self.session.open(mlehdGenreScreen)
		elif auswahl == "Canna-Power":
			self.session.open(cannaGenreScreen)
		elif auswahl == "Ran.de":
			self.session.open(ranGenreScreen)
		elif auswahl == "Movie25":
			self.session.open(movie25GenreScreen)
		elif auswahl == "80s & 90s Music":
			self.session.open(eightiesGenreScreen)
		elif auswahl == "Teledunet":
			self.session.open(teleGenreScreen)
		elif auswahl == "GEO.de":
			self.session.open(GEOdeGenreScreen)
		elif auswahl == "Deluxemusic":
			self.session.open(deluxemusicGenreScreen)
		elif auswahl == "Nuna":
			self.session.open(nunaGenreScreen)
		elif auswahl == "Watchseries":
			self.session.open(watchseriesGenreScreen)
		elif auswahl == "Myvideo Top 100":
			self.session.open(myvideoTop100GenreScreen)
		elif auswahl == "MTV.de Charts":
			self.session.open(MTVdeChartsGenreScreen)
		elif auswahl == "Musicstream.cc":
			self.session.open(show_MSCC_Genre)
		elif auswahl == "Vibeo":
			self.session.open(vibeoFilmListeScreen)
		elif auswahl == "heiseVIDEO":
			self.session.open(HeiseTvGenreScreen)

		# mediatheken
		elif auswahl == "VOXNOW":
			self.session.open(VOXnowGenreScreen)
		elif auswahl == "RTLNOW":
			self.session.open(RTLnowGenreScreen)
		elif auswahl == "N-TVNOW":
			self.session.open(NTVnowGenreScreen)
		elif auswahl == "RTL2NOW":
			self.session.open(RTL2nowGenreScreen)
		elif auswahl == "RTLNITRONOW":
			self.session.open(RTLNITROnowGenreScreen)
		elif auswahl == "SUPERRTLNOW":
			self.session.open(SUPERRTLnowGenreScreen)
		elif auswahl == "ZDF Mediathek":
			self.session.open(ZDFGenreScreen)
		elif auswahl == "ORF TVthek":
			self.session.open(ORFGenreScreen)
		elif auswahl == "SRF Player":
			self.session.open(SRFGenreScreen)
		elif auswahl == "KIKA+":
			self.session.open(kikaGenreScreen)
		elif auswahl == "Wrestlingnetwork":
			self.session.open(wrestlingnetworkGenreScreen)
		elif auswahl == "retro-tv":
			self.session.open(retrotvFilmListeScreen)
		#elif auswahl == "Viewster":
		#	self.session.open(viewsterGenreScreen)
		elif auswahl == "ARD Mediathek":
			self.session.open(ARDGenreScreen)
		elif auswahl == "Galileo-Videolexikon":
			self.session.open(galileovlGenreScreen)
		elif auswahl == "Sport1.fm":
			self.session.open(sport1fmGenreScreen)

		# porn
		elif auswahl == "4Tube":
			self.pornscreen = fourtubeGenreScreen
		elif auswahl == "Ah-Me":
			self.pornscreen = ahmeGenreScreen
		elif auswahl == "AmateurPorn":
			self.pornscreen = amateurpornGenreScreen
		elif auswahl == "beeg":
			self.pornscreen = beegGenreScreen
		elif auswahl == "DrTuber":
			self.pornscreen = drtuberGenreScreen
		elif auswahl == "El-Ladies":
			self.pornscreen = elladiesGenreScreen
		elif auswahl == "Eporner":
			self.pornscreen = epornerGenreScreen
		elif auswahl == "EroProfile":
			self.pornscreen = eroprofileGenreScreen
		elif auswahl == "ExtremeTube":
			self.pornscreen = extremetubeGenreScreen
		elif auswahl == "Free Online Movies":
			self.pornscreen = freeomovieGenreScreen
		elif auswahl == "G-Stream-XXX":
			self.pornscreen = gstreaminxxxGenreScreen
		elif auswahl == "HDPorn":
			self.pornscreen = hdpornGenreScreen
		elif auswahl == "hotshame":
			self.pornscreen = hotshameGenreScreen
		elif auswahl == "MegaSkanks":
			self.pornscreen = megaskanksGenreScreen
		elif auswahl == "IStream-XXX":
			self.pornscreen = showIStreamGenre
			self.cat = "porn"
		elif auswahl == "Movie4k-XXX":
			self.pornscreen = m4kGenreScreen
			self.cat = "porn"
		elif auswahl == "ParadiseHill":
			self.pornscreen = paradisehillGenreScreen
		elif auswahl == "Pinkrod":
			self.pornscreen = pinkrodGenreScreen
		elif auswahl == "PlayPorn":
			self.pornscreen = playpornGenreScreen
		elif auswahl == "PornerBros":
			self.pornscreen = pornerbrosGenreScreen
		elif auswahl == "Pornhub":
			self.pornscreen = pornhubGenreScreen
		elif auswahl == "PORNMVZ":
			self.pornscreen = pornmvzGenreScreen
		elif auswahl == "PornoStreams":
			self.pornscreen = pornostreamsGenreScreen
		elif auswahl == "PornRabbit":
			self.pornscreen = pornrabbitGenreScreen
		elif auswahl == "RealGFPorn":
			self.pornscreen = realgfpornGenreScreen
		elif auswahl == "RedTube":
			self.pornscreen = redtubeGenreScreen
		elif auswahl == "SeXXX-HD":
			self.pornscreen = sexxxhdGenreScreen
		elif auswahl == "SunPorno":
			self.pornscreen = sunpornoGenreScreen
		elif auswahl == "TheNewPorn":
			self.pornscreen = thenewpornGenreScreen
		elif auswahl == "UpdateTube":
			self.pornscreen = updatetubeGenreScreen
		elif auswahl == "WetPlace":
			self.pornscreen = wetplaceGenreScreen
		elif auswahl == "xHamster":
			self.pornscreen = xhamsterGenreScreen
		elif auswahl == "XXXSaVe":
			self.pornscreen = xxxsaveFilmScreen
		elif auswahl == "YouPorn":
			self.pornscreen = youpornGenreScreen

		if self.pornscreen:
			if config.mediaportal.pornpin.value:
				self.session.openWithCallback(self.pincheckok, PinInput, pinList = [(config.mediaportal.pincode.value)], triesEntry = self.getTriesEntry(), title = _("Please enter the correct pin code"), windowTitle = _("Enter pin code"))
			else:
				if self.cat == "":
					self.session.open(self.pornscreen)
				else:
					self.session.open(self.pornscreen, self.cat)

	def pincheckok(self, pincode):
		if pincode:
			if self.cat == "":
				self.session.open(self.pornscreen)
			else:
				self.session.open(self.pornscreen, self.cat)

	def	keyLeft(self):
		if self.check_empty_list():
			return
		if self.selektor_index > 1:
			self.selektor_index -= 1
			self.move_selector()
		else:
			self.page_back()

	def	keyRight(self):
		if self.check_empty_list():
			return
		if self.selektor_index < 40 and self.selektor_index != len(self.mainlist[int(self.select_list)]):
			self.selektor_index += 1
			self.move_selector()
		else:
			self.page_next()

	def keyUp(self):
		if self.check_empty_list():
			return
		if self.selektor_index-8 > 1:
			self.selektor_index -=8
			self.move_selector()
		else:
			self.selektor_index = 1
			self.move_selector()

	def keyDown(self):
		if self.check_empty_list():
			return
		if self.selektor_index+8 <= len(self.mainlist[int(self.select_list)]):
			self.selektor_index +=8
			self.move_selector()
		else:
			self.selektor_index = len(self.mainlist[int(self.select_list)])
			self.move_selector()

	def page_next(self):
		if self.check_empty_list():
			return
		if self.select_list < len(self.mainlist)-1:
			self.paint_hide()
			self.select_list += 1
			self.paint_new()

	def page_back(self):
		if self.check_empty_list():
			return
		if self.select_list > 0:
			self.paint_hide()
			self.select_list -= 1
			self.paint_new_last()

	def check_empty_list(self):
		if len(self.plugin_liste) == 0:
			self['name'].setText('Keine Plugins der Kategorie %s aktiviert !' % config.mediaportal.filter.value)
			self["frame"].hide()
			return True
		else:
			return False

	def paint_hide(self):
		for x in self.mainlist[int(self.select_list)]:
			self["zeile"+str(x)].hide()

	def paint_new_last(self):
		pageinfo = "%s / %s" % (self.select_list+1, len(self.mainlist))
		self['page'].setText(pageinfo)
		self.selektor_index = len(self.mainlist[int(self.select_list)])
		#self.selektor_index = self.mainlist[int(self.select_list)][-1]
		print self.selektor_index
		self.move_selector()
		# Apple Page Style
		if config.mediaportal.showapplepagestyle.value and len(self.plugin_liste_page_tmp) != 0:
			self.refresh_apple_page_bar()

		for x in self.mainlist[int(self.select_list)]:
			self["zeile"+str(x)].show()

	def paint_new(self):
		pageinfo = "%s / %s" % (self.select_list+1, len(self.mainlist))
		self['page'].setText(pageinfo)
		self.selektor_index = 1
		self.move_selector()
		# Apple Page Style
		if config.mediaportal.showapplepagestyle.value and len(self.plugin_liste_page_tmp) != 0:
			self.refresh_apple_page_bar()

		for x in self.mainlist[int(self.select_list)]:
			self["zeile"+str(x)].show()

	# Apple Page Style
	def refresh_apple_page_bar(self):
		for x in range(1,len(self.mainlist)+1):
			if x == self.select_list+1:
				self["page_empty"+str(x)].hide()
				self["page_sel"+str(x)].show()
			else:
				self["page_sel"+str(x)].hide()
				self["page_empty"+str(x)].show()

	def keySetup(self):
		if config.mediaportal.setuppin.value:
			self.session.openWithCallback(self.pinok, PinInput, pinList = [(config.mediaportal.pincode.value)], triesEntry = self.getTriesEntry(), title = _("Please enter the correct pin code"), windowTitle = _("Enter pin code"))
		else:
			self.session.openWithCallback(self.restart, hauptScreenSetup)

	def keyHelp(self):
		self.session.open(HelpScreen)

	def getTriesEntry(self):
		return config.ParentalControl.retries.setuppin

	def pinok(self, pincode):
		if pincode:
			self.session.openWithCallback(self.restart, hauptScreenSetup)

	def chSort(self):
		print "Sort: %s" % config.mediaportal.sortplugins.value

		if config.mediaportal.sortplugins.value == "hits":
			config.mediaportal.sortplugins.value = "abc"
		elif config.mediaportal.sortplugins.value == "abc":
			config.mediaportal.sortplugins.value = "user"
		elif config.mediaportal.sortplugins.value == "user":
			config.mediaportal.sortplugins.value = "hits"

		print "Sort changed:", config.mediaportal.sortplugins.value
		self.restart()

	def chFilter(self):
		print "Filter:", config.mediaportal.filter.value

		if config.mediaportal.filter.value == "ALL":
			config.mediaportal.filter.value = "Mediathek"
		elif config.mediaportal.filter.value == "Mediathek":
			config.mediaportal.filter.value = "Grauzone"
		elif config.mediaportal.filter.value == "Grauzone":
			config.mediaportal.filter.value = "Sport"
		elif config.mediaportal.filter.value == "Sport":
			config.mediaportal.filter.value = "Music"
		elif config.mediaportal.filter.value == "Music":
			config.mediaportal.filter.value = "Fun"
		elif config.mediaportal.filter.value == "Fun":
			config.mediaportal.filter.value = "Porn"
		elif config.mediaportal.filter.value == "Porn":
			config.mediaportal.filter.value = "ALL"

		print "Filter changed:", config.mediaportal.filter.value
		self.restartAndCheck()

	def restartAndCheck(self):
		if config.mediaportal.filter.value != "ALL":
			dump_liste2 = self.dump_liste
			self.plugin_liste = []
			self.plugin_liste = [x for x in dump_liste2 if re.search(config.mediaportal.filter.value, x[2])]
			if len(self.plugin_liste) == 0:
				print "Filter ist deaktviert.. recheck..: %s" % config.mediaportal.filter.value
				self.chFilter()
			else:
				print "Mediaportal restart."
				config.mediaportal.filter.save()
				configfile.save()
				self.close(self.session, False)
		else:
			print "Mediaportal restart."
			config.mediaportal.filter.save()
			configfile.save()
			self.close(self.session, False)

	def showPorn(self):
		if config.mediaportal.showporn.value:
			config.mediaportal.showporn.value = False
			if config.mediaportal.filter.value == "Porn":
				self.chFilter()
			config.mediaportal.showporn.save()
			config.mediaportal.filter.save()
			configfile.save()
			self.restart()
		else:
			self.session.openWithCallback(self.showPornOK, PinInput, pinList = [(config.mediaportal.pincode.value)], triesEntry = self.getTriesEntry(), title = _("Please enter the correct pin code"), windowTitle = _("Enter pin code"))

	def showPornOK(self, pincode):
		if pincode:
			config.mediaportal.showporn.value = True
			config.mediaportal.showporn.save()
			configfile.save()
			self.restart()

	def keyCancel(self):
		config.mediaportal.filter.save()
		configfile.save()
		self.close(self.session, True)

	def restart(self):
		print "Mediaportal restart."
		config.mediaportal.filter.save()
		config.mediaportal.sortplugins.save()
		configfile.save()
		self.close(self.session, False)

def exit(session, result):
	if not result:
		if config.mediaportal.ansicht.value == "liste":
			session.openWithCallback(exit, haupt_Screen)
		else:
			session.openWithCallback(exit, haupt_Screen_Wall, config.mediaportal.filter.value)

def main(session, **kwargs):
	if config.mediaportal.ansicht.value == "liste":
		session.openWithCallback(exit, haupt_Screen)
	else:
		session.openWithCallback(exit, haupt_Screen_Wall, config.mediaportal.filter.value)

def Plugins(path, **kwargs):
	mp_globals.pluginPath = path

	return PluginDescriptor(name=_("MediaPortal"), description="MediaPortal", where = [PluginDescriptor.WHERE_PLUGINMENU, PluginDescriptor.WHERE_EXTENSIONSMENU], icon="plugin.png", fnc=main)