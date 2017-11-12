#!/usr/bin/env bash

# Check for the lock file, if it exists, we know this vagrant VM has already been
# provisioned and we simply want to reload everything
# lockfile=/home/vagrant/kickstart.lock testing
lockfile=~/kickstart.lock

if [ -e "$lockfile" ]; then
    # Reload steps
    echo "Reload detected."
else
    apt-get update

    # base packages
    apt-get -y install gcc build-essential git python3.4-venv python3-dev pandoc libssl-dev libffi-dev python-dev python2.7 postgresql postgresql-contrib python-pip python-virtualenv python3-psycopg2 libpq-dev

    # Place the lockfile
    # touch /home/vagrant/kickstart.lock testing
    touch ~/kickstart.lock
fi
