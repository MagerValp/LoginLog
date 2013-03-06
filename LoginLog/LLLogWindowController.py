#-*- coding: utf-8 -*-
#
#  LLLogWindowController.py
#  LoginLog
#
#  Created by Pelle on 2013-03-05.
#  Copyright (c) 2013 Göteborgs universitet. All rights reserved.
#

from objc import YES, NO, IBAction, IBOutlet
from Foundation import *
from AppKit import *


class LLLogViewDataSource(NSObject):
    
    logFileData = NSMutableArray.alloc().init()
    lastLineIsPartial = False
    
    def addLine_partial_(self, line, isPartial):
        if self.lastLineIsPartial:
            joinedLine = self.logFileData.lastObject() + line
            self.logFileData.removeLastObject()
            self.logFileData.addObject_(joinedLine)
        else:
            self.logFileData.addObject_(line)
        self.lastLineIsPartial = isPartial
    
    def removeAllLines(self):
        self.logFileData.removeAllObjects()
    
    def lineCount(self):
        return self.logFileData.count()
    
    def numberOfRowsInTableView_(self, tableView):
        return self.lineCount()
    
    def tableView_objectValueForTableColumn_row_(self, tableView, column, row):
        return self.logFileData.objectAtIndex_(row)
    

class LLLogWindowController(NSObject):
    
    window = IBOutlet()
    logView = IBOutlet()
    backdropWindow = IBOutlet()
    logFileData = LLLogViewDataSource.alloc().init()
    fileHandle = None
    updateTimer = None
    
    def showLogWindow(self):
        self.window.setCanBecomeVisibleWithoutLogin_(True)
        self.window.setLevel_(NSScreenSaverWindowLevel - 1)
        self.window.center()
        self.window.setOpaque_(False)
        self.window.setAlphaValue_(0.0)
        self.window.orderFrontRegardless()
        NSAnimationContext.beginGrouping()
        NSAnimationContext.currentContext().setDuration_(0.5)
        self.window.animator().setAlphaValue_(1.0)
        NSAnimationContext.endGrouping()
        
        self.backdropWindow.setCanBecomeVisibleWithoutLogin_(True)
        self.backdropWindow.setLevel_(NSStatusWindowLevel)
        screenRect = NSScreen.mainScreen().frame()
        self.backdropWindow.setFrame_display_(screenRect, True)
        translucentColor = NSColor.blackColor().colorWithAlphaComponent_(0.75)
        self.backdropWindow.setBackgroundColor_(translucentColor)
        self.backdropWindow.setOpaque_(False)
        self.backdropWindow.setIgnoresMouseEvents_(False)
        self.backdropWindow.setAlphaValue_(0.0)
        self.backdropWindow.orderFrontRegardless()
        NSAnimationContext.beginGrouping()
        NSAnimationContext.currentContext().setDuration_(2.0)
        self.backdropWindow.animator().setAlphaValue_(1.0)
        NSAnimationContext.endGrouping()
    
    def watchLogFile_(self, logFile):
        self.stopWatching()
        self.logFileData.removeAllLines()
        self.logView.setDataSource_(self.logFileData)
        self.logView.reloadData()
        self.fileHandle = NSFileHandle.fileHandleForReadingAtPath_(logFile)
        self.refreshLog()
        self.updateTimer = NSTimer.scheduledTimerWithTimeInterval_target_selector_userInfo_repeats_(
            0.25,
            self,
            u"refreshLog",
            None,
            YES
        )
    
    def stopWatching(self):
        if self.fileHandle is not None:
            self.fileHandle.closeFile()
            self.fileHandle = None
        if self.updateTimer is not None:
            self.updateTimer.invalidate()
            self.updateTimer = None
    
    def refreshLog(self):
        data = self.fileHandle.availableData()
        if data.length():
            utf8string = NSString.alloc().initWithData_encoding_(
                data,
                NSUTF8StringEncoding
            )
            for line in utf8string.splitlines(True):
                if line.endswith(u"\n"):
                    self.logFileData.addLine_partial_(line.rstrip(u"\n"), False)
                else:
                    self.logFileData.addLine_partial_(line, True)
            self.logView.reloadData()
            self.logView.scrollRowToVisible_(self.logFileData.lineCount() - 1)
    
