from flask_restful import Api,Resource,marshal,fields,reqparse,marshal_with
from models import user
from flask import Blueprint,jsonify

user_fields =   {
    "id"        :   fields.Integer,
    "username"  :   fields.String,
    "email"     :   fields.String
}

class Users(Resource):
    def __init__(self):

        self.reqparser   = reqparse.RequestParser()

        self.reqparser.add_argument(
            "username",
            required    =   True,
            help        =   "username harus diisi",
            location    =['form','json']
        )

        self.reqparser.add_argument(
            "passwd",
            required    =   True,
            help        =   "Pasword Harus Ada",
            location    =   ['form','json']
        )

        self.reqparser.add_argument(
            "email",
            required    =   True,
            help        =   "email Harus Ada",
            location    =   ['form','json']
        )

    def get(self):
        users   =   [marshal(users,user_fields) for users in user.Users.select()]
        return {"users":users}

    def post(self):
        args = self.reqparser.parse_args()
        user.Users.create(**args)
        return jsonify({"Status":True})

class User(Resource):
    def __init__(self):

        self.reqparser   = reqparse.RequestParser()

        self.reqparser.add_argument(
            "username",
            required    =   True,
            help        =   "username harus diisi",
            location    =['form','json']
        )


        self.reqparser.add_argument(
            "email",
            required    =   True,
            help        =   "email Harus Ada",
            location    =   ['form','json']
        )

    @marshal_with(user_fields)
    def get(self,id):
        row    =   user.Users.get_by_id(id)
        return row

    def delete(self,id):
        user.Users.delete_by_id(id)
        user.Users.save()
        return {"status":True}
        
        





users_api   =   Blueprint("resources_api.user",__name__)
api         =   Api(users_api)

api.add_resource(Users,"/api/users")
api.add_resource(User,"/api/user/<int:id>")


