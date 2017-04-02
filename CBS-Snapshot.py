"""
CraftyBackupSnapshot v1
colebob9

To organize the latest versions of all archives into one place.
"""

import time
import os, os.path
import shutil

print("CraftyBackupSnapshot v1")

# Config
showExtraInfo = True

datetime = time.strftime("%m-%d-%Y--%I:%M%p")

snapshotPath = "Snapshots/" + datetime + "/"
# End Config

currentDirPath = os.path.dirname(os.path.realpath(__file__))

if not os.path.exists("Snapshots"):
    os.mkdir("Snapshots")
    print("Auto-created Snapshots directory.")
os.mkdir("Snapshots/%s" % datetime)
    
def snapshot(savePath):
    # Shows list of found files in directory
    if showExtraInfo:
        print("Using path: " + savePath)
        for filename in os.listdir(savePath):
                print("Found file: " + filename)
    
    # Figure out what file is the newest
    os.chdir(savePath)
    newest = max([x for x in os.listdir() if x.endswith(".7z")], key = os.path.getctime)
    os.chdir(currentDirPath)
    
    print("Newest in directory: " + newest)
    
    archiveFile = savePath + newest
    snapshotFile = snapshotPath + newest

    print("Copying file from: " + archiveFile + " to: " + snapshotFile)
    shutil.copy(archiveFile, snapshotFile)
       
    print("Done copying backup archives.")

snapshot("Archives/Bungee/") # BungeeCord Server
snapshot("Archives/Creative/") # Creative Server
