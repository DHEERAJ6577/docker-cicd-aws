from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "<h1>Docker CI/CD Deployed Successfully 🚀</h1><p>Docker + GitHub Actions + AWS EC2</p>"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80)