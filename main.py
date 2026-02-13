from src.extract_data import extract_weather_data 
from src.transform_data import data_transformations
from src.load_data import load_weather_data

import os
from pathlib import Path
from dotenv import load_dotenv

import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s', datefmt='%d/%m/%Y - %H:%M:%S')

env_path = Path(__file__).resolve().parent.parent / 'config' / '.env'
load_dotenv(env_path)

API_KEY = os.getenv('api_key')

url = f'https://api.openweathermap.org/data/2.5/weather?q=Rio%20de%20Janeiro&units=metric&appid={API_KEY}'
table_name = 'rj_weather'

def pipeline():
    try:
        logging.info("1 - Extração")
        extract_weather_data(url)
        
        logging.info("2 - Transformação")
        df = data_transformations()

        logging.info("3 - Load")
        load_weather_data(table_name, df)

        print("\n" + "="*60)
        print("Pipeline concluida com sucesso!")
        print("="*60)
    
    except Exception as e:
        logging.error("Erro na pipeline: {e}")
        import traceback
        traceback.print_exc()

pipeline()