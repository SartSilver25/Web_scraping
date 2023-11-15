import requests
from bs4 import BeautifulSoup
import json

def scrape_and_save(url, output_file):
    # Envoyer une requête GET à l'URL
    response = requests.get(url)

    # Vérifier si la requête a réussi (statut 200)
    if response.status_code == 200:
        # Analyser le contenu HTML de la page
        soup = BeautifulSoup(response.text, 'html.parser')

        # Extraire le texte de toutes les balises <p>
        paragraphs = [paragraph.get_text() for paragraph in soup.find_all('p')]

        # Enregistrer les données dans un fichier JSON
        with open(output_file, 'w', encoding='utf-8') as json_file:
            json.dump(paragraphs, json_file, ensure_ascii=False, indent=2)
        
        print(f"Données extraites avec succès et enregistrées dans {output_file}")
    else:
        print(f"Échec de la requête avec le code d'état {response.status_code}")

def compare_json_files(file1, file2):
    # Charger les données des fichiers JSON
    with open(file1, 'r', encoding='utf-8') as json_file1:
        data1 = json.load(json_file1)

    with open(file2, 'r', encoding='utf-8') as json_file2:
        data2 = json.load(json_file2)

    # Comparer les données
    if data1 == data2:
        print("Les fichiers JSON sont identiques.")
    else:
        print("Les fichiers JSON sont différents.")

# URL de la page à scraper
url_to_scrape = ['https://www.20minutes.fr/', 'https://www.lemonde.fr/']

# Noms des fichiers JSON de sortie
output_json_file1 = '20minutes.json'
output_json_file2 = 'lemonde.json'

# Appeler la fonction pour extraire et enregistrer les données
scrape_and_save(url_to_scrape[0], output_json_file1)
scrape_and_save(url_to_scrape[1], output_json_file2)

# Appeler la fonction pour comparer les fichiers JSON
compare_json_files(output_json_file1, output_json_file2)
