from api.parsers.grammars.g_num_pairs_list import parse
from api import an_known_format as formats
import os
from random import uniform
# import grammars
class NumPairsList:
    """ parsea como las lineas como una serie, de listas de pares x,y donde x puede
        ser un numero o un label y si x no aparece en el par se toma 1 2 3 4 ... por defc
        [[value1,value2],....,[valuen,valuem]]
    """
    def parse(self, data):
        """ Ver si matchea el texto "data" completo con la gramatica definida! 
        retorna un FK si matchea con num separados por saltos de linea
        val"salto"... """
        info = parse(data)
        if info:
            formts=[]
            new_format=formats.PairsSeries()
            new_format.reset_with_series(info)
            formts.append((new_format,1))
            return formts
        return None

    def help(self):
        return ''' parsea como las lineas como una serie, de listas de pares x,y donde x puede
        ser un numero o un label y si x no aparece en el par se toma 1 2 3 4 ... por defc
                EJ: 
                [[1.1,1.2],[2.1,2.2]]
                [[3.1,3.2],[4.1,4.2]]
                [[5.1,5.2],[6.1,6.2]]
                [[7.1,7.2],[8.1,8.2]]'''


    def data_generator(self,path ,amount=50, on_top=50, below=100):
        ''' Genera juego de datos con el formato que reconoce el parser para analizarlo
        amount= 50 cantidad de lineas, lineas =label + value +'\\n'
        on_top=50  below=100 numeros x on_top<=x<=below
        '''
        data_files = [item
                      for item in os.listdir(path) if item.__contains__("d_num_pairs_list_")]
        file = open(path+"/d_num_pairs_list_" +
                    str(len(data_files)+1)+".txt", "w")
        for item in range(0, amount):
            data = ''
            num_of_elements=int(uniform(1,amount))
            middle_data = ''
            for x in range(0, num_of_elements):
                middle_data +=str([uniform(on_top, below)for x in range(0, 2)])+","
            middle_data = middle_data[:-1]
            data+="["+middle_data+"]"
            file.write(data+"\n")
        file.close()
