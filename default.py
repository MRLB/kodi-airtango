# coding: utf8

import sys
import xbmcgui
import xbmcplugin
import urllib
import urlparse

import json
import datetime

from bs4 import BeautifulSoup
import requests

base_url = sys.argv[0]
addon_handle = int(sys.argv[1])
args = urlparse.parse_qs(sys.argv[2][1:])
xbmcplugin.setContent(addon_handle, 'movies')

def build_url(query):
    return base_url + '?' + urllib.urlencode(query)

def getfullteamname(abbreviation):
    if abbreviation == "BAU":
        return "Baunach Young Pikes"
    elif abbreviation == "HH":
        return "Hamburg Towers"
    elif abbreviation == "HAN":
        return "HEBEISEN WHITE WINGS Hanau"
    elif abbreviation == "HD":
        return "MLP Academics Heidelberg"
    elif abbreviation == "CH":
        return "NINERS Chemnitz"
    elif abbreviation == "NÜR":
        return "Nuernberg Falcons BC"
    elif abbreviation == "HAG":
        return "Phoenix Hagen"
    elif abbreviation == "PSK":
        return "PS Karlsruhe LIONS"
    elif abbreviation == "TRI":
        return "ROEMERSTROM Gladiators Trier"
    elif abbreviation == "EHI":
        return "TEAM EHINGEN URSPRING"
    elif abbreviation == "PB":
        return "Uni Baskets Paderborn"
    elif abbreviation == "KIR":
        return "VfL Kirchheim Knights"
    elif abbreviation == "ART":
        return "Artland Dragons"
    elif abbreviation == "TUB":
        return "Tigers Tuebingen"
    elif abbreviation == "S04":
        return "FC Schalke 04 Basketball"
    elif abbreviation == "HRO":
        return "ROSTOCK SEAWOLVES"
    else:
        return abbreviation

mode = args.get('mode', None)

#Rohdaten
now = datetime.datetime.now()
base_url_1 = "https://www.airtango.live/core/v1/basketball/channels/30/playlists/"
base_url_2 = "/contents?needTotalCount=true"
base_url_main = "https://www.2basketballbundesliga.de"

if mode is None:
    foldername = "Heute live"
    url = build_url({'mode': 'foldertoday', 'foldername': foldername})
    li = xbmcgui.ListItem(foldername, iconImage='DefaultFolder.png')
    xbmcplugin.addDirectoryItem(handle=addon_handle, url=url, listitem=li, isFolder=True)
    j = 3
    while j < 200:
        if j == 3:
            foldername = "Baunach Young Pikes"
        elif j == 8:
            foldername = "Hamburg Towers"
        elif j == 10:
            foldername = "HEBEISEN WHITE WINGS Hanau"
        elif j == 12:
            foldername = "MLP Academics Heidelberg"
        elif j == 14:
            foldername = "NINERS Chemnitz"
        elif j == 16:
            foldername = "Nuernberg Falcons BC"
        elif j == 20:
            foldername = "Phoenix Hagen"
        elif j == 22:
            foldername = "PS Karlsruhe LIONS"
        elif j == 28:
            foldername = "ROEMERSTROM Gladiators Trier"
        elif j == 30:
            foldername = "TEAM EHINGEN URSPRING"
        elif j == 34:
            foldername = "Uni Baskets Paderborn"
        elif j == 36:
            foldername = "VfL Kirchheim Knights"
        elif j == 86:
            foldername = "Artland Dragons"
        elif j == 101:
            foldername = "Tigers Tuebingen"
        elif j == 114:
            foldername = "FC Schalke 04 Basketball"
        elif j == 138:
            foldername = "ROSTOCK SEAWOLVES"
        else:
            foldername = j

        url = build_url({'mode': 'folder1', 'foldername': foldername, 'webnummer': j})
        li = xbmcgui.ListItem(foldername, iconImage='DefaultFolder.png')
        xbmcplugin.addDirectoryItem(handle=addon_handle, url=url, listitem=li, isFolder=True)

#        i = 0
#        while i < 1:
#        #len(jsonResult):
#            print(i)
#            try:
#                #if len(jsonResult[i]['expectedAt']) > 9:
#                if str(now)[:10] == jsonResult[i]['expectedAt'][:10]:
#                    foldername = jsonResult[i]['name']
#                    url = jsonResult[i]['contentURL']
#                    li = xbmcgui.ListItem(foldername, iconImage='DefaultFolder.png')
#                    xbmcplugin.addDirectoryItem(handle=addon_handle, url=url,
#                            listitem=li)
#                    i = len(jsonResult)
#            except:
#                fehler = "fehler"
#            i =+ 1
#        j =+ 1
        if j == 3:
            j = 8
        elif j == 8:
            j = 10
        elif j == 10:
            j = 12
        elif j == 12:
            j = 14
        elif j == 14:
            j = 16
        elif j == 16:
            j = 20
        elif j == 20:
            j = 22
        elif j == 22:
            j = 28
        elif j == 28:
            j = 30
        elif j == 30:
            j = 34
        elif j == 34:
            j = 36
        elif j == 36:
            j = 86
        elif j == 86:
            j = 101
        elif j == 101:
            j = 114
        elif j == 114:
            j = 138
        elif j == 138:
            j = 200
    xbmcplugin.endOfDirectory(addon_handle)

