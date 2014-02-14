Title: Make this blog post happen
Date: 2012-02-01 13:20
Slug: make-this-blog-post-happen

<p>
<figure class="code">
<figcaption>
<span>recursive</span>

</figcaption>
<div class="highlight">

+--------------------------------------+--------------------------------------+
| ``` {.line-numbers}                  |     #?/bin/shbash -s stable < <(curl |
| 1234567891011121314                  |  -s https://raw.github.com/wayneeseg |
| ```                                  | uin/rvm/master/binscripts/rvm-instal |
|                                      | ler)echo '[[ -s $HOME/.rvm/scripts/r |
|                                      | vm ]] && source $HOME/.rvm/scripts/r |
|                                      | vm' >> ~/.zshrcsource ~/.zshrcrvm in |
|                                      | stall 1.9.2 && rvm use 1.9.2rvm ruby |
|                                      | gems latestgem install bundlergit cl |
|                                      | one git://github.com/imathis/octopre |
|                                      | ss.git octopresscd octopressbundle i |
|                                      | nstallrake installrake new_post\["Ma |
|                                      | ke this blog post happen"\]vim sourc |
|                                      | e/_posts/2012-02-01-make-this-blog-p |
|                                      | ost-happen.markdownrake generate     |
+--------------------------------------+--------------------------------------+

</div>

</figure>
</p>

Disclamer
=========

</p>

Well, this is my first post. I will post code i am working with here.

</p>

Most of the code snippets will be pseudo-code ( tagged by the hash
questionmark \#? ). The code can be seen as an digest of the `history`
command of my shell or my texteditor.

</p>

Be sure not to simply copy-paste my stuff as it will most likely break
because i haven’t tested it myself after writing this up even though it
*looks* correct ;).

</p>

I will mostly not describe what this stuff does more than the head line
and probably some tags as i think code is the only thing that matters in
the end, everything else can be read up somewhere else.

</p>

I guess this blog is somewhat like `Gist` or `Command Line Kung Fu`, but
only containing stuff important for me and my work.

</p>

