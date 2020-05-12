# Chatbot Pokemon

A chatbot using a neural network to predict the output of the user and in the same time scraping data from a website to return the response. (HTML , Python , JSON)

--------------------------------------------------------------------------------------------------------
Files :

	- scrapping.py : fichier python qui s'occupe de scrap les données utiles à notre chatbot
	- display.py : fichier python qui affiche les resultats 
	- intents.json : tous les patterns a reconnaitres dans les phrases de l'utilisateur 
	- main.py : chatbot pour dialoguer avec la console 
	- main2_chatbot.py : chatbot pour dialoguer avec Discord ou Messenger
	- pokemon.txt : tous les noms de pokemons
	- chatbot_messenger.py : programme python du Chatbot Messenger 
	- chatbot_discord.py : programme python du chatbot Discord
	- retrain.py : programme python permettant de supprimer tous les fichiers du folder hormis ceux cités précédement
		            et donc sert à re-entrainer notre model de Deep learning en cas de changement
--------------------------------------------------------------------------------------------------------

L'activation du chatbot nécessite python 3.6. Une version ultérieure ne fonctionne pas.

Pour cela, on peut créer un environnement virtuel : (nous utilons l'environnement anaconda)

  - On ouvre un CMD
  - On se place dans le répertoire du projet (cd path)

  -> conda create -n chatbot python=3.6 (sans espace pour python=3.6, et créer une seule fois suffit)

  - On active le chatbot via la commande activate chatbot

  -> il est possible que la réinstallation des packages soit nécessaire, avec une version
  de tensorflow à 1.14

  Pour cela:

  -> pip install numpy
  -> pip install nltk
  -> pip install tensorflow==1.14
  -> pip install tflearn
  -> pip install selenium
  -> pip install tflearn
  -> pip install pandas
  -> pip install requests
  -> pip install bs4

 
  - Pour lancer le chatbot et dialoguer en console avec lui via la console :

  -> python main.py

Nous avons fait le choix de ne pas utiliser d'API mais plutôt d'utiliser le scrapping de données sur des pages web, 
la plupart des API étaient en anglais tout comme les noms de pokemon, c'est pourquoi nous utilisons cette méthode.

Notre chatbot fonctionne avec un reseaux de neuronnes qui analyse la phrase rentrée par un user et nous renvoie 
une liste de probabilité selon les tag/ pattern a identifier.

--------------------------------------------------------------------------------------------------------
Vidéo explication code (7min):  https://youtu.be/DBEkaccdS8o

Vidéo demonstration du chatbot sur discord (3min) : https://youtu.be/oodcWX87W-U
(suite rapide de la vidéo du dessus) gestion des erreurs par le tchatbot (20 sec) :  https://youtu.be/dXIPAa0QYqs

pour lancer le bot il faut au préalable faire des manipulation sur discord  app pour obtenir le token de 
notre discord et ensuite celui de notre BOT pour lui donner les permissions : 

	->python chatbot_discord.py

--------------------------------------------------------------------------------------------------------
Video demonstration du chatbot sur Messenger ( 2 min) : https://www.youtube.com/watch?v=D8eAA3Atno8

une fois les manipulation URL de rappel et verify token rentré on peut utiliser le chatbot avec :

	->python chatbot_messenger.py

---------------------------------------------------------------------------------------------------------
