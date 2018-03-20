import os

CLI_TOOL_PATH = os.getenv('CLI_TOOL_PATH', '')
if CLI_TOOL_PATH not in sys.path:
    sys.path.append(CLI_TOOL_PATH)

from cli_tool import manager

if __name__ == '__main__':
    print 'excute like this:./main.py MegaRAID/storcli create/makejobb/del'
    driver = manager.RaidManager(os.sys.argv[1])
    op = os.sys.argv[2]
    if op == 'create':
        driver.create_raid()
    elif op == 'makejobb':
        pass
    else:
        pass