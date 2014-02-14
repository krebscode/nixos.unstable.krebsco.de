FTP Share with Python on Windows
################################
:date: 2012-03-06 14:34
:tags: ftp,python,windows

Installation of dependencies
============================

.. code-block:: bat
  
    #! cmd.exe
    wget http://www.python.org/ftp/python/2.7.2/python-2.7.2.msi
    msiexec python-2.7.2.msi
    # get easy_install
    wget
    http://pypi.python.org/packages/2.7/s/setuptools/setuptools-0.6c11.win32-py2.7.exe
    .\setuptools-0.6.c11.win32-py2.7.exe

    cd c:\Python27\Scripts
    easy_install pywin32
    easy_install pyftpdlib


anon_serv.py
============
in addition to serve anonymous ftp, the current hostname is copied to the
clipboard share it via instant-messenger.

.. code-block:: python
    
    #!/usr/bin/python
    import socket
    fullhn=socket.getfqdn()
    print ("My Hostname: %s" % fullhn )

    import win32clipboard as w
    import win32con
    w.OpenClipboard()
    w.EmptyClipboard()
    w.SetClipboardData(win32con.CF_TEXT,fullhn)
    w.CloseClipboard()

    from pyftpdlib import ftpserver
    authorizer = ftpserver.DummyAuthorizer()
    authorizer.add_anonymous("C:\\\\ftp",perm="elradfmw")
    handler = ftpserver.FTPHandler
    handler.authorizer = authorizer
    address = ("0.0.0.0", 21)
    ftpd = ftpserver.FTPServer(address, handler)
    ftpd.serve_forever()
