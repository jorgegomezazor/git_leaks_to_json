import pandas as pd
from git import Repo
import re, signal, sys, time

def handler_signal(signal, frame): # Ctrl + C
    print('\n\n [!] Out......... \n') # Mensaje de salida
    sys.exit(1)
signal.signal(signal.SIGINT,handler_signal) 
REPO_DIR = './skale/skale-manager' # Directorio del repositorio
def extract(url): # Clono el repositorio
    repo = Repo(url) # Obtengo los commits
    commits = open('commits.txt', 'w') 
    for commit in repo.iter_commits(): # Obtengo los archivos modificados
        commits.write(str(commit.message) + '\n') # Escribo los commits en un fichero
def transform():
    palabras_clave = ['password', 'secret', 'key', 'credential', 'access', 'private', 'secret'] # Palabras clave
    git_leaks = []
    commits = open('commits.txt', 'r') # Leo el fichero de commits
    for linea in commits:
        for p in palabras_clave:
            if re.search(p, linea): # Si la palabra clave está en el commit
                git_leaks.append(linea) # Añado el commit a la lista de leaks
    return git_leaks
def load(leaks):
    df = pd.DataFrame(leaks)
    df.to_json('git_leaks.json') # Guardo los leaks en un fichero json
if __name__ == '__main__':
    extract(REPO_DIR)
    leaks = transform()
    load(leaks)
