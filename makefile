#INSTALAR DEPENDENCIAS NECESARIAS
instalar:
					sudo apt-get install python2.7 python-pip python-dev build-essential python-qt4
					sudo pip install -r dependencias/requirements.txt
					sudo pip install tweepy networkx matplotlib

#EJECUTAR LA APLICACIÓN				
ejecutar:
					cd src/ && python -W ignore inicio.py

#EJECUTAR LOS TEST UNITARIOS					
tests:
					cd test/ && python test.py

#BORRAR MANUALMENTE TODOS LOS ARCHIVOS DE LOS DIRECTORIOS TWEETS Y SEGUIDOS
borrar:
					cd datos/tweets/ && rm *
					cd datos/seguidos/ && rm *
					
#CREAMOS LOS DIRECTORIOS TWEETS Y SEGUIDOS, POR SI ALGUNA VEZ LOS BORRAMOS
crearDirectorios:
					mkdir datos
					cd datos && mkdir tweets/
					cd datos && mkdir seguidos/
					
#CREAMOS LA DOCUMENTACIÓN DE LA API DE LA APLICACIÓN EN FORMATO PDF
documentacionPDF:
					epydoc --parse-only --name "Categorizacion de Informacion en Redes Sociales. Aplicacion a la Ciberseguridad." -o doc/DocumentacionPDF --pdf src/inicio.py src/creaVentanas.py src/funcionesTwitter.py src/manejoGrafo.py src/grafo.py src/finGrafo.py src/informacion.py src/categoria.py src/error.py src/alertaUsuario.py
					cp doc/DocumentacionPDF/api.pdf doc/
					mv doc/api.pdf doc/CategorizacionDeInformacionEnRedesSocialesAPI.pdf
				
#CREAMOS LA DOCUMENTACIÓN DE LA API DE LA APLICACIÓN EN FORMATO HTML
documentacionHTML:
					epydoc --parse-only --name "Categorizacion de Informacion en Redes Sociales. Aplicacion a la Ciberseguridad." -o doc/DocumentacionHTML --html src/inicio.py src/creaVentanas.py src/funcionesTwitter.py src/manejoGrafo.py src/grafo.py src/finGrafo.py src/informacion.py src/categoria.py src/error.py src/alertaUsuario.py
