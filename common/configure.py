import os
import sys
CLI_TOOL_PATH = os.getenv('CLI_TOOL_PATH', '')
if CLI_TOOL_PATH not in sys.path:
    sys.path.append(CLI_TOOL_PATH)

import json
import file

class Configura(object):
    def __init__(self):
        self.conf = json.load(file(CLI_TOOL_PATH + 'conf.txt'))

    def get_raids(self):
        return self.conf['add_raids']

    def get_del_logic_drives(self):
        return self.conf['del_logic_drive']

    def get_no_raid(self):
        return self.conf['non_raid']

    def get_enable_disks(self):
        return self.conf['enable_disk_cache']