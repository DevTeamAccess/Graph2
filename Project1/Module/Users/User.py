import graphene
from Project1.Common1.Common import Common1

class Account(graphene.ObjectType):
    AccountNo =graphene.String()
    Bank= graphene.String()
    Address= graphene.String()
    Contact = graphene.String()
    GegNo= graphene.ID()
class ResidenceAddress(graphene.ObjectType):
    FlatNo =graphene.String()
    Address = graphene.String()
    Contact = graphene.String()
    Landmark =graphene.String() 
class PermanentAddress(graphene.ObjectType):
    FlatNo =graphene.String()
    Address = graphene.String()
    Contact = graphene.String()
    Landmark =graphene.String() 
class User(graphene.ObjectType):
    id= graphene.String()
    Name = graphene.String()
    ResidenceAddress =graphene.List(ResidenceAddress)
    PermanentAddress= graphene.List(PermanentAddress)
    Gender =  graphene.String()
    BankDetail = graphene.List(Account)
class UserList:
    def UserDetails(args):
        data=[]
        for i in Common1.exeFunc1 ('proc_ContractUserlist',args):
            for index in i:
                Data1= index["Result"]
                for Data in Data1:  
                    UserObj= User()
                    UserObj.id=Data['id']
                    UserObj.Name=Data['Details']['Name']
                    UserObj.Gender=Data['Details']['Gender']
                    Raddress=[]
                    Paddress=[]
                    BankDetail=[]
                    BankDetail.append(Account(
                    AccountNo=Data['Details']['BankDetail']['AccountNo'] ,
                    Bank=Data['Details']['BankDetail']['Bank'] ,
                    Address=Data['Details']['BankDetail']['Address'] ,
                    Contact=Data['Details']['BankDetail']['Contact'] ,
                    GegNo = Data['Details']['BankDetail']['GegNo'] ))

                    Raddress.append(ResidenceAddress(
                    FlatNo=Data['Details']['ResidenceAddress']['FlatNo'] ,
                    Address=Data['Details']['ResidenceAddress']['Address'] ,
                    Contact=Data['Details']['ResidenceAddress']['Contact'] ,
                    Landmark=Data['Details']['ResidenceAddress']['Landmark'] ))
                    Paddress.append(PermanentAddress(
                    FlatNo=Data['Details']['PermanentAddress']['FlatNo'] ,
                    Address=Data['Details']['PermanentAddress']['Address'] ,
                    Contact=Data['Details']['PermanentAddress']['Contact'] ,
                    Landmark=Data['Details']['PermanentAddress']['Landmark'] ))
                    UserObj.BankDetail=BankDetail
                    UserObj.PermanentAddress=Paddress
                    UserObj.ResidenceAddress=Raddress
                    data.append(UserObj)
        return data
class CreateUser(graphene.Mutation):
    id= graphene.String()
    Name = graphene.String()
    ResidenceAddress =graphene.List(ResidenceAddress)
    PermanentAddress= graphene.List(PermanentAddress)
    Gender =  graphene.String()
    BankDetail = graphene.List(Account)
    class Arguments:
        id= graphene.String()
        Name = graphene.String()
        ResidenceAddress =graphene.types.json.JSONString()
        PermanentAddress= graphene.types.json.JSONString()
        Gender =  graphene.String()
        BankDetail =graphene.types.json.JSONString()
    def mutate(self, id, Name, ResidenceAddress, PermanentAddress, Gender, BankDetail):
        return CreateUser(
        id= "id",
        Name = "Name",
        ResidenceAddress = ResidenceAddress(
                    FlatNo="FlatNo" ,
                    Address="Address" ,
                    Contact="Contact",
                    Landmark="sdfdsf"),
        PermanentAddress= PermanentAddress(
                    FlatNo="FlatNo" ,
                    Address="Address" ,
                    Contact="Contact",
                    Landmark="sdfdsf"),
        Gender =  "Gender",
        BankDetail =Account(
                    AccountNo="SSS",
                    Bank="ddfdf",
                    Address="jhdsfhj" ,
                    Contact="dsfsdf" ,
                    GegNo ="sdfdsf")
        )
        #return CreateUser(CreateUser=CreateUser1)


# if __name__ == "__main__":
#     datat=UserList
#     args=()
#     data11=datat.UserDetails(args)
#     hhshs=data11