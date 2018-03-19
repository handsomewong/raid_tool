import os
CLI_TOOL_PATH = os.getenv('CLI_TOOL_PATH', '')
if CLI_TOOL_PATH not in sys.path:
    sys.path.append(CLI_TOOL_PATH)

MAPPING = {
    'mega_raid':'cli_tool.mega_raid.mega_raid.MegaCli',
}

import configure

class RaidManager(object):
    def __init__(self, tool_name):
        self.tool = cli_tool.importutils.import_object(MAPPING[tool_name])
        self.conf = configure.Configura()

    def create_raid(self):
        raid_tpl = self.tool.get_raid_tp()
        endskcache_tpl = self.tool.get_endskcache_tp()

        self.conf.get_raids()

    def create_no_raid(self):
        no_raid_tpl = self.tool.get_no_raid_tp()
        self.conf.get_logic_drives()

    def del_logic_drives(self):
        vd_tp = self.tool.get_del_vd_tp()
        self.conf.get_no_raid()