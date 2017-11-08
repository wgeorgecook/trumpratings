# run sql configuration script

lockfile=/home/vagrant/setup-db.lock

if [ -e "$lockfile" ]; then
    # Reload steps
    echo "Reload detected"
else
  sudo cp /home/vagrant/deployment/pg_hba.conf /etc/postgresql/9.3/main/pg_hba.conf # configure for trust
  sudo /etc/init.d/postgresql restart # loads copied file
  psql -U postgres < deployment/psql_setup.sql # configures the DB
  touch /home/vagrant/setup-db.lock # Place the lockfile
fi
