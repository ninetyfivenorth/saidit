from pylons import config
from pylons import tmpl_context as c
from pylons import app_globals as g
from pylons.i18n import N_

from urllib import quote

from r2.lib.wrapped import Templated

# CUSTOM, for temp chat upgrade
import random, string
from r2.lib.validator.preferences import set_prefs

# Note: User and subreddit chat preferences have already been checked in pages.py
class SidebarChat(Templated):

    # NOTE: system is 'subreddit', suject is subreddit name
    def __init__(self, system, subject):
        self.chat_channel = quote(g.chat_channel_name_prefix + subject + g.chat_channel_name_suffix)
        self.chat_user = c.user.pref_chat_user
        self.chat_client_user = c.user.pref_chat_client_user
        self.chat_client_password = c.user.pref_chat_client_password
        self.chat_client = g.chat_client
        self.chat_client_url = g.chat_client_url
        self.user_is_loggedin = c.user_is_loggedin

        Templated.__init__(self)
