# -*- coding: utf-8 -*-

'''
    nightwing Add-on

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <http://www.gnu.org/licenses/>.
'''


import sys
from six.moves import urllib_parse
import xbmcgui

params = dict(urllib_parse.parse_qsl(sys.argv[2].replace('?','')))

action = params.get('action')

name = params.get('name')

title = params.get('title')

year = params.get('year')

imdb = params.get('imdb')

tvdb = params.get('tvdb')

tmdb = params.get('tmdb')

season = params.get('season')

episode = params.get('episode')

tvshowtitle = params.get('tvshowtitle')

premiered = params.get('premiered')

url = params.get('url')

image = params.get('image')

meta = params.get('meta')

select = params.get('select')

query = params.get('query')

source = params.get('source')

content = params.get('content')

windowedtrailer = params.get('windowedtrailer')
windowedtrailer = int(windowedtrailer) if windowedtrailer in ("0","1") else 0


if action == None:
    from resources.lib.indexers import navigator
    from resources.lib.modules import cache
    from resources.lib.modules import control
    cache.cache_version_check()
    if control.setting('startup.sync.trakt.status') == 'true':
        from resources.lib.modules import trakt
        trakt.syncTraktStatus()
    navigator.navigator().root()

elif action == "furkNavigator":
    from resources.lib.indexers import navigator
    navigator.navigator().furk()
    


elif action == "docsNavigator":
    from resources.lib.indexers import navigator
    navigator.navigator().docs()
    
elif action == "kidsNavigator":
    from resources.lib.indexers import navigator
    navigator.navigator().kids()
    
elif action == "fitnessNavigator":
    from resources.lib.indexers import navigator
    navigator.navigator().fitness()
    
    
elif action == "channelsNavigator":
    from resources.lib.indexers import navigator
    navigator.navigator().channels()




elif action == "furkMetaSearch":
    from resources.lib.indexers import furk
    furk.furk().furk_meta_search(url)

elif action == "furkSearch":
    from resources.lib.indexers import furk
    furk.furk().search()

elif action == "furkUserFiles":
    from resources.lib.indexers import furk
    furk.furk().user_files()

elif action == "furkSearchNew":
    from resources.lib.indexers import furk
    furk.furk().search_new()

elif action == 'movieNavigator':
    from resources.lib.indexers import navigator
    navigator.navigator().movies()

elif action == 'movieliteNavigator':
    from resources.lib.indexers import navigator
    navigator.navigator().movies(lite=True)

elif action == 'mymovieNavigator':
    from resources.lib.indexers import navigator
    navigator.navigator().mymovies()

elif action == 'mymovieliteNavigator':
    from resources.lib.indexers import navigator
    navigator.navigator().mymovies(lite=True)

elif action == 'tvNavigator':
    from resources.lib.indexers import navigator
    navigator.navigator().tvshows()

elif action == 'tvliteNavigator':
    from resources.lib.indexers import navigator
    navigator.navigator().tvshows(lite=True)

elif action == 'mytvNavigator':
    from resources.lib.indexers import navigator
    navigator.navigator().mytvshows()

elif action == 'mytvliteNavigator':
    from resources.lib.indexers import navigator
    navigator.navigator().mytvshows(lite=True)

elif action == 'customNavigator':
    from resources.lib.indexers import navigator
    navigator.navigator().custom()

elif action == 'customliteNavigator':
    from resources.lib.indexers import navigator
    navigator.navigator().custom(lite=True)

elif action == 'imdbLists':
    from resources.lib.indexers import navigator
    navigator.navigator().imdbLists()

elif action == 'movieMosts':
    from resources.lib.indexers import navigator
    navigator.navigator().movieMosts()

elif action == 'showMosts':
    from resources.lib.indexers import navigator
    navigator.navigator().showMosts()

elif action == 'downloadNavigator':
    from resources.lib.indexers import navigator
    navigator.navigator().downloads()

elif action == 'libraryNavigator':
    from resources.lib.indexers import navigator
    navigator.navigator().library()

elif action == 'toolNavigator':
    from resources.lib.indexers import navigator
    navigator.navigator().tools()

elif action == 'searchNavigator':
    from resources.lib.indexers import navigator
    navigator.navigator().search()

elif action == 'viewsNavigator':
    from resources.lib.indexers import navigator
    navigator.navigator().views()

elif action == 'clearCache':
    from resources.lib.indexers import navigator
    navigator.navigator().clearCache()

