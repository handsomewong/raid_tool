1.conf.txt,like this:
```
{
    "add_raids": [{
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
    ],
    "non_raid": [
        {"adapter":"0",
        "physical_drivers": "$enclosure1:$slot2,$enclosure3:$slot3,...."},
        {"adapter":"1",
        "physical_drivers": "$enclosure1:$slot2,$enclosure3:$slot3,...."}
    ],
    "del_logic_drive":[
        {"adapter":"0",
        logic_dirvers:[1,2..3]},
        {"adapter":"1",
        logic_dirvers:[1,2..3]}
    ]
}
```
2.config env
export "CLI_TOOL_PATH"=/opt/MegaRAID/MegaCli/
export "RAID_TOOL_PATH"=/home/code/raid_tool

3.install python-fire
