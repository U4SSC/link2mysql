from flask import Flask, request, render_template, redirect, url_for, session
import dbconnect
import hashlib
from datetime import timedelta
import os
import csv 
import json

app = Flask(__name__) # __name__ 代表目前執行的模組
app.config['SECRET_KEY'] = os.urandom(24)
app.config['PERMANENT_SESSION_LIFETIME'] = timedelta(days=31)
app.config['UPLOAD_FOLDER'] = "./csvupload"
ALLOWED_EXTENSIONS = set(['csv']) # only csv file can upload

#==========================================
country = ["Afghanistan","Angola","Albania","United Arab Emirates","Argentina","Armenia","Australia","Austria","Azerbaijan","Burundi","Belgium","Benin","Burkina Faso","Bangladesh","Bulgaria","Bahrain","Bahamas, The","Bosnia and Herzegovina","Belarus","Belize","Bolivia","Brazil","Barbados","Brunei Darussalam","Bhutan","Botswana","Central African Republic","Canada","Switzerland","Chile","China","Cote d'Ivoire","Cameroon","Congo, Rep.","Colombia","Comoros","Cabo Verde","Costa Rica","Cuba","Cyprus","Czech Republic","Germany","Denmark","Dominican Republic","Algeria","Ecuador","Egypt, Arab Rep.","Eritrea","Spain","Estonia","Ethiopia","Finland","Fiji","France","Gabon","United Kingdom","Georgia","Ghana","Guinea","Gambia,The","Guinea-Bissau","Equatorial Guinea","Greece","Guatemala","Guyana","Hong Kong SAR, China","Honduras","Croatia","Haiti","Hungary","Indonesia","India","Ireland","Iran, Islamic Rep.","Iraq","Iceland","Israel","Italy","Jamaica","Jordan","Japan","Kazakhstan","Kenya","Kyrgyz Republic","Cambodia","Korea, Rep.","Kuwait","Lao PDR","Lebanon","Liberia","Libya","Sri Lanka","Lesotho","Lithuania","Luxembourg","Latvia","Macao SAR, China","Morocco","Moldova","Madagascar","Maldives","Mexico","Macedonia, FYR","Mali","Malta","Myanmar","Montenegro","Mongolia","Mozambique","Mauritania","Mauritius","Malawi","Malaysia","Namibia","Niger","Nigeria","Nicaragua","Netherlands","Norway","Nepal","New Zealand","Oman","Pakistan","Panama","Peru","Philippines","Papua New Guinea","Poland","Puerto Rico","Korea, Dem. People's Rep.","Portugal","Paraguay","Qatar","Romania","Russian Federation","Rwanda","Saudi Arabia","Sudan","Senegal","Singapore","Solomon Islands","Sierra Leone","El Salvador","Somalia","Serbia","Suriname","Slovak Republic","Slovenia","Sweden","Swaziland","Syrian Arab Republic","Chad","Togo","Thailand","Tajikistan","Turkmenistan","Timor-Leste","Trinidad and Tobago","Tunisia","Turkey","Tanzania","Uganda","Ukraine","Uruguay","United States","Uzbekistan","Venezuela, RB","Vietnam","West Bank and Gaza","Yemen, Rep.","South Africa","Congo, Dem. Rep.","Zambia","Zimbabwe"]
#==========================================

def allowed_file(filename:str):
    return '.' in filename and \
           filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS

@app.route("/") # 函式的裝置 (Decorator): 以函式為基礎，提供附加的功能
def index():
    return render_template("index.html",country=country)
    
@app.route('/create_2d_plot', methods=['POST'])
def create_2d_plot():
    # print(request.form['data'])

    json_country = request.get_json()
    print(json_country)
    with open("country_list.json", "w") as outfile:
        json.dump(json_country, outfile)

    os.system("python create_2d_plot.py")

    return "123"

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
        if(row == False):
            return redirect("/login")
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

@app.route("/admin/addfile", methods=['POST', 'GET']) # addfile
def addfile():
    # === check auth ===
    if session.get("username") == "admin":
        return render_template("admin/addfile.html")
    # ==================
    return redirect("/")


@app.route("/reference")
def reference_page():
    return render_template("reference.html")

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

        # update html
        os.system("python generator.py")
        
        return redirect("/admin/backend")
    return redirect("/")
#==========================================

if __name__ == "__main__": # 如果以上程式執行
    app.run(debug=True) # 立刻啟動伺服器

