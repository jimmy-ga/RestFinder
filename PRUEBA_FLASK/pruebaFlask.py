#<link rel=stylesheet type=text/css href="{{ url_for('static', filename='style.css') }}">
from flask import Flask
from flask import render_template
import restaurantes
from flask import request
from ctypes import *

app=Flask(__name__)
listaRest=""

@app.route("/")
def index():
	return render_template('index.html')

@app.route("/consulta")
def todosRest():
	return render_template('consulta.html')

@app.route("/todosRestaurantes",methods=['GET', 'POST'])
def todosRestaurantes():
	if request.method == 'POST':
		#lista=restaurantes.imprimirRest()
		lista=restaurantes.buscaRestaurantesXNombre("abc")
		if len(lista)>0:
			return render_template("resultados.html",entradas=lista)
		else:
			return render_template("resultados.html",entradas=["No hay resultados"])
#		else:
#			return render_template("resultados.html",entradas=["No hay resultados"])

@app.route("/consultaTipo",methods=['GET', 'POST'])
def consultaTipo():
	form = SignupForm()
	if request.method == 'POST':
		tipocomida="sdf"#form.tipocomida.data
		#lista=restaurantes.restaurantesXtipo(tipocomida)
		#print lista
		return render_template("resultados.html",entradas=tipocomida)
		
if __name__=="__main__":
	#listaRest=restaurantes.imprimirRest()	
	#app.debug=True
	app.run()
