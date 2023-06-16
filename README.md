# Web Service de Consulta de Acciones

### Integrantes:
- Sergio Escudero Tabares - 2040801
- Esteban Andrés Hernandez Cortés - 2042817

Este es un web service que permite consultar información sobre acciones utilizando el método 'POST'.

Instrucciones para ejecutar el web service:

1. Asegúrate de tener Python instalado en tu sistema.

2. Instala las dependencias necesarias de python, usa el siguiente comando "pip install -r requirements.txt"

3. Para ejecutar el web service utiliza el siguiente comando "python app.py", en la consola estará ejecutandose el web service, y podrás ver todas las consultas que se realizan a este mismo.

Con esto el web service estará en funcionamiento, para poder consultar valores de una acción tienes dos alternativas:

## Consultar por medio de un archivo python

1. En el archivo ejemplo.py encontrará la lógica para solicitar una búsqueda al web service, puedes editar el json 'data' para variar la acción a consultar y las fechas.

2. Para ejecutarlo puedes utilizar el comando "python ejemplo.py", el cual te retornará en consola el resultado de la búsqueda.

## Consultar por medio de cURL

1. En la carpeta raíz se encuentra un datosEjemplo.json, el cual si deseas puedes modificar para consultar otra acción u otro rango de fechas.

2. Para poder hacer una consulta al web service con ese json puedes utilizar el comando:
- curl -X POST -H "Content-Type: application/json" -d @datosEjemplo.json http://localhost:5000/

3. Este comando te retornará en consola el resultado de la búsqueda.
