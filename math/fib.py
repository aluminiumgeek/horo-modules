# fib.py (c) Mikhail Mezyakov <mihail265@gmail.com>
# Released under the GNU GPL v.3
# 
# Module returns line of the Fibonacci numbers


def horo(channel, user, args):
    """Calculate line of the Fibonacci numbers. If '-n' option was specified, return only nth number. Usage: fib [-n] <count>"""

    if args[0] == '-n':
        if args[1] == "0":
            result = '0'

        elif args[1] == "1":
            result = '0'

        else:
            a = [0, 1]
            i = 1
            while i <= int(args[1]) - 2:
                a.append(a[-1] + a[-2])

                del a[0]

                i += 1

            out = str(a[len(a) - 1])

            result = out

    elif args[0] == "0":
        result = '0'

    elif args[0] == "1":
        result = '0'

    elif args[0] == "2":
        result = '0 1'

    else:
        a = [0, 1]
        out = "0 1 "
        i = 1
        while i <= int(args[0]) - 2:
            a.append(a[-1] + a[-2])

            out += str(a[-1]) + " "

            del a[0]
            i += 1

        result = out

    return u'PRIVMSG {channel} :{result}'.format(channel=channel, result=result)
