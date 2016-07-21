#include <stdio.h>
#include <syslog.h>

int main(int argc, char* argv[])
{
    int oldLogMask = 0;
    int newLogMask = 0;

    openlog("SmartConn-Syslog", LOG_PID|LOG_CONS, LOG_USER);
    
    // Log an informational message when logging is enabled for all priorities.
    syslog(LOG_INFO, "This is an informational message.\n");
    
    // Set the log priority mask to LOG_UPTO(LOG_ERR) which is the mask of all priorities 
    // up to and including LOG_ERR. Note that LOG_MASK(LOG_ERR) returns the bit mask 
    // corresponding to LOG_ERR.
    newLogMask = LOG_UPTO(LOG_ERR);
    oldLogMask = setlogmask(newLogMask);
    printf("The old log mask is 0x%08x and the new log mask is 0x%08x\n", oldLogMask, newLogMask);

    // Log an error message which should be seen in the syslog, usually in /var/log/syslog.
    syslog(LOG_ERR, "This is an error message.\n");
    
    // Log a warning message which shouldn't be seen in the syslog, since the current log mask 
    // is up to and including LOG_ERR.
    syslog(LOG_WARNING, "This is a warning message.\n");

    newLogMask = LOG_UPTO(LOG_INFO);
    oldLogMask = setlogmask(newLogMask);
    printf("The old log mask is 0x%08x and the new log mask is 0x%08x\n", oldLogMask, newLogMask);

    // Log a warning message which should be seen in the syslog, since the current log mask has 
    // been changed into up to and including LOG_INFO.
    syslog(LOG_WARNING, "This is a warning message again.\n");

    closelog();

    return 0;
}
