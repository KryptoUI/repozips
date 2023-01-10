from contextlib import contextmanager
from collections import defaultdict

from .log import log
from .exceptions import Error, Exit

_signals = defaultdict(list)
_skip = defaultdict(int)

AFTER_RESET     = 'after_reset'
ON_SERVICE      = 'on_service'
BEFORE_DISPATCH = 'before_dispatch'
AFTER_DISPATCH  = 'after_dispatch'
ON_ERROR        = 'on_error'
ON_EXCEPTION    = 'on_exception'
ON_CLOSE        = 'on_close'
ON_SETTINGS_CHANGE = 'on_settings_changed'

def skip_next(signal):
    _skip[signal] += 1

def on(signal):
    def decorator(f):
        _signals[signal].append(f)
        return f
    return decorator

def emit(signal, *args, **kwargs):
    if _skip[signal] > 0:
        _skip[signal] -= 1
        log.debug("SKIPPED SIGNAL: {}".format(signal))
        return

    log.debug("SIGNAL: {}".format(signal))
    for f in _signals.get(signal, []):
        f(*args, **kwargs)

@contextmanager
def throwable():
    try:
        yield 
    except Exit as e:
        pass
    except Error as e:
        emit(ON_ERROR, e)
    except Exception as e:
        emit(ON_EXCEPTION, e)
