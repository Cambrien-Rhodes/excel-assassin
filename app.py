from flask import Flask, render_template, request, send_file
from engine import run_assassin

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html')

@app.route('/assassinate', methods=['POST'])
def assassinate():
    uploaded_file = request.files["uploaded_file"]
    threshold = request.form.get("threshold", type=int) 
    if uploaded_file:
        processed_file = run_assassin(uploaded_file, threshold)
        return send_file(processed_file, as_attachment=True, download_name="assassinated.xlsx")
    return "No file uploaded", 400


if __name__ == '__main__':
    app.run(debug=True)