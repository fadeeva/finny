import re

full_cmnd = []
def get_cmnd_name(screen_name, cmnd):
    cmnd_list = {
        'main_menu': ['si', 'sp', 'cf', 'pm', 'c', 'f', 'o', 'm']
    }
    if screen_name in cmnd_list.keys() and cmnd[0] not in (301, 303, 304, 305, 306):
        if len(full_cmnd) == 2: full_cmnd.clear()
        full_cmnd.append(cmnd[1])
    print(full_cmnd)

def clean_text(dirty):
    dirty = dirty.replace('[/font]', '')
    dirty = dirty.replace('\n', ' ')
    dirty = re.sub(r'\[font=fonts\/[a-zA-Z0-9_-]*\]', '', dirty)
    return dirty.lower()