from linkedin import Linkedin
import time
import os



def main():
    linkedin = Linkedin()
    linkedin.getData()
    time.sleep(3)
    if os.path.isfile(r'C:\Users\Agustin Orsato\Devs\ejemplo\Proyectos\linkedin-analisis-puestos\linkedin-search-prueba.xlsx'):
        linkedin.insertData()
    else:
        linkedin.writeData()
    
if __name__ == "__main__":
    main()