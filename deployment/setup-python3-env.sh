#!/usr/bin/env bash

# Check for the lock file, if it exists, we know this vagrant VM has already been
# provisioned and we simply want to reload everything
lockfile=/home/vagrant/install-python3.lock

if [ -e "$lockfile" ]; then
    # Reload steps
    echo "Reload detected, refreshing env"

    # Run pip install on requirements to pick up new packages
    /home/vagrant/python3_env/bin/pip install -r /home/vagrant/deployment/requirements.txt
else
    # Setup the env
    virtualenv -p /usr/bin/python3  /home/vagrant/python3_env

    # Upgrade pip
    /home/vagrant/python3_env/bin/pip install --upgrade

    # Pip install the requirements
    /home/vagrant/python3_env/bin/pip install -r /home/vagrant/deployment/requirements.txt

    # Make this env activate on log in
    echo "source ~/python3_env/bin/activate" >> ~/.profile

    # Place the lockfile
    touch /home/vagrant/install-python3.lock
    echo "Python 3 setup complete"
fi
