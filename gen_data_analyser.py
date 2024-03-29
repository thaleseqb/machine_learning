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

    # the sql database manipulation was not implemented yet
    
    @property
    def set_uri(self):
        """Defines uri"""
        return self.uri
    
    @set_uri.setter
    def set_uri(self, new_uri):
        """The user could change the uri if it is desired"""
        self.uri = new_uri

    def _data_set(self):
        """Defines the data to analyse the dataset"""

        if '.csv' in self.uri:
            data = _pd.read_csv(self.uri)
            self.data = data
        
        return data

    def _replace_tilda(self, strin, dic):
        """This method removes tilda symbol and others symbols above the letters"""

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

    def processing_data(self, tilda):
        data = self._data_set()
        column_list = data.columns

        for index, iten in enumerate(column_list):
            column = _np.array(data[iten]).tolist()
            if isinstance(column[0], str):
                if tilda:
                    column = self._replace_tilda(' '.join(column), self.dic).split()
                    data[iten] = column
                else:
                    data[iten] = ' '.join(column).lower().split()

                dic = self.map
                keys = list(dic.keys())
                # esse trecho de codigo precisa abranger outras possibilidades
                if keys[0] in _np.array(data[iten]):
                    data[iten] = data[iten].map(dic)

        return data
