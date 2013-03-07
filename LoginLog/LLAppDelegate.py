#-*- coding: utf-8 -*-
#
#  LoginLogAppDelegate.py
#  LoginLog
#
#  Created by Pelle on 2013-03-05.
#  Copyright Göteborgs universitet 2013. All rights reserved.
#

from objc import IBOutlet
from Foundation import *
from AppKit import *


class LLAppDelegate(NSObject):
    
    logWindowController = IBOutlet()
    
    def applicationDidFinishLaunching_(self, sender):
        logfile = self.getPref_default_(u"logfile", u"/var/log/system.log")
        self.logWindowController.showLogWindow_(logfile)
        self.logWindowController.watchLogFile_(logfile)
    
    def getPref_default_(self, prefName, defaultValue):
        bundleID = NSBundle.mainBundle().bundleIdentifier()
        value = CFPreferencesCopyAppValue(prefName, bundleID)
        return defaultValue if value is None else value
    
