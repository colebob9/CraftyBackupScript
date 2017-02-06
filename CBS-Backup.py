"""
CraftyBackupScript - Backup
v0.5.0
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
    
    Delete backup file outside of file limit determined by last file creation date.
    
Send `stop` command to make server restart.
~~~~~~~~~~~~~~~~~


"""
import subprocess
import shlex
import time
import os, os.path

# Start elasped time
start = time.time()

# :::Config:::
#

# Minecraft Server
minecraftServer = True # REQUIRED FOR USING WITH A MINECRAFT SERVER 
                       # Turns on whether to send commmands to safely manage a Minecraft server during a backup. 
                       # (Toggles autosaving in order to not corrupt the backup copy.)
screenName = "minecraft" # Name of opened screen where the Minecraft server is online.
stopServerAfter = False # If the Minecraft server will be told to stop after a backup. Meant for use with CraftyStartScript.

# File Paths (needs to be changed)
serverPath = "/home/cabox/workspace/CCNetwork/Server1/" # Path to folder of server to be backed up.
savePath = "/home/cabox/workspace/CCNetwork/Backup/BackupArchives/Server1/" # To keep backup archives

# Archive Naming
datetime = time.strftime("%m-%d-%Y--%I:%M%p") # Time format
archiveName = "Server1_Backup_" + datetime  # Name of backup archive

# Script
showExtraInfo = False # Whether to show lines like file paths or commands used.
saveAllTime = 8 # Time in seconds to wait for the manual save before continuing.

# Aged File Cleanup
agedFileCleanup = True # Whether to enable deleting files after a certain amount of time. (Highly recommended for automatically run backups.)
keepFileTime = 7 # Time in days to wait before deleting an old backup.


#
# :::End Config.:::

# To send commands to a Minecraft server in a Screen
def minecraftCommand(serverCommand):
    subprocess.call(shlex.split("screen -S %s -p 0 -X stuff \"%s\n\"" % (screenName, serverCommand)))
    if showExtraInfo:
        print("Using command:\nscreen -S %s -p 0 -X stuff \"%s\"\n" % (screenName, serverCommand))

# Title
print("CraftyBackupScript v0.5.0")
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
else:
    print("Minecraft mode disabled, continuing...")

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

# Aged file cleanup

# Shows list of found files in directory
if agedFileCleanup:
    if showExtraInfo:
        print("Using path: " + savePath)
        for filename in os.listdir(savePath):
                print("Found file: " + filename)

    # Declaring variables
    fileDeleted = False   
    countOfFilesDeleted = 0

    current_time = time.time()
    for f in os.listdir(savePath):
        file = savePath + f # Combined variable
        creation_time = os.path.getctime(file)
        if (current_time - creation_time) // (24 * 3600) >= keepFileTime:
            if file.endswith('.7z'):
                os.remove(file)
                if showExtraInfo:
                    print('%s removed.' % (file)) # Shows entire path + file name.
                else:
                    print('%s removed.' % (f)) # Only shows file name.
                
                fileDeleted = True
                countOfFilesDeleted = countOfFilesDeleted + 1
                
    if fileDeleted:
        print("%s files cleaned up outside of %s days." % (countOfFilesDeleted, keepFileTime))
    else:
        print("No old files found outside of %s days!" % (keepFileTime))
else:
    print("Aged file cleanup disabled.")
        
        
# Elapsed time for entire process
end = time.time()
elaspedTime = (end - start)
print("Overall backup process took " + str(round(elaspedTime , 1)) + " seconds")



