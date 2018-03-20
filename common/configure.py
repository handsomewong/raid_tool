import os
import sys
ROOT_PATH = os.getenv('ROOT_PATH', '')
if ROOT_PATH not in sys.path:
    sys.path.append(ROOT_PATH)

import json

class Configura(object):
    def __init__(self):
        self.conf = json.load(file(ROOT_PATH + '/conf.txt'))

    def get_raids(self):
        return self.conf['add_raids']

    def get_del_logic_drives(self):
        return self.conf['del_logic_drive']

    def get_no_raid(self):
        return self.conf['non_raid']

    def get_enable_disks(self):
        return self.conf['enable_disk_cache']