import re

COMMANDS = {
    'main_menu' : ['si', 'sp', 'cf', 'pm', 'c', 'f', 'o', 'm'],
    'si'  : [],
    'sp'  : [],
    'cf'  : [],
    'pm'  : [],
    'c' : [],
    'f'   : [],
    'o'   : [],
    'm'   : [],
    'ignore_keycode' : [300, 301, 303, 304, 305, 306] # numlock, rshift, rctrl, lshift, rshift
}

## NEED add enter after each command
full_cmnd = []
def get_cmnd_name(screen_name, cmnd):
    if screen_name in COMMANDS.keys() and cmnd[0] not in COMMANDS['ignore_keycode']:
        if cmnd[0] == 13 : full_cmnd.clear()
        full_cmnd.append(cmnd[1])
        
        ans = [''.join(full_cmnd)]
        if ans[0] in COMMANDS[screen_name]:
            ans.append('Yes')
        else:
            ans.append('No')
            
    print(ans)

def clean_text(dirty):
    dirty = dirty.replace('[/font]', '')
    dirty = dirty.replace('\n', ' ')
    dirty = re.sub(r'\[font=fonts\/[a-zA-Z0-9_-]*\]', '', dirty)
    return dirty.lower()