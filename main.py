import os
import sys

ROOT_PATH = os.getenv('ROOT_PATH', '')
if ROOT_PATH not in sys.path:
    sys.path.append(ROOT_PATH)

from cli_tool import manager

if __name__ == '__main__':
    print 'excute like this:./main.py MegaRAID/storcli create/makejobb/del'
    driver = manager.RaidManager(os.sys.argv[1])
    import pdb
    pdb.set_trace()
    op = os.sys.argv[2]
    if op == 'create':
        driver.create_raid()
    elif op == 'makejobb':
        pass
    else:
        pass