elif action == 'clearCacheProviders':
    from resources.lib.indexers import navigator
    navigator.navigator().clearCacheProviders()

elif action == 'clearDebridCheck':
    from resources.lib.indexers import navigator
    navigator.navigator().clearDebridCheck()

elif action == 'clearCacheSearch':
    from resources.lib.indexers import navigator
    navigator.navigator().clearCacheSearch()

elif action == 'clearAllCache':
    from resources.lib.indexers import navigator
    navigator.navigator().clearCacheAll()

elif action == 'infoCheck':
    from resources.lib.indexers import navigator
    navigator.navigator().infoCheck('')

elif action == 'movies':
    from resources.lib.indexers import movies
    movies.movies().get(url)

elif action == 'moviePage':
    from resources.lib.indexers import movies
    movies.movies().get(url)

elif action == 'movieWidget':
    from resources.lib.indexers import movies
    movies.movies().widget()

elif action == 'movieSearch':
    from resources.lib.indexers import movies
    movies.movies().search()

elif action == 'movieSearchnew':
    from resources.lib.indexers import movies
    movies.movies().search_new()

elif action == 'movieSearchterm':
    from resources.lib.indexers import movies
    movies.movies().search_term(name)

elif action == 'moviePerson':
    from resources.lib.indexers import movies
    movies.movies().person()

elif action == 'movieGenres':
    from resources.lib.indexers import movies
    movies.movies().genres()

elif action == 'movieLanguages':
    from resources.lib.indexers import movies
    movies.movies().languages()

elif action == 'movieCertificates':
    from resources.lib.indexers import movies
    movies.movies().certifications()

elif action == 'movieYears':
    from resources.lib.indexers import movies
    movies.movies().years()

elif action == 'movieDecades':
    from resources.lib.indexers import movies
    movies.movies().decades()

elif action == 'moviePersons':
    from resources.lib.indexers import movies
    movies.movies().persons(url)

elif action == 'movieUserlists':
    from resources.lib.indexers import movies
    movies.movies().userlists()

elif action == 'channels':
    from resources.lib.indexers import channels
    channels.channels().get()

elif action == 'tvshows':
    from resources.lib.indexers import tvshows
    tvshows.tvshows().get(url)

elif action == 'tvshowPage':
    from resources.lib.indexers import tvshows
    tvshows.tvshows().get(url)

elif action == 'tvSearch':
    from resources.lib.indexers import tvshows
    tvshows.tvshows().search()

elif action == 'tvSearchnew':
    from resources.lib.indexers import tvshows
    tvshows.tvshows().search_new()

elif action == 'tvSearchterm':
    from resources.lib.indexers import tvshows
    tvshows.tvshows().search_term(name)
    
elif action == 'tvPerson':
    from resources.lib.indexers import tvshows
    tvshows.tvshows().person()

elif action == 'tvGenres':
    from resources.lib.indexers import tvshows
    tvshows.tvshows().genres()

elif action == 'tvNetworks':
    from resources.lib.indexers import tvshows
    tvshows.tvshows().networks()

elif action == 'kidsNetworks':
    from resources.lib.indexers import tvshows
    tvshows.tvshows().kidsnetworks()

elif action == 'tvLanguages':
    from resources.lib.indexers import tvshows
    tvshows.tvshows().languages()

elif action == 'tvCertificates':
    from resources.lib.indexers import tvshows
    tvshows.tvshows().certifications()

elif action == 'tvPersons':
    from resources.lib.indexers import tvshows
    tvshows.tvshows().persons(url)

elif action == 'tvUserlists':
    from resources.lib.indexers import tvshows
    tvshows.tvshows().userlists()

elif action == 'seasons':
    from resources.lib.indexers import episodes
    episodes.seasons().get(tvshowtitle, year, imdb, tvdb)

elif action == 'episodes':
    from resources.lib.indexers import episodes
    episodes.episodes().get(tvshowtitle, year, imdb, tvdb, season, episode)

elif action == 'calendar':
    from resources.lib.indexers import episodes
    episodes.episodes().calendar(url)

elif action == 'tvWidget':
    from resources.lib.indexers import episodes
    episodes.episodes().widget()

elif action == 'calendars':
    from resources.lib.indexers import episodes
    episodes.episodes().calendars()

elif action == 'episodeUserlists':
    from resources.lib.indexers import episodes
    episodes.episodes().userlists()

elif action == 'refresh':
    from resources.lib.modules import control
    control.refresh()

