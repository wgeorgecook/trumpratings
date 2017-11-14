# Configure the DB for first use. See Vagrantfile for usage.


from peewee import *
from lib.psql.models import Twitter_info
from settings import DB_SETTINGS


class MakeDB(object):
    def __init__(self):
        self.dbconnection = DB_SETTINGS.get('db')
        self.dbuser = DB_SETTINGS.get('user')
        self.dbpass = DB_SETTINGS.get('password')
        self.dbhost = DB_SETTINGS.get('host')
        self.check_exist = "SELECT * FROM twitter_info"

        self.psql_db = PostgresqlDatabase(
            self.dbconnection,
            user=self.dbuser,
            password=self.dbpass,
            host=self.dbhost,
            )
        self.psql_db.connect()


    def check_tables(self):
        try:
            try:
                self.psql_db.execute_sql(self.check_exist)
                return True
                self.psql_db.close()
            except ProgrammingError:
                return False
                self.psql_db.close()
        except InternalError:
            self.psql_db.rollback()
            print("# Check_tables error: Connection broken. Transaction rolled back. #")

    def create_tables(self):
        try:
            if self.check_tables() is True:
                print("##### Tables exist. Config not necessary. #####")
                return True
            else:
                print("##### Creating DB tables #####")
                self.psql_db.create_table(Twitter_info)
                self.psql_db.close()
                print("##### DB configured! #####")
                return True
        except InternalError:
            self.psql_db.rollback()
            print("## Create_tables error: Connection broken. Transaction rolled back. ##")