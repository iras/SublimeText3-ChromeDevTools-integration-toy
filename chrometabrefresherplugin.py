"""
-----------------------------------------------------------------------------
    SublimeText 3 Google Chrome's Tab refresher scripted plugin - 1st part
-----------------------------------------------------------------------------

by Ivano Ras (ivano.ras@gmail.com)

MIT License

"""

import sublime, sublime_plugin
import subprocess, os


# Python 3.3 class
class ChromeTabRefresher (sublime_plugin.EventListener):

	def displayNotification (self, msg):
		cmd = '/usr/local/bin/growlnotify -a "Sublime Text 3" -t "Chrome Tab Refreshing" -m "'+msg+'"'
		subprocess.call (cmd, shell=True)

	def delegateChromeTabRefresh (self):
		cmd = 'python ~/Desktop/system_scripts/chrometabrefresherST3.py'
		subprocess.call (cmd, shell=True)
	
	def on_post_save (self, view):
		# you can shut up this visual notification by commenting out the 2 lines below.
		#filename = os.path.basename (view.file_name())
		#self.displayNotification (filename)

		# this is the bit that calls the external standalone script which handles the Chrome's remote debugging functionality.
		self.delegateChromeTabRefresh ()
