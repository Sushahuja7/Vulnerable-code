import os
import subprocess
from flask import Flask, request

app = Flask(__name__)

# 🔥 Vulnerable to Remote Code Execution (RCE) & Code Injection
@app.route("/rce", methods=["GET"])
def rce():
    cmd = request.args.get("cmd")  # Getting user input from URL
    output = os.popen(cmd).read()  # ⚠️ Directly executing user input!
    return f"Command Output: {output}"

# 🔥 Another RCE Vulnerability (Using subprocess)
@app.route("/rce2", methods=["GET"])
def rce_subprocess():
    cmd = request.args.get("cmd")  
    result = subprocess.check_output(cmd, shell=True)  # ⚠️ Dangerous execution
    return f"Subprocess Output: {result.decode()}"

# 🔥 Code Injection via eval()
@app.route("/eval", methods=["GET"])
def eval_function():
    code = request.args.get("code")  
    result = eval(code)  # ⚠️ Arbitrary code execution!
    return f"Eval Output: {result}"

# 🔥 Malicious Function Execution (exec)
@app.route("/exec", methods=["GET"])
def exec_function():
    code = request.args.get("code")  
    exec(code)  # ⚠️ Executes user-supplied code!
    return "Code executed!"

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