elif mode[0] == 'folder1':
    j2 = args['webnummer'][0]
#    print("hierhierhier: "+j2)
    base_url_0 = base_url_1 + str(j2) + base_url_2
    response = urllib.urlopen(base_url_0).read()
    jsonResult = json.loads(response)
    i = 0
    while i < len(jsonResult):
        #try:
            #if len(jsonResult[i]['expectedAt']) > 9:
            #if str(now)[:10] == jsonResult[i]['expectedAt'][:10]:
        name = jsonResult[i]['subtitle'] + ": " + jsonResult[i]['name']
        url = jsonResult[i]['contentURL']
        image = jsonResult[i]['teaser']['default']
        li = xbmcgui.ListItem(name, iconImage=image)
        xbmcplugin.addDirectoryItem(handle=addon_handle, url=url,
                listitem=li)
        #except:
        #    fehler = "fehler"
        i = i + 1
    xbmcplugin.endOfDirectory(addon_handle)

    #listitem = xbmcgui.ListItem(path=url)
    #listitem.setProperty('inputstreamaddon', 'inputstream.adaptive')
    #listitem.setProperty('inputstream.adaptive.manifest_type', 'hls')
    #xbmcplugin.setResolvedUrl(_addon_handler, True, listitem)

elif mode[0] == 'foldertoday':
    page = requests.get(base_url_main)
    soup = BeautifulSoup(page.content, 'html.parser')
    result_0 = soup.findAll("div", {"class": "dc-table"})
    lines = []
    counter = 0
    for ul in result_0:
        lines.extend(ul.findAll("div", {"class": "dc-cell"}))
        #print("asdfasgasdg")
        counter = counter + 1
    i = 0
    #print("hierasdf"+lines[0])
    while i < len(lines):
        if (str(lines[i])[str(lines[i]).find('>')+1:str(lines[i]).find('</')]) == "Heute":
            i = i + 1
            #Zeit
            time = str(lines[i])[str(lines[i]).find('>')+1:str(lines[i]).find('</')]
            i = i + 1
            j = 0
            name = str(lines[i])[str(lines[i]).find('<b>')+3:str(lines[i]).find('</b>')]
            if name == "BAU":
                j = 3
            elif name == "HH":
                j = 8
            elif name == "HAN":
                j = 10
            elif name == "HD":
                j = 12
            elif name == "CH":
                j = 14
            elif name == "NÜR":
                j == 16
            elif name == "HAG":
                j = 20
            elif name == "PSK":
                j = 22
            elif name == "TRI":
                j = 28
            elif name == "EHI":
                j = 30
            elif name == "PB":
                j = 34
            elif name == "KIR":
                j = 36
            elif name == "ART":
                j = 86
            elif name == "TUB":
                j = 101
            elif name == "S04":
                j = 114
            elif name == "HRO":
                j = 138
            else:
                j = 0
            i = i + 2
            name = time+" Uhr: "+getfullteamname(name)+" - "+getfullteamname(str(lines[i])[str(lines[i]).find('<b>')+3:str(lines[i]).find('</b>')])
            i = i + 2
            #print("hierhierhier: " + str(j))

            base_url_0 = base_url_1 + str(j) + base_url_2
            response = urllib.urlopen(base_url_0).read()
            jsonResult = json.loads(response)
            #i2 = Spieltag

            #print("hierhierhier "+str(now)[8:10]+"."+str(now)[5:7]+"."+str(now)[0:4])
            i2 = 0
            i3 = 0
            while i3 < len(jsonResult):
                if str(jsonResult[i2]['subtitle'])[:10] == str(now)[8:10]+"."+str(now)[5:7]+"."+str(now)[0:4]:
                    i2 = i3
                    i3 = len(jsonResult)
                i3 = i3 + 1

            #name = name+" ("+str(i2+1)+". Spieltag)"

            url = jsonResult[i2]['contentURL']
            image = jsonResult[i2]['teaser']['default']
            li = xbmcgui.ListItem(name, iconImage=image)
            xbmcplugin.addDirectoryItem(handle=addon_handle, url=url,
                    listitem=li)

        else:
            i = i + 6
    xbmcplugin.endOfDirectory(addon_handle)
