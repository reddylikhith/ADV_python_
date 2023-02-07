from hcl_database_connection import MysqlDatabaseConnection
class HclPythonTransaction(MysqlDatabaseConnection):
    def excecute_transaction_query(self):
        custid=2
        sql="delete from customer where cust_id=%s"
        try:
            self.cursor.execute(sql,(custid,))
            self.connection.commit()
        except:
            self.connection.rollback()
            print("something goes wrong")
        finally:
            if(self.connection.is_connected()):
                self.cursor.close()
                self.connection.close()
connection_obj=HclPythonTransaction()
connect_obj.connect('localhost','root')
connection_obj.excecute_transaction_query()