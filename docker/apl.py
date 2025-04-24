from flask import Flask
import os

app = Flask(__name__)

@app.route("/")
def hello():
    return "Flask inside Docker!!"


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=True,host='0.0.0.0',port=port)

debug = os.environ.get('FLASK_DEBUG', 'False') == 'True'
app.run(debug=debug, host='0.0.0.0', port=port)

output_dir = "results"
os.makedirs(output_dir, exist_ok=True)  # This ensures the folder is created

