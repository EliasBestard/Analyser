from matplotlib import pyplot
from highcharts import Highchart
import random

def IsListOfTuple_StrInt(list):
    """ Chequea que 'list' sea una lista de tuplas[(str,int)].
    Retorna dos listas, ([str],[int]) """
    labels = []
    values = []
    for item in list:
        if type(item) == tuple:
            labels.append(item[0])
            values.append(item[1])
        else:
            # labels.append("")
            values.append(item)
    return labels, values


class Line_Graph:
    """ Crear un grafico de linea """

    def graphic(self, output,format_known):
        """ Graficar los elementos con sus labels si tienen y sale por el output """
        # self.__elements = format_known.elements
        # self.__labels, self.__values = IsListOfTuple_StrInt(self.__elements)
        # print(self.__elements)
        if output == "stdout":
            return self.__make_graph(format_known)
        return self.__make_JS_code(format_known)

    def __make_graph(self, format_known):
        ''' hace el grafico en pyplot '''
        try:
            if not format_known.labels:
                pyplot.plot(format_known.elements)
                pyplot.show()
            else:
                pyplot.plot(format_known.values)
        except:
            return

    def __make_JS_code(self, format_known):
        ''' Genera el codigo de JS para highcharts y lo retorna '''
        chart = Highchart(renderTo="line_container_" +
                          str(random.uniform(0, 999999)))
        chart.set_options('chart', {})
        options = {
            'title': {
                'text': 'A Line Chart'
            },
            'tooltip': {
                'pointFormat': '{series.name}: <b>{point.percentage:.1f}%</b>'
            },
            'plotOptions': {
                'pie': {
                    'allowPointSelect': True,
                    'format': '<b>{point.name}</b>: {point.value} ',
                }
            }
        }
        chart.set_dict_options(options)
        if format_known.series:
            for item in range(len(format_known.values)):
                data = format_known.values[item]
                label = format_known.labels[item]
                chart.add_data_set(data=data, name=label, series_type="line")
        else:
            chart.add_data_set(format_known.elements, "line")
        chart.buildhtml()
        return chart.content
