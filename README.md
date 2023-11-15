# Web_scraping
Dans le code on definit la fonction scrape and save qui prend en paramètre l'url et le output file pour avoir l'url du site que l'on veut et ensuite crée le fichier de sortie avec les éléments du site qui sera crée une fois la fonction démmaré
on crée la reponse qui va faire la requetes à l'url passer en paramètre pour stocker les informations dans la variable reponse
si la réponse est valide on recois le code 200 et on va pouvoir crée un objet de la classe beautifulsoup qui va prendre la réponse pour l'analyser (parser)
on crée une liste "paragraphs" qui va récupérer tout les paragraphes du site
les deux ligne suivante vont ouvrir un fichier json en mode écriture pour pouvoir y mettre tout les paragraphes du site web dedans
Et pour finir on dit a l'utilisateur que les données on bien été sauvegarder ou non
Et en fin de page on peut modifier le url to scrape pour changer de site que l'on veut scrape et dessous changer le nom du fichier json