elif action == 'queueItem':
    from resources.lib.modules import control
    control.queueItem()

elif action == 'openSettings':
    from resources.lib.modules import control
    control.openSettings(query)

elif action == 'artwork':
    from resources.lib.modules import control
    control.artwork()

elif action == 'addView':
    from resources.lib.modules import views
    views.addView(content)

elif action == 'moviePlaycount':
    from resources.lib.modules import playcount
    playcount.movies(imdb, query)

elif action == 'episodePlaycount':
    from resources.lib.modules import playcount
    playcount.episodes(imdb, tvdb, season, episode, query)

elif action == 'tvPlaycount':
    from resources.lib.modules import playcount
    playcount.tvshows(name, imdb, tvdb, season, query)

elif action == 'trailer':
    from resources.lib.modules import trailer
    trailer.trailer().play(name, url, windowedtrailer)

elif action == 'traktManager':
    from resources.lib.modules import trakt
    trakt.manager(name, imdb, tvdb, content)

elif action == 'authTrakt':
    from resources.lib.modules import trakt
    trakt.authTrakt()

elif action == 'smuSettings':
    try: import resolveurl
    except: pass
    resolveurl.display_settings()

elif action == 'nightwingscrapersettings':
    from resources.lib.modules import control
    control.openSettings('0.0', 'script.module.nightwingscrapers')

elif action == 'installNightwingScrapers':
    from resources.lib.modules import control
    control.installAddon('script.module.nightwingscrapers')
    control.sleep(200)
    control.refresh()

elif action == 'download':
    import simplejson as json
    from resources.lib.modules import sources
    from resources.lib.modules import downloader
    try: downloader.download(name, image, sources.sources().sourcesResolve(json.loads(source)[0], True))
    except: pass


elif action == 'play':
    from resources.lib.indexers import playlists
    if not content == None:
        playlists.player().play(url, content)
    else:
        from resources.lib.modules import sources
        sources.sources().play(title, year, imdb, tvdb, season, episode, tvshowtitle, premiered, meta, select)

elif action == 'addItem':
    from resources.lib.modules import sources
    sources.sources().addItem(title)

elif action == 'playItem':
    from resources.lib.modules import sources
    sources.sources().playItem(title, source)

elif action == 'alterSources':
    from resources.lib.modules import sources
    sources.sources().alterSources(url, meta)

elif action == 'clearSources':
    from resources.lib.modules import sources
    sources.sources().clearSources()

elif action == 'random':
    rtype = params.get('rtype')
    if rtype == 'movie':
        from resources.lib.indexers import movies
        rlist = movies.movies().get(url, create_directory=False)
        r = sys.argv[0]+"?action=play"
    elif rtype == 'episode':
        from resources.lib.indexers import episodes
        rlist = episodes.episodes().get(tvshowtitle, year, imdb, tvdb, season, create_directory=False)
        r = sys.argv[0]+"?action=play"
    elif rtype == 'season':
        from resources.lib.indexers import episodes
        rlist = episodes.seasons().get(tvshowtitle, year, imdb, tvdb, create_directory=False)
        r = sys.argv[0]+"?action=random&rtype=episode"
    elif rtype == 'show':
        from resources.lib.indexers import tvshows
        rlist = tvshows.tvshows().get(url, create_directory=False)
        r = sys.argv[0]+"?action=random&rtype=season"
    from random import randint
    import simplejson as json
    try:
        from resources.lib.modules import control
        rand = randint(1,len(rlist))-1
        for p in ['title','year','imdb','tvdb','season','episode','tvshowtitle','premiered','select']:
            if rtype == "show" and p == "tvshowtitle":
                try: r += '&'+p+'='+urllib_parse.quote_plus(rlist[rand]['originaltitle'])
                except: pass
            else:
                if rtype == "movie":
                    rlist[rand]['title'] = rlist[rand]['originaltitle']
                elif rtype == "episode":
                    rlist[rand]['tvshowtitle'] = urllib_parse.unquote_plus(rlist[rand]['tvshowtitle'])
                try: r += '&'+p+'='+urllib_parse.quote_plus(rlist[rand][p])
                except: pass
        try: r += '&meta='+urllib_parse.quote_plus(json.dumps(rlist[rand]))
        except: r += '&meta={}'
        if rtype == "movie":
            try: control.infoDialog('%s (%s)' % (rlist[rand]['title'], rlist[rand]['year']), control.lang(32536), time=20000)
            except: pass
        elif rtype == "episode":
            try: control.infoDialog('%s - %01dx%02d . %s' % (urllib_parse.unquote_plus(rlist[rand]['tvshowtitle']), int(rlist[rand]['season']), int(rlist[rand]['episode']), rlist[rand]['title']), control.lang(32536), time=20000)
            except: pass
        control.execute('RunPlugin(%s)' % r)
    except:
        from resources.lib.modules import control
        control.infoDialog(control.lang(32537), time=8000)

