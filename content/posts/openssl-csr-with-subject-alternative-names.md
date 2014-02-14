Title: OpenSSL CSR with Subject Alternative Names
Date: 2012-02-07 09:54
Slug: openssl-csr-with-subject-alternative-names

<p>
<figure class="code">
<figcaption>
<span>SAN in CSR</span>
</figcaption>
<div class="highlight">

+--------------------------------------+--------------------------------------+
| ``` {.line-numbers}                  |     #?/bin/shcat > my.ncf <<EOF[ req |
| 123456789101112131415161718192021222 |  ]default_bits        = 2048default_ |
| 324252627282930                      | keyfile     = privkey.pemdistinguish |
| ```                                  | ed_name  = req_distinguished_namereq |
|                                      | _extensions     = req_ext # The exte |
|                                      | ntions to add to the self signed cer |
|                                      | t [ req_distinguished_name ]countryN |
|                                      | ame           = Country Name (2 lett |
|                                      | er code)countryName_default   = DEst |
|                                      | ateOrProvinceName   = State or Provi |
|                                      | nce Name (full name)stateOrProvinceN |
|                                      | ame_default = Upper CornerlocalityNa |
|                                      | me          = Locality Name (eg, cit |
|                                      | y)localityName_default  = Internetor |
|                                      | ganizationName          = Organizati |
|                                      | on Name (eg, company)organizationNam |
|                                      | e_default  = Krebs CocommonName      |
|                                      |        = Common Name (eg, YOUR name) |
|                                      | commonName_default    = euer.krebsco |
|                                      | .decommonName_max        = 64 [ req_ |
|                                      | ext ]subjectAltName          = @alt_ |
|                                      | names [alt_names]DNS.1   = euer.kreb |
|                                      | sco.deDNS.2   = euerEOFopenssl req - |
|                                      | new -nodes -out my.csr -config my.cn |
|                                      | fopenssl req -noout -text -in my.csr |
+--------------------------------------+--------------------------------------+

</div>

</figure>
</p>

