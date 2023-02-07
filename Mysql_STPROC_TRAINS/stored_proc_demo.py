from mysql.connector import Error
from hcl_database_connection import MysqlDatabaseConnection
class HclstoredProcedure(MysqlDatabaseConnection):
    pass
connect_obj=HclstoredProcedure()
connect_obj.connect('localhost','root','root','hcl_vijayawada')
print(connect_obj)