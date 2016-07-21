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

## More about syslog.

### Watch live syslog in a terminal.

```bash
$ tail -f /var/log/syslog
```

Here we assume that syslog is written into the log file /var/log/syslog.

### Redirect the syslog messages to an unused tty session.

Take Ubuntu 14.04 LTS as an example where tty12 is selected as the unused tty session.

1. Grant the access for /dev/tty12 to the syslog user.

    (1) Add the syslog user to the owner group tty of /dev/tty12.

    ```bash
    $ sudo gpasswd --add syslog tty
    ```

	(2) Grant the read and write access of /dev/tty12 to the group tty.

	```bash
	$ sudo chmod g+rw /dev/tty12
	```

    (3) Kill all processes owned by the syslog user.
    
    ```bash
    $ sudo pkill -KILL -u syslog
    ```

    (4) Verify that the syslog user has been added to the group tty.

    ```bash
    $ groups syslog
    ```

2. Configure the syslog service to write the logging messages with the facility "user" to /dev/tty12.

    ```bash
    $ sudo vi /etc/rsyslog.d/50-default.conf
    ```

    Add the following line at the bottom of the conf file.

    ```
    user.*	|/dev/tty12
    ```

    The above "user" can be replaced by another facility or "*" (to match all facilities).

    Then restart the syslog service to make effective the configuration change.

    ```bash
	$ sudo service rsyslog restart
    ```
    
	Note that the syslog service on Ubuntu is named as "rsyslog".

3. After running the C/Python exectuable, you can switch to the tty12 session either via "Ctrl + Alt + F12" or the command 
	
```bash
$ sudo chvt 12
```

, and you should be able to view the syslog messages with the facility "user" there.

If somehow the tty12 session hangs, you can switch back to the X session (i.e., the normal desktop), find the tty12 process, and kill it.

```bash
$ sudo fuser /dev/tty12
$ sudo kill [process-ID]
```

