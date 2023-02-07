import mysql.connector
class MysqlDatabaseConnection:
    def __init__(self, host, user, password, db):
            self.host = host
            self.user = user
            self.password = password
            self.db = db
            try:
                self.connection = mysql.connector.connect(host=self.host,
                                                          user=self.user,
                                                          password=self.password,
                                                          database=self.db)
            except Exception as e:
                print(e)
connect_obj=MysqlDatabaseConnection()
connect_obj.connect('loclahost','root','root','hcl_vijayawada')
print(connect_obj)