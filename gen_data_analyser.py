from sklearn.svm import LinearSVC, SVC
from sklearn.tree import DecisionTreeClassifier
import pandas as pd
import numpy as np

class MLDataAnalysis:

    def __init__(self, uri):
        self.uri = uri

    # por enquanto essa classe é apenas um esqueleto do que eu quero que ela seja futuramente.
    # quero automatizar as manipulações que geralmente são feitas nas tabelas proveniente das
    # bases de dados que podem vir de uri's ou de servidores sql.

    # Essa função vai ler e armazenar os dados referentes a nossa base de dados que será analisada
    def reading_uri(self):
        if '.csv' in self.uri:
            data = pd.read_csv()

    # talvez seja legal agrupar as informações por classificações categóricas e numéricas
    # acredito que isso não seja exatamente uma tarefa muito simples porque parece ser 
    # subjetivo, mas é possível tentar.

    # Essa função vai realizar alguns tratamentos necessários na nossa base de dados
    def processing_data(self):
        pass

