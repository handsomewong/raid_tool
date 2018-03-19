import os

CLI_TOOL_PATH = os.getenv('CLI_TOOL_PATH', '')
if CLI_TOOL_PATH not in sys.path:
    sys.path.append(CLI_TOOL_PATH)

from cli_tool import manager

if __name__ == '__main__':
    driver = manager.RaidManager('mega_raid')
    driver.create_raid()