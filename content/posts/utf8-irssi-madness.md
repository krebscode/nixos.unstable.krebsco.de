Title: Utf8 in an Irssi/tmux/putty/windows Stack
Date: 2012-06-22
Tags: irssi, utf8

Getting irssi running with utf8 support in a putty/tmux stack is madness. Here
is what you have to do.

add lines in .{ba,z}shrc:
    
    :::bash
    export LANG=en_US.utf8
    export LC_ALL=en_US.utf8

add lines in .tmux.conf:

    :::bash
    set-option -g default-terminal "rxvt"
    set-window-option -g utf8 on

in irssi:
    
    :::bash
    /set term_charset UTF-8
    /set recode_autodetect_utf8 ON
    /set recode_fallback UTF-8
    /set recode ON
    /set recode_out_default_charset UTF-8
    /set recode_transliterate ON
    /save
    /quit

in putty config:

    window -> translation -> Received data assumed to be in which character set: UTF-8
                          -> Use Unicode line drawing code points
