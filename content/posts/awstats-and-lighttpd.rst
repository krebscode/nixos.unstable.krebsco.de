awstats and lighttpd
####################
:date: 2012-02-06 13:40
:tags: awstats, lighttpd, graphite

These snippets are in a ”*worked* for me” state. most of this stuff will
break your system when executing.

Assumptions:

  -   **/srv/http/euer.krebsco.de** - served by lighttpd on public
      interface
  -   **/srv/http/priv** - served on private interface (darknet)

lighttpd seperate subdomain logging and awstats
-----------------------------------------------

.. code-block:: bash

    #?/bin/sh
    apt-get install python-django python-cairo
    sudo easy_install django-tagging

    pip install carbon
    pip install whisper
    pip install graphite-web
    cd /opt/graphite/conf
    cp carbon.conf.example carbon.conf
    cp graphite.wsgi.example graphite.wsgi
    cp storage-schemas.conf.example storage-schemas.conf
    cd ..
    cp examples/example-graphite-vhost.conf
    /etc/apache2/sites-enabled/000-default.conf
    chown www-data:www-data -R storage/ webapp/
    cd webapp/graphite
    cp local_settings.py.example local_settings.py
    python manage.py syncdb
    python /opt/graphite/bin/carbon-cache.py start
    /etc/init.d/apache2 restart


awstats for subdomain
---------------------
    
.. code-block:: bash

    #?/bin/sh
    apt-get install awstats
    cat > /etc/awstats/awstats.euer.krebsco.de.conf  <<EOF
    LogFile="/var/log/lighttpd/euer.krebsco.de/access.log"
    SiteDomain="euer.krebsco.de"
    LogFormat=1
    Include "/etc/awstats/awstats.conf.local"
    EOF
    ln -s /usr/share/awstats/icon /srv/http/priv/awstats-icon
    cp /usr/lib/cgi-bin/awstats.pl /srv/http/priv/awstats
    awstats -config=euer.krebsco.de -update
