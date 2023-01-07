# Authors 
************KACI Fraoucen************
**********IZOUAOUEN Aghiles**********
**********HAMAIDI Claas************** 


# Project Name 
Data Engineering 

# About Project 

1 - Flask / Machine Learning 

Les étapes à implémenter dans la partie machine learning sont (davantage de fonctionnalités seront éventuellement ajoutées) : 

    -   Chargement de données depuis un fichier local 
    -   Transformation/Preprocessing des données 
    -   Application d'un modèle de regression linéaire 
    -   Première évaluation du modèle 




2 - Github 

les étapes réalisées à présent :

    -   Création d'un repository public 
    -   Initialisation Git 
    -   Commit du fichier README


3 - Docker

Il y a deux manières possible de lancer notre application flask en local :

    1- La première manière la plus fastidieuse consiste à refaire quasiment toutes les étapes que l'on a suivi afin de construire notre image et lancer un conteneur docker basé sur cette image pour exécuter notre appliaction.
    
    2- La deuxième manière est la manière à préviligier, qui consiste à seulement récupérer notre image docker que l'on a construit et push auparavant sur le dockerhub, cette image est déjà prête il suffit juste de lancer le conteneur qui exécute notre application.

Les étapes à suivre afin de reconstruire  l'image Docker de A à Z et de créer un conteneur à partir de cette image pour lancer notre application Flask  (la première façon): 

    1- faire un git clone du projet : git clone git@github.com:fraoucen/Projet_Data_Engineering.git
    
    2- S'assurer que le deamon docker est connecté au dockerhub pour pouvoir pull une image python:3.8.16 qui est l'image de base à partir de laquelle nous avons contruit notre image.
    
    3- se mettre à la racine du projet git ou se trouve notre Dockerfile
    
    4- Construire l'image graçe au Dockerfile qui décrit le contenu de l'image : docker build -t nom_de_image.
    
    5- Créer un volume sur la machine hôte : docker volume create --driver local --opt type=none --opt device="chemin_vers_le_projet_git" --opt o=bind nom_du_volume
    
    6- Lancer le script portscan.sh qui permet de savoir une plage de ports ceux qui sont open et ceux qui sont close afin d'éviter de choisir un port déjà utiliser lorsque on créé le conteneur et on fait le mapping des ports : ./portscan.sh 127.0.0.1 debut_de_la_plage_de_numero_de_port fin_de_la_plage_de_numero_de_port (ex : ./portscan.sh 127.0.0.1 5000 5020 pour voir les ports qui sont utilisés parmi les ports numurotés de 5000 à 5020 )
    
    7- Créer un conteneur dans lequel l'application s'exécute (ici le port 5000 sur le host n'est pas utilisé) : docker run -d --name nom_du_conteneur  -v nom_du_volume:/app/ -p 5000:5000 nom_de_image_docker

Les étapes à suivre afin d'éviter de reconstruire l'image et d'utiliser une image déjà prête pour créer un conteneur à partir de cette image pour lancer notre application Flask  (la deuxième façon):
    
    1- S'assurer que le deamon docker est connecté au dockerhub pour pouvoir pull l'image

    2- Pull l'image : docker pull aghilesizou/projet_data_engineering_repository:latest

    3- Créer un volume sur la machine hôte : docker volume create --driver local --opt type=none --opt device="chemin_vers_le_projet_git" --opt o=bind nom_du_volume

    4- Lancer le script portscan.sh (ex : ./portscan.sh 127.0.0.1 5000 5020 pour voir les ports qui sont utilisés parmi les ports numurotés de 5000 à 5020)

    5- Créer un conteneur dans lequel l'application s'exécute (ici le port 5000 sur le host n'est pas utilisé) : docker run -d --name nom_du_conteneur  -v nom_du_volume:/app/ -p 5000:5000 nom_de_image_docker


