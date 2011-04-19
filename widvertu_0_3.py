#!BPY

""" Registration info for Blender menus:
Name: 'WidVerTU 0.3'
Blender: 249
Group: 'System'
Tooltip: 'Sends a thumbnail render to a Shotgun server'
"""

# --------------------------------------------------------------------------
# ***** BEGIN GPL LICENSE BLOCK *****
#
# Copyright (C) 2009 - ??
#
# This program is free software; you can redistribute it and/or
# modify it under the terms of the GNU General Public License
# as published by the Free Software Foundation; either version 2
# of the License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software Foundation,
# Inc., 59 Temple Place - Suite 330, Boston, MA  02111-1307, USA.
#
# ***** END GPL LICENCE BLOCK *****
# --------------------------------------------------------------------------
# 
#
# 
# 
__author__ = "Ted Gocek"
__url__ = ("")
__version__ = "0.3"

__bpydoc__ = """\
Uploads a rendered image to a Shotgun server Version database entry.
Usefull for sending thumbnails to Shotgun automatically without
having to log into the server and manually change it.
"""
# PROJECT WIDOW Shotgun / Blender Python API Experiments
# ---------------------------------------------------------------------------------------------
# Widow Version Thumb Uploader
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
import Blender
from Blender import Draw, BGL, Window
from Blender.BGL import *


# ---------------------------------------------------------------------------------------------
# System Globals
# ---------------------------------------------------------------------------------------------

DEFAULT_SHOTGUN_API = "/usr/share/pyshared/shotgun_api3.py" # Place this in your Pyshared directory
VERSION = '0.3'

# ---------------------------------------------------------------------------------------------
# Shotgun Production Globals
# ---------------------------------------------------------------------------------------------

SERVER_PATH = "https://yourshotgunsite.shotgunstudio.com"
SCRIPT_NAME = "test_001"
SCRIPT_KEY = 'shotgungeneratedkeynumber' # Script key number

# ---------------------------------------------------------------------------------------------
# Shotgun Testing Globals
# ---------------------------------------------------------------------------------------------

#SERVER_PATH = "https://yourshotgunsite.shotgunstudio.com"
#SCRIPT_NAME = "test_001"
#SCRIPT_KEY = 'shotgungeneratedkeynumber' # Script key number

# ---------------------------------------------------------------------------------------------
# Shotgun Project Id's
# ---------------------------------------------------------------------------------------------

# Project Widow ID
PROJECT = {'type':'Project', 'id':64}


# ---------------------------------------------------------------------------------------------
# Blender GUI
# ---------------------------------------------------------------------------------------------

EVENT_Button = 10
EVENT_Type = 11
EVENT_shtoguntype = 12
EVENT_String = 13
EVENT_Bitmap = 14
EVENT_WVTU_1 = 15
Object_Button = Draw.Create(0.0)
Object_Type = Draw.Create("")
Object_shtoguntype = Draw.Create(0.0)
Object_String = Draw.Create("0")
Object_Bitmap = BGL.Buffer(GL_BYTE, (0, 0, 3))
Object_WVTU_1 = Draw.Create("")

# ---------------------------------------------------------------------------------------------
# Main 
# ---------------------------------------------------------------------------------------------

def draw():     # Define the draw function (which draws your GUI).
	global EVENT_Button
	global EVENT_Type
	global EVENT_shtoguntype
	global EVENT_String
	global EVENT_Bitmap
	global EVENT_WVTU_1
	global Object_Button
	global Object_Type
	global Object_shtoguntype
	global Object_String
	global Object_Bitmap
	global Object_WVTU_1

	BGL.glClearColor(0.244564, 0.244406, 0.244406, 0.0)
	BGL.glClear(GL_COLOR_BUFFER_BIT)

	BGL.glColor3f(1.000000, 1.000000, 1.000000)
	Object_Button = Draw.Button("Connect to Shotgun", EVENT_Button, 20, 8, 200, 20, "")
	BGL.glRasterPos2i(100, 108)
	Object_Type = Draw.Text("Type")
	Object_shtoguntype = Draw.Menu("Asset", EVENT_shtoguntype, 20, 100, 60, 20, Object_shtoguntype.val, "Type of Shotgun entry")
	Object_String = Draw.String("id : ", EVENT_String, 20, 60, 60, 20,Object_String.val, 399, "ID # for the Shotgun entry")
	BGL.glRasterPos2i(24, 210)
	BGL.glDrawPixels(0, 0, GL_RGB, GL_UNSIGNED_BYTE, Object_Bitmap)
	BGL.glRasterPos2i(24, 152)
	Object_WVTU_1 = Draw.Text("WVTU "+VERSION+"")

def event(event, value):
	_Input_Events_Callback(event, value)

def b_event(event):
	global EVENT_Button
	global EVENT_Type
	global EVENT_shtoguntype
	global EVENT_String
	global EVENT_Bitmap
	global EVENT_WVTU_1
	global Object_Button
	global Object_Type
	global Object_shtoguntype
	global Object_String
	global Object_Bitmap
	global Object_WVTU_1

	if event == 0: pass
	elif event == EVENT_Button:
		Button_Callback()
	elif event == EVENT_Type:
		Type_Callback()
	elif event == EVENT_shtoguntype:
		shtoguntype_Callback()
	elif event == EVENT_String:
		String_Callback()
	elif event == EVENT_Bitmap:
		Bitmap_Callback()
	elif event == EVENT_WVTU_1:
		WVTU_1_Callback()
	Draw.Draw()

Draw.Register(draw, event, b_event)

def Button_Callback():
	print ""+SCRIPT_NAME+" "+VERSION+"\n"
	print "Connecting to %s..." % (SERVER_PATH),

	sg = Shotgun(SERVER_PATH, SCRIPT_NAME, SCRIPT_KEY)
	print "\n\nConnected\n\n"
		
		
		
# ---------------------------------------------------------------------------------------------
# Testing Block BEGIN
# ---------------------------------------------------------------------------------------------

	result = sg.schema_entity_read()
	pprint(result)

	print ""+SERVER_PATH+"\n ... completed\n"
		
	pass

# ---------------------------------------------------------------------------------------------
# Testing Block END
# ---------------------------------------------------------------------------------------------


def _Input_Events_Callback(Event, Value):
	if Event == Draw.ESCKEY and not Value: Draw.Exit()


def Type_Callback():
	#***Place your code for Object Type here***#
	pass

def shtoguntype_Callback():
	#***Place your code for Object shtoguntype here***#
	pass

def String_Callback():
	#***Place your code for Object String here***#
	pass

def Bitmap_Callback():
	#***Place your code for Object Bitmap here***#
	pass

def WVTU_1_Callback():
	#***Place your code for Object WVTU_1 here***#
	pass
