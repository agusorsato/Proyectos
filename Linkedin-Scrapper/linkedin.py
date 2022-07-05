from selenium import webdriver
import time
from bs4 import BeautifulSoup
import xlsxwriter
from datetime import datetime
import pandas as pd



class Linkedin():
    def getData(self):
        options = webdriver.ChromeOptions()
        options.binary_location = r'..Application\chrome.exe'
        chrome_driver_binary = r'..linkedin-scrapper\chromedriver.exe'
        driver = webdriver.Chrome(chrome_driver_binary, chrome_options=options)

        driver.get('https://www.linkedin.com/login')
        driver.find_element_by_id('username').send_keys('agustinorsato@gmail.com') #Enter username of linkedin account here
        driver.find_element_by_id('password').send_keys('36133238Ao')  #Enter Password of linkedin account here
        driver.find_element_by_xpath("//*[@type='submit']").click()
        time.sleep(3)

        #*********** Poner directorio de csv para leer trabajos ***************#
        ##search_key = ["go developer", "data scientist"] # Aca poner el trabajo que quieres buscar a manopla

        read_csv = pd.read_csv(r'...linkedin-scrapper\perfiles-it.csv')
        read = pd.DataFrame(read_csv)
        dataIn = read.values.tolist()
        search_key = dataIn
 
        global data
        data = []

        #*********** Recorremos todos los trabajos y buscamos las cantidades de resultados ***************#

        for i in range(len(search_key)):
            search_url = "https://www.linkedin.com/jobs/search/?distance=25.0&geoId=100446943&keywords={}".format(search_key[i])
            driver.get(search_url)
            driver.maximize_window()
            time.sleep(2)
            page = BeautifulSoup(driver.page_source,'lxml')
            try:
                title = str(page.find("h1", attrs = {'class':'jobs-search-results-list__text t-16 truncate'}).text).strip()
            except:
                title = 'None'
            try:
                number = str(page.find("small", attrs = {'class':'jobs-search-results-list__text display-flex t-12 t-black--light t-normal'}).text).strip()
            except:
                number = 'None'
            try:
                day = datetime.now().strftime("%d %B, %Y %H:%M:%S.%f")
            except:
                day = 'None'
            data.append({'title':title, 'number':number, 'datetime':day})
        
        print("!!!!!! Informacion Capturada desde pagina REYYY !!!!!!", data)
                    
        driver.quit()

    #*********** esta funcion crea e inserta los datos en un excel para su posterior analisis ***************#

    def writeData(self):
         workbook = xlsxwriter.Workbook(r'...linkedin-analisis-puestos\linkedin-scrapper.xlsx')
         worksheet = workbook.add_worksheet('DATOS')
         bold = workbook.add_format({'bold': True})
         worksheet.write(0,0,'title',bold)
         worksheet.write(0,1,'number',bold)
         worksheet.write(0,2,'datetime',bold)
         #recorrer el arreglo de datos y escribir en el excel cada uno de los datos
         for i in range(len(data)):
            worksheet.write(i+1,0,data[i]['title'])
            worksheet.write(i+1,1,data[i]['number'])
            worksheet.write(i+1,2,data[i]['datetime'])
        
         workbook.close()
         print("!!!!!! Informacion Capturada desde write data REYYY !!!!!!", data)

    #*********** esta funcion inserta los datos en un excel ya existente para su posterior analisis ***************#
    
    def insertData(self):
        read = pd.read_excel(r'...linkedin-analisis-puestos\linkedin-scrapper.xlsx', sheet_name='DATOS')
        data_frame = pd.DataFrame(read)
        newData = pd.DataFrame(data, columns=['title', 'number', 'datetime'])
        new_dataF = pd.concat([data_frame, newData])
        new_dataF.to_excel(r'...linkedin-analisis-puestos\linkedin-scrapper.xlsx', sheet_name='DATOS', index=False)
        print("!!!!!! Informacion Capturada desde insert data REYYY !!!!!! \n", new_dataF)
