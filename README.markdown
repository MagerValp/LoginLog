LoginLog
========

Dim the login window and display a log file of your choice over it.

![loginlog](https://cloud.githubusercontent.com/assets/404393/2719374/b909345e-c55f-11e3-8c2e-7399f8e2b9a2.png)

How to use it
-------------

* Build LoginLog.app.
* Copy it to a test machine as /Library/PrivilegedHelperTools/LoginLog.app
* Configure the logfile argument in se.gu.it.LoginLog.plist and copy it to /Library/LaunchAgents on the test machine.
* launchctl load -S loginwindow /Library/LaunchAgents/se.gu.it.LoginLog.plist
* launchctl unload -S loginwindow /Library/LaunchAgents/se.gu.it.LoginLog.plist


Credits
-------

* Code by Per Olofsson, <per.olofsson@gu.se>
* Code to display a backdrop over the login window borrowed from Munki by Greg Neagle


License
-------

    Copyright 2013 Per Olofsson, University of Gothenburg
    
    Licensed under the Apache License, Version 2.0 (the "License");
    you may not use this file except in compliance with the License.
    You may obtain a copy of the License at
    
        http://www.apache.org/licenses/LICENSE-2.0
    
    Unless required by applicable law or agreed to in writing, software
    distributed under the License is distributed on an "AS IS" BASIS,
    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
    See the License for the specific language governing permissions and
    limitations under the License.
