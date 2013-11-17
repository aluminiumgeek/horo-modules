# 4chan.py (c) Mikhail Mezyakov <mihail265@gmail.com>
# Released under the GNU GPL v.3
# 
# Return first post from any board of 4chan

import re
import json

from HTMLParser import HTMLParser
from urllib import urlopen

class NoSuchBoard(Exception):
    def __str__(self):
        return "No such board"


def plain_text(text):
    text = text.replace('<br>', ' ')
    text = re.compile(r'<.*?>').sub('', text)
    
    h = HTMLParser()
    
    return h.unescape(text)

def get_data(url):
    connection = urlopen(url)
    raw_data = connection.read()
    
    if raw_data:
        data = json.loads(raw_data, encoding='utf-8')
    else:
        raise NoSuchBoard
    
    return data


def horo(channel, user, args):
    if args[0] in ('--list', '-l'):
        data = get_data('https://api.4chan.org/boards.json')
        
        boards = map(lambda x: '/{0}/'.format(x['board']), data['boards'])
        
        result = ' '.join(boards)
    
    else:
        board = args[0]
        
        try:
            data = get_data('https://api.4chan.org/{0}/0.json'.format(board))
            
        except NoSuchBoard, e:
            result = str(e)
            
        else:
            thread = data['threads'][0]['posts'][0]
            
            text = plain_text(thread['com'])
            image = 'https://images.4chan.org/{board}/src/{tim}{ext}'.format(
                board = board,
                tim = thread['tim'],
                ext = thread['ext']
            )
            replies = thread['replies']

            result = u'{text} | {image} | {replies} replies'.format(
                text = text[:100],
                image = image,
                replies = replies
            )
    
    return 'PRIVMSG {channel} :{result}'.format(
        channel = channel,
        result = result
    )
