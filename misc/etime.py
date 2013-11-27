# -*- coding: utf-8 -*-
# time.py (c) Mikhail Mezyakov <mihail265@gmail.com>
# Released under the GNU GPL v.3
# 
# Print execution time of another module

import time
import importlib

def horo(channel, user, args):
    """Show execution time of any module. If '-p' option was specified, print module's output. Usage: etime [-p] <module name> [<module options>]. Example: etime fib 20"""
    
    output = False
    if args[0] == '-p':
        output = True
        del args[0]
    
    module = importlib.import_module('modules.{0}'.format(args[0]))
    module_args = args[1:]

    start = time.time()
    ret = module.horo(channel, user, module_args)
    end = time.time()
    
    result = 'Execution time: %ss'%str(end - start)
    
    if output: 
        result = ret + '\n' + result
        
    ret = []
    for r in result.split('\n'):
        ret.append(u'PRIVMSG {channel} :{result}'.format(
            channel = channel,
            result = result
        ))
    
    return '\n'.join(ret)
