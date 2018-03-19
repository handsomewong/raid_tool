import os

RAID_TOOL_PATH = os.getenv('RAID_TOOL_PATH', '')
if RAID_TOOL_PATH not in sys.path:
    sys.path.append(RAID_TOOL_PATH)

import cli_tool.base

class MegaCli(RaidToolBase):
    def __init__(self):
        self.tool_path = RAID_TOOL_PATH + 'MegaCli64'

    def get_raid_tp(self):
        return self.tool_path + ' -CfgLdAdd -r%(raid_level)s[%(enclosure)s:%(slot)s] %(write_policy)s %(read_policy)s Cached -a%(adapter)s'

    def get_no_raid_tp(self):
        return self.tool_path + ' -PDMakeJBOD -PhysDrv[%(enclosure)s:%(slot)s] -a%(adapter)s'

    def get_del_vd_tp(self):
        return self.tool_path + ' -CfgLdDel -L%(logic_dirver)s -a%(adapter)s'

    def get_endskcache_tp(self):
        return self.tool_path + ' -LDSetProp -EnDskCache -L%(logic_dirver)s -a%(adapter)s'