elif action == 'movieToLibrary':
    from resources.lib.modules import libtools
    libtools.libmovies().add(name, title, year, imdb, tmdb)

elif action == 'moviesToLibrary':
    from resources.lib.modules import libtools
    libtools.libmovies().range(url)

elif action == 'moviesToLibrarySilent':
    from resources.lib.modules import libtools
    libtools.libmovies().silent(url)

elif action == 'tvshowToLibrary':
    from resources.lib.modules import libtools
    libtools.libtvshows().add(tvshowtitle, year, imdb, tvdb)

elif action == 'tvshowsToLibrary':
    from resources.lib.modules import libtools
    libtools.libtvshows().range(url)

elif action == 'tvshowsToLibrarySilent':
    from resources.lib.modules import libtools
    libtools.libtvshows().silent(url)

elif action == 'updateLibrary':
    from resources.lib.modules import libtools
    libtools.libepisodes().update(query)

elif action == 'service':
    from resources.lib.modules import libtools
    libtools.libepisodes().service()

elif action == 'syncTraktStatus':
    from resources.lib.modules import trakt
    trakt.syncTraktStatus()

elif action == 'changelog':
    from resources.lib.modules import changelog
    changelog.get()	

elif action == 'cleanSettings':
    from resources.lib.modules import control
    control.clean_settings()
##############################################################################################

elif action == 'xmlsNavigator':
    from resources.lib.indexers import navigator
    navigator.navigator().xmls()
    
elif action == 'wolfNavigator':
    from resources.lib.indexers import navigator
    navigator.navigator().wolf()

elif action == 'magNavigator':
    from resources.lib.indexers import navigator
    navigator.navigator().playlists()
    
elif action == 'extinfo':
    from resources.lib.indexers import playlists
    playlists.indexer().rootextinfo()
    
elif action == 'lists1':
    from resources.lib.indexers import playlists
    playlists.indexer().rootlists1()
    
elif action == 'kids1':
    xbmc.executebuiltin('PlayMedia(https://494e639cacb24ad484819d7154a3f100.mediatailor.us-east-1.amazonaws.com/v1/master/04fd913bb278d8775298c26fdca9d9841f37601f/Plex_KidsPangTV/playlist.m3u8?ads.wurl_channel=841&ads.wurl_name=KidsPangTV&ads.coppa=1&ads.us_privacy=1---&ads.psid=62274240-07e7-5d94-8dc8-ef68cf19e175&ads.targetopt=0&ads.plex_token=24Q6qvbp3Nc5vrD_13WN&ads.plex_id=60d4eddfb2fdec002c141139&ads.ua=okhttp%2F4.9.0&ads.app_bundle=com.plexapp.android&ads.app_store_url=https%3A%2F%2Fplay.google.com%2Fstore%2Fapps%2Fdetails%3Fid%3Dcom.plexapp.android&ads.gdpr=0&ads.consent=0&ads.device_type=handset&ads.device_id_type=)')
    xbmc.executebuiltin('PlayerControl(repeatall)')
    xbmc.executebuiltin('PlayerControl(RandomOn)')
    
elif action == 'horror1':
    xbmc.executebuiltin('PlayMedia(https://service-stitcher-ipv4.clusters.pluto.tv/stitch/hls/channel/569546031a619b8f07ce6e25/master.m3u8?advertisingId=&appName=web&appVersion=5.2.2-d60060c7283e0978cc63ba036956b5c1657f8eba&architecture=&buildVersion=&clientTime=&deviceDNT=0&deviceId=ab2ddaa3-1108-4e91-9826-d7295603d915&deviceLat=33.6647&deviceLon=-117.1743&deviceMake=Chrome&deviceModel=Chrome&deviceType=web&deviceVersion=80.0.3987.149&includeExtendedEvents=false&marketingRegion=US&sid=2c6d09b0-1e23-11ec-bbb6-dca632884a02&userId=)')
    xbmc.executebuiltin('PlayerControl(repeatall)')
    xbmc.executebuiltin('PlayerControl(RandomOn)')
    
