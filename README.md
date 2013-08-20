SublimeText3-ChromeDevTools-integration-toy
===========================================

cobbled together by Ivano Ras (ivano.ras@gmail.com)

This toy plugin performs the automatic refresh of targeted Chrome tab(s) upon pressing Meta-S (or Ctrl-S) in the Sublime Text editor. It's all made up of a couple of very short Python scripts put together last Sunday afternoon just for kicks.

The plugin's workflow is drawn below (MacOS X environment).



              ST3 plugin (part 1)

                      |
                      +--------------------------------+
                      |                                |
                      |                            (OPTIONAL)
               calls (part 2)               sends notification out to
                      |                                |
                      v                                v

               ChromeDevsTools                    GrowlNotify
               Remote Debugger         (could be Apple Notification Center.
                                        I haven't tried that one out yet)



Part 1 is the Python 3.3 script chrometabrefresherplugin.py and part 2 is the standalone Python 2.7 script chrometabrefresherST3.py. Part 2 talks to the Chrome's Remote Debugger. Part 2 could've been fitted into the Part 1 script except that including the references of an external library (websocket-client) inside of a SublimeText plugin could be somehow a bit of a pain as suggested [here](http://www.sublimetext.com/forum/viewtopic.php?f=2&t=5835).
An automatic notification to Growl has also been kept (debugging purposes mainly) but can be easily commented out.

Once all works fine, an extra instance of the Chrome app (more precisely the Chrome Remote Debugger) gets created and that also brings up the desired web page. Such extra Chrome instance doesn't seem to affect the main Chrome app instance that can be called by clicking on the Chrome dock's icon as usual.

Dependencies :

i.  [websocket-client 0.11](https://pypi.python.org/pypi/websocket-client/) (Python 2.7)

ii. [GrowlNotify 2.0](http://growl.info/downloads) (MacOSX app) (OPTIONAL)

Scripts locations :

i.  The 1st-part script chrometabrefresherplugin.py needs to be dropped into ~/Library/Application Support/Sublime Text 3/Packages/User/ The 2nd-part script can be placed anywhere you want. I put it on the Desktop. 

ii. The filename of the local html page you want to be automatically refreshed needs to be amended at the bottom of the other script chrometabrefresherST3.py

Basic know-how (thanks guys!) : [i.](https://github.com/flxfxp/My-Stuff/blob/master/Sublime%20Text%202/Plugins/growlnotifier.py) and [ii.](http://stackoverflow.com/questions/11344414/windows-chrome-refresh-tab-0or-current-tab-via-command-line)

Optional know-how for developing the plugin further : [i.](http://www.macdrifter.com/2012/08/making-a-sublime-text-plugin-markdown-reference-viewer.html)  [ii.](http://net.tutsplus.com/tutorials/python-tutorials/how-to-create-a-sublime-text-2-plugin/)
 and  [iii.] (http://sublimetext.info/docs/en/extensibility/plugins.html)

(*) Notice that SublimeText3 now uses Python 3.3 (ST2 used to use Python 2.6 instead)

This plugin has been tested on MacOSX 10.8 successfully.


Notes:
------

i. Multiple Chrome Tabs can be refreshed at once just by adding amended copies of the last line at the bottom of the script chrometabrefresherST3.py.

ii. By enabling the SSH tunnelling, you can code on your laptop and test the result out on another machine just by pressing Meta-S (Ctrl-S) on your machine. Check the following [link](https://coderwall.com/p/kmoe2a) out on how to enable ssh tunnelling.

iii. I'm quite sure there must be a more optimised way to achieve the same cross-app communication. Anyway, this one was good fun :-)


Known Issues:
-------------

Very rarely the communication between the 2nd script and Chrome Remote Debugger gets probably lost. If you've got the doubt that has just happened, please shut down the Chrome Remote Debugger app and then save again from Sublime Text, that should bring the Chrome Remote Debugger back on. I will add a callback informing the user of loss of communication at some point unless someone else wishes to do so by forking the repo.

Thanks to @ronanklyne for further advice on reducing the plugin's configuration to a minimum.
