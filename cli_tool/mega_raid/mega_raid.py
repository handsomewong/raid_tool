import os
import sys

RAID_TOOL_PATH = os.getenv('RAID_TOOL_PATH', '')
if RAID_TOOL_PATH not in sys.path:
    sys.path.append(RAID_TOOL_PATH)

from cli_tool import base
from common import configure

class MegaCli(base.RaidToolBase):
    def __init__(self):
        self.conf = configure.Configura()
        self.tool_path = RAID_TOOL_PATH + 'MegaCli64'

    def get_build_raid_cmds(self):
        '''
        raids = [{
                    "adapter":"0",
                    "raid_level": "0",
                    "physical_drivers": "$enclosure1:$slot0,$enclosure3:$slot11,....",
                    "read_policy": "no read ahead",
                    "write_policy": "write back",
                    "disk_cache_policy": "enabled"
                },
                {
                    "adapter":"0",
                    "raid_level": "1",
                    "physical_drivers": "$enclosure1:$slot2,$enclosure3:$slot3,....",
                    "read_policy": "read ahead",
                    "write_policy": "write back",
                    "disk_cache_policy": "enabled"
                }
            ]
        '''
        cmds = []
        tp = self.tool_path + 
            ' -CfgLdAdd -r%(raid_level)s[%(physical_drivers)s] ' + 
            '%(write_policy)s %(read_policy)s Cached -a%(adapter)s'
        raids = self.conf.get_raids()
        for raid in raids:
            cmd = tp % raid
            cmds.append(cmd)      

        return cmds

    def get_no_raid_cmds(self):
        '''
        no_raids = [
                {"adapter":"0",
                "physical_drivers": "$enclosure1:$slot2,$enclosure3:$slot3,...."},
                {"adapter":"1",
                "physical_drivers": "$enclosure1:$slot2,$enclosure3:$slot3,...."}
            ]
        '''
        cmds = []
        no_raids = self.conf.get_no_raid()
        tp = self.tool_path + 
            ' -PDMakeJBOD -PhysDrv[%(physical_drivers)s] -a%(adapter)s'
        for raid in no_raids:
            cmd = tp % raid
            cmds.append(cmd)

        return cmds

    def get_del_vd_cmds(self):
        '''
        del_drives = [
                {"adapter":"0",
                logic_dirvers:[1,2..3]},
                {"adapter":"1",
                logic_dirvers:[1,2..3]}
            ]
        '''
        cmds = []
        del_drives = self.conf.get_del_logic_drives()
        tp = self.tool_path + ' -CfgLdDel -L%(logic_dirver)s -a%(adapter)s'
        for del_drive in del_drives:
            cmd = tp % del_drive
            cmds.append(cmd)

        return cmds

    def get_endskcache_cmd(self):
        '''
        enable_disk_cache = [
                {"adapter":"0",
                logic_dirvers:[1,2..3]},
                {"adapter":"1",
                logic_dirvers:[1,2..3]}
            ]
        '''
        cmds = []
        enable_disks = self.conf.get_enable_disks()
        tp = self.tool_path + ' -LDSetProp -EnDskCache -L%(logic_dirver)s -a%(adapter)s'
        for enable_disk in enable_disks:
            cmd = tp % enable_disk
            cmds.append(cmd)

        return cmds