elif action == 'docs1':
    xbmc.executebuiltin('PlayMedia(https://service-stitcher-ipv4.clusters.pluto.tv/stitch/hls/channel/5b85a7582921777994caea63/master.m3u8?advertisingId=&appName=web&appVersion=5.2.2-d60060c7283e0978cc63ba036956b5c1657f8eba&architecture=&buildVersion=&clientTime=&deviceDNT=0&deviceId=ab2ddaa3-1108-4e91-9826-d7295603d915&deviceLat=33.6647&deviceLon=-117.1743&deviceMake=Chrome&deviceModel=Chrome&deviceType=web&deviceVersion=80.0.3987.149&includeExtendedEvents=false&marketingRegion=US&sid=2c6d09b0-1e23-11ec-bbb6-dca632884a02&userId=)')
    xbmc.executebuiltin('PlayerControl(repeatall)')
    xbmc.executebuiltin('PlayerControl(RandomOn)')
    
elif action == 'random1':
    xbmc.executebuiltin('PlayMedia(https://repo.encrypticmh.appboxes.co/xml/mov1.m3u)')
    xbmc.executebuiltin('PlayerControl(repeatall)')
    xbmc.executebuiltin('PlayerControl(RandomOn)')

elif action == 'fantastic1':
    xbmc.executebuiltin('PlayMedia(https://service-stitcher-ipv4.clusters.pluto.tv/stitch/hls/channel/5b64a245a202b3337f09e51d/master.m3u8?advertisingId=&appName=web&appVersion=5.2.2-d60060c7283e0978cc63ba036956b5c1657f8eba&architecture=&buildVersion=&clientTime=&deviceDNT=0&deviceId=ab2ddaa3-1108-4e91-9826-d7295603d915&deviceLat=33.6647&deviceLon=-117.1743&deviceMake=Chrome&deviceModel=Chrome&deviceType=web&deviceVersion=80.0.3987.149&includeExtendedEvents=false&marketingRegion=US&sid=2c6d09b0-1e23-11ec-bbb6-dca632884a02&userId=)')
    xbmc.executebuiltin('PlayerControl(repeatall)')
    xbmc.executebuiltin('PlayerControl(RandomOn)')
    


    
elif action == 'action1':
    xbmc.executebuiltin('PlayMedia(https://service-stitcher-ipv4.clusters.pluto.tv/stitch/hls/channel/561d7d484dc7c8770484914a/master.m3u8?advertisingId=&appName=web&appVersion=5.2.2-d60060c7283e0978cc63ba036956b5c1657f8eba&architecture=&buildVersion=&clientTime=&deviceDNT=0&deviceId=ab2ddaa3-1108-4e91-9826-d7295603d915&deviceLat=33.6647&deviceLon=-117.1743&deviceMake=Chrome&deviceModel=Chrome&deviceType=web&deviceVersion=80.0.3987.149&includeExtendedEvents=false&marketingRegion=US&sid=2c6d09b0-1e23-11ec-bbb6-dca632884a02&userId=)')
    xbmc.executebuiltin('PlayerControl(repeatall)')
    xbmc.executebuiltin('PlayerControl(RandomOn)')
    
elif action == 'comedy1':
    xbmc.executebuiltin('PlayMedia(https://service-stitcher-ipv4.clusters.pluto.tv/stitch/hls/channel/5a4d3a00ad95e4718ae8d8db/master.m3u8?advertisingId=&appName=web&appVersion=5.2.2-d60060c7283e0978cc63ba036956b5c1657f8eba&architecture=&buildVersion=&clientTime=&deviceDNT=0&deviceId=ab2ddaa3-1108-4e91-9826-d7295603d915&deviceLat=33.6647&deviceLon=-117.1743&deviceMake=Chrome&deviceModel=Chrome&deviceType=web&deviceVersion=80.0.3987.149&includeExtendedEvents=false&marketingRegion=US&sid=2c6d09b0-1e23-11ec-bbb6-dca632884a02&userId=)')
    xbmc.executebuiltin('PlayerControl(repeatall)')
    xbmc.executebuiltin('PlayerControl(RandomOn)')
    
