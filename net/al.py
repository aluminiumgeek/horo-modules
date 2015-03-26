# -*- coding: utf-8 -*-
# al.py (c) Mikhail Mezyakov <mihail265@gmail.com>
# Released under the GNU GPL v.3
# 
# LME aluminium, bauxites, etc prices

import re
import urllib


def delta_check(data):
    d = data.find('td class="delta')
    s = 'delta up'

    if s in data[d:data.find('delta-value', d)]:
        al = '+'
    else:
        al = '-'

    d = data.find('td class="delta', d + 30)

    if s in data[d:data.find('delta-value', d)]:
        alloy = '+'
    else:
        alloy = '-'

    d = data.find('td class="delta', d + 30)

    if s in data[d:data.find('delta-value', d)]:
        nasaac = '+'
    else:
        nasaac = '-'

    d = data.find('td class="delta', d + 30)

    if s in data[d:data.find('delta-value', d)]:
        baux = '+'
    else:
        baux = '-'

    return al, alloy, nasaac, baux


def horo(channel, user, args):
    """Get LME aluminium, bauxites, etc prices"""

    page = urllib.urlopen('http://aluminiumleader.com')
    data = page.read()

    data = data[data.find('"exchange"') - 21:data.find('"trade-date"') + 30]

    deltas = delta_check(data)

    data = re.compile(r'<.*?>').sub('', data).decode('cp1251')
    data = data.replace('\t', '')
    data = data.split('\r\n\r\n\r\n')

    result = []

    i = 0
    for entr in data:
        if not u'Дата' in entr:
            entr = entr.split('\r\n')

            res = entr[0] + ': ' + entr[1] + ' (' + deltas[i] + entr[2] + ')'
            res = res.replace('&ndash;', '')
            i += 1

            result.append(res.encode('utf-8'))
        else:
            result.append(entr.encode('utf-8'))

    ret = []
    for r in result:
        ret.append(u'PRIVMSG {channel} :{result}'.format(channel=channel,
                                                         result=r))

    return '\n'.join(ret)
