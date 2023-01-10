import json
from time import time

from slyguy import settings, signals
from slyguy.session import Session
from slyguy.log import log
from slyguy.monitor import monitor
from slyguy.drm import set_drm_level
from slyguy.donor import check_donor

from .proxy import Proxy
from .player import Player
from .util import check_updates
from .constants import *

def _check_news():
    _time = int(time())
    if _time < settings.getInt('_last_news_check', 0) + NEWS_CHECK_TIME:
        return

    settings.setInt('_last_news_check', _time)

    with Session(timeout=15) as session:
        news = session.gz_json(NEWS_URL)
    if not news:
        return

    if 'id' not in news or news['id'] == settings.get('_last_news_id'):
        return

    settings.set('_last_news_id', news['id'])
    settings.set('_news', json.dumps(news))

@signals.on(signals.ON_SETTINGS_CHANGE)
def settings_changed():
    log.debug('Shared Service: Settings Changed')

def start():
    log.debug('Shared Service: Started')

    proxy = Proxy()
    player = Player()

    try:
        proxy.start()
    except Exception as e:
        log.error('Failed to start proxy server')
        log.exception(e)

    try:
        set_drm_level()
    except Exception as e:
        log.error('Failed to set DRM level')
        log.exception(e)

    is_donor = False
    try:
        is_donor = check_donor()
    except Exception as e:
        log.error('Failed to check donor')
        log.exception(e)

    if is_donor:
        log.debug('Welcome SlyGuy donor!')

    ## Inital wait on boot
    monitor.waitForAbort(5)

    try:
        while not monitor.abortRequested():
            try: check_updates()
            except Exception as e: log.exception(e)

            if not is_donor or settings.getBool('show_news'):
                try: _check_news()
                except Exception as e: log.exception(e)

            if monitor.waitForAbort(60):
                break
    except KeyboardInterrupt:
        pass
    except Exception as e:
        log.exception(e)

    try: proxy.stop()
    except: pass

    log.debug('Shared Service: Stopped')
