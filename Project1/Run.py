from flask import Flask ,jsonify 
from flask_cors import CORS
from flask_graphql import GraphQLView
from .Module.Users.User import UserList,User,CreateUser
from .Module.Users.Contract import ContactList,Contract
from graphene import ObjectType, String,Schema, Boolean, ID, List, Field, Int
app = Flask(__name__)
CORS(app)
class Mutation(ObjectType):
    UserEntry =CreateUser.Field()
class Query(ObjectType):
    UserDetails=Field(List(User))
    ContactDetails=Field(List(Contract))
    def resolve_UserDetails(self, args):
        args=()
        return UserList.UserDetails(args)
    def resolve_ContactDetails(self, args):
        args=()
        return ContactList.ContactDetails(args)
view_func = GraphQLView.as_view("graphql",graphiql=True ,schema=Schema(query=Query, mutation=Mutation) )
app.add_url_rule("/", view_func=view_func)
def run():
    app.run()
@app.errorhandler(404)
def not_found(e): 
    Result={}
    Result['Result']= None
    Result['Status']="404"
    Result['Message']="Invalid Url requested "
    return jsonify(Result),404
