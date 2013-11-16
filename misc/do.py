# do.py (c) Mikhail Mezyakov <mihail265@gmail.com>
# Released under the GNU GPL v.3
# 
# Send raw-command to a server
# You must set OWNER

OWNER = "mynickname"

def horo(channel, user, args):
    line = u' '.join(args)

    owner_commands = ('part', 'quit')

    for command in owner_commands:
        if command.lower() in line.lower() and user != OWNER:
            return "PRIVMSG " + channel + " :No way!"

    return line.replace('; ', '\n')
