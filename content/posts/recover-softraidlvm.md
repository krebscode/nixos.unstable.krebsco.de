Title: Recover Softraid/LVM
Date: 2012-02-06 10:24
Slug: recover-softraidlvm

MD Array fails to assemble
--------------------------

</p>

<p>
<figure class="code">
<figcaption>
<span>Find the Problem</span>

</figcaption>
<div class="highlight">

+--------------------------------------+--------------------------------------+
| ``` {.line-numbers}                  |     #?/bin/shcat /proc/mdstatmdadm - |
| 12345                                | D --scanmdadm -E --scanmdadm -E /dev |
| ```                                  | /sd[abcdef]1                         |
+--------------------------------------+--------------------------------------+

</div>

</figure>
</p>

<p>
<figure class="code">
<figcaption>
<span>Try to assemble manually</span>

</figcaption>
<div class="highlight">

+--------------------------------------+--------------------------------------+
| ``` {.line-numbers}                  |     #?/bin/shmdadm --stop /dev/md{0, |
| 123                                  | 127}mdadm --assemble /dev/md0 /dev/s |
| ```                                  | d{a,b,c,d,e,f}1 --force              |
+--------------------------------------+--------------------------------------+

</div>

</figure>
</p>

<p>
<figure class="code">
<figcaption>
<span>recover a failed device in the array</span>

</figcaption>
<div class="highlight">

+--------------------------------------+--------------------------------------+
| ``` {.line-numbers}                  |     #?/bin/shmdadm /dev/md0 --re-add |
| 123456                               |  /dev/sdx1 # will likely failmdadm - |
| ```                                  | -zero-superblock /dev/sdx1 # reap th |
|                                      | e deviceecho 200000 > /proc/sys/dev/ |
|                                      | raid/speed_limit_min # speed up reco |
|                                      | verymdadm /dev/md0 --add /dev/sde1sl |
|                                      | eep 56000 && echo "FINISHED!"        |
+--------------------------------------+--------------------------------------+

</div>

</figure>
</p>

Recover LVM after doing something stupid
----------------------------------------

</p>

<p>
<figure class="code">
<figcaption>
<span>Restore VolGroup Partitioning</span>

</figcaption>
<div class="highlight">

+--------------------------------------+--------------------------------------+
| ``` {.line-numbers}                  |     #?/bin/sh# imagine you did somet |
| 123456789                            | hing like 'vgremove vg'vgdisplay -v  |
| ```                                  | # > logical volume: empty :(# lvm st |
|                                      | ores backup of partitioning, yayvgcf |
|                                      | grestore -f /etc/lvm/archive/vg_0001 |
|                                      | 8-2146062166.vg -v vgvgchange -ayvgd |
|                                      | isplay -v # > logical volume: files1 |
|                                      |  e2fsck /dev/vg/files1mount /dev/vg/ |
|                                      | files1                               |
+--------------------------------------+--------------------------------------+

</div>

</figure>
</p>

