from cherrypy import expose
import cherrypy
from jinja2 import Environment, FileSystemLoader
env = Environment(loader=FileSystemLoader('templates'))
from restaurantes import *
from pyswip import *
cherrypy.server.socket_host = '192.168.0.106'
p=Prolog()

##agregarRest(nombre,tipoComida,ubicacion,telefono,horario)

class Adder:

	@expose
	def index(self):
		tmpl = env.get_template('agregarRest.html')
		return tmpl.render()

	@expose
	def addRest(self, nombreRest,tipoComida,ubicacionrest,numeroRest,horarioRest):
		#arch = file("rest.pl","a")
		#functor="restaurante("
		#functor=functor+nombreRest+","+tipoComida+","+ubicacionrest+","+numeroRest+","+horarioRest+")."
		#arch.write(functor)
		#p.assertz("'"+functor+"'") #con esto carga las varas a la base de conocimientos

		agregarRest(nombreRest,tipoComida,ubicacionrest,numeroRest,horarioRest)
		return self.index()

if __name__ == "__main__":
    from cherrypy import quickstart
    quickstart(Adder())
    
