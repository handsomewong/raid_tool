class RaidToolBase(object):
    def get_build_raid_cmds(self):
        pass

    def get_no_raid_cmds(self):
        pass

    def get_del_vd_cmds(self):
        pass

    def get_endskcache_cmd(self, virtual_disk):
        pass
