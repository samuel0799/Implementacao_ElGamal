from flask import Flask, render_template, request, redirect, url_for
from elgamal import encrypt_text, decrypt_pairs

app = Flask(__name__)

encrypted_storage = [] 

@app.route("/")
def index():
    return redirect(url_for("cifrar"))

@app.route("/cifrar", methods=["GET", "POST"])
def cifrar():
    result = {}
    if request.method == "POST":
        text = request.form["message"]
        encrypted = encrypt_text(text)
        encrypted_storage.clear()
        encrypted_storage.extend(encrypted)
        result["original"] = text
        result["encrypted"] = encrypted
    return render_template("cifrar.html", result=result)

@app.route("/decifrar", methods=["GET", "POST"])
def decifrar():
    if request.method == "POST":
        
        pairs_input = request.form["pairs"]
        
        pairs_list = []
        for pair in pairs_input.split(";"):
            a_str, b_str = pair.strip("() ").split(",")
            pairs_list.append((int(a_str), int(b_str)))
        decrypted = decrypt_pairs(pairs_list)
        return render_template("decifrar.html", decrypted=decrypted)
    return render_template("decifrar.html")

if __name__ == "__main__":
    app.run(debug=True)
