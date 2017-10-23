import weechat, os, re, HTMLParser

try:
	import urllib, requests
except:
	raise ImportError("Something's not right.")

urlStart = "http://www.network-science.de/ascii/ascii.php?TEXT="
urlEnd = "&FONT=standard&RICH=no&FORM=left&STRE=no&WIDT=80"
regex = r"<pre>((.|\s)*?)</pre>"

description = "Generates annoyingly large ascii art text. Likely to get you banned for flood";

weechat.register("AsciiArtText", "Ergot", "VERSION", "LICENSE", description, "", "")
weechat.hook_command("aartt", "Generate ascii art text", "", "", "", "floodAsciiArt", "")

def floodAsciiArt(data, buffer, args):
	message = "".join(args);
	text = requests.get(urlStart + message + urlEnd).text
	match = re.findall(regex, text, re.I)[1][0]
	art = "." + HTMLParser.HTMLParser().unescape(match)[1:];

	weechat.command("", "/msg " + art)

	return weechat.WEECHAT_RC_OK
