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

import requests

reload(sys)
sys.setdefaultencoding('utf8')

base_url = sys.argv[0]
addon_handle = int(sys.argv[1])
args = urlparse.parse_qs(sys.argv[2][1:])
#xbmcplugin.setContent(addon_handle, 'movies')

_addon_id      = 'plugin.video.airtango'
_addon         = xbmcaddon.Addon(id=_addon_id)
_addon_name    = _addon.getAddonInfo('name')
_addon_handler = int(sys.argv[1])
_addon_url     = sys.argv[0]
_addon_path    = xbmc.translatePath(_addon.getAddonInfo("path") )

def build_url(query):
    return base_url + '?' + urllib.urlencode(query)

def createOrdner(mode, foldername, pressekonferenzID, reliveID, highlightsID):
    url = build_url(
        {'mode': mode, 'foldername': foldername, 'pressekonferenzID': pressekonferenzID,
         'reliveID': reliveID, 'highlightsID': highlightsID})
    li = xbmcgui.ListItem(foldername, iconImage='DefaultFolder.png')
    xbmcplugin.addDirectoryItem(handle=addon_handle, url=url, listitem=li, isFolder=True)

mode = args.get('mode', None)

#Rohdaten
now = datetime.datetime.now()
base_url_1 = "https://www.airtango.live/api/content-box/?baseconfig=40&module=2551&live=true&exclude=76925"
#Aufbaue Relive/Highlights/Pressekonferenz: base_url_2a + id + base_url_2b
base_url_2a = "https://www.airtango.live/api/module/"
base_url_2b = "/content"
base_url_3 = "https://www.airtango.live/api/content-box/?baseconfig=40&module=3561&live=true"
base_url_4 = "https://www.airtango.live/api/content-box/?baseconfig=40&module=3561&live=false"
#base_url_main = "https://www.2basketballbundesliga.de"
stream_url_1 = "https://www.airtango.live/api/v2/content/"
stream_url_2 = "/access"
useragent = {'User-Agent': 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3'}
if mode is None:
    foldername = "Nächste Liveevents (alle)"
    url = build_url({'mode': '2BasketballBundesligaAuswahlApi', 'foldername': foldername})
    li = xbmcgui.ListItem(foldername, iconImage='DefaultFolder.png')
    xbmcplugin.addDirectoryItem(handle=addon_handle, url=url, listitem=li, isFolder=True)

    foldername = "Nächste Liveevents (nur 2. Basketball Bundesliga)"
    url = build_url({'mode': '2BasketballBundesligaAuswahlApi', 'foldername': foldername})
    li = xbmcgui.ListItem(foldername, iconImage='DefaultFolder.png')
    xbmcplugin.addDirectoryItem(handle=addon_handle, url=url, listitem=li, isFolder=True)

    foldername = "2. Basketball Bundesliga Archiv"
    url = build_url({'mode': '2BasketballBundesliga', 'foldername': foldername})
    li = xbmcgui.ListItem(foldername, iconImage='DefaultFolder.png')
    xbmcplugin.addDirectoryItem(handle=addon_handle, url=url, listitem=li, isFolder=True)

    xbmcplugin.endOfDirectory(addon_handle)

elif mode[0] == '2BasketballBundesliga':
    foldername = "Neueste Uploads"
    url = build_url({'mode': '2BasketballBundesligaAuswahlApi', 'foldername': foldername, 'apiID': '3561'})
    li = xbmcgui.ListItem(foldername, iconImage='DefaultFolder.png')
    xbmcplugin.addDirectoryItem(handle=addon_handle, url=url, listitem=li, isFolder=True)

    #PS Karlsruhe LIONS
    createOrdner('2BasketballBundesligaAuswahl', 'PS Karlsruhe LIONS', '4598', '4597', '4594')

    #Artland Dragons
    createOrdner('2BasketballBundesligaAuswahl', 'Artland Dragons', '4493', '4438', '4433')

    #ROSTOCK SEAWOLVES
    createOrdner('2BasketballBundesligaAuswahl', 'ROSTOCK SEAWOLVES', '4500', '4504', '4505')

    #Bayer Giants Leverkusen
    createOrdner('2BasketballBundesligaAuswahl', 'Bayer Giants Leverkusen', '4448', '4446', '4445')

    #RÖMERTROM Gladiators Trier
    createOrdner('2BasketballBundesligaAuswahl', 'RÖMERSTROM Gladiators Trier', '4515', '4513', '4510')

    #Eisbären Bremerhaven
    createOrdner('2BasketballBundesligaAuswahl', 'Eisbären Bremerhaven', '4463', '4461', '4459')

    #Science City Jena
    createOrdner('2BasketballBundesligaAuswahl', 'Science City Jena', '4522', '4519', '4518')

    #FC Schalke 04 Basketball
    createOrdner('2BasketballBundesligaAuswahl', 'FC Schalke 04 Basketball', '4475', '4473', '4472')

    #TEAM EHINGEN URSPRING
    createOrdner('2BasketballBundesligaAuswahl', 'TEAM EHINGEN URSPRING', '4530', '4528', '4525')

    #MLP Academics Heidelberg
    createOrdner('2BasketballBundesligaAuswahl', 'MLP Academics Heidelberg', '4483', '4481', '4478')

    #Tigers Tübingen
    createOrdner('2BasketballBundesligaAuswahl', 'Tigers Tübingen', '4539', '4537', '4534')

    #Niners Chemnitz
    createOrdner('2BasketballBundesligaAuswahl', 'Niners Chemnitz', '3661', '3659', '3658')

    #Uni Baskets Paderborn
    createOrdner('2BasketballBundesligaAuswahl', 'Uni Baskets Paderborn', '4548', '4546', '4543')

    #Nürnberg Falcons BC
    createOrdner('2BasketballBundesligaAuswahl', 'Nürnberg Falcons BC', '4492', '4491', '4489')

    #VFL Kirchheim Knights
    createOrdner('2BasketballBundesligaAuswahl', 'VFL Kirchheim Knights', '4556', '4555', '4553')

    #Phoenix Hagen
    createOrdner('2BasketballBundesligaAuswahl', 'Phoenix Hagen', '4500', '4499', '4496')

    #wiha Panthers Schwennigen
    createOrdner('2BasketballBundesligaAuswahl', 'wiha Panthers Schwennigen', '4565', '4562', '4559')

    xbmcplugin.endOfDirectory(addon_handle)

elif mode[0] == '2BasketballBundesligaAuswahl':
    foldername = args['foldername'][0]+"-Archiv:"
    li = xbmcgui.ListItem(foldername, iconImage='DefaultFolder.png')
    xbmcplugin.addDirectoryItem(handle=addon_handle, url='', listitem=li)

    foldername = "Relive"
    url = build_url({'mode': '2BasketballBundesligaAuswahlApi', 'foldername': foldername, 'apiID':args['reliveID'][0] })
    li = xbmcgui.ListItem(foldername, iconImage='DefaultFolder.png')
    xbmcplugin.addDirectoryItem(handle=addon_handle, url=url, listitem=li, isFolder=True)

    foldername = "Highlights"
    url = build_url({'mode': '2BasketballBundesligaAuswahlApi', 'foldername': foldername, 'apiID':args['highlightsID'][0] })
    li = xbmcgui.ListItem(foldername, iconImage='DefaultFolder.png')
    xbmcplugin.addDirectoryItem(handle=addon_handle, url=url, listitem=li, isFolder=True)

    foldername = "Pressekonferenz"
    url = build_url({'mode': '2BasketballBundesligaAuswahlApi', 'foldername': foldername, 'apiID':args['pressekonferenzID'][0] })
    li = xbmcgui.ListItem(foldername, iconImage='DefaultFolder.png')
    xbmcplugin.addDirectoryItem(handle=addon_handle, url=url, listitem=li, isFolder=True)

    xbmcplugin.endOfDirectory(addon_handle)

elif mode[0] == '2BasketballBundesligaAuswahlApi':
    j = 0
    # Aufbaue Relive/Highlights/Pressekonferenz: base_url_2a + id + base_url_2b
    if args['foldername'][0] == 'Nächste Liveevents (alle)':
        response = urllib.urlopen(base_url_1).read()
    elif args['foldername'][0] == 'Nächste Liveevents (nur 2. Basketball Bundesliga)':
        response = urllib.urlopen(base_url_3).read()
    elif args['foldername'][0] == 'Neueste Uploads':
        response = urllib.urlopen(base_url_4).read()
    else:
        base_url_2a = "https://www.airtango.live/api/module/"
        base_url_2b = "/content"
        base_url_2komplett = base_url_2a+args['apiID'][0]+base_url_2b
        response = urllib.urlopen(base_url_2komplett).read()

    jsonResult = json.loads(response)

    while j < len(jsonResult['data']):
        gameID = jsonResult['data'][j]['id']
        startzeit = jsonResult['data'][j]['start_datetime']['date']
        description = jsonResult['data'][j]['fields']['Title'][0]['description']
        # xbmc.log(startzeit[:16])
        foldername = startzeit[:16] + ": " + jsonResult['data'][j]['fields']['Title'][0]['title']
        url = build_url({'mode': 'playGame', 'foldername': foldername, 'gameID': gameID})
        li = xbmcgui.ListItem(foldername, iconImage='DefaultFolder.png')
        li.setProperty('IsPlayable', 'true')
        li.setInfo('video', {'plot': description})
        xbmcplugin.addDirectoryItem(handle=addon_handle, url=url, listitem=li)
        j = j + 1
    xbmcplugin.endOfDirectory(addon_handle)

elif mode[0] == 'playGame':
#    xbmc.log("hiaerad: "+args['gameID'][0])
    stream_url_0 = stream_url_1 + args['gameID'][0]+stream_url_2
    xbmc.log("URL: "+stream_url_0)
    streamURL_response = requests.post(url=stream_url_0, headers = useragent)
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
