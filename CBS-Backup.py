"""
CraftyBackupScript - Backup
v0.2.0
Linux only.

~~~~~~~~~~~~~~~~~
Psuedocode:
(Can be configured one at a time to backup)

Send `save-off` and `save-all` commands in screen spigot process
   
Start backup process
    Send `say This server is backing up... Expect lag...` or similar message
    Compress all server data and put in their respective .ZIP or 7z archives.
        Save with format `<servername>_mm-dd-yy_hh-mm.7z`
    `save-on`
    Delete backup file outside of file limit determined by last file creation date.
    
Send `stop` command to make server restart.
~~~~~~~~~~~~~~~~~

command for inside screen:
screen -S minecraft -p 0 -X stuff "say test123$(printf \\r)"

Requirements on Linux:
p7zip
p7zip-full
screen

"""
import subprocess
import shlex
import time

# Config

minecraftServer = False # To put in minecraft server mode. 

# File Paths (needs to be changed)
serverPath = "/home/cabox/workspace/CCNetwork/Server1/" # Path to folder of server to be backed up.
savePath = "/home/cabox/workspace/CCNetwork/Backup/BackupArchives/Server1/" # To keep backup archives

# Archive Naming
datetime = time.strftime("%m-%d-%Y--%I:%M%p") # Time format
archiveName = "Server1_Backup_" + datetime  # Name of backup archive

# End Config.

print("CraftyBackupScript")
print("")

# Name preview
print("Archive named:\n%s.7z" % (archiveName))
# Compress with 7z.
# -mx9 = Ultra Compression | -t7z = Specify .7z format | -mmt = Multithreading
print("Using command:\n7z a -mx9 -t7z -mmt %s%s.7z %s*" % (savePath, archiveName, serverPath))
subprocess.call(shlex.split("7z a -mx9 -t7z -mmt %s%s.7z %s*" % (savePath, archiveName, serverPath)))

