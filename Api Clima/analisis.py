import json
import pandas as pd
import xlsxwriter


class analisis:
    #leer archivos json y generar excel con los datos de la ciudad en lineas
    def leer_json(self, nombre_carpeta):
        lista = []
        with open(nombre_carpeta) as f:
            for linea in f:
                d = json.loads(linea)
                lista.append(d)
        df = pd.DataFrame(lista)
        

        ## escribimos la informacion en un excel
        def writeData(self):
            workbook = xlsxwriter.Workbook(r'C:\Users\Agustin Orsato\Devs\ejemplo\Proyectos\Api Clima\analisis-cordoba.xlsx')
            worksheet = workbook.add_worksheet('location')
            bold = workbook.add_format({'bold': True})
            worksheet.write(0,0,'name',bold)
            worksheet.write(0,1,'region',bold)
            worksheet.write(0,2,'country',bold)
            worksheet.write(0,3,'lat',bold)
            worksheet.write(0,4,'lon',bold)
            worksheet.write(0,5,'tz_id',bold)
            worksheet.write(0,6,'localtime_epoch',bold)
            worksheet.write(0,7,'localtime',bold)
            worksheet.write(0,8,'temp',bold)
            worksheet.write(0,9,'feels_like',bold)
            worksheet = workbook.add_worksheet('current')
            bold = workbook.add_format({'bold': True})
            worksheet.write(0,0,'last_updated_epoch',bold)
            worksheet.write(0,1,'last_updated',bold)
            worksheet.write(0,2,'temp_c',bold)
            worksheet.write(0,4,'is_day',bold)
            worksheet = workbook.add_worksheet('condition')
            bold = workbook.add_format({'bold': True})
            worksheet.write(0,0,'text',bold)
            worksheet.write(0,1,'icon',bold)
            worksheet.write(0,2,'code',bold)
            worksheet = workbook.add_worksheet('wind')
            bold = workbook.add_format({'bold': True})
            worksheet.write(0,0,'wind_kph',bold)
            worksheet.write(0,1,'wind_degree',bold)
            worksheet.write(0,2,'wind_dir',bold)
            worksheet = workbook.add_worksheet('rain')
            bold = workbook.add_format({'bold': True})
            worksheet.write(0,0,'rain_mm',bold)
            worksheet.write(0,1,'rain_in',bold)
            worksheet = workbook.add_worksheet('snow')
            bold = workbook.add_format({'bold': True})
            worksheet.write(0,0,'snow_mm',bold)
            worksheet.write(0,1,'snow_in',bold)

            
            #recorrer el arreglo de datos y escribir en el excel cada uno de los datos
            for i in range(len(df)):
                worksheet.write(i+1,0,df[i]['name'])
                worksheet.write(i+1,1,df[i]['region'])
                worksheet.write(i+1,2,df[i]['country'])
                worksheet.write(i+1,3,df[i]['coord']['lat'])
                worksheet.write(i+1,4,df[i]['coord']['lon'])
                worksheet.write(i+1,5,df[i]['timezone_id'])
                worksheet.write(i+1,6,df[i]['localtime_epoch'])
                worksheet.write(i+1,7,df[i]['localtime'])
                worksheet.write(i+1,8,df[i]['current']['temp_c'])
                worksheet.write(i+1,9,df[i]['current']['feels_like'])
                worksheet.write(i+1,10,df[i]['current']['is_day'])
                worksheet.write(i+1,11,df[i]['current']['condition']['text'])
                worksheet.write(i+1,12,df[i]['current']['condition']['icon'])
                worksheet.write(i+1,13,df[i]['current']['condition']['code'])
                worksheet.write(i+1,14,df[i]['current']['wind_kph'])
                worksheet.write(i+1,15,df[i]['current']['wind_degree'])
                worksheet.write(i+1,16,df[i]['current']['wind_dir'])
                worksheet.write(i+1,17,df[i]['current']['rain_mm'])
                worksheet.write(i+1,18,df[i]['current']['rain_in'])
                worksheet.write(i+1,19,df[i]['current']['snow_mm'])
                worksheet.write(i+1,20,df[i]['current']['snow_in'])
            workbook.close()
            print("!!!!!! Informacion Capturada desde write data REYYY !!!!!!", df)
        
        writeData(self)
        return df
        