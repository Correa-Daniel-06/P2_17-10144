--Listado  organizaciones

	Este script permite listar todas las organizaciones a las que tienes acceso con la API de Cisco Meraki.

-- Requisitos
	- Python 3.8 o superior.
	- Clave de API válida.

-- Uso
1. Clona este repositorio:
   bash : git clone https:(https://github.com/Correa-Daniel-06/P2_17-10144)
2. Instalar dependencias (requests) con: pip install requests
3. Ejecutar el script: python3 main.py

-Descripción
Script main.py de la rama principal genera una lista con la información de todas las organizaciones a las que tiene acceso la key de la api de meraki suministrada. Para ello se extrae desde la api la lista de organizaciones con acceso, con nombre, ubicación, region e id. 

script main.py de la rama de inventario genera un archivo csv de los dispositivos que de tipo wireless y appliance que se encuentran en la organización a la cual se tiene acceso desde la api  key, de esta forma se obtiene y se imprime en pantalla una lista de dispositivos con informaci´´on expecífica, como modelo, tipo de producto, id, direcciones mac e ip. De toda esta lista se filtran aquellos de tipo wireless y appliance que son los que se encuentran generados dentro del archivo csv. En dicho archivo se almacena el nombre del dispositivo, el modelo, la dirección mac, la dirección ip publica, la dirección ip lan, el serial y el estatus de los dispositivos filtrados. Esto permite obtener información específica de los equipos que deseamos estudiar. 
