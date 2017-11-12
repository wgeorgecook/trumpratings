# run sql configuration script

# lockfile=/home/vagrant/setup-db.lock
lockfile=~/setup-db.lock

if [ -e "$lockfile" ]; then
    # Reload steps
    echo "Reload detected - no need to configure DB"
else

  # Configure for trust
  sudo cp /home/vagrant/deployment/pg_hba.conf /etc/postgresql/9.3/main/pg_hba.conf

  # Loads copied file
  sudo /etc/init.d/postgresql restart

  # Configures the DB
  psql -U postgres < deployment/psql_setup.sql

  # Place the lockfile
  # touch /home/vagrant/setup-db.lock
  touch ~/setup-db.lock
fi
