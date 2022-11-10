from flask import Flask, request, render_template, redirect, url_for
import dbconnect

app = Flask(__name__) # __name__ 代表目前執行的模組

@app.route("/") # 函式的裝置 (Decorator): 以函式為基礎，提供附加的功能
def index():
    return render_template("index.html")

@app.route("/KPI_1")
def showDB():
    data = dbconnect.select_all("kpi_1")
    return render_template("KPI_1.html", data = data)

@app.route("/login")
def login_page():
    return render_template("login.html")

@app.route("/checkAuth", methods=['POST'])
def checkAuth():
    if request.method == "POST":
        # === check username & password ===
        if 1:
            return redirect(url_for("admin/backend"))
        # =================================
    return redirect(url_for("login", fail = True))

@app.route("/admin/backend")
def backend_page():
    # === check auth ===
    
    # ==================
    return render_template("admin/backend_html")

if __name__ == "__main__": # 如果以上程式執行
    app.run(debug=True) # 立刻啟動伺服器

