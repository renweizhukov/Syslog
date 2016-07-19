#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Logging tutorial: https://docs.python.org/2/howto/logging.html#logging-basic-tutorial
# SysLogHandler help info: https://docs.python.org/2/library/logging.handlers.html#logging.handlers.SysLogHandler
import logging
from logging.handlers import SysLogHandler

moduleName = 'Module-Name'

def main():
    # Create a logger which is named after the module. This logger name is used as the unique identifier of logger 
    # instances, so multiple calls to getLogger() with the same name will return a reference to the same logger object.
    mylogger = logging.getLogger(moduleName)
    # Set the lowest-severity log message a logger will handle.
    mylogger.setLevel(logging.INFO)

    # Create a logging handler where the address is set to '/dev/log', i.e., the messages will be written into the 
    # syslog file /var/log/syslog. Note that in general the address can be set to a remote UNIX machine which is 
    # given in the form of a (host, port) tuple.
    myhandler = SysLogHandler(address = '/dev/log')

    # Set the format of the logging messages.
    # (1) levelname: the priority/severity name, e.g., INFO, ERROR.
    # (2) name: the logger name which is the modulename here.
    # (3) process: process ID.
    # (4) message: the actual logging message passed in the logging function, e.g., logcanger.warning(), logger.error().
    myformatter = logging.Formatter('%(levelname)s %(name)s[%(process)d]: %(message)s')
    myhandler.setFormatter(myformatter)
    
    # Add the specified syslog handler to the logger.
    mylogger.addHandler(myhandler)

    # The current severity level is INFO, so we should see this message in syslog.
    mylogger.info("This is a informational message.")

    # Change the severity level from INFO into ERROR.
    mylogger.setLevel(logging.ERROR)

    # We should see the error message in syslog but not the warning message.
    mylogger.warning("This is a warning message.")
    mylogger.error("This is an error message.")

# This is the standard boilerplate that calls the main() function.
if __name__ == '__main__':
    main()
