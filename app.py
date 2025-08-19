from flask import Flask, request, render_template_string

app = Flask(__name__)

HTML_TEMPLATE = """
<!DOCTYPE html>
<html>
<head>
    <title>Python Syntax Checker</title>
    <style>
        body { font-family: Arial; margin: 30px; }
        textarea { width: 100%; height: 300px; font-family: monospace; }
        button { margin-top: 10px; padding: 10px 20px; font-size: 16px; cursor: pointer; }
        .result { margin-top: 20px; font-weight: bold; padding: 10px; border-radius: 5px; }
        .success { background-color: #d4edda; color: #155724; }
        .error { background-color: #f8d7da; color: #721c24; }
    </style>
</head>
<body>
    <h2>🐍 Python Syntax Checker Tool</h2>
    <form method="post">
        <textarea name="code" placeholder="Paste your Python code here...">{{ code }}</textarea><br>
        <button type="submit">Check Syntax</button>
    </form>
    {% if result %}
        <div class="result {% if '✅' in result %}success{% else %}error{% endif %}">
            {{ result }}
        </div>
    {% endif %}
</body>
</html>
"""

@app.route("/", methods=["GET", "POST"])
def index():
    result = None
    code = ""
    if request.method == "POST":
        code = request.form["code"]
        try:
            compile(code, "<string>", "exec")
            result = "✅ No Syntax Errors Found"
        except SyntaxError as e:
            result = f"❌ Syntax Error at line {e.lineno}: {e.msg}"
    return render_template_string(HTML_TEMPLATE, result=result, code=code)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
