import psycopg2
from psycopg2 import Error
import os
class dbConnect1:
    def Connection():  
        try :
            connection = psycopg2.connect(user=os.getenv("user"),
                                  password=os.getenv("password"),
                                  host=os.getenv("host"),
                                  port=os.getenv("port"),
                                  database=os.getenv("database"))
            cursor = connection.cursor()
            return [cursor,connection]
        except (Exception, psycopg2.DatabaseError) as error:
            return error
    # def Connection1():  
    #     try :
    #         connection = psycopg2.connect(user="postgres",password="admin",host="localhost",port="5432",database="DbContract")
    #         cursor = connection.cursor()
    #         return [cursor,connection]
    #     except (Exception, psycopg2.DatabaseError) as error:
    #         return error