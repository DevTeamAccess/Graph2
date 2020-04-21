from flask.views import MethodView 
import logging
import os,json
from Project. Importmodules.Importmodules import ProcDetails, _msg,ValidateItems,Common
from flask import  request,  jsonify
logger=logging.getLogger(__name__)
class HttpverbsNotfound(MethodView):
    def get():
        return "Not Cond"
    def update():        
        return "Not Cond"
    def post():
        return "Not Cond"
    def delete():
        
        return "Not Cond"
class Httpverbs (MethodView):
    def get(self ,Func):
        return "Post"
    def update(self ,Func):
        return "Update"
    def post (self ,Func):
        #data=os.getenv("db")
        Result={}    
        logger.warning(f'Requested URL  "{Func}"')
        Invalid,ProcDetaisl=ProcDetails(Func,Func)
        if Invalid:
            Result['Result']=None
            Result['Status']="OK"
            Result['Message']=_msg.Msg("Notfound")            
            return jsonify(Result), 404
        if str(ProcDetaisl[0]['methods']).upper()=="post".upper():
            Status,Msg=ValidateItems._ValidateItem(ProcDetaisl[0]['RequirFild'],request.json)   
            if Status:
                args=()
                for i in  ProcDetaisl[0]['Sequence']:
                    for key in i.keys():
                        if key.upper()=="Details".upper():
                            args+=json.dumps(request.json[key]),   
                        else :
                            args+=request.json[key],
                logger.warning(args) 
                try:
                    for i in Common.exeFunc(ProcDetaisl[0]['Proc'],args):
                        for index in i:
                            Result['Result']= index["Result"]
                            Result['Status']=index["Status"]
                            Result['Message']=index["Msg"]["Massage"]
                            logger.warning(Result)
                except Exception as ex:
                    logger.warning(ex) 
                    Result['Result']=None
                    Result['Status']="OK"
                    Result['Message']="Some Internal Issue please try some time"
                    return jsonify(Result),200

                return jsonify(Result),200 
            else :
                Result['Result']=None
                Result['Status']="OK"
                Result['Message']=Msg
                return jsonify(Result),200
        else:
            return jsonify(Msg),404 
    def delete(self ,Func):
        return "Delete"    