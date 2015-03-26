# -*- coding: utf-8 -*-
# impc.py (c) Mikhail Mezyakov <mihail265@gmail.com>
# Released under the GNU GPL v.3
# 
# IRC mpc -- Module that controls Music Player Daemon (mpd)
# Required mpd (http://musicpd.org) and mpc (http://mpd.wikia.com/wiki/Client:Mpc)
# You must set OWNER

import os

OWNER = 'mynickname'

commands = ['toggle', 'next', 'prev', 'stop', 'random', 'current', 'status']
altcommands = ['t', 'n', 'p', 's', 'r', 'c', 'st']


def commpc(command):
    import os
    ret = os.popen('mpc ' + command, 'r').read().replace('\n', '. ')
    return ret


def horo(channel, user, args):
    """Control Music Player Daemon. Usage: impc <command>. Commands: toggle, next, prev, stop, random, current, status"""

    com = args[0]
    if (com in commands or com in altcommands) and user == OWNER:
        result = "---"

        if com == 'toggle' or com == 't':
            result = commpc('toggle')

        elif com == 'next' or com == 'n':
            result = commpc('next')

        elif com == 'prev' or com == 'p':
            result = commpc('prev')

        elif com == 'stop' or com == 's':
            result = commpc('stop')

        elif com == 'random' or com == 'r':
            result = commpc('random')

        elif com == 'current' or com == 'c':
            result = commpc('current')

        elif com == 'status' or com == 'st':
            result = commpc('status')

    else:
        result = 'Permission denied'

    return u'PRIVMSG {user} :mpd: {result}'.format(user=user, result=result)
