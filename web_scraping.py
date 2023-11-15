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

# URL de la page à scraper
url_to_scrape = 'https://www.forum.fr/'

# Nom du fichier JSON de sortie
output_json_file = 'forum.json'

# Appeler la fonction pour extraire et enregistrer les données
scrape_and_save(url_to_scrape, output_json_file)
