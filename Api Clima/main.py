import api, analisis
import sys


def main():
	apiMain = api.API()
	analsisMain = analisis.analisis()
	apiMain.getData()
	analsisMain.leer_json('...\Api Clima\analisis-cordoba.xlsx')





if __name__ == "__main__":
    main()