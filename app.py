from flask import Flask, request, render_template, redirect, url_for, session
import dbconnect
import hashlib
from datetime import timedelta
import os
import csv 


app = Flask(__name__) # __name__ 代表目前執行的模組
app.config['SECRET_KEY'] = os.urandom(24)
app.config['PERMANENT_SESSION_LIFETIME'] = timedelta(days=31)
app.config['UPLOAD_FOLDER'] = "./csvupload"
ALLOWED_EXTENSIONS = set(['csv']) # only csv file can upload


def allowed_file(filename:str):
    return '.' in filename and \
           filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS

@app.route("/") # 函式的裝置 (Decorator): 以函式為基礎，提供附加的功能
def index():
    return render_template("index.html")

@app.route('/circle_world_plot_2014')
def circle_world_plot_2014():
    return render_template('circle_world_plot_2014.html')

@app.route('/flat_world_plot_2014')
def flat_world_plot_2014():
    return render_template('flat_world_plot_2014.html')

@app.route('/scatter_plot_2014')
def scatter_plot_2014():
    return render_template('scatter_plot_2014.html')

@app.route("/KPI_1")
def showDB():
    data = dbconnect.select_all("kpi_1")
    return render_template("KPI_1.html", data = data)

@app.route("/login")
def login_page():
    return render_template("login.html")

@app.route("/logout")
def logout():
    session["username"] = False
    return redirect("/")

@app.route("/checkAuth", methods=['POST', 'GET']) # check auth 
def checkAuth():
    if request.method == "POST":
        # === check username & password ===
        username = request.form['username']
        password = request.form['password']
        row = dbconnect.find_user(username)
        if row["password"] == hashlib.sha512(str(password).encode("utf-8")).hexdigest():
            session["username"] = username
            return redirect("/admin/backend")
        # =================================
    return redirect("/login")

@app.route("/admin/backend") # web_path
def backend_page():
    # === check auth ===
    if session.get("username") == "admin":
        return render_template("admin/backend.html")
    # ==================
    return redirect("/")


@app.route("/admin/addfile") # web_path
def addfile_page():
    # === check auth ===
    if session.get("username") == "admin":
        return render_template("admin/addfile.html")
    # ==================
    return redirect("/")

#=============upload====================
@app.route('/admin/upload', methods=['POST', 'GET'])
def upload():
    if session.get("username") == "admin" and request.method == 'POST':
        file = request.files['upload_file']
        fname = file.filename
        savepath = os.path.join(app.config['UPLOAD_FOLDER'] , fname)
        file.save( savepath )
        with open( savepath , newline='', encoding="utf-8" ) as csvfile: # open file 
            data = list( csv.reader( csvfile ) )

        dbconnect.delete_data( )
        dbconnect.insert_data(  data  )

        #os.unlink( savepath )
        return redirect("/admin/addfile")
    return redirect("/")
#==========================================

if __name__ == "__main__": # 如果以上程式執行
    app.run(debug=True) # 立刻啟動伺服器

