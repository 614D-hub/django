from flask import Flask, render_template
app=Flask(__name__)

class Item:
    def __init__(self, name):
        self.name = name
nimi = "Essi Esimerkki"
lista = [1, 1, 2, 3, 4, 5, 8, 11]
esinnet = []
esinnet.append(Item("Eka"))
esinnet.append(Item("Toka"))
esinnet.append(Item("Kolmas"))
esinnet.append(Item("Neljas"))
print(esinnet)


@app.route("/")
def hello():
    return render_template('index.html')

@app.route("/demo")
def content():
    return render_template('demo.html',nimi=nimi, lista=lista, esinnet=esinnet)



if __name__ == "__main__":
    app.run(debug=True)

