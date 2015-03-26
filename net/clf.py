# -*- coding: utf-8 -*-
# clf.py (c) Mikhail Mezyakov <mihail265@gmail.com>
# Released under the GNU GPL v.3
# 
# Random shell commands from commandlinefu.com

import urllib


def horo(channel, user, args):
    """Get random shell command from commandlinefu.com"""

    url = 'http://www.commandlinefu.com/commands/random/plaintext'
    data = urllib.urlopen(url).read()

    data = data.split('\n')
    del data[0]  # David Winterbottom's comment

    ret = []
    for line in data:
        if line:
            ret.append('PRIVMSG ' + channel + ' :' + line)

    return '\n'.join(ret)
