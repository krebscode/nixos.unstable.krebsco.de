Custom CD Images on Sansa U3
############################
:date: 2012-02-13 14:00
:tags: usb,iso,autosart

I’m using a Sandisk Cruzer 8GB SDCZ36-008G-E11 (not B35) to deploy ISOs
on the virtual CD-Rom drive (U3 Smart).

write iso
---------
Some computers do better with a **real** cd-rom drive when botting a live
system.

.. code-block:: bash

    #?/bin/sh
    dmesg | grep CD-ROM
    u3-tool -i /dev/sdx1
    #resize cd-drive to N blocks
    u3-tool -p 7065646592 /dev/sdx1 
    u3-tool -l debian.iso /dev/sdx1

create own iso
--------------
In some cases you want to write a **special** iso to the usb stick, for example
to automate some tasks on a friends computer or make use of the great autostart
feature which will only be available for cd-rom drives but not usb-sticks.

.. code-block:: bash

    #?/bin/sh
    mkdir myiso
    cat << EOF > myiso/autorun.inf
    [autorun]
    action=Open folder to view files
    shellexecute=calc.exe
    icon=folder.ico
    EOF
    wget folder.ico calc.exe
    mkisofs -V FreeStuff -J -r -o my.iso myiso
    u3-tool /dev/sdx1 my.iso

See also http://forums.hak5.org/index.php?showtopic=17267 for a sweet
USB Switchblade (pyblade).
