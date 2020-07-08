from flask import jsonify
from flask import render_template
from flask import request
from Naked.toolshed.shell import  muterun_js
from bcloop_ui import app

@app.route("/", defaults={"js": "home"})
@app.route("/<any(home):js>")
def index(js):
    return render_template(f"{js}.html", js=js)


@app.route("/home", methods=["POST"])
def home():
    a = request.form.get("a", type=str)
    exec_cmd = "/Users/viraajimothukuri/BCloop/UI/HLF/Home.js" + " " +a+ ""
    print(a)
    print(exec_cmd)
    result = muterun_js(exec_cmd)
    if result.exitcode == 0:
        print(result.stdout)
        res = result.stdout
    print("from py", result, res)
    return jsonify(result=str(res))