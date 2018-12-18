# run sql configuration script

# lockfile=/home/vagrant/setup-db.lock
lockfile=/home/pi/setup-db.lock

if [ -e "$lockfile" ]; then
    # Reload steps
    echo "Reload detected - no need to configure DB"
else

  # Configure for trust
  sudo cp /var/www/trumpratings/deployment/pg_hba.conf /etc/postgresql/9.6/main/pg_hba.conf

  # Loads copied file
  sudo /etc/init.d/postgresql restart

  # Configures the DB
  psql -U postgres < /var/www/trumpratings/deployment/psql_setup.sql

  # Place the lockfile
  # touch /home/vagrant/setup-db.lock
  touch ~/setup-db.lock
fi
