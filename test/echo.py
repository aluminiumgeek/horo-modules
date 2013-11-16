# echo.py (c) Mikhail Mezyakov <mihail265@gmail.com>
# Released under the GNU GPL v.3
# 
# Returns copy of input line

def horo(channel, user, args):
    return u'PRIVMSG {channel} :{message}'.format(
        channel = channel,
        message = ' '.join(args)
    )
