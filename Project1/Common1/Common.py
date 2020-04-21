
from Project1.db1.dbConnect import dbConnect1
class Common1:
    def exeQuery1(Query):
        _Cursor=dbConnect1.Connection('')
        _Cursor.execute(Query)
        data=_Cursor.fetchall()
        _Cursor.close()        
        return data
    def exeFunc1(Func,*args):
        try:
            _Cursor,Connection=dbConnect1.Connection() 
            args[0] if _Cursor.callproc(Func,args[0]) else _Cursor.callproc(Func)
            Connection.commit()
            data=_Cursor.fetchall()
            return data
        except Exception as ex:
            print(ex)
            return ex            
