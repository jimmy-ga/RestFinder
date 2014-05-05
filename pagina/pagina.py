from flask import Flask
from flask import render_template
import restaurantes

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/todosRestaurantes',methods=['GET', 'POST'])
def todosRestaurantes():
	#if request.method == 'POST':
		#lista=restaurantes.imprimirRest()
	lista=restaurantes.buscaRestaurantesXNombre("abc")
	if len(lista)>0:
		return render_template("resultados.html",entradas=lista)
	else:
		return render_template("resultados.html",entradas=["No hay resultados"])

if __name__ == '__main__':
    app.run(debug=False,host="192.168.1.103",port=9090)
