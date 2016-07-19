#!/usr/bin/env python
# -*- coding: utf-8 -*-

# For detailed info about syslog, please refer to https://docs.python.org/2/library/syslog.html.
import syslog

def main():
    # (1) ident, i.e., identity: the name of the program which will write the logging messages to syslog and will be 
    # prepended to every message. It defaults to sys.argv[0] with leading path components stripped if not set.
    # (2) logoption: options for opening the connection or writing messages which can be an OR of multiple options, 
    # e.g., LOG_PID -- include PID with each message; 
    #       LOG_CONS -- write directly to system console if there is an error while sending to system logger.
    # (3) facility: specify what type of program is logging the message. For user applications, it should be the 
    # default value -- LOG_USER.
    # For a complete list of logoption and facility values, please refer to syslog help via "man 3 syslog".
    syslog.openlog(ident = 'Program-Name', logoption = syslog.LOG_PID|syslog.LOG_CONS, facility = syslog.LOG_USER)
    syslog.syslog(syslog.LOG_INFO, "This is an informational message.")

    # By default, syslog logs messages of all priorities. The return value of syslog.setlogmask is the old value 
    # of the log mask which is the default value 0xff here. The new value of the log mask is 
    # syslog.LOG_UPTO(syslog.LOG_ERR) = 0x0f.
    oldLogMask = syslog.setlogmask(syslog.LOG_UPTO(syslog.LOG_ERR))
    print "The old priority mask is 0x%x and the new priority mask is 0x%x." \
          % (oldLogMask, syslog.LOG_UPTO(syslog.LOG_ERR))
    
    # Since the priority mask is "up to" LOG_ERR, we should see the error message in /var/log/syslog but not the 
    # warning message.
    syslog.syslog(syslog.LOG_WARNING, "This is a warning message.")
    syslog.syslog(syslog.LOG_ERR, "This is an error message.")
    
    # Reset the syslog module values (e.g., ident, logoption, facility, logmask) and call the system library closelog().
    syslog.closelog()
 
# This is the standard boilerplate that calls the main() function.
if __name__ == '__main__':
    main()
