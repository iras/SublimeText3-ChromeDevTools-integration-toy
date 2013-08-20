"""
----------------------------------------------------------------------------------------
    SublimeText 3 Google Chrome's Tab refresher scripted plugin - part 2 - standalone
----------------------------------------------------------------------------------------

script adapted from here (many thanks!) : http://stackoverflow.com/questions/11344414/windows-chrome-refresh-tab-0or-current-tab-via-command-line
by Ivano Ras (ivano.ras@gmail.com)

The filename of the local html page you want to be refreshed needs to be amended
at the bottom of the this script.

Python 2.7 standalone script.

MIT License

"""

import subprocess, os
import urllib2, urllib, json

from websocket import create_connection


# Python 2.7 functions
def refreshTab(url):
    data = json.load(urllib2.urlopen('http://localhost:9222/json'))

    found_tab = False
    for tab in data:
        
        if tab['url'].lower() == url.lower():

            found_tab = True
            websocketURL = tab['webSocketDebuggerUrl']
            ws = create_connection(websocketURL)

            obj = {"id": 0,
                   "method": "Page.reload",
                   "params":
                     {
                       "ignoreCache": True,
                       "scriptToEvaluateOnLoad": ""
                     }
                  }

            dev_request = json.dumps(obj)
            ws.send(dev_request)
            result =  ws.recv()
            ws.close()
    if not found_tab:
        raise Exception(" - tab not found -")

def openOrRefresh(file_name):

    file_name = os.path.expanduser (file_name)
    file_name = "".join ([f if f in r'\/:*?"<>|' else  urllib.quote(f) for f in file_name])
    file_name = 'file://' + file_name.replace ('\\', '/')
    file_name = file_name.encode ('ascii', 'ignore')
    try:
        refreshTab (file_name)
    except:

        # MacOS X version
        try:
            cmd = (r'/Applications/Google\ Chrome.app/Contents/MacOS/Google\ Chrome'%os.environ
              + r' --remote-debugging-port=9222  --profile-directory=Default --user-data-dir=/tmp/ %s'
              % file_name)
            
            subprocess.Popen (cmd, shell=True)
        except OSError as e:
            print '--> Error ' + str(e.errno) + ' ' + str(e.filename) + ' ' + str(e.strerror)



openOrRefresh (r"~/Desktop/js_tests/test03.html")
