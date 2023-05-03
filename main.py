from flask import Flask, render_template, request, redirect

#variable
app = Flask(__name__)
nom = ""
llistaNoms=[]

#definimos la ruta
@app.route("/")
@app.route("/inici")
def inici():
    #return "<h1>Hola</h1>"
    nomAula = "Info3"
    return render_template("inici.html", nom="Delia", nomAula=nomAula)

@app.route("/info")
def informacio():
    paramRebut = request.args.get("param1")
    paramRebut2 = request.args.get("param2")

    print(llistaNoms)
    return render_template("info.html", paramRebut=paramRebut, paramRebut2=paramRebut2, nomPost=nom, llistaNoms=llistaNoms)

@app.route("/registrar", methods=["POST"])
def registrar():
    # Si és un mètode post, ha de ser un .form no un .args
    nom = request.form.get("nom")
    print(nom)
    llistaNoms.append(nom)
    return redirect("/info")


if __name__ == "__main__":
    app.run(debug=True)

