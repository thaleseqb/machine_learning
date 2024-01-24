from sklearn.svm import LinearSVC, SVC
from sklearn.tree import DecisionTreeClassifier
import pandas as _pd
import numpy as _np

class MLDataAnalysis:

    def __init__(self, uri, version):
        self.uri = uri

        if 'portuguese' in version:
            self.map = {'sim':1,'nao':0}
        elif 'english' in version:
            self.map =  {'yes':1, 'no':0}

        self.dic = {
                ord('a'):_np.array([ord('à'),ord('á'),ord('ã'),ord('â')]),
                ord('o'): _np.array([ord('ó')]),
                ord('i'): _np.array([ord('í')]),
                ord('e'): _np.array([ord('é')]),
                ord('u'): _np.array([ord('ú')])
            }
        
        self.data = None
        
    # por enquanto essa classe é apenas um esqueleto do que eu quero que ela seja futuramente.
    # quero automatizar as manipulações que geralmente são feitas nas tabelas proveniente das
    # bases de dados que podem vir de uri's ou de servidores sql.

    # Essa função vai ler e armazenar os dados referentes a nossa base de dados que será analisada

    # é interessante identificar quando uma base de dados possui 'sim/yes' e 'não/no'
    # para isso seria interessante fazer uma estrutura de repetição para percorrer os dados e juntamente com o mapa 
    
    # @property
    # def uri(self):
    #     """."""
    #     return self.uri
    
    # @uri.setter
    # def uri(self, new_uri):
    #     """Defines a new uri"""
    #     self.uri = new_uri

    def _data_set(self):
        """Defines the data to analyse the dataset"""

        if '.csv' in self.uri:
            data = _pd.read_csv(self.uri)
            self.data = data
        
        return data 

    def processing_data(self):
        data = self._data_set()
        column_list = data.columns

        for index, iten in enumerate(column_list):
            column = _np.array(data[iten]).tolist()
            if isinstance(column[0], str):
                data[iten] = ' '.join(column).lower().split()

                dic = self.map
                keys = list(dic.keys())
                # esse trecho de codigo precisa abranger outras possibilidades
                if keys[0] in _np.array(data[iten]):
                    data[iten] = data[iten].map(dic)

        return data

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