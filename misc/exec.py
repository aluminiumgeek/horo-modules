# -*- coding: utf-8 -*-
# exec.py (c) Mikhail Mezyakov <mihail265@gmail.com>
# Released under the GNU GPL v.3
# 
# Execute python code
# You must set OWNER

import os

OWNER = 'mynickname'

def horo(channel, user, args):
    """Execute python code. Usage: exec <some python code>"""
    
    if user == OWNER:
        command = u' '.join(args)
        result = os.popen('python -c "'+command+'"').read()
    else: 
        result = 'No way!'

    return u'PRIVMSG {channel} :{result}'.format(
        channel = channel,
        result = result
    )
