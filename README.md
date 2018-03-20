This tool is trying to build raids with all physical drives at one time, and we also want it to
 support different vendor's servers

1.configure conf.txt like this:
```
{
    "add_raids": [{
            "adapter": "0",
            "raid_level": "0",
            "physical_drivers": "$enclosure1:$slot0,$enclosure3:$slot11,....",
            "read_policy": "NORA",
            "write_policy": "WB"
        },
        {
            "adapter": "0",
            "raid_level": "1",
            "physical_drivers": "$enclosure1:$slot2,$enclosure3:$slot3,....",
            "read_policy": "NORA",
            "write_policy": "WB"
        }
    ],
    "non_raid": [{
            "adapter": "0",
            "physical_drivers": "$enclosure1:$slot2"
        },
        {
            "adapter": "1",
            "physical_drivers": "$enclosure1:$slot2"
        }
    ],
    "del_logic_drive": [{
            "adapter": "0",
            "logic_dirvers": [1, 2, 3]
        },
        {
            "adapter": "1",
            "logic_dirvers": [1, 2, 3]
        }
    ],
    "enable_disk_cache": [{
            "adapter": "0",
            "logic_dirvers": [1, 2, 3]
        },
        {
            "adapter": "1",
            "logic_dirvers": [1, 2, 3]
        }
    ]
}
```
2.configure enviroment variable
```
#export CLI_TOOL_PATH=/opt/MegaRAID/MegaCli/
#export ROOT_PATH=/home/code/raid_tool
```
