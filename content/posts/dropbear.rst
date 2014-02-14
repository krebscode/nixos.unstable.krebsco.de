Dropbear Public-Key Authentication 
##################################
:date: 2012-08-07 00:00
:tags: openssh, dropbear

ssh-copy-id does not work out of the box for dropbear.
The issue is that dropbear may only have one authorizedKeys file while openssh
handles this file for each user.
To fix it symlink the root users authorizedKeys file to the dropbear one.
    
.. code-block:: bash

    openwrt>> ln -s /root/.ssh/authorized_keys /etc/dropbear/
    remote>>> ssh-copy-id root@openwrt
 
There, you fixed it
