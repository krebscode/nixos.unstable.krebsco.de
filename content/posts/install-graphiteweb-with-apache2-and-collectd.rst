install graphite+web with apache2 and collectd
##############################################
:date: 2012-06-01 10:40
:tags: apache, collectd, graphite

After some try and error, this is how i got graphite and graphite\_web
running under a debian derivative (ubuntu 12.04).


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


See http://geek.michaelgrace.org/2011/09/how-to-install-graphite-on-ubuntu/
for a bloated version of the installation.

configure bucky and collectd
============================

.. code-block:: bash

    #?/bin/sh
    aptitude install collectd
    pip install bucky

    cat >>/etc/collectd/collectd.conf <<EOF
    LoadPlugin "network"
    <Plugin "network">
      Server "127.0.0.1" "25826"
    </Plugin>
    EOF

    /etc/init.d/collectd restart

    cat >>/etc/supervisor/conf.d/bucky.conf <<EOF
    [program:bucky]
    command=/usr/local/bin/bucky
    redirect_stderr=true
    user=nobody
    autorestart=true
    EOF

    supervisorctl reread
    supervisorctl update
