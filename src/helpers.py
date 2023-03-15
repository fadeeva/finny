import re

COMMANDS = {
    'si' : 'stock_info',
    'sp' : 'stock_profit',
    'cf' : 'cash_flow',
    'pm' : 'portfolio_management',
    'c'  : 'cfd',
    'f'  : 'futures',
    'o'  : 'options',
    'm'  : 'multipliers',
    'ignore_keycode' : [300, 301, 303, 304, 305, 306, 27], # numlock, rshift, rctrl, lshift, rshift, escape(?)
    'enter': 13
}

full_cmnd = []
def get_cmnd_name(cmnd):
    if cmnd[0] not in COMMANDS['ignore_keycode']:
        if cmnd[0] == COMMANDS['enter']:
            curr_cmnd = ''.join(full_cmnd)
            if curr_cmnd in COMMANDS.keys():
                full_cmnd.clear()
                return COMMANDS[curr_cmnd]
            full_cmnd.clear()
        else:
            full_cmnd.append(cmnd[1])


def clean_text(dirty):
    dirty = dirty.replace('[/font]', '')
    dirty = dirty.replace('\n', ' ')
    dirty = re.sub(r'\[font=fonts\/[a-zA-Z0-9_-]*\]', '', dirty)
    return dirty.lower()