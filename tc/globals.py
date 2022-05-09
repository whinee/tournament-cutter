import locale
import os
from os import get_terminal_size

config_path = None
TW = get_terminal_size().columns

if os.name != 'posix':
    import ctypes

    POSIX = 0

    CFLOP = [
        fr"{os.getcwd()}\tc.yml",
        fr"{os.getenv('USERPROFILE')}\AppData\Roaming\tc\videos.yml"
    ]
    LOCALE = locale.windows_locale[ctypes.windll.kernel32.GetUserDefaultUILanguage()][:2]
else:
    POSIX = 1
    CFLOP = [
        f"{os.getcwd()}/tc.yml",
        "~/.config/tc/vidoes.yml",
        "~/.tc",
        "/etc/tc/videos.yml"
    ]
    if xch:=os.getenv('XDG_CONFIG_HOME'):
        CFLOP.insert(1, f"{xch}/tc/videos.yml")
    LOCALE = locale.getdefaultlocale()[0][:2]