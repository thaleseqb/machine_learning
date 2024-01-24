from sklearn.svm import LinearSVC, SVC
from sklearn.tree import DecisionTreeClassifier
import pandas as _pd
import numpy as _np

class MLDataAnalysis:

    def __init__(self, uri):
        self.uri = uri
        self.map = {'yes':1,'sim':1,'não':0,'no':0}
        self.dic = {
            ord('a'):_np.array([ord('à'),ord('á'),ord('ã'),ord('â')]),
            ord('o'): _np.array([ord('ó')]),
            ord('i'): _np.array([ord('í')]),
            ord('e'): _np.array([ord('é')]),
            ord('u'): _np.array([ord('ú')])
            }

    # por enquanto essa classe é apenas um esqueleto do que eu quero que ela seja futuramente.
    # quero automatizar as manipulações que geralmente são feitas nas tabelas proveniente das
    # bases de dados que podem vir de uri's ou de servidores sql.

    # Essa função vai ler e armazenar os dados referentes a nossa base de dados que será analisada

    # é interessante identificar quando uma base de dados possui 'sim/yes' e 'não/no'
    # para isso seria interessante fazer uma estrutura de repetição para percorrer os dados e juntamente com o mapa 
    def reading_uri(self):
        if '.csv' in self.uri:
            data = _pd.read_csv()

    # talvez seja legal agrupar as informações por classificações categóricas e numéricas
    # acredito que isso não seja exatamente uma tarefa muito simples porque parece ser 
    # subjetivo, mas é possível tentar.

    # Essa função vai realizar alguns tratamentos necessários na nossa base de dados
    def processing_data(self):
        pass

    # método para retirar as letras que possuem til
    def replace_tilda(strin, dic):

        strin = strin.lower()
        alfanumeric_string = [ord(alpha_num) for alpha_num in strin]
        alfanumeric_string = _np.array(alfanumeric_string)

        for iten in dic:
            bool_array = _np.isin(alfanumeric_string,dic[iten])
            if True in bool_array:
                replace_coord = _np.where(bool_array==True)[0]
                alfanumeric_string[replace_coord] = iten

        transformed_chr = [chr(number) for number in alfanumeric_string]
        string = ''.join(transformed_chr)

        return string