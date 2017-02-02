"""
CraftyBackupScript - Backup
v0.4.0
Linux only.
Written by colebob9 in Python 3.
Released under the MIT License.

Required Packages for Linux:
    p7zip
    p7zip-full
    screen
    python3

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
    
    ::Delete backup file outside of file limit determined by last file creation date.:: <- Last thing to add
    
Send `stop` command to make server restart.
~~~~~~~~~~~~~~~~~


"""
import subprocess
import shlex
import time

# Start elasped time
start = time.time()

# :::Config:::
#

# Minecraft Server
minecraftServer = True # To put in minecraft server mode. 
screenName = "minecraft" # Name of opened screen.
stopServerAfter = False # If the Minecraft server will be told to stop after a backup. Meant for use with CraftyStartScript.

# File Paths (needs to be changed)
serverPath = "/home/cabox/workspace/CCNetwork/Server1/" # Path to folder of server to be backed up.
savePath = "/home/cabox/workspace/CCNetwork/Backup/BackupArchives/Server1/" # To keep backup archives

# Archive Naming
datetime = time.strftime("%m-%d-%Y--%I:%M%p") # Time format
archiveName = "Server1_Backup_" + datetime  # Name of backup archive

# Time
saveAllTime = 8 # Time in seconds to wait for the manual save before continuing.

# Script
showExtraInfo = False # Whether to show lines like file paths or commands used.

#
# :::End Config.:::

# To send commands to a Minecraft server in a Screen
def minecraftCommand(serverCommand):
    subprocess.call(shlex.split("screen -S %s -p 0 -X stuff \"%s\n\"" % (screenName, serverCommand)))
    if showExtraInfo:
        print("Using command:\nscreen -S %s -p 0 -X stuff \"%s\"\n" % (screenName, serverCommand))

# Title
print("CraftyBackupScript v0.4.0")
print("")

# Minecraft Server Managing
if minecraftServer:
    minecraftCommand("") # Enter to clear out any previous command.
    print("Saying warning message(s)")
    if stopServerAfter:
        minecraftCommand("say Server is backing up and restarting...")
    else:
        minecraftCommand("say Server is now backing up...")
    print("Turning saving off temporarily...")
    minecraftCommand("save-off") # save-off
    time.sleep(1)
    print("Manually saving...")
    minecraftCommand("save-all") # save-all
    time.sleep(saveAllTime)
    

# Name preview
print("Archive named:\n%s.7z" % (archiveName))
# Compress with 7zip.
# -mx9 = Ultra Compression | -t7z = Specify .7z format | -mmt = Multithreading
if showExtraInfo:
    print("Using command:\n7z a -mx9 -t7z -mmt %s%s.7z %s*" % (savePath, archiveName, serverPath))
start7z = time.time()
subprocess.call(shlex.split("7z a -mx9 -t7z -mmt %s%s.7z %s*" % (savePath, archiveName, serverPath)))
end7z = time.time()
print("Done with backup.")

elaspedTime7z = (end7z - start7z)
print("Compression took " + str(round(elaspedTime7z , 1)) + " seconds")

if minecraftServer:
    # Re-enabling saves
    print("Re-enabling saving.")
    minecraftCommand("save-on")
    minecraftCommand("save-all") # Save once more in case of long backup process.
    # Stop Minecraft server
    if stopServerAfter:
        print("Stopping server in 5 seconds...")
        time.sleep(5)
        print("Now stopping server.")
        minecraftCommand("say Server is now restarting...")
        minecraftCommand("stop") # stop


# Elapsed time for entire process
end = time.time()
elaspedTime = (end - start)
print("Overall backup process took " + str(round(elaspedTime , 1)) + " seconds")

