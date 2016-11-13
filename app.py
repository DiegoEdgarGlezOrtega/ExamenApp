import web
import csv

render = web.template.render('')
urls = (
    
    '/(.*)','index'
    
)
class index:
    def GET(self,resultados):
        datos=[]
        with open("cct13.csv","r") as file:
            data=csv.reader(file,delimiter=",")
            for row in data:
                 datos.append(row)

        
        AllCentros=[]
        Urbanos=[]
        Rurales=[]

            
        def BusquedaDeCentroEducativoUrbano():
            for a in range(len(datos)):
                   Urbanos= datos[a][8]
            return Urbanos

        def BusquedaDeCentroEducativoRural():
            
            for a in range(len(datos)):
                   Rurales=datos[a][9]
            return Rurales

        resultados=[BusquedaDeCentroEducativoUrbano(),BusquedaDeCentroEducativoRural()]

        return render.index(resultados)
            
        

    
if __name__ == '__main__':
    app = web.application(urls,globals())
    web.config.debug = True
    app.run()