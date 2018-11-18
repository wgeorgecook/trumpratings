#!/usr/bin/env bash

# Check for the lock file, if it exists, we know this vagrant VM has already been
# provisioned and we simply want to reload everything
# lockfile=/home/vagrant/install-python3.lock
lockfile=/home/vagrant/install-python3.lock
vagrant_dir="/home/vagrant/"
trump_dir="/var/www/trumpratings"

if [ -e "$vagrant_dir" ]; then
    echo "################################"
    echo "#   Vagrant detected.          #"
    echo "#   Running setup-py3-env      #"
    echo "#   provisioner shell script.  #"
    echo "################################"

    # Vagrant script below
    lockfile=/home/vagrant/install-python3.lock

    if [ -e "$lockfile" ]; then
        # Reload steps
        echo "Reload detected, refreshing env"


        # Cat-ing out the requirements txt to make sure it's populated
        echo "Packages to be installed:"
        cat /home/vagrant/deployment/requirements.txt


        # Run pip install on requirements to pick up new packages
        /home/vagrant/python3_env/bin/pip install -Ur /home/vagrant/deployment/requirements.txt
    else
        # Setup the env
        virtualenv -p /usr/bin/python3  /home/vagrant/python3_env

        # Cat-ing out the requirements txt to make sure it's populated
        echo "Packages to be installed:"
        cat /home/vagrant/deployment/requirements.txt

        # Upgrade pip
        /home/vagrant/python3_env/bin/pip install --upgrade pip

        # Pip install the requirements
        /home/vagrant/python3_env/bin/pip install -r /home/vagrant/deployment/requirements.txt

        # Make this env activate on log in
        echo "source ~/python3_env/bin/activate" >> /home/vagrant/.profile

        # Place the lockfile
        touch /home/vagrant/install-python3.lock
        echo "Python 3 setup complete"
    fi




elif [ -e "$lockfile" ]; then
    # Reload steps
    echo "Reload detected, refreshing env"

    # Run pip install on requirements to pick up new packages
    ~/python3_env/bin/pip install -r ~/deployment/requirements.txt
else
    # Check for www pathway
    if [ ! -d "$trump_dir" ]; then
        mkdir /var/www/trumpratings
    fi

    # Setup the env
    virtualenv -p /usr/bin/python3  /var/www/trumpratings/python3_env

    # Upgrade pip
    /var/www/trumpratings/python3_env/bin/pip install --upgrade

    # Pip install the requirements
    /var/www/trumpratings/python3_env/bin/pip install -r /var/www/trumpratings/deployment/requirements.txt

    # Make this env activate on log in
    echo "source /var/www/trumpratings/python3_env/bin/activate" >> ~/.profile

    # Place the lockfile
    touch /var/www/trumpratings/install-python3.lock
    echo "Python 3 setup complete"
fi