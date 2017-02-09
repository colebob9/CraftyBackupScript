# CraftyBackupScript
Script to automatically backup any folder, easily and efficiently. Has special features for Minecraft Servers in mind.

## Download

Simply download a .zip file [from the main repo page](https://github.com/colebob9/CraftyBackupScript/archive/master.zip) or download a more stable release [from the Releases Page. (preferred)](https://github.com/colebob9/CraftyBackupScript/releases)

## Features
* Compresses entire folder into a 7zip archive, and puts the archive into the specified folder
* Proper Minecraft save toggling (optional)
* Optional Minecraft server stopping after backup (best for non-peak hours, to be used with [CraftyStartScript](https://github.com/colebob9/CraftyStartScript) for a restart)
* Keeps track of how long a backup can take
* Configuration options to tweak the script to your liking (config options inside script)
* Labels archive with date and time

## Instructions
Edit the "Config" section inside the script for the server you want to backup. (Completely separate scripts are needed for each different server)

The required sections you need to edit for the script to work are `screenName`, `serverPath`, `filePath`, and the prefix of `archiveName`. Everything else is up to personal preference.

This script is designed to be ran manually or by a [cron job](http://www.howtogeek.com/101288/how-to-schedule-tasks-on-linux-an-introduction-to-crontab-files/). Configure as needed.

Run with command `python3 CBS-Backup.py`


## Requirements
* Python 3 (to run the script)
* Any plain text editor: Notepad, Notepad++, TextEdit, or nano will do fine.
* Linux packages: `p7zip`, `p7zip-full`, `python3`, `screen`

## Notes
[Released under the MIT license.](https://github.com/colebob9/CraftyBackupScript/blob/master/LICENSE) 

Please [report any issues](https://github.com/colebob9/CraftyBackupScript/issues) my program may have. [Pull requests](https://github.com/colebob9/CraftyBackupScript/pulls) are welcome too!


Tested with Debian 8 minimal and Ubuntu 14.04 Server. This script was written with only Linux in mind, so any other OS will not be supported. 
