# coding: utf8

import sys
import xbmcgui
import xbmcplugin
import urllib
import urlparse
import xbmc
import xbmcaddon

import json
import datetime

from bs4 import BeautifulSoup
import requests

reload(sys)
sys.setdefaultencoding('utf8')

base_url = sys.argv[0]
addon_handle = int(sys.argv[1])
args = urlparse.parse_qs(sys.argv[2][1:])
xbmcplugin.setContent(addon_handle, 'movies')

_addon_id      = 'plugin.video.airtango'
_addon         = xbmcaddon.Addon(id=_addon_id)
_addon_name    = _addon.getAddonInfo('name')
_addon_handler = int(sys.argv[1])
_addon_url     = sys.argv[0]
_addon_path    = xbmc.translatePath(_addon.getAddonInfo("path") )

def build_url(query):
    return base_url + '?' + urllib.urlencode(query)

mode = args.get('mode', None)

#Rohdaten
now = datetime.datetime.now()
base_url_1 = "https://www.airtango.live/api/content-box/?baseconfig=40&module=2551&live=true&exclude=76925"
#base_url_2 = "/contents?needTotalCount=true"
#base_url_main = "https://www.2basketballbundesliga.de"
stream_url_1 = "https://www.airtango.live/api/v2/content/"
stream_url_2 = "/access"
if mode is None:
    #foldername = "Heute live"
    #url = build_url({'mode': 'foldertoday', 'foldername': foldername})
    #li = xbmcgui.ListItem(foldername, iconImage='DefaultFolder.png')
    #xbmcplugin.addDirectoryItem(handle=addon_handle, url=url, listitem=li, isFolder=True)
    j = 0
    #base_url_0 = base_url_1
    response = urllib.urlopen(base_url_1).read()
    jsonResult = json.loads(response)

    while j < len(jsonResult['data']):
        gameID = jsonResult['data'][j]['id']
        startzeit = jsonResult['data'][j]['start_datetime']['date']
        #xbmc.log(startzeit[:16])
        foldername = startzeit[:16]+": "+jsonResult['data'][j]['fields']['Title'][0]['title']
        url = build_url({'mode': 'playGame', 'foldername': foldername, 'gameID': gameID})
        li = xbmcgui.ListItem(foldername, iconImage='DefaultFolder.png')
        #, isFolder=True
        xbmcplugin.addDirectoryItem(handle=addon_handle, url=url, listitem=li)
        j = j + 1
    xbmcplugin.endOfDirectory(addon_handle)

elif mode[0] == 'playGame':
#    xbmc.log("hiaerad: "+args['gameID'][0])
    stream_url_0 = stream_url_1 + args['gameID'][0]+stream_url_2
    streamURL_response = requests.post(url=stream_url_0)
    xbmc.log("hierasddd: "+streamURL_response.json()['status'])
    if streamURL_response.json()['status'] == "error":
        xbmcgui.Dialog().ok(_addon_name, "Spiel noch nicht verfügbar - ggf. noch nicht begonnen?")
        xbmcplugin.setResolvedUrl(_addon_handler, False, xbmcgui.ListItem())
    else:
        streamURL = streamURL_response.json()['data']['stream']
     #   xbmc.log("hierasd "+stream_url_1+" - "+streamURL)
        listitem = xbmcgui.ListItem(path=streamURL)
        listitem.setProperty('inputstreamaddon', 'inputstream.adaptive')
        listitem.setProperty('inputstream.adaptive.manifest_type', 'hls')
        listitem.setInfo('video', '')
        listitem.setProperty('IsPlayable', 'true')
        xbmcplugin.setResolvedUrl(_addon_handler, True, listitem)

#elif mode[0] == 'folder1':
#    j2 = args['gameID'][0]
#    print("hierhierhier: "+j2)
#    response = urllib.urlopen(base_url_1).read()
#    jsonResult = json.loads(response)
#    i = 0
#    while i < len(jsonResult):
#        #try:
#            #if len(jsonResult[i]['expectedAt']) > 9:
#            #if str(now)[:10] == jsonResult[i]['expectedAt'][:10]:
#        name = jsonResult[i]['subtitle'] + ": " + jsonResult[i]['name']
#        url = jsonResult[i]['contentURL']
#        image = jsonResult[i]['teaser']['default']
#        li = xbmcgui.ListItem(name, iconImage=image)
#        xbmcplugin.addDirectoryItem(handle=addon_handle, url=url,
#                listitem=li)
        #except:
        #    fehler = "fehler"
