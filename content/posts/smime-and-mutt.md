Title: S/MIME and Mutt
Date: 2012-02-01 16:32
Slug: smime-and-mutt

This is the PoC shell code for exchaning encrypted mails with MS
Outlook.

</p>

<p>
<figure class="code">
<figcaption>
<span>enable smime for mutt</span>

</figcaption>
<div class="highlight">

+--------------------------------------+--------------------------------------+
| ``` {.line-numbers}                  |     #?/bin/shecho "source /usr/share |
| 1234567891011121314151617181920      | /doc/mutt/samples/smime.rc" >> ~/.mu |
| ```                                  | ttrcsmime_keys init# create private  |
|                                      | CA and derive mail certificate (see  |
|                                      | below)#  OR # get free trusted certi |
|                                      | ficate from #       http://www.comod |
|                                      | o.com/home/email-security/free-email |
|                                      | -certificate.phpsmime_keys add_p12 m |
|                                      | ail.p12echo 'set smime_default_key=" |
|                                      | <see output above>"' >> ~/.muttrcwge |
|                                      | t http://services.support.alcatel-lu |
|                                      | cent.com/PKI/rootCA.crtsmime_keys ad |
|                                      | d_root rootCA.crtmutt# receive signe |
|                                      | d mail of crypto partner## CTRL-K# f |
|                                      | ix the ~/.smime/certificates/.index  |
|                                      | as extraction of complete chains # d |
|                                      | oes not work correctly as of today ( |
|                                      | 31.01.2012) see Mutt #3559           |
+--------------------------------------+--------------------------------------+

</div>

</figure>
</p>

<p>
<figure class="code">
<figcaption>
<span>Create own CA</span>

</figcaption>
<div class="highlight">

+--------------------------------------+--------------------------------------+
| ``` {.line-numbers}                  |     mkdir caopenssl req -new -x509 - |
| 123456789101112131415161718192021222 | keyout ca/root_encrypted.key -out ca |
| 324252627282930313233343536373839404 | /root.pem -days 9001openssl rsa -in  |
| 142                                  | ca/root_encrypted.key > ca/root.keyr |
| ```                                  | m ca/root_encrypted.keycat > root.cn |
|                                      | f <<EOF[ ca ]default_ca = ca_default |
|                                      | [ ca_default ]dir = ./cacerts = $dir |
|                                      | new_certs_dir = $dir/ca.db.certsdata |
|                                      | base = $dir/ca.db.indexserial = $dir |
|                                      | /ca.db.serialRANDFILE = $dir/ca.db.r |
|                                      | andcertificate = $dir/ca.crtprivate_ |
|                                      | key = $dir/ca.keydefault_days = 365d |
|                                      | efault_crl_days = 30default_md = md5 |
|                                      | preserve = nopolicy = generic_policy |
|                                      | [ generic_policy ]countryName = opti |
|                                      | onalstateOrProvinceName = optionallo |
|                                      | calityName = optionalorganizationNam |
|                                      | e = optionalorganizationalUnitName = |
|                                      |  optionalcommonName = suppliedemailA |
|                                      | ddress = optionalEOFecho '100001' >c |
|                                      | a/ca.db.serialtouch ./ca/ca.db.index |
|                                      | mkdir ./ca/ca.db.certsopenssl req -n |
|                                      | ew -keyout mail.key -out mail.csr -d |
|                                      | ays 9001openssl ca -config root.cnf  |
|                                      | -out mail.crt -infiles mail.csropens |
|                                      | sl pkcs12 -export -inkey mail.key -c |
|                                      | ertfile ca/root.crt -out mail.p12 -i |
|                                      | n mail.crtsmime_keys add_root ca/roo |
|                                      | t.crtsmime_keys add_cert ca/root.crt |
+--------------------------------------+--------------------------------------+

</div>

</figure>
</p>

