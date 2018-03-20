import os

RAID_TOOL_PATH = os.getenv('RAID_TOOL_PATH', '')
if RAID_TOOL_PATH not in sys.path:
    sys.path.append(RAID_TOOL_PATH)

from cli_tool import base
from common import configure

class MegaCli(base.RaidToolBase):
    def __init__(self):
        self.tool_path = RAID_TOOL_PATH + 'MegaCli64'

    def get_build_raid_cmds(self):
        raids = self.conf.get_raids()
        cmd = endskcache_tpl % raids
        
        return self.tool_path + ' -CfgLdAdd -r%(raid_level)s[%(enclosure)s:%(slot)s] %(write_policy)s %(read_policy)s Cached -a%(adapter)s'

    def get_no_raid_cmds(self):
        return self.tool_path + ' -PDMakeJBOD -PhysDrv[%(enclosure)s:%(slot)s] -a%(adapter)s'

    def get_del_vd_cmds(self):
        return self.tool_path + ' -CfgLdDel -L%(logic_dirver)s -a%(adapter)s'

    def get_endskcache_cmd(self, virtual_disk):
        return self.tool_path + ' -LDSetProp -EnDskCache -L%(logic_dirver)s -a%(adapter)s'