#        i = i + 1
#    xbmcplugin.endOfDirectory(addon_handle)

#    #listitem = xbmcgui.ListItem(path=url)
#    #listitem.setProperty('inputstreamaddon', 'inputstream.adaptive')
#    #listitem.setProperty('inputstream.adaptive.manifest_type', 'hls')
#    #xbmcplugin.setResolvedUrl(_addon_handler, True, listitem)

#elif mode[0] == 'foldertoday':
#    page = requests.get(base_url_main)
#    soup = BeautifulSoup(page.content, 'html.parser')
#    result_0 = soup.findAll("div", {"class": "dc-table"})
#    lines = []
#    counter = 0
#    for ul in result_0:
#        lines.extend(ul.findAll("div", {"class": "dc-cell"}))
#        #print("asdfasgasdg")
#        counter = counter + 1
#    i = 0
#    #print("hierasdf"+lines[0])
#    while i < len(lines):
#        if (str(lines[i])[str(lines[i]).find('>')+1:str(lines[i]).find('</')]) == "Heute":
#            i = i + 1
#            #Zeit
#            time = str(lines[i])[str(lines[i]).find('>')+1:str(lines[i]).find('</')]
#            i = i + 1
#            j = 0
#            name = str(lines[i])[str(lines[i]).find('<b>')+3:str(lines[i]).find('</b>')]
#            if name == "BAU":
#                j = 3
#            elif name == "HH":
#                j = 8
#            elif name == "HAN":
#                j = 10
#            elif name == "HD":
#                j = 12
#            elif name == "CH":
#                j = 14
#            elif name == "NÜR":
#                j == 16
#            elif name == "HAG":
#                j = 20
#            elif name == "PSK":
#                j = 22
#            elif name == "TRI":
#                j = 28
#            elif name == "EHI":
#                j = 30
#            elif name == "PB":#
#                j = 34
#            elif name == "KIR":
#                j = 36
#            elif name == "ART":
#                j = 86
#            elif name == "TUB":
#                j = 101
#            elif name == "S04":
#                j = 114
#            elif name == "HRO":
#                j = 138
#            else:
#                j = 0
#            i = i + 2
#            name = time+" Uhr: "+getfullteamname(name)+" - "+getfullteamname(str(lines[i])[str(lines[i]).find('<b>')+3:str(lines[i]).find('</b>')])
#            i = i + 2
#            #print("hierhierhier: " + str(j))

#            base_url_0 = base_url_1 + str(j) + base_url_2
#            response = urllib.urlopen(base_url_0).read()
#            jsonResult = json.loads(response)
#            #i2 = Spieltag

#            #print("hierhierhier "+str(now)[8:10]+"."+str(now)[5:7]+"."+str(now)[0:4])
#            i2 = 0
#            i3 = 0
#            while i3 < len(jsonResult):
#                if str(jsonResult[i3]['subtitle'])[:10] == str(now)[8:10]+"."+str(now)[5:7]+"."+str(now)[0:4]:
#                    i2 = i3
#                    i3 = len(jsonResult)
#                i3 = i3 + 1
#            #print name+" asdfasgasgasdg "+str(jsonResult[i2]['subtitle'])[:10]
#            #print(str(now)[8:10]+"."+str(now)[5:7]+"."+str(now)[0:4])

 #           #name = name+" ("+str(i2+1)+". Spieltag)"
 #           #name = name+" "+str(i2)

#            url = jsonResult[i2]['contentURL']
#            image = jsonResult[i2]['teaser']['default']
#            li = xbmcgui.ListItem(name, iconImage=image)
#            xbmcplugin.addDirectoryItem(handle=addon_handle, url=url,
#                    listitem=li)

#        else:
#            i = i + 6
#    xbmcplugin.endOfDirectory(addon_handle)