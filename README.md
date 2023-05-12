# cms-sync
A Python3 script to sync folders with Cascade CMS.  This program will scan the contents of the current directory with a .cms config folder and sync files with a Cascade CMS server via Cascade's REST API.  Designed for those locations where login access to a web server is not available.  Tested on Ubuntu Linux, other operating systems may work as long as you have the required python libraries.

# Installation Instructions
The code below will clone the repository into your home directory.

`cd
git clone https://github.com/jskenney/cms-sync.git
cd cms-sync
chmod 755 cmssync`

# Configuration
Once you have the repository cloned, the next step is to go into the folder you want to sync with the CMS server and create a .cms/config.py file and define the required entries, there is an example in the repository that can be copied and taylored as needed.

# Performing the sync
Go into the folder that has the .cms directory and run:
`~/cms-sync/cmssync`