elif action == 'drama1':
    xbmc.executebuiltin('PlayMedia(https://service-stitcher-ipv4.clusters.pluto.tv/stitch/hls/channel/5b4e92e4694c027be6ecece1/master.m3u8?advertisingId=&appName=web&appVersion=5.2.2-d60060c7283e0978cc63ba036956b5c1657f8eba&architecture=&buildVersion=&clientTime=&deviceDNT=0&deviceId=ab2ddaa3-1108-4e91-9826-d7295603d915&deviceLat=33.6647&deviceLon=-117.1743&deviceMake=Chrome&deviceModel=Chrome&deviceType=web&deviceVersion=80.0.3987.149&includeExtendedEvents=false&marketingRegion=US&sid=2c6d09b0-1e23-11ec-bbb6-dca632884a02&userId=)')
    xbmc.executebuiltin('PlayerControl(repeatall)')
    xbmc.executebuiltin('PlayerControl(RandomOn)')

elif action == 'romance1':
    xbmc.executebuiltin('PlayMedia(https://service-stitcher-ipv4.clusters.pluto.tv/stitch/hls/channel/5a66795ef91fef2c7031c599/master.m3u8?advertisingId=&appName=web&appVersion=5.2.2-d60060c7283e0978cc63ba036956b5c1657f8eba&architecture=&buildVersion=&clientTime=&deviceDNT=0&deviceId=ab2ddaa3-1108-4e91-9826-d7295603d915&deviceLat=33.6647&deviceLon=-117.1743&deviceMake=Chrome&deviceModel=Chrome&deviceType=web&deviceVersion=80.0.3987.149&includeExtendedEvents=false&marketingRegion=US&sid=2c6d09b0-1e23-11ec-bbb6-dca632884a02&userId=)')
    xbmc.executebuiltin('PlayerControl(repeatall)')
    xbmc.executebuiltin('PlayerControl(RandomOn)')
    
elif action == 'crime1':
    xbmc.executebuiltin('PlayMedia(https://service-stitcher-ipv4.clusters.pluto.tv/stitch/hls/channel/5f4d8594eb979c0007706de7/master.m3u8?advertisingId=&appName=web&appVersion=5.2.2-d60060c7283e0978cc63ba036956b5c1657f8eba&architecture=&buildVersion=&clientTime=&deviceDNT=0&deviceId=ab2ddaa3-1108-4e91-9826-d7295603d915&deviceLat=33.6647&deviceLon=-117.1743&deviceMake=Chrome&deviceModel=Chrome&deviceType=web&deviceVersion=80.0.3987.149&includeExtendedEvents=false&marketingRegion=US&sid=2c6d09b0-1e23-11ec-bbb6-dca632884a02&userId=)')
    xbmc.executebuiltin('PlayerControl(repeatall)')
    xbmc.executebuiltin('PlayerControl(RandomOn)')
    
    
elif action == 'lists2':
    from resources.lib.indexers import playlists
    playlists.indexer().rootlists2()
    
elif action == 'lists3':
    from resources.lib.indexers import playlists
    playlists.indexer().rootlists3()
    
elif action == 'lists4':
    from resources.lib.indexers import playlists
    playlists.indexer().rootlists4()
    
elif action == 'lists5':
    from resources.lib.indexers import playlists
    playlists.indexer().rootlists5()
    
elif action == 'lists6':
    from resources.lib.indexers import playlists
    playlists.indexer().rootlists6()
    
elif action == 'lists7':
    from resources.lib.indexers import playlists
    playlists.indexer().rootlists7()

elif action == 'directory':
    from resources.lib.indexers import playlists
    playlists.indexer().get(url)

elif action == 'qdirectory':
    from resources.lib.indexers import playlists
    playlists.indexer().getq(url)

elif action == 'xdirectory':
    from resources.lib.indexers import playlists
    playlists.indexer().getx(url)

elif action == 'developer':
    from resources.lib.indexers import playlists
    playlists.indexer().developer()

elif action == 'tvtuner':
    from resources.lib.indexers import playlists
    playlists.indexer().tvtuner(url)

elif 'youtube' in str(action):
    from resources.lib.indexers import playlists
    playlists.indexer().youtube(url, action)

elif action == 'browser':
    from resources.lib.indexers import playlists
    playlists.resolver().browser(url)

elif action == 'search':
    from resources.lib.indexers import playlists
    playlists.indexer().search()

elif action == 'addSearch':
    from resources.lib.indexers import playlists
    playlists.indexer().addSearch(url)

elif action == 'delSearch':
    from resources.lib.indexers import playlists
    playlists.indexer().delSearch()
    
elif action == 'ruSettings':
    from resources.lib.modules import control
    control.openSettings(id='script.module.resolveurl')