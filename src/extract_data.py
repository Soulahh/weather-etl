import requests
import json
from pathlib import Path
import logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s', datefmt='%d/%m/%Y - %H:%M:%S')
api_key = '02e0f4d72ff1dbce2dc69c6139b56794'
url = f'https://api.openweathermap.org/data/2.5/weather?q=Rio de Janeiro,BR&units=metric&appid={api_key}'

def extrair_dados_clima(url: str) -> list:
    
    
    response = requests.get(url)
    data = response.json()

    if response.status_code != 200:
        print("Erro na requisição")
        return []
    
    if not data:
        print("Nenhum dado retornado!")
        return []
    


    output_path = 'data/weather_data.json'
    output_dir = Path(output_path).parent
    output_dir.mkdir(parents=True, exist_ok=True)

    with open(output_path, 'w') as f:
        json.dump(data, f, indent=4)
    

    print(f"Arquivo salvo em {output_path}")
    return data

extrair_dados_clima(url)