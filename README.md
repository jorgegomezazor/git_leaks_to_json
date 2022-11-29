# Git Leaks
Obtención los leaks de un repositorio de git guardados en un json
## Funcionamiento
A continuación se explicarán los pasos necesarios para ejecutar correctamente el programa.
### Librerías
Instalar las librerías aportadas en el requirements.txt siguiendo este ejemplo:
```
pip install pandas
```
O mediante:
```
pip install -r requirements.txt
```
### Archivos
De la carpeta comprimida skale se tiene que descomprimir la carpeta que hay dentro. Esa carpeta tendrá que estar en el directorio donde se ejecute el programa. El archivo a ejectutar es git_leaks_a_json.py de esta forma:
```
python git_leaks_a_json.py
```
## Output
La salida es un json (git_leaks.json) con los leaks.
