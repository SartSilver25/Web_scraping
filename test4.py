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
        paragraphs = [paragraph.get_text() for paragraph in soup.find_all()]

        # Enregistrer les données dans un fichier JSON
        with open(output_file, 'w', encoding='utf-8') as json_file:
            json.dump(paragraphs, json_file, ensure_ascii=False, indent=2)
        
        print(f"Données extraites avec succès et enregistrées dans {output_file}")
    else:
        print(f"Échec de la requête avec le code d'état {response.status_code}")

def compare_json_files(file1, file2, file3):
    # Charger les données des fichiers JSON
    with open(file1, 'r', encoding='utf-8') as json_file1:
        data1 = json.load(json_file1)

    with open(file2, 'r', encoding='utf-8') as json_file2:
        data2 = json.load(json_file2)

    with open(file3, 'r', encoding='utf-8') as json_file3:
        data3 = json.load(json_file3)

    # Comparer les données
    if data1 == data2 and data1 == data3 and data2 == data3:
        print("Les fichiers JSON sont identiques.")
    else:
        print("Les fichiers JSON sont différents.")

def create_summary_file(file1, file2, file3, output_file):
    # Charger les données des fichiers JSON
    with open(file1, 'r', encoding='utf-8') as json_file1:
        data1 = set(json.load(json_file1))

    with open(file2, 'r', encoding='utf-8') as json_file2:
        data2 = set(json.load(json_file2))

    with open(file3, 'r', encoding='utf-8') as json_file3:
        data3 = set(json.load(json_file3))

    # Trouver les données similaires
    common_data = list(data1.intersection(data2)) and list(data1.intersection(data3))

    # Enregistrer les données similaires dans un fichier JSON
    with open(output_file, 'w', encoding='utf-8') as json_file:
        json.dump(common_data, json_file, ensure_ascii=False, indent=2)
    
    print(f"Données similaires enregistrées dans {output_file}")

# URLs des pages à scraper
urls_to_scrape = ['https://www.20minutes.fr/', 'https://www.lemonde.fr', 'https://news.google.com/home?hl=fr&gl=FR&ceid=FR:fr']

# Noms des fichiers JSON de sortie
output_json_file1 = '20minutes.json'
output_json_file2 = 'lemonde.json'
output_json_file3 = 'google_news.json'
summary_output_file = 'resume.json'

# Appeler la fonction pour extraire et enregistrer les données
scrape_and_save(urls_to_scrape[0], output_json_file1)
scrape_and_save(urls_to_scrape[1], output_json_file2)
scrape_and_save(urls_to_scrape[2], output_json_file3)

# Appeler la fonction pour comparer les fichiers JSON
compare_json_files(output_json_file1, output_json_file2, output_json_file3)

# Appeler la fonction pour créer un résumé des données similaires
create_summary_file(output_json_file1, output_json_file2, output_json_file3, summary_output_file)
