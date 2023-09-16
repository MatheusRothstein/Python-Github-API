import requests
import json

class ListaDeRepo():
    def __init__(self, usuario):
        self.usuario = usuario

    def requisicao_api(self):
        resposta = requests.get(f'https://api.github.com/users/{self.usuario}/repos')

        if resposta.status_code == 200:
            return resposta.json()
        else:
            return resposta.status_code

    def imprime_reposito(self):
        repositorio = self.requisicao_api()
        if type(repositorio) is not int:
            for i in range(len(repositorio)):
                print(repositorio[i]['name'])
        else:
            print(repositorio)

repositorios = ListaDeRepo('MatheusRothstein')
repositorios.imprime_reposito()
    