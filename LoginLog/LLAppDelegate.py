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
        self.logWindowController.showLogWindow_(u"/var/log/system.log")
        self.logWindowController.watchLogFile_(u"/var/log/system.log")
