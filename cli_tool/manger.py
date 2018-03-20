import os
import sys

ROOT_PATH = os.getenv('ROOT_PATH', '')
if ROOT_PATH not in sys.path:
    sys.path.append(ROOT_PATH)

import time
from common import importutils

MAPPING = {
    'MegaRAID':'cli_tool.mega_raid.mega_raid.MegaCli',
}

class RaidManager(object):
    def __init__(self, tool_name):
        self.tool = importutils.import_object(MAPPING[tool_name])

    def create_raid(self):
        build_cmds = self.tool.get_build_raid_cmds()
        for cmd in build_cmds:
            result = os.popen(cmd).readlines()
            print result
            time.sleep(5)

    def create_no_raid(self):
        build_cmds = self.tool.get_no_raid_cmds()
        for cmd in build_cmds:
            result = os.popen(cmd).readlines()
            print result
            time.sleep(5)
        
    def del_logic_drives(self):
        del_cmds = self.tool.get_del_vd_cmds()
        for cmd in del_cmds:
            result = os.popen(cmd).readlines()
            print result
            time.sleep(5)

    def enable_disk_cache(self):
        endskcache_cmds = self.tool.get_endskcache_cmd()
        for cmd in endskcache_cmds:
            result = os.popen(cmd).readlines()
            print result
            time.sleep(5)       
