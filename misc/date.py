# -*- coding: utf-8 -*-
# date.py (c) Mikhail Mezyakov <mihail265@gmail.com>
# Released under the GNU GPL v.3
# 
# Print current date and time

from datetime import datetime

def horo(channel, user, args):
    date = datetime.now().strftime('%d.%m.%Y %H:%M:%S')
    
    return u'PRIVMSG {channel} :{date}'.format(
        channel = channel,
        date = date
    )
