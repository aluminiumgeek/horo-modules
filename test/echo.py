# echo.py (c) Mikhail Mezyakov <mihail265@gmail.com>
# Released under the GNU GPL v.3
# 
# Returns copy of input message

def horo(channel, user, args):
    """Return your message. Usage: echo <message>"""
    
    return u'PRIVMSG {channel} :{message}'.format(
        channel = channel,
        message = ' '.join(args)
    )
