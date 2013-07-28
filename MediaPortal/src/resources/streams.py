from Screens.MessageBox import MessageBox
from twisted.web.client import getPage
from twisted.web import client, error as weberror
from twisted.internet import reactor
from twisted.internet import defer
from urllib import quote, urlencode
import re, urllib2, urllib, cookielib
from jsunpacker import cJsUnpacker
from flashx import Flashx
from userporn import Userporn
from twagenthelper import TwAgentHelper


# cookies
ck = {}
cj = {}

class get_stream_link:

	def __init__(self, session):
		self._callback = None
		self.session = session
		self.showmsgbox = True
		self.tw_agent_hlp = TwAgentHelper()

	def check_link(self, data, got_link, showmsgbox=True):
		print "check_link"
		self._callback = got_link
		self.showmsgbox = showmsgbox
		if data:
			if re.match(".*?http://www.putlocker.com/(file|embed)/", data, re.S):
				link = data.replace('file','embed')
				#print "ok:", link
				if link:
					getPage(link, headers={'Content-Type':'application/x-www-form-urlencoded'}).addCallback(self.streamPutlockerSockshare, link, "putlocker").addErrback(self.errorload)

			elif re.match(".*?http://www.sockshare.com/(file|embed)/", data, re.S):
				link = data.replace('file','embed')
				#print link
				if link:
					getPage(link, headers={'Content-Type':'application/x-www-form-urlencoded'}).addCallback(self.streamPutlockerSockshare, link, "sockshare").addErrback(self.errorload)

			elif re.match(".*?http://streamcloud.eu/", data, re.S):
				#link = re.findall("(http://streamcloud.eu/.*?)'", data, re.S)
				link = data
				if link:
					getPage(link, cookies=ck, headers={'Content-Type':'application/x-www-form-urlencoded'}).addCallback(self.streamcloud).addErrback(self.errorload)

			elif re.match('.*?http://xvidstage.com', data, re.S):
				link = data
				#print "xvidstage"
				getPage(link, headers={'Content-Type':'application/x-www-form-urlencoded'}).addCallback(self.xvidstage_post, link).addErrback(self.errorload)

			elif re.match('.*?http://filenuke.com', data, re.S):
				link = data
				getPage(link, headers={'Content-Type':'application/x-www-form-urlencoded'}).addCallback(self.filenuke, link).addErrback(self.errorload)

			elif re.match('.*?http://movreel.com/', data, re.S):
				link = data
				#print link
				getPage(link, headers={'Content-Type':'application/x-www-form-urlencoded'}).addCallback(self.movreel_data, link).addErrback(self.errorload)

			elif re.match('.*?http://xvidstream.net/', data, re.S):
				link = data
				#print link
				getPage(link, headers={'Content-Type':'application/x-www-form-urlencoded'}).addCallback(self.xvidstream).addErrback(self.errorload)

			elif re.match('.*?http://(www|embed).nowvideo.eu', data, re.S):
				link = data
				#print link
				getPage(link, headers={'Content-Type':'application/x-www-form-urlencoded'}).addCallback(self.nowvideo).addErrback(self.errorload)

			elif re.match('.*?http://www.uploadc.com', data, re.S):
				link = data
				#print link
				getPage(link, headers={'Content-Type':'application/x-www-form-urlencoded'}).addCallback(self.uploadc, link).addErrback(self.errorload)

			elif re.match('.*?http://vreer.com', data, re.S):
				link = data
				#print link
				getPage(link, headers={'Content-Type':'application/x-www-form-urlencoded'}).addCallback(self.vreer, link).addErrback(self.errorload)

			elif re.match('.*?http://www.monsteruploads.eu', data, re.S):
				link = data
				#print link
				getPage(link, headers={'Content-Type':'application/x-www-form-urlencoded'}).addCallback(self.monsteruploads, link).addErrback(self.errorload)

			elif re.match('.*?flashstream.in', data, re.S):
				link = data
				#print link
				getPage(link, headers={'Content-Type':'application/x-www-form-urlencoded'}).addCallback(self.flashstream).addErrback(self.errorload)

			elif re.match('.*?ginbig.com', data, re.S):
				link = data
				#print link
				getPage(link, headers={'Content-Type':'application/x-www-form-urlencoded'}).addCallback(self.ginbig_flashstream, link).addErrback(self.errorload)

			elif re.match('.*?videoweed.es', data, re.S):
				link = data
				#print link
				getPage(link, headers={'Content-Type':'application/x-www-form-urlencoded'}).addCallback(self.videoweed).addErrback(self.errorload)

			elif re.match('.*?novamov.com', data, re.S):
				link = data
				#print link
				getPage(link, headers={'Content-Type':'application/x-www-form-urlencoded'}).addCallback(self.novamov).addErrback(self.errorload)

			elif re.match('.*?.movshare.net', data, re.S):
				link = data
				#print link
				getPage(link, cookies=cj, headers={'Content-Type':'application/x-www-form-urlencoded'}).addCallback(self.movshare, link).addErrback(self.errorload)

			elif re.match('.*divxstage', data, re.S):
				link = data
				#print link
				getPage(link, headers={'Content-Type':'application/x-www-form-urlencoded'}).addCallback(self.divxstage).addErrback(self.errorload)

			elif re.match('.*?yesload.net', data, re.S):
				link = data
				#print link
				id = link.split('/')
				id = id[-1]
				if id:
					#print id
					api_url = "http://yesload.net/player_api/info?token=%s" % id
					getPage(api_url, headers={'Content-Type':'application/x-www-form-urlencoded'}).addCallback(self.yesload).addErrback(self.errorload)
				else:
					self.stream_not_found()

			elif re.match('.*?faststream', data, re.S):
				link = data
				#print link
				getPage(link, headers={'Content-Type':'application/x-www-form-urlencoded'}).addCallback(self.faststream, link).addErrback(self.errorload)

			elif re.match('.*?primeshare', data, re.S):
				link = data
				#print link
				getPage(link, cookies=cj, headers={'Content-Type':'application/x-www-form-urlencoded'}).addCallback(self.primeshare, link).addErrback(self.errorload)

			elif re.match('.*?http://vidstream.us', data, re.S):
				link = data
				#print link
				getPage(link, cookies=cj, headers={'Content-Type':'application/x-www-form-urlencoded'}).addCallback(self.vidstream_us).addErrback(self.errorload)

			elif re.match('.*?http://vidstream.in', data, re.S):
				link = data
				#print link
				getPage(link, cookies=cj, headers={'Content-Type':'application/x-www-form-urlencoded'}).addCallback(self.vidstream_in, link).addErrback(self.errorload)

			elif re.match('.*?video.istream.ws/embed', data, re.S):
				link = data
				#print link
				getPage(link, cookies=cj, headers={'Content-Type':'application/x-www-form-urlencoded'}).addCallback(self.check_istream_link).addErrback(self.errorload)

			elif re.match('.*?http:/.*?flashx.tv', data, re.S):
			#elif re.match('.*?http:/disabled', data, re.S):
				link = data
				#print link
				hash = re.findall('http://flashx.tv/video/(.*?)/', link)
				if hash:
					getPage(link, headers={'Content-Type':'application/x-www-form-urlencoded'}).addCallback(self.flashx_tv3b).addErrback(self.errorload)
				elif re.match('.*?embed.php\?hash=', link) or re.match('.*?embed_player.php\?hash=', link) or re.match('.*?embed_player.php\?vid=', link) or re.match('.*?embed.php\?vid=', link):
					self.flashx_tv3(link)
				elif re.match('.*?player/fxtv.php.hash=', link):
					self.tw_agent_hlp.getRedirectedUrl(self.check_link, self.stream_not_found, link, self._callback, False)
				else:
					print "flashx_tv link not found: ",link
					self.stream_not_found()

			elif re.match('.*?putme.org', data, re.S):
				link = data
				#print link
				getPage(link, cookies=cj, headers={'Content-Type':'application/x-www-form-urlencoded'}).addCallback(self.putme_org, link).addErrback(self.errorload)

			elif re.match('.*?divxmov.net', data, re.S):
				link = data
				#print link
				getPage(link, headers={'Content-Type':'application/x-www-form-urlencoded'}).addCallback(self.divxmov).addErrback(self.errorload)

			elif re.match('.*?sharesix.com/', data, re.S):
				link = data
				#print link
				getPage(link, headers={'Content-Type':'application/x-www-form-urlencoded'}).addCallback(self.sharesix).addErrback(self.errorload)

			elif re.match('.*?zooupload.com/', data, re.S):
				link = data
				#print link
				getPage(link, headers={'Content-Type':'application/x-www-form-urlencoded'}).addCallback(self.zooupload).addErrback(self.errorload)

			elif re.match('.*?http://wupfile.com', data, re.S):
				link = data
				print link
				getPage(link, headers={'Content-Type':'application/x-www-form-urlencoded'}).addCallback(self.wupfile_post, link).addErrback(self.errorload)

			elif re.match('.*?http://bitshare.com', data, re.S):
				link = data
				#print link
				getPage(link, headers={'Content-Type':'application/x-www-form-urlencoded'}).addCallback(self.bitshare).addErrback(self.errorload)

			elif re.match('.*?userporn.com', data, re.S):
				link = data
				#print link
				self.userporn_tv(link)

			elif re.match('.*?ecostream.tv', data, re.S):
				link = data
				getPage(link, headers={'Content-Type':'application/x-www-form-urlencoded'}).addCallback(self.eco_read).addErrback(self.errorload)

			elif re.match('.*?http://played.to', data, re.S):
				link = data
				getPage(link, cookies=cj, headers={'Content-Type':'application/x-www-form-urlencoded'}).addCallback(self.played, link).addErrback(self.errorload)

			elif re.match('.*?stream2k.com', data, re.S):
				link = data
				getPage(link, headers={'referer':link}).addCallback(self.stream2k).addErrback(self.errorload)

			elif re.match('.*?limevideo.net', data, re.S):
				link = data
				getPage(link, headers={'Content-Type':'application/x-www-form-urlencoded'}).addCallback(self.lmv, link).addErrback(self.errorload)

			elif re.match('.*?videomega.tv', data, re.S):
				link = data
				if re.match('.*?iframe.php', link):
					getPage(link, headers={'Content-Type':'application/x-www-form-urlencoded'}).addCallback(self.videomega).addErrback(self.errorload)
				else:
					id = link.split('ref=')
					if id:
						link = "http://videomega.tv/iframe.php?ref=%s" % id[1]
						getPage(link, headers={'Content-Type':'application/x-www-form-urlencoded'}).addCallback(self.videomega).addErrback(self.errorload)
					else:
						self.stream_not_found()

			elif re.match('.*?vk.com', data, re.S):
				link = data
				getPage(link, headers={'Content-Type':'application/x-www-form-urlencoded'}).addCallback(self.vkme).addErrback(self.errorload)

			elif re.match('.*?mightyupload.com/embed', data, re.S):
				link = data
				getPage(link, headers={'Content-Type':'application/x-www-form-urlencoded'}).addCallback(self.mightyupload).addErrback(self.errorload)

			elif re.match('.*?mightyupload.com', data, re.S):
				link = data
				id = link.split('/')
				url = "http://www.mightyupload.com/embed-%s.html" % id[3]
				print url
				getPage(url, headers={'Content-Type':'application/x-www-form-urlencoded'}).addCallback(self.mightyupload).addErrback(self.errorload)

			elif re.match('.*?http://youwatch.org', data, re.S):
				link = data
				id = link.split('org/')
				url = "http://youwatch.org/embed-%s.html" % id[1]
				getPage(url, headers={'Content-Type':'application/x-www-form-urlencoded'}).addCallback(self.youwatch).addErrback(self.errorload)

			else:
				message = self.session.open(MessageBox, _("No supported Stream Hoster, try another one !"), MessageBox.TYPE_INFO, timeout=5)
		else:
			print "Invalid link",link
			if self.showmsgbox:
				message = self.session.open(MessageBox, _("Invalid Stream link, try another Stream Hoster !"), MessageBox.TYPE_INFO, timeout=5)

	def stream_not_found(self):
		self._callback(None)
		print "stream_not_found!"
		if self.showmsgbox:
			message = self.session.open(MessageBox, _("Stream not found, try another Stream Hoster."), MessageBox.TYPE_INFO, timeout=5)

	def youwatch(self, data):
		stream_url = re.findall('file: "(.*?)"', data, re.S)
		if stream_url:
			print stream_url[0]
			self._callback(stream_url[0])
		else:
			self.stream_not_found()

	def mightyupload(self, data):
		get_packedjava = re.findall("<script type=.text.javascript.>eval.function(.*?)</script>", data, re.S|re.DOTALL)
		if get_packedjava:
			print get_packedjava
			sJavascript = get_packedjava[1]
			sUnpacked = cJsUnpacker().unpackByString(sJavascript)
			if sUnpacked:
				print "unpacked"
				print sUnpacked
				if re.match('.*?type="video/divx', sUnpacked):
					print "DDIIIIIIIIIVVVXXX"
					stream_url = re.findall('type="video/divx"src="(.*?)"', sUnpacked)
					if stream_url:
						print stream_url[0]
						self._callback(stream_url[0])
					else:
						self.stream_not_found()
				elif re.match(".*?file", sUnpacked):
					print "FFFFFFFFLLLLLLLLLLLVVVVVVVV"
					stream_url = re.findall("file','(.*?)'", sUnpacked)
					if stream_url:
						print stream_url[0]
						self._callback(stream_url[0])
					else:
						self.stream_not_found()
			else:
				self.stream_not_found()
		else:
			self.stream_not_found()

	def vkme(self, data):
		print "vk.me.."
		stream_urls = re.findall('url[0-9]+=(http://.*?.vk.me/.*?/videos/.*?[0-9]+.mp4)', data)
		if stream_urls:
			print stream_urls
			stream_url = stream_urls[-1]
			print stream_url
			self._callback(stream_url)
		else:
			self.stream_not_found()

	def videomega(self, data):
		unescape = re.findall('unescape."(.*?)"', data, re.S)
		if unescape:
			javadata = urllib2.unquote(unescape[0])
			if javadata:
				stream_url = re.findall('file: "(.*?)"', javadata, re.S)
				if stream_url:
					print stream_url[0]
					self._callback(stream_url[0])
				else:
					self.stream_not_found()
			else:
				self.stream_not_found()
		else:
			self.stream_not_found()

	def lmv(self, data, url):
		dataPost = {}
		r = re.findall('input type="hidden".*?name="(.*?)".*?value="(.*?)"', data, re.S)
		for name, value in r:
			dataPost[name] = value
			dataPost.update({'method_free':'Continue to Video'})
		print dataPost
		getPage(url, method='POST', postdata=urlencode(dataPost), headers={'Content-Type':'application/x-www-form-urlencoded'}).addCallback(self.lmv2, url).addErrback(self.errorload)

	def lmv2(self, data, url):
		dataPost = {}
		r = re.findall('input type="hidden".*?name="(.*?)".*?value="(.*?)"', data, re.S)
		for name, value in r:
			dataPost[name] = value
			dataPost.update({'method_free':'Continue to Video'})
		print dataPost
		getPage(url, method='POST', postdata=urlencode(dataPost), headers={'Content-Type':'application/x-www-form-urlencoded'}).addCallback(self.lmvPlay).addErrback(self.errorload)

	def lmvPlay(self, data):
		print data
		get_packedjava = re.findall("<script type=.text.javascript.>eval.function(.*?)</script>", data, re.S|re.DOTALL)
		if get_packedjava:
			print get_packedjava
			sJavascript = get_packedjava[0]
			sUnpacked = cJsUnpacker().unpackByString(sJavascript)
			if sUnpacked:
				print "unpacked"
				print sUnpacked
				if re.match('.*?type="video/divx', sUnpacked):
					print "DDIIIIIIIIIVVVXXX"
					stream_url = re.findall('type="video/divx"src="(.*?)"', sUnpacked)
					if stream_url:
						print stream_url[0]
						self._callback(stream_url[0])
					else:
						self.stream_not_found()
				elif re.match(".*?file", sUnpacked):
					print "FFFFFFFFLLLLLLLLLLLVVVVVVVV"
					stream_url = re.findall("file','(.*?)'", sUnpacked)
					if stream_url:
						print stream_url[0]
						self._callback(stream_url[0])
					else:
						self.stream_not_found()
			else:
				self.stream_not_found()
		else:
			self.stream_not_found()

	def stream2k(self, data):
		file = re.findall("file: '(.*?)'", data, re.S)
		if file:
			self._callback(file[0])
		else:
			self.stream_not_found()

	def played(self, data, url):
		print "hole daten"
		op = re.findall('type="hidden" name="op".*?value="(.*?)"', data, re.S)
		id = re.findall('type="hidden" name="id".*?value="(.*?)"', data, re.S)
		fname = re.findall('type="hidden" name="fname".*?value="(.*?)"', data, re.S)
		referer = re.findall('type="hidden" name="referer".*?value="(.*?)"', data, re.S)
		hash = re.findall('type="hidden" name="hash".*?value="(.*?)"', data, re.S)
		if op and id and fname and referer:
			info = urlencode({
				'fname': fname[0],
				'id': id[0],
				'imhuman': "Continue to Video",
				'op': "download1",
				'referer': "",
				'hash': hash[0],
				'usr_login': ""})

			print info
			getPage(url, method='POST', cookies=cj, postdata=info, headers={'Content-Type':'application/x-www-form-urlencoded'}).addCallback(self.played_data2).addErrback(self.errorload)
			#reactor.callLater(5, self.played_data, url, method='POST', cookies=cj, postdata=info, headers={'Content-Type':'application/x-www-form-urlencoded'})
		else:
			self.stream_not_found()

	def played_data(self, *args, **kwargs):
		print "drin"
		getPage(*args, **kwargs).addCallback(self.played_data2).addErrback(self.errorload)

	def played_data2(self, data):
		print data
		stream_url = re.findall('file: "(.*?)"', data, re.S)
		if stream_url:
			print stream_url[0]
			self._callback(stream_url[0])
		else:
			self.stream_not_found()

	def eco_read(self, data):
		post_url = re.findall('<form name="setss" method="post" action="(.*?)">', data, re.S)
		if post_url:
			info = urlencode({'': '1', 'sss': '1'})
			print info
			getPage(post_url[0], method='POST', postdata=info, headers={'Content-Type':'application/x-www-form-urlencoded'}).addCallback(self.eco_post).addErrback(self.errorload)
		else:
			self.stream_not_found()

	def eco_post(self, data):
		url = "http://www.ecostream.tv/assets/js/common.js"
		data2 = urllib.urlopen(url).read()
		post_url = re.findall("url: '(http://www.ecostream.tv/.*?)\?s=", data2, re.S)
		if post_url:
			print post_url
			sPattern = "var t=setTimeout\(\"lc\('([^']+)','([^']+)','([^']+)','([^']+)'\)"
			r = re.findall(sPattern, data)
			if r:
				for aEntry in r:
					sS = str(aEntry[0])
					sK = str(aEntry[1])
					sT = str(aEntry[2])
					sKey = str(aEntry[3])

				print "current keys:", sS, sK, sT, sKey
				sNextUrl = post_url[0]+"?s="+sS+'&k='+sK+'&t='+sT+'&key='+sKey
				print "URL:", sNextUrl
				info = urlencode({'s': sS, 'k': sK, 't': sT, 'key': sKey})
				print "POST:", info
				getPage(sNextUrl, method='POST', postdata=info, headers={'Referer':'http://www.ecostream.tv', 'X-Requested-With':'XMLHttpRequest'}).addCallback(self.eco_final).addErrback(self.errorload)
			else:
				self.stream_not_found()
		else:
			self.stream_not_found()

	def eco_final(self, data):
		print "final gefunden"
		stream_url = re.findall('flashvars="file=(.*?)&', data)
		if stream_url:
			kkStreamUrl = "http://www.ecostream.tv"+stream_url[0]+"&start=0"
			kkStreamUrl = urllib2.unquote(kkStreamUrl)
			print kkStreamUrl
			self._callback(kkStreamUrl)
		else:
			self.stream_not_found()

	def zooupload(self, data):
		get_packedjava = re.findall("<script type=.text.javascript.>eval.function(.*?)</script>", data, re.S|re.DOTALL)
		if get_packedjava:
			print get_packedjava
			sJavascript = get_packedjava[1]
			sUnpacked = cJsUnpacker().unpackByString(sJavascript)
			if sUnpacked:
				print "unpacked"
				print sUnpacked
				if re.match('.*?type="video/divx', sUnpacked):
					print "DDIIIIIIIIIVVVXXX"
					stream_url = re.findall('type="video/divx"src="(.*?)"', sUnpacked)
					if stream_url:
						print stream_url[0]
						self._callback(stream_url[0])
					else:
						self.stream_not_found()
				elif re.match(".*?file", sUnpacked):
					print "FFFFFFFFLLLLLLLLLLLVVVVVVVV"
					stream_url = re.findall("file','(.*?)'", sUnpacked)
					if stream_url:
						print stream_url[0]
						self._callback(stream_url[0])
					else:
						self.stream_not_found()
			else:
				self.stream_not_found()
		else:
			self.stream_not_found()

	def wupfile_post(self, data, url):
		print "hole daten"
		op = re.findall('type="hidden" name="op".*?value="(.*?)"', data, re.S)
		id = re.findall('type="hidden" name="id".*?value="(.*?)"', data, re.S)
		fname = re.findall('type="hidden" name="fname".*?value="(.*?)"', data, re.S)
		referer = re.findall('type="hidden" name="referer".*?value="(.*?)"', data, re.S)
		if op and id and fname and referer:
			info = urlencode({
				'fname': fname[0],
				'id': id[0],
				'method_free': "Kostenloser Download",
				'op': "download1",
				'referer': "",
				'usr_login': ""})

			print info
			getPage(url, method='POST', postdata=info, headers={'Content-Type':'application/x-www-form-urlencoded'}).addCallback(self.wupfile_data).addErrback(self.errorload)
		else:
			self.stream_not_found()

	def wupfile_data(self, data):
		print "hole streamlink"
		get_packedjava = re.findall("<script type=.text.javascript.>eval.function(.*?)</script>", data, re.S|re.DOTALL)
		if get_packedjava:
			print get_packedjava
			sJavascript = get_packedjava[1]
			sUnpacked = cJsUnpacker().unpackByString(sJavascript)
			if sUnpacked:
				print "unpacked"
				print sUnpacked
				if re.match('.*?type="video/divx', sUnpacked):
					print "DDIIIIIIIIIVVVXXX"
					stream_url = re.findall('type="video/divx"src="(.*?)"', sUnpacked)
					if stream_url:
						print stream_url[0]
						self._callback(stream_url[0])
					else:
						self.stream_not_found()
				elif re.match(".*?file", sUnpacked):
					print "FFFFFFFFLLLLLLLLLLLVVVVVVVV"
					stream_url = re.findall("file','(.*?)'", sUnpacked)
					if stream_url:
						print stream_url[0]
						self._callback(stream_url[0])
					else:
						self.stream_not_found()
			else:
				self.stream_not_found()
		else:
			self.stream_not_found()

	def sharesix(self, data):
		get_packedjava = re.findall("<script type=.text.javascript.>eval.function(.*?)</script>", data, re.S|re.DOTALL)
		if get_packedjava:
			print get_packedjava
			sJavascript = get_packedjava[1]
			sUnpacked = cJsUnpacker().unpackByString(sJavascript)
			if sUnpacked:
				print "unpacked"
				print sUnpacked
				if re.match('.*?type="video/divx', sUnpacked):
					print "DDIIIIIIIIIVVVXXX"
					stream_url = re.findall('type="video/divx"src="(.*?)"', sUnpacked)
					if stream_url:
						print stream_url[0].replace('0://','http://')
						self._callback(stream_url[0].replace('0://','http://'))
					else:
						self.stream_not_found()
				elif re.match(".*?file", sUnpacked):
					print "FFFFFFFFLLLLLLLLLLLVVVVVVVV"
					stream_url = re.findall("file','(.*?)'", sUnpacked)
					if stream_url:
						print stream_url[0].replace('0://','http://')
						self._callback(stream_url[0].replace('0://','http://'))
					else:
						self.stream_not_found()
				else:
					self.stream_not_found()
			else:
				self.stream_not_found()
		else:
			self.stream_not_found()


	def divxmov(self, data):
		stream_url = re.findall('<embed type="video/divx" src="(.*?)"', data, re.S)
		if stream_url:
			self._callback(stream_url[0])
		else:
			self.stream_not_found()

	def putme_org(self, data, url):
		print "hole post infos"
		dataPost = {}
		r = re.findall('input type="hidden".*?name="(.*?)".*?value="(.*?)"', data, re.S)
		if r:
			for name, value in r:
				dataPost[name] = value
				dataPost.update({'method_free':'Continue to Video'})

			print dataPost
			getPage(url, method='POST', cookies=cj, postdata=urlencode(dataPost), headers={'Content-Type':'application/x-www-form-urlencoded'}).addCallback(self.putme_org_post, url).addErrback(self.errorload)
		else:
			self.stream_not_found()

	def putme_org_post(self, data, url):
		print "hole post infos2"
		dataPost = {}
		r = re.findall('input type="hidden".*?name="(.*?)".*?value="(.*?)"', data, re.S)
		if r:
			for name, value in r:
				dataPost[name] = value
				dataPost.update({'method_free':'Continue to Video'})

			print dataPost
			getPage(url, method='POST', postdata=urlencode(dataPost), headers={'Content-Type':'application/x-www-form-urlencoded'}).addCallback(self.putme_org_data).addErrback(self.errorload)
		else:
			self.stream_not_found()

	def putme_org_data(self, data):
		get_packedjava = re.findall("<script type=.text.javascript.>eval.function(.*?)</script>", data, re.S|re.DOTALL)
		if get_packedjava:
			print get_packedjava
			sJavascript = get_packedjava[1]
			sUnpacked = cJsUnpacker().unpackByString(sJavascript)
			if sUnpacked:
				print "unpacked"
				print sUnpacked
				if re.match('.*?type="video/divx', sUnpacked):
					print "DDIIIIIIIIIVVVXXX"
					stream_url = re.findall('type="video/divx"src="(.*?)"', sUnpacked)
					if stream_url:
						print stream_url[0].replace('0://','http://')
						self._callback(stream_url[0].replace('0://','http://'))
					else:
						self.stream_not_found()

				elif re.match(".*?file:", sUnpacked):
					print "FFFFFFFFLLLLLLLLLLLVVVVVVVV"
					stream_url = re.findall("file:'(.*?)'", sUnpacked)
					if stream_url:
						print stream_url[0].replace('0://','http://')
						self._callback(stream_url[0].replace('0://','http://'))
					else:
						self.stream_not_found()

				elif re.match('.*?value="src=', sUnpacked):
					stream_url = re.findall('value="src=(.*?flv)&', sUnpacked)
					if stream_url:
						print stream_url[0]
						self._callback(stream_url[0])
					else:
						self.stream_not_found()
				else:
					self.stream_not_found()
			else:
				self.stream_not_found()
		else:
			self.stream_not_found()

	def errorload(self, error):
		print "[streams]:", error
		self.stream_not_found()

	def flashx_tv(self, data):
		stream_url = re.findall('<file>(http://.*?flashx.tv.*?)</file>', data)
		if stream_url:
			self._callback(stream_url[0])
		else:
			self.stream_not_found()

	def flashx_tv2(self, data):
		print "flashx_tv2: ",data
		hash = re.findall('http://play.flashx.tv/player/fxtv.php.hash=(.*?)&', data, re.S)
		if hash:
			url = "http://play.flashx.tv/nuevo/player/cst.php?hash=%s" % hash[0]
			#print url
			getPage(url, headers={'Content-Type':'application/x-www-form-urlencoded'}).addCallback(self.flashx_tv).addErrback(self.errorload)
		else:
			self.stream_not_found()

	def flashx_tv3(self, link):
		print "flashx_tv3: ",link
		fx = Flashx()
		stream_url = fx.getVidUrl(link)
		if stream_url:
			self._callback(stream_url)
		else:
			self.stream_not_found()

	def flashx_tv3b(self, data):
		stream_url = re.findall('id="normal_player_cont">.*?src="(.*?)"', data, re.S)
		if stream_url:
			self.flashx_tv3(stream_url[0])
		else:
			self.stream_not_found()


	def vidstream_in(self, data, url):
		id = re.findall('type="hidden" name="id".*?value="(.*?)"', data, re.S)
		fname = re.findall('type="hidden" name="fname".*?value="(.*?)"', data, re.S)
		hash = re.findall('type="hidden" name="hash".*?value="(.*?)"', data, re.S)
		if id and fname and hash:
			print id, fname, hash
			post_data = urlencode({'op': "download1", 'usr_login': "", 'id': id[0], 'fname': fname[0], 'hash': hash[0], 'referer': "", 'imhuman': "	Proceed+to+video"})
			#getPage(url, method='POST', cookies=cj, postdata=post_data, headers={'Content-Type':'application/x-www-form-urlencoded'}).addCallback(self.vidstream_in_data).addErrback(self.errorload)
			reactor.callLater(6, self.vidstream_in_getPage, url, method='POST', cookies=cj, postdata=post_data, headers={'Content-Type':'application/x-www-form-urlencoded'})
			message = self.session.open(MessageBox, _("Stream startet in 6 sec."), MessageBox.TYPE_INFO, timeout=6)
		else:
			self.stream_not_found()
	def vidstream_in_getPage(self, *args, **kwargs):
		print "drin"
		getPage(*args, **kwargs).addCallback(self.vidstream_in_data).addErrback(self.errorload)

	def vidstream_in_data(self, data):
		stream_url = re.findall('file: "(.*?)"', data, re.S)
		if stream_url:
			self._callback(stream_url[0])
		else:
			self.stream_not_found()

	def vidstream_us(self, data):
		get_packedjava = re.findall("<script type=.text.javascript.>eval.function(.*?)</script>", data, re.S|re.DOTALL)
		if get_packedjava:
			sJavascript = get_packedjava[1]
			sUnpacked = cJsUnpacker().unpackByString(sJavascript)
			if sUnpacked:
				if re.match('.*?type="video/divx', sUnpacked):
					print "DDIIIIIIIIIVVVXXX"
					stream_url = re.findall('type="video/divx"src="(.*?)"', sUnpacked)
					if stream_url:
						print stream_url[0]
						self._callback(stream_url[0])
					else:
						self.stream_not_found()
				elif re.match(".*?'file'", sUnpacked):
					print "FFFFFFFFLLLLLLLLLLLVVVVVVVV"
					stream_url = re.findall("'file','(.*?)'", sUnpacked)
					if stream_url:
						self._callback(stream_url[0])
					else:
						self.stream_not_found()
				else:
					self.stream_not_found()
			else:
				self.stream_not_found()
		else:
			self.stream_not_found()


	def primeshare(self, data, url):
		hash = re.findall('<input type="hidden".*?name="hash".*?value="(.*?)"', data)
		if hash:
			info = urlencode({'hash': hash[0]})
			print info
			reactor.callLater(16, self.primeshare_getPage, url, method='POST', cookies=cj, postdata=info, headers={'Content-Type':'application/x-www-form-urlencoded'})
			message = self.session.open(MessageBox, _("Stream startet in 16 sec."), MessageBox.TYPE_INFO, timeout=16)
		else:
			self.stream_not_found()

	def primeshare_getPage(self, *args, **kwargs):
		print "drin"
		getPage(*args, **kwargs).addCallback(self.primeshare_data).addErrback(self.errorload)

	def primeshare_data(self, data):
		print data
		stream_url = re.findall('file: \'(.*?)\'', data, re.S)
		if stream_url:
			self._callback(stream_url[0])
		else:
			#re.findall("'(http://.*?primeshare.tv.*?)'", url)
			stream_url = re.findall("provider: 'stream'.*?url: '(http://.*?primeshare.tv.*?)'", data, re.S)
			if stream_url:
				self._callback(stream_url[0])
			else:
				self.stream_not_found()

	def faststream(self, data, url):
		op = re.findall('type="hidden" name="op".*?value="(.*?)"', data, re.S)
		id = re.findall('type="hidden" name="id".*?value="(.*?)"', data, re.S)
		fname = re.findall('type="hidden" name="fname".*?value="(.*?)"', data, re.S)
		referer = re.findall('type="hidden" name="referer".*?value="(.*?)"', data, re.S)
		hash = re.findall('type="hidden" name="hash".*?value="(.*?)"', data, re.S)
		if op and id and fname and referer and hash:
			info = urlencode({
				'fname': fname[0],
				'hash': hash[0],
				'id': id[0],
				'imhuman': "Proceed to video",
				'op':"download1",
				'referer': "",
				'usr_login': ""})

			print info
			reactor.callLater(5, self.faststream_getPage, url, method='POST', postdata=info, headers={'Content-Type':'application/x-www-form-urlencoded'})
			message = self.session.open(MessageBox, _("Stream startet in 6 sec."), MessageBox.TYPE_INFO, timeout=6)
		else:
			self.stream_not_found()

	def faststream_getPage(self, *args, **kwargs):
		print "drin"
		getPage(*args, **kwargs).addCallback(self.faststream_data).addErrback(self.errorload)

	def faststream_data(self, data):
		stream_url = re.findall('file: "(.*?)"', data, re.S)
		if stream_url:
			self._callback(stream_url[0])
		else:
			self.stream_not_found()

	def yesload(self, data):
		stream_url = re.findall('url=(.*?.flv)', data)
		if stream_url:
			self._callback(stream_url[0])
		else:
			self.stream_not_found()

	def videoweed(self, data):
		print "drin okdf"
		r = re.search('flashvars.domain="(.+?)".*flashvars.file="(.+?)".*' + 'flashvars.filekey="(.+?)"', data, re.DOTALL)
		if r:
			domain, fileid, filekey = r.groups()
			api_call = ('%s/api/player.api.php?user=undefined&codes=1&file=%s' + '&pass=undefined&key=%s') % (domain, fileid, filekey)
			if api_call:
				getPage(api_call, method='GET').addCallback(self.videoweed_data).addErrback(self.errorload)
			else:
				self.stream_not_found()
		else:
			self.stream_not_found()

	def videoweed_data(self, data):
		rapi = re.search('url=(.+?)&title=', data)
		if rapi:
			stream_url = rapi.group(1)
			if stream_url:
				print stream_url
				self._callback(stream_url)
			else:
				self.stream_not_found()
		else:
			self.stream_not_found()

	def novamov(self, data):
		file = re.findall('flashvars.file="(.*?)"', data)
		key = re.findall('flashvars.filekey="(.*?)"', data)
		if file and key:
			url = "http://www.novamov.com/api/player.api.php?file=%s&key=%s" % (file[0], key[0])
			aage = "Mozilla/5.0 (Windows; U; Windows NT 6.1; de; rv:1.9.2.17) Gecko/20110420 Firefox/3.6.17"
			getPage(url, agent=aage, method='GET').addCallback(self.novamov_data).addErrback(self.errorload)
		else:
			self.stream_not_found()

	def novamov_data(self, data):
		ar = re.search('url=(.+?)&title', data)
		if ar:
			stream_url = ar.group(1)
			print stream_url
			self._callback(stream_url)
		else:
			self.stream_not_found()

	def divxstage(self, data):
		print "divxstage drin"
		file = re.findall('flashvars.file="(.*?)"', data)
		key = re.findall('flashvars.filekey="(.*?)"', data)
		if file and key:
			url = "http://www.divxstage.eu/api/player.api.php?file=%s&key=%s" % (file[0], key[0])
			print url
			aage = "Mozilla/5.0 (Windows; U; Windows NT 6.1; de; rv:1.9.2.17) Gecko/20110420 Firefox/3.6.17"
			getPage(url, agent=aage, method='GET').addCallback(self.movshare_xml).addErrback(self.errorload)
		else:
			print "ja"
			self.stream_not_found()

	def movshare(self, data, url):
		info = {}
		getPage(url, method='POST', cookies=cj, postdata=info, headers={'Content-Type':'application/x-www-form-urlencoded'}).addCallback(self.movshare_post).addErrback(self.errorload)

	def movshare_post(self, data):
		print "movshare drin"
		file = re.findall('flashvars.file="(.*?)"', data, re.S)
		key = re.findall('flashvars.filekey="(.*?)"', data, re.S)
		if file and key:
			url = "http://www.movshare.net/api/player.api.php?file=%s&key=%s" % (file[0], key[0])
			print url
			getPage(url, method='GET').addCallback(self.movshare_xml).addErrback(self.errorload)
		else:
			print "ja"
			self.stream_not_found()

	def movshare_xml(self, data):
		file_link = re.search('url=(.+?)&title=', data)
		if file_link:
			stream_url = file_link.group(1)
			print stream_url
			self._callback(stream_url)
		else:
			self.stream_not_found()

	def flashstream(self, data):
		get_packedjava = re.findall("<script type=.text.javascript.>eval.function(.*?)</script>", data, re.S|re.DOTALL)
		if get_packedjava:
			sJavascript = get_packedjava[1]
			sUnpacked = cJsUnpacker().unpackByString(sJavascript)
			if sUnpacked:
				if re.match('.*?type="video/divx', sUnpacked):
					print "DDIIIIIIIIIVVVXXX"
					stream_url = re.findall('type="video/divx"src="(.*?)"', sUnpacked)
					if stream_url:
						print stream_url[0]
						self._callback(stream_url[0])
					else:
						self.stream_not_found()
				elif re.match(".*?'file'", sUnpacked):
					print "FFFFFFFFLLLLLLLLLLLVVVVVVVV"
					stream_url = re.findall("'file','(.*?)'", sUnpacked)
					if stream_url:
						self._callback(stream_url[0])
					else:
						self.stream_not_found()
				else:
					self.stream_not_found()
			else:
				self.stream_not_found()
		else:
			self.stream_not_found()

	def ginbig_flashstream(self, data, url):
		op = re.findall('<input type="hidden" name="op" value="(.*?)">', data, re.S)
		id = re.findall('<input type="hidden" name="id" value="(.*?)">', data, re.S)
		fname = re.findall('<input type="hidden" name="fname" value="(.*?)">', data, re.S)
		if op and id and fname:
			post_data = urlencode({'op': 'download1', 'usr_login': '', 'id': id[0],	'fname': fname[0], 'referer': '', 'method_free': 'Kostenloser Download'	})
			getPage(url, method='POST', postdata = post_data, headers={'Content-Type':'application/x-www-form-urlencoded'}).addCallback(self.ginbig__flashstream_data).addErrback(self.errorload)
		else:
			self.stream_not_found()

	def ginbig__flashstream_data(self, data):
		get_packedjava = re.findall("<script type=.text.javascript.>eval.function(.*?)</script>", data, re.S|re.DOTALL)
		if get_packedjava:
			sJavascript = get_packedjava[1]
			sUnpacked = cJsUnpacker().unpackByString(sJavascript)
			if sUnpacked:
				stream_url = re.findall("'file','(.*?)'", sUnpacked)
				if stream_url:
					self._callback(stream_url[0])
				else:
					self.stream_not_found()
			else:
				self.stream_not_found()
		else:
			self.stream_not_found()

	def monsteruploads(self, data, url):
		if not re.match('.*?eval\(function\(p\,a\,c\,k\,e\,d', data, re.S):
			id = re.findall('type="hidden" name="id".*?value="(.*?)"', data, re.S)
			fname = re.findall('type="hidden" name="fname".*?value="(.*?)"', data, re.S)
			referer = re.findall('type="hidden" name="referer".*?value="(.*?)"', data, re.S)
			info = urlencode({
				'op':           "download2",
				'usr_login':    "",
				'id':           id[0],
				'fname':        fname[0],
				'referer':      "",
				'method_free':  "Kostenloser Download"
				})
			getPage(url, method='POST', postdata = info, headers={'Content-Type':'application/x-www-form-urlencoded'}).addCallback(self.monsteruploads_post).addErrback(self.errorload)

		else:

			get_packedjava = re.findall("<script type=.text.javascript.>eval.function(.*?)</script>", data, re.S|re.DOTALL)
			if get_packedjava:
				sJavascript = get_packedjava[1]
				sUnpacked = cJsUnpacker().unpackByString(sJavascript)
				if sUnpacked:
					stream_url = re.findall('type="video/divx"src="(.*?)"', sUnpacked)
					if stream_url:
						print stream_url[0]
						self._callback(stream_url[0])
					else:
						self.stream_not_found()
				else:
					self.stream_not_found()
			else:
				self.stream_not_found()

	def	monsteruploads_post(self, data):
		get_packedjava = re.findall("<script type=.text.javascript.>eval.function(.*?)</script>", data, re.S|re.DOTALL)
		if get_packedjava:
			sJavascript = get_packedjava[1]
			sUnpacked = cJsUnpacker().unpackByString(sJavascript)
			if sUnpacked:
				if re.match('.*?type="video/divx', sUnpacked):
					stream_url = re.findall('type="video/divx"src="(.*?)"', sUnpacked)
					if stream_url:
						print stream_url[0]
						self._callback(stream_url[0])
					else:
						self.stream_not_found()
				elif re.match('.*?playlist:.*?http://www.monsteruploads.eu', sUnpacked):
					stream_url = re.findall("playlist:.'(.*?)'", sUnpacked)
					if stream_url:
						print stream_url[0]
						self._callback(stream_url[0])
					else:
						self.stream_not_found()
				else:
					self.stream_not_found()
			else:
				self.stream_not_found()
		else:
			self.stream_not_found()

	def vreer(self, data, url):
		id = re.findall('type="hidden" name="id".*?value="(.*?)"', data, re.S)
		fname = re.findall('type="hidden" name="fname".*?value="(.*?)"', data, re.S)
		hash = re.findall('type="hidden" name="hash".*?value="(.*?)"', data, re.S)
		referer = re.findall('type="hidden" name="referer".*?value="(.*?)"', data, re.S)
		if id and fname and hash and referer:
			post_data = urlencode({'op': "download2", 'usr_login': "", 'id': id[0], 'fname': fname[0], 'hash': hash[0], 'referer': "", 'method_free': "Free Download"})
			getPage(url, method='POST', postdata = post_data, headers={'Content-Type':'application/x-www-form-urlencoded'}).addCallback(self.vreer_post).addErrback(self.errorload)

		else:
			self.stream_not_found()

	def vreer_post(self, data):
		if re.match('.*?video.flv', data, re.S):
			stream_url = re.findall('file:."(.*?)"', data, re.S)
			if stream_url:
				print stream_url[0]
				self._callback(stream_url[0])

			else:
				self.stream_not_found()
		else:
			self.stream_not_found()

	def uploadc(self, data, url):
		ipcount_val = re.findall('<input type="hidden" name="ipcount_val".*?value="(.*?)">', data)
		id = re.findall('<input type="hidden" name="id".*?value="(.*?)">', data)
		fname = re.findall('<input type="hidden" name="fname".*?alue="(.*?)">', data)
		if id and fname and ipcount_val:
			post_data = urllib.urlencode({'ipcount_val' : ipcount_val[0], 'op' : 'download2', 'usr_login' : '', 'id' : id[0], 'fname' : fname[0], 'method_free' : 'Slow access'})
			print post_data
			getPage(url, method='POST', postdata = post_data, headers={'Content-Type':'application/x-www-form-urlencoded'}).addCallback(self.uploadc_post).addErrback(self.errorload)
		else:
			print "keine post infos gefunden."
			self.stream_not_found()

	def uploadc_post(self, data):
		print data
		stream = re.findall("'file','(.*?)'", data, re.S)
		get_packedjava = re.findall("<script type=.text.javascript.>eval.function(.*?)</script>", data, re.S|re.DOTALL)
		if stream:
			print stream
			self._callback(stream[0])

		elif get_packedjava:
			sJavascript = get_packedjava[1]
			print sJavascript
			sUnpacked = cJsUnpacker().unpackByString(sJavascript)
			if sUnpacked:
				print sUnpacked
				stream_url = re.findall('type="video/divx"src="(.*?)"', sUnpacked)
				if stream_url:
					print stream_url[0]
					self._callback(stream_url[0])
				else:
					self.stream_not_found()
			else:
				self.stream_not_found()
		else:
			self.stream_not_found()

	def nowvideo(self, data):
		file = re.findall('flashvars.file="(.*?)"', data)
		key = re.findall('flashvars.filekey="(.*?)"', data)
		if file and key:
			url = "http://www.nowvideo.eu/api/player.api.php?file=%s&key=%s" % (file[0], key[0])
			getPage(url, headers={'Content-Type':'application/x-www-form-urlencoded'}).addCallback(self.nowvideo_xml).addErrback(self.errorload)
		else:
			self.stream_not_found()

	def nowvideo_xml(self, data):
		rapi = re.search('url=(.+?)&title=', data)
		if rapi:
			stream_url = rapi.group(1)
			self._callback(stream_url)
		else:
			self.stream_not_found()

	def xvidstream(self, data):
		get_packedjava = re.findall("<script type=.text.javascript.>eval.function(.*?)</script>", data, re.S|re.DOTALL)
		if get_packedjava:
			sJavascript = get_packedjava[1]
			sUnpacked = cJsUnpacker().unpackByString(sJavascript)
			if sUnpacked:
				stream_url = re.findall('type="video/divx"src="(.*?)"', sUnpacked)
				if stream_url:
					print stream_url[0]
					self._callback(stream_url[0])
				else:
					self.stream_not_found()
			else:
				self.stream_not_found()
		else:
			self.stream_not_found()

	def movreel_data(self, data, url):
		id = re.findall('<input type="hidden" name="id".*?value="(.*?)">', data)
		fname = re.findall('<input type="hidden" name="fname".*?value="(.*?)">', data)
		if id and fname:
			post_data = urllib.urlencode({'op': 'download1', 'usr_login': '', 'id': id[0], 'fname': fname[0], 'referer': '', 'method_free': ' Kostenloser Download'})
			getPage(url, method='POST', postdata = post_data, headers={'Content-Type':'application/x-www-form-urlencoded'}).addCallback(self.movreel_post_data, url, fname[0]).addErrback(self.errorload)
		else:
			self.stream_not_found()

	def movreel_post_data(self, data, url, fname):
		id = re.findall('<input type="hidden" name="id".*?value="(.*?)">', data)
		rand = re.findall('<input type="hidden" name="rand".*?value="(.*?)">', data)
		if id and rand:
			post_data = urllib.urlencode({'op': 'download2', 'usr_login': '', 'id': id[0], 'rand': rand[0], 'referer': '', 'method_free': ' Kostenloser Download'})
			getPage(url, method='POST', postdata = post_data, headers={'Content-Type':'application/x-www-form-urlencoded'}).addCallback(self.movreel_post_data2, fname).addErrback(self.errorload)
		else:
			self.stream_not_found()

	def movreel_post_data2(self, data, fname):
		stream_url = re.findall("var file_link = '(.*?)'", data, re.S)
		if stream_url:
			self._callback(stream_url[0])
		else:
			self.stream_not_found()

	def filenuke(self, data, url):
		print "drin "
		id = re.findall('<input type="hidden" name="id".*?value="(.*?)">', data)
		fname = re.findall('<input type="hidden" name="fname".*?alue="(.*?)">', data)
		post_data = urllib.urlencode({'op': 'download1', 'usr_login': '', 'id': id[0], 'fname': fname[0], 'referer': '', 'method_free': 'free'})
		#print post_data
		getPage(url, method='POST', postdata = post_data, headers={'Content-Type':'application/x-www-form-urlencoded'}).addCallback(self.filenuke_data).addErrback(self.errorload)

	def filenuke_data(self, data):
		print "drin2"
		get_packedjava = re.findall("<script type=.text.javascript.>eval.function(.*?)</script>", data, re.S|re.DOTALL)
		if get_packedjava:
			print get_packedjava
			sJavascript = get_packedjava[1]
			sUnpacked = cJsUnpacker().unpackByString(sJavascript)
			if sUnpacked:
				print "unpacked"
				print sUnpacked
				if re.match('.*?type="video/divx', sUnpacked):
					print "DDIIIIIIIIIVVVXXX"
					stream_url = re.findall('type="video/divx"src="(.*?)"', sUnpacked)
					if stream_url:
						print stream_url[0]
						self._callback(stream_url[0])
					else:
						self.stream_not_found()
				elif re.match(".*?file", sUnpacked):
					print "FFFFFFFFLLLLLLLLLLLVVVVVVVV"
					stream_url = re.findall("file','(.*?)'", sUnpacked)
					if stream_url:
						print stream_url[0]
						self._callback(stream_url[0])
					else:
						self.stream_not_found()
			else:
				self.stream_not_found()
		else:
			self.stream_not_found()

	def streamPutlockerSockshare(self, data, url, provider):
		if re.match('.*?File Does not Exist', data, re.S):
			message = self.session.open(MessageBox, "File Does not Exist, or Has Been Removed", MessageBox.TYPE_INFO, timeout=5)
		elif re.match('.*?Encoding to enable streaming is in progresss', data, re.S):
			message = self.session.open(MessageBox, "Encoding to enable streaming is in progresss. Try again soon.", MessageBox.TYPE_INFO, timeout=5)
		else:
			print "provider:", provider
			enter = re.findall('<input type="hidden" value="(.*?)" name="fuck_you">', data)
			print "enter:", enter
			values = {'fuck_you': enter[0], 'confirm': 'Close+Ad+and+Watch+as+Free+User'}
			user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
			headers = { 'User-Agent' : user_agent}
			cookiejar = cookielib.LWPCookieJar()
			cookiejar = urllib2.HTTPCookieProcessor(cookiejar)
			opener = urllib2.build_opener(cookiejar)
			urllib2.install_opener(opener)
			data = urlencode(values)
			req = urllib2.Request(url, data, headers)
			try:
				response = urllib2.urlopen(req)
			except urllib2.HTTPError, e:
				print e.code
				self.stream_not_found()
			except urllib2.URLError, e:
				print e.args
				self.stream_not_found()
			else:
				link = response.read()
				if link:
					print "found embed data"
					embed = re.findall("get_file.php.stream=(.*?)'\,", link, re.S)
					if embed:
						req = urllib2.Request('http://www.%s.com/get_file.php?stream=%s' %(provider, embed[0]))
						req.add_header('User-Agent', user_agent)
						try:
							response = urllib2.urlopen(req)
						except urllib2.HTTPError, e:
							print e.code
							self.stream_not_found()
						except urllib2.URLError, e:
							print e.args
							self.stream_not_found()
						else:
							link = response.read()
							if link:
								stream_url = re.findall('<media:content url="(.*?)"', link, re.S)
								print stream_url[1].replace('&amp;','&')
								self._callback(stream_url[1].replace('&amp;','&'))
							else:
								self.stream_not_found()
					else:
						self.stream_not_found()
				else:
					self.stream_not_found()

	def streamcloud(self, data):
		id = re.findall('<input type="hidden" name="id".*?value="(.*?)">', data)
		fname = re.findall('<input type="hidden" name="fname".*?alue="(.*?)">', data)
		hash = re.findall('<input type="hidden" name="hash" value="(.*?)">', data)
		if id and fname and hash:
			url = "http://streamcloud.eu/%s" % id[0]
			post_data = urllib.urlencode({'op': 'download2', 'usr_login': '', 'id': id[0], 'fname': fname[0], 'referer': '', 'hash': hash[0], 'imhuman':'Weiter+zum+Video'})
			getPage(url, method='POST', cookies=ck, postdata=post_data, headers={'Content-Type':'application/x-www-form-urlencoded'}).addCallback(self.streamcloud_data).addErrback(self.errorload)
		else:
			self.stream_not_found()

	def streamcloud_data(self, data):
		stream_url = re.findall('file: "(.*?)"', data)
		if stream_url:
			print stream_url
			self._callback(stream_url[0])
		elif re.match('.*?This video is encoding now', data, re.S):
			self.session.open(MessageBox, _("This video is encoding now. Please check back later."), MessageBox.TYPE_INFO, timeout=10)
		else:
			self.stream_not_found()

	def xvidstage_post(self, data, url):
		print "hole daten"
		op = re.findall('type="hidden" name="op".*?value="(.*?)"', data, re.S)
		id = re.findall('type="hidden" name="id".*?value="(.*?)"', data, re.S)
		fname = re.findall('type="hidden" name="fname".*?value="(.*?)"', data, re.S)
		referer = re.findall('type="hidden" name="referer".*?value="(.*?)"', data, re.S)
		if op and id and fname and referer:
			info = urlencode({
				'fname': fname[0],
				'id': id[0],
				'method_free': "Weiter zu Video / Stream Video",
				'op': "download1",
				'referer': "",
				'usr_login': ""})
			getPage(url, method='POST', postdata=info, headers={'Content-Type':'application/x-www-form-urlencoded'}).addCallback(self.xvidstage_data).addErrback(self.errorload)
		else:
			self.stream_not_found()

	def xvidstage_data(self, data):
		print "drin"
		get_packedjava = re.findall("<script type=.text.javascript.>eval.function(.*?)</script>", data, re.S|re.DOTALL)
		if get_packedjava:
			print get_packedjava[1]
			sJavascript = get_packedjava[1]
			sUnpacked = cJsUnpacker().unpackByString(sJavascript)
			if sUnpacked:
				#stream_url = re.findall("'file','(.*?)'", sUnpacked)
				stream_url = re.findall('type="video/divx"src="(.*?)"', sUnpacked)
				if stream_url:
					print stream_url[0]
					self._callback(stream_url[0])
				else:
					self.stream_not_found()
			else:
				self.stream_not_found()
		else:
			self.stream_not_found()

	def bitshare(self, data):
		stream_url = re.findall('(url: |src=)\'(.*?.avi|.*?.mp4)\'', data)
		if stream_url:
			link = stream_url[0][1]
			reactor.callLater(6, self.bitshare_start, link)
			self.session.open(MessageBox, _("Stream startet in 6 sec."), MessageBox.TYPE_INFO, timeout=6)
		else:
			self.stream_not_found()

	def bitshare_start(self, link):
		#print "bs_start: ",link
		self._callback(link)

	def userporn_tv(self, link):
		#print "userporn: ",link
		fx = Userporn()
		stream_url = fx.get_media_url(link)
		if stream_url:
			self._callback(stream_url)
		else:
			self.stream_not_found()

	def check_istream_link(self, data):
		self.check_link(data, self._callback)