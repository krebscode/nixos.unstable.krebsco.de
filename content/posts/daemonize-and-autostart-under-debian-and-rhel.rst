Daemonize and Autostart under Debian and RHEL
#############################################

:date: 2012-04-05 11:57
:tags: debian,redhat,autostart

Daemonizing and autostarting a process is still a pain in the ass, so
here are two scripts which can be placed under /etc/init.d and if you
are lucky everything will work. 


Example is the punani backend, an universal package resolver and installer
which is essentially a python webserver (now obsolete).

debian init-script
==================

.. code-block:: bash

    #! /bin/sh
    # uses template from /etc/init.d/skeleton
    ### BEGIN INIT INFO
    # Provides:          punani
    # Required-Start:    
    # Required-Stop:     
    # Default-Start:     2 3 4 5
    # Default-Stop:      0 1 6
    # Short-Description: punani
    # Description:       starts punani daemon
    #                    
    ### END INIT INFO
    
    PATH=/sbin:/usr/sbin:/bin:/usr/bin
    NAME=punani
    DESC="$NAME daemon"
    DAEMON=/usr/bin/python
    DAEMON_ARGS="/krebs/punani/index.py"
    PIDFILE=/var/run/$NAME.pid
    SCRIPTNAME=/etc/init.d/$NAME
    
    [ -x "$DAEMON" ] || exit 0
    [ -r /etc/default/$NAME ] && . /etc/default/$NAME
    . /lib/init/vars.sh
    . /lib/lsb/init-functions
    
    do_start()
    {
      #   0 if daemon has been started
      #   1 if daemon was already running
      #   2 if daemon could not be started
      start-stop-daemon -b --start --quiet --make-pidfile --pidfile $PIDFILE --exec $DAEMON --test > /dev/null \
              || return 1
      start-stop-daemon -b --start --quiet --make-pidfile --pidfile $PIDFILE --exec $DAEMON -- \
          $DAEMON_ARGS \
          || return 2
    }
    
    do_stop()
    {
      #   0 if daemon has been stopped
      #   1 if daemon was already stopped
      #   2 if daemon could not be stopped
      start-stop-daemon --stop --retry=TERM/30/KILL/5 --pidfile $PIDFILE
      RETVAL="$?"
      [ "$RETVAL" = 2 ] && return 2
      rm -f $PIDFILE
      return "$RETVAL"
    }
    
    do_reload() {
      start-stop-daemon --stop --signal 1 --quiet --pidfile $PIDFILE
      return 0
    }
    
    case "$1" in
      start)
      [ "$VERBOSE" != no ] && log_daemon_msg "Starting $DESC" "$NAME"
      do_start
      case "$?" in
          0|1) [ "$VERBOSE" != no ] && log_end_msg 0 ;;
          2) [ "$VERBOSE" != no ] && log_end_msg 1 ;;
      esac
      ;;
      stop)
      [ "$VERBOSE" != no ] && log_daemon_msg "Stopping $DESC" "$NAME"
      do_stop
      case "$?" in
          0|1) [ "$VERBOSE" != no ] && log_end_msg 0 ;;
          2) [ "$VERBOSE" != no ] && log_end_msg 1 ;;
      esac
      ;;
      status)
           status_of_proc "$DAEMON" "$NAME" && exit 0 || exit $?
           ;;
      restart|force-reload)
      log_daemon_msg "Restarting $DESC" "$NAME"
      do_stop
      case "$?" in
        0|1)
          do_start
          case "$?" in
              0) log_end_msg 0 ;;
              1) log_end_msg 1 ;;
              *) log_end_msg 1 ;;
          esac
          ;;
        *)
          # Failed to stop
          log_end_msg 1
          ;;
      esac
      ;;
      *)
      echo "Usage: $SCRIPTNAME {start|stop|status|restart|force-reload}" >&2
      exit 3
      ;;
    esac
    
    :

    
register the script
-------------------

.. code-block:: bash

    update-rc.d punani defaults
    service punani start

RHEL Init Script
================
    
.. code-block:: bash

    #!/bin/bash
    # `forked` (read stolen) from http://bitten.edgewall.org/wiki/BittenSlaveDaemonRedhat
    # 
    # processname:       punani
    # config:            /krebs/punani/config.json
    # pidfile:           /var/run/punani.pid
    # chkconfig: 2345 99 01
    # description:       punani daemon
    
    # Source function library.
    . /etc/rc.d/init.d/functions
    
    PATH=/sbin:/usr/sbin:/bin:/usr/bin
    DESC="punani daemon"
    NAME=punani
    DAEMON=/usr/bin/python
    DAEMON_ARGS="/krebs/punani/index.py"
    DAEMON_USER=nobody
    PIDFILE=/var/run/$NAME.pid
    
    [ -x "$DAEMON" ] || exit 0
    
    [ -r /etc/sysconfig/$NAME ] && . /etc/sysconfig/$NAME
    
    start() {
            echo -n $"Starting $NAME: "
            daemon --user="$DAEMON_USER" --pidfile="$PIDFILE" "$DAEMON $DAEMON_ARGS &" # daemonize here
            RETVAL=$?
            pid=`ps -A | grep $NAME | cut -d" " -f2`
            pid=`echo $pid | cut -d" " -f2`
            if [ -n "$pid" ]; then
                    echo $pid > "$PIDFILE"
            fi
            echo
            return $RETVAL
    }
    stop() {
            echo -n $"Stopping $NAME: "
            killproc -p "$PIDFILE" -d 10 "$DAEMON"
            RETVAL="$?"
            echo
            [ $RETVAL = 0 ] && rm -f "$PIDFILE"
            return "$RETVAL"
    }
    
    case "$1" in
      start)
            start
            ;;
      stop)
            stop
            ;;
      restart)
            stop
            start
            ;;
      *)
            echo "Usage: $NAME {start|stop|restart}" >&2
            exit 1
            ;;
    esac
    
    exit $RETVAL

register RHEL init-config
-------------------------

.. code-block:: bash

    chkconfig punani on
    service punani start
