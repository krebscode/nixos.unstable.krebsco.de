Getting Hama Nano DVB-T Stick to work
#####################################
:date: 2012-04-12 12:43
:tags: dvb-t, rtl2832u

I initially bought it because i wanted to play around with software
defined radio on the cheap [#]_ but haven’t had the time. As this thingy
is originally an DVB-T stick i wanted to try this out first. As it
contains a fairly common RTL2832U chip, it shouldn’t be that much of a
problem. It turns out it is ...

This Pseudo-script running under Arch Linux.

install and configure the Hama Nano DVB-T Stick
===============================================

.. code-block:: bash

    #?/bin/sh
    yaourt -S dvb-usb-rtl2832u-openpli
    modprobe dvb_usb_rtl2832u
    pacman -S linuxtv-dvb-apps
    #find a good place for the antenna
    scan /usr/share/dvb/dvb-t/de-Berlin | tee ~/.mplayer/channels.conf

    # you can also use the most current sender file from :
    # wget -O de-Berlin http://wiki.ubuntuusers.de/_attachment?target=dvb-utils%2Fchannels.conf%28Berlin%29
    # scan de-Berlin | ~/.mplayer/channels.conf

    mplayer "dvb://Das Erste"

If you do not live in Berlin(duh), have a look through /usr/share/dvb/dvb-t folder or have a look at  http://wiki.ubuntuusers.de/dvb-utils#Basisdaten for more accurate results.

.. [#] http://hardware.slashdot.org/story/12/03/31/1914217/software-defined-radio-for-11
