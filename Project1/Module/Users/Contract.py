import graphene
from Project1.Common1.Common import Common1

class Detail (graphene.ObjectType):
    Name = graphene.String()
    Description =graphene.String()
class Contract(graphene.ObjectType):
    id= graphene.String()
    Details=  graphene.List(Detail)
    
class ContactList:
    def ContactDetails(args):
        data=[]
        for i in Common1.exeFunc1 ('proc_contractlist',args):
            for index in i:
                Data1= index["Result"]
                for Data in Data1:
                    DetailsObj= Contract()
                    DetailsObj.id=Data['id']
                    Detail1=[]
                    Detail1.append(Detail(Name=Data['Details']['Name'], Description=Data['Details']['description']))
                    DetailsObj.Details=Detail1
                    data.append(DetailsObj)
        return data

