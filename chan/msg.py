# msg.py (c) Mikhail Mezyakov <mihail265@gmail.com>
# Released under the GNU GPL v.3
# 
# Send message to any user/channel

def horo(channel, user, args):
    destination = args[0]
    del args[0]
    
    message = u' '.join(args)
    
    return u'PRIVMSG {destination} :{message}'.format(
        destination = destination,
        message = message
    )

