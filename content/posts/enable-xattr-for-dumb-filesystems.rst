Enable xattr for dumb filesystems
#################################

:date: 2012-05-04 15:17
:tags: xattr,filesystems,davfs

I was looking for a way to enable extended attributes for encfs(userland
crypto Wrapper) on davfs(userland Webdav fs wrapper) to use them with
glusterfs to create a high-availability distributed secure cloud storage
on the cheap. 

After many hours looking for a way to enable xattrs on encfs or ecryptfs
and davfs or wdfs i found pyfilesystems to write and mount an xattr
wrapper for the retard fs.


install pyfilesystem and encfs davfs
====================================

.. code-block:: bash

    pip install fs
    apt-get install davfs2 encfs

mount davfs and encfs
=====================

.. code-block:: bash

    #?/bin/sh
    echo "https://path/to/webdav   username    password" >> /etc/davfs2/secrets
    mkdir /mnt/{1,2,3}
    mkdir /mnt/1/.encfs
    mount.davfs https://path/to/webdav /mnt/1
    encfs /mnt/1/.encfs /mnt/2


mount wrapper fs
================

.. code-block:: python

    #?/usr/bin/python
    from  fs.osfs import OSFS
    from fs.xattrs import SimulateXAttr
    stupid_fs = OSFS("/mnt/2")
    xattr_fs = SimulateXAttr(stupid_fs)
    fuse.mount(xattr_fs,"/mnt/3")


Now /mnt/3 can be used as a brick in glusterfs. Or just use tahoe-lafs ;P
