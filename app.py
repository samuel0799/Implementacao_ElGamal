from flask import Flask, render_template, request, redirect, url_for, jsonify
from elgamal import encrypt_text, decrypt_pairs, set_parameters, get_parameters, generate_random_parameters

app = Flask(__name__)

encrypted_storage = [] 

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        p = int(request.form["p"])
        g = int(request.form["g"])
        x = int(request.form["x"])
        set_parameters(p, g, x)
        return redirect(url_for("cifrar"))
    return render_template("index.html", params=get_parameters())

@app.route("/generate_params", methods=["POST"])
def generate_params():
    p, g, x = generate_random_parameters(bits=512)
    set_parameters(p, g, x)
    return jsonify({"p": str(p), "g": str(g), "x": str(x)})

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
