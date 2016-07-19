# Syslog

C and Python Syslog samples.

## C

Use Unix syslog APIs to log various levels of messages. 

### Build

To build the executable syslogexample, 

```bash
# Generate configure and Makefile.in.
$ aclocal
$ autoconf
$ automake --add-missing

# Build the program syslog_example.c.
$ ./configure
$ make
```

### Run 

After running the executable, you should see the following output in console,

```bash
The old log mask is 0x000000ff and the new log mask is 0x0000000f
The old log mask is 0x0000000f and the new log mask is 0x0000007f
```

and the following messages in the syslog which in Ubuntu is the file /var/log/syslog.

```
Jul 18 18:52:09 renwei-ubuntu SmartConn-Syslog[21940]: This is an informational message.
Jul 18 18:52:09 renwei-ubuntu SmartConn-Syslog[21940]: This is an error message.
Jul 18 18:52:09 renwei-ubuntu SmartConn-Syslog[21940]: This is a warning message again.
```

### Help info

1. For detailed info about syslog APIs openlog, syslog, and closelog, please refer to "man 3 syslog". 

2. For detailed info about setlogmask, please refer to "man 3 setlogmask".

## Python

Use the syslog and logger+SysLogHandler modules to log various levels of messages.

### syslog

After running syslogExample.py, you should see the following output in console,

```bash
The old priority mask is 0xff and the new priority mask is 0xf.
```

and the following messages in the syslog which in Ubuntu is the file /var/log/syslog.

```
Jul 18 20:05:12 renwei-ubuntu Program-Name[22188]: This is an informational message.
Jul 18 20:05:12 renwei-ubuntu Program-Name[22188]: This is an error message.
```

### logger+SysLogHandler

After running syslogHandlerExample.py, you should see the following messages in the syslog which in Ubuntu is the file /var/log/syslog.

```
Jul 18 20:05:42 renwei-ubuntu INFO Module-Name[22196]: This is a informational message.
Jul 18 20:05:42 renwei-ubuntu ERROR Module-Name[22196]: This is an error message.
```

### syslog vs. logger+SysLogHandler

1. syslog is more straight-forward to use than logger+SysLogHandler.

2. In general, logger+SysLogHandler modules are more powerful than syslog, since they can log the 
messages to a remote UNIX machine.

3. logger+SysLogHandler can customize the format of the logging messages but syslog can't.
