"""
CraftyBackupScript - Backup
v0.3.0
Linux only.

Requirements on Linux:
p7zip
p7zip-full
screen

command for inside screen:
screen -S minecraft -p 0 -X stuff "say Backing up the server...\n"

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


"""
import subprocess
import shlex
import time

# Config

# Minecraft Server
minecraftServer = True # To put in minecraft server mode. 
screenName = "" # Name of opened screen.
stopServerAfter = True # If the Minecraft server will be told to stop after a backup. Meant for use with CraftyStartScript.

# File Paths (needs to be changed)
serverPath = "/home/cabox/workspace/CCNetwork/Server1/" # Path to folder of server to be backed up.
savePath = "/home/cabox/workspace/CCNetwork/Backup/BackupArchives/Server1/" # To keep backup archives

# Archive Naming
datetime = time.strftime("%m-%d-%Y--%I:%M%p") # Time format
archiveName = "Server1_Backup_" + datetime  # Name of backup archive

# End Config.

print("CraftyBackupScript")
print("")

# Minecraft Server Managing
if minecraftServer:
    subprocess.call(shlex.split("screen -S minecraft -p 0 -X stuff \"\n\"")) # Presses Enter in case of left over command.
    print("Saying warning message(s)")
    subprocess.call(shlex.split("screen -S minecraft -p 0 -X stuff \"say Backing up the server...\n\""))
    print("Turning saving off temporarily...")
    subprocess.call(shlex.split("screen -S minecraft -p 0 -X stuff \"save-off\n\"")) # save-off
    time.sleep(1)
    print("Manually saving...")
    subprocess.call(shlex.split("screen -S minecraft -p 0 -X stuff \"save-all\n\"")) # save-all
    time.sleep(10)
    

# Name preview
print("Archive named:\n%s.7z" % (archiveName))
# Compress with 7z.
# -mx9 = Ultra Compression | -t7z = Specify .7z format | -mmt = Multithreading
print("Using command:\n7z a -mx9 -t7z -mmt %s%s.7z %s*" % (savePath, archiveName, serverPath))
subprocess.call(shlex.split("7z a -mx9 -t7z -mmt %s%s.7z %s*" % (savePath, archiveName, serverPath)))

print("Done with backup.")

if minecraftServer:
    print("Re-enabling saving.")
    subprocess.call(shlex.split("screen -S minecraft -p 0 -X stuff \"save-on\n\""))
    if stopServerAfter:
        print("Stopping server in 5 seconds...")
        time.sleep(5)
        print("Now stopping server.")
        subprocess.call(shlex.split("screen -S minecraft -p 0 -X stuff \"stop\n\""))


