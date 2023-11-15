 # Web_scraping
 
Informations d'utilisation : 

La première étape va être de modifier les URL des sites web avec celle que vous souhaiter.
Ensuite, vous pouvez si vous le voulez modifier le nom des fichiers json de sortie pour chaque URL
Puis il vous reste juste à lancer le programme et attendre que vos fichiers apparaissent dans votre dossier et il ne vous reste plus qu'à les ouvrir pour y consulter les informations qui y ont été enregistrées.

Explication de la création du code et du code étapes par étapes :

Méthodes : 

Nous avons procédé éléments par éléments :
En commençant par le scrape puis la comparaison, et pour finir l'enregistrement qui nous à permis de ne pas nous perdre dans le code et pouvoir vérifier à chaque étape si le code était fonctionnel.

Explication du code :

Dans le code, on définit la fonction scrape and save qui prend en paramètre URL et l'output file pour avoir URL du site que l'on veut et ensuite crée le fichier de sortie avec les éléments du site qui sera créé une fois la fonction démarrée.
On crée la réponse qui va faire la requêtes à URL passer en paramètre pour stocker les informations dans la variable réponse.
Si la réponse est valide, on reçoit le code 200 et on va pouvoir créer un objet de la classe beautifulsoup qui va prendre la réponse pour l'analyser (parser).
On crée une liste "paragraphs" qui va récupérer tous les paragraphes du site.
Les deux lignes suivantes vont ouvrir un fichier json en mode écriture pour pouvoir y mettre tous les paragraphes du site web dedans.
Ensuite, on dit a l'utilisateur que les données on bien été sauvegarder ou non.
On crée une deuxième définition nommée compare_json avec 3 paramètre, ce sont trois paramètres vont être ouvert pour y mettre une variable data qui va charger les éléments du fichier json, une fois les 3 fichiers chargés, on va ensuite pouvoir comparer les 3 data pour afficher si les fichiers sont identiques ou non.
Après nous avons la fonction create_summary_file ou on lui passe 4 paramètres, les trois premier servent à ouvrir les fichiers json puis à créer une variable data dans lequel on va charger puis enregistrer les fichiers json. Une fois enregistrer, on crée une variable de type list qui fait une liste de toutes les intersections (mot commun au trois datas) ensuite, on ouvre la 4 ème variable rentrer en paramètre et on y enregistre la liste de toutes les intersections. Et on affiche à l'utilisateur que tout est bien enregistré.
Ensuite, on a la variable de type liste contenant les trois URL des sites web que l'on veut examiner et dessous changer le nom du fichier des trois json.
Les trois lignes vont être un appel à la fonctions scrape_and_save, elle est appelé trois fois pour pouvoir scrape nos trois url.
Par la suite, on appelle la fonctions compare_json_files avec en paramètre nos trois output_json qui va donc comparer les fichiers de sortie pour voir s'ils sont identiques. 
Et pour finir, on appelle la fonction create_summary_file pour créer le fichier avec les mots en commun.

Résultats de l'analyse : 

Après avoir fait des tests, nous avons conclu que les éléments communs à tous les fichiers ont bien été noté dans le fichier résumer.json. Dans les trois articles, nous n'avons pas de mot en commun, mais suite à des tests avec des articles où nous savions qu'il y avait des mots en commun, c'est mot là, on bien été placé dans notre fichier de résumer. Pour avoir plus de chance de trouver des mots communs dans notre résumé, il faut aller à ligne 15 et retirer le paramètre de la méthode find all puis exécuter le code.

Défis rencontrés : 

Vu que les sites choisis n'avais que très peu voir même pas de mot en commun nous pensions que c'était notre code qui ne fonctionnais pas donc nous avons plusieurs fois crée des versions différentes pour modifier des éléments de notre code.
L'élément le plus dur à faire pour notre part a été la fonctions scrape.
