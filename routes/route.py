from flask import Blueprint,render_template,request,redirect,url_for
from requests import get,delete,post,put
import models

route   =   Blueprint("routes.route",__name__)

@route.route("/admin")
def index():
    data_api    =   get("http://127.0.0.1:5000/api/users")
    data        =   data_api.json()
    return render_template("admin.html",data=data["users"])

@route.route("/admin/user/<int:id>")
def detail_user(id):
    data_api    =   get(f"http://127.0.0.1:5000/api/user/{id}")
    data        =   data_api.json()   
    return render_template("detail.html",data=data)


@route.route("/admin/user/add",methods=["POST","GET"])
def add_user():
    if request.method == "POST":
        post(f"http://127.0.0.1:5000/api/users",data=request.form)
        return redirect(url_for("routes.route.index"))



@route.route("/admin/user/del/<int:id>")
def delete_user(id):
    delete(f"http://127.0.0.1:5000/api/user/{id}")
    return redirect(url_for("routes.route.index"))
        




