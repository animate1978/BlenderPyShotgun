# PROJECT WIDOW Shotgun / Blender Python API Experiments
# ---------------------------------------------------------------------------------------------
# Widow Version Thumb Uploader (WidVerTU 0.1)
# ---------------------------------------------------------------------------------------------
#	This script will upload a render saved to disk from within Blender, into
#	a Version on a Shotgun server. While the script needs much work to
#	be a bit more useful, the principle working prototype works.
# ---------------------------------------------------------------------------------------------

# ---------------------------------------------------------------------------------------------
# Imports
# ---------------------------------------------------------------------------------------------

import os
import sys
import urllib
from shotgun_api3 import Shotgun # Shotgun API 3
from pprint import pprint # useful for debugging

# ---------------------------------------------------------------------------------------------
# Globals
# ---------------------------------------------------------------------------------------------

DEFAULT_SHOTGUN_API = "/usr/share/pyshared/shotgun_api3.py" # Place this in your Pyshared directory
SERVER_PATH = "https://yourshotgunsite.shotgunstudio.com"
SCRIPT_NAME = "test_001"
SCRIPT_KEY = 'shotgungeneratedkeynumber' # Script key number

# ---------------------------------------------------------------------------------------------
# Project Id's
# ---------------------------------------------------------------------------------------------

# Project Widow ID
PROJECT = {'type':'Project', 'id':64}

# ---------------------------------------------------------------------------------------------
# Main 
# ---------------------------------------------------------------------------------------------

sg = Shotgun(SERVER_PATH, SCRIPT_NAME, SCRIPT_KEY)
print "\n\nUploading thumbnail to "+SERVER_PATH+"\n\n"

if __name__ == '__main__':

	version_id = 23 # Version ID

	thumbnail = '/home/user/Renders/testing.jpg' # Replace this 
	result = sg.upload_thumbnail("Version",version_id,thumbnail) # magic happens.
	print result

print ""+SCRIPT_NAME+"...complete!\n"