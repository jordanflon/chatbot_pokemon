import nltk
nltk.download('punkt')
from nltk.stem.lancaster import LancasterStemmer
stemmer = LancasterStemmer()

import scrapping
import display as disp
import numpy as np
import tflearn
import tensorflow as tf
import random
import json
import pickle

with open("intents.json") as file:
    data = json.load(file)
try:
    with open("data.pickle", "rb") as f :
        words,labels, training, output = pickle.load(f)
except:
    words = []
    labels = []
    docs_x = []
    docs_y=[]

    for intent in data["intents"]:
        for pattern in intent["patterns"]:
            wrds = nltk.word_tokenize(pattern)
            words.extend(wrds)
            docs_x.append(wrds)
            docs_y.append(intent["tag"])

        if intent["tag"] not in labels:
            labels.append(intent["tag"])

    words = [stemmer.stem(w.lower()) for w in words if w != "?"]
    words = sorted(list(set(words)))

    labels = sorted(labels)

    training =[]
    output=[]

    out_empty=[0 for _ in range(len(labels))]


    for x,doc in enumerate(docs_x):
        bag=[]

        wrds = [stemmer.stem(w) for w in doc]

        for w in words:
            if w in wrds :
                bag.append(1)
            else:
                bag.append(0)

        output_row= out_empty[:]
        output_row[labels.index(docs_y[x])] = 1

        training.append(bag)
        output.append(output_row)

    training = np.array(training)
    output = np.array(output)

    with open("data.pickle", "wb") as f :
        pickle.dump((words, labels, training, output), f)


tf.reset_default_graph()

net = tflearn.input_data(shape=[None, len(training[0])])
net = tflearn.fully_connected(net, 16)
net = tflearn.fully_connected(net, 16)
net = tflearn.fully_connected(net, len(output[0]), activation = "softmax")
net = tflearn.regression(net)

model = tflearn.DNN(net)


try :
    model.load("model.tflearn")
except:
    model = tflearn.DNN(net)
    model.fit(training, output, n_epoch=1000, batch_size=10, show_metric=True)
    model.save("model.tflearn")



def bag_of_words(s, words):
    bag = [0 for _ in range(len(words))]

    s_words = nltk.word_tokenize(s)
    s_words = [stemmer.stem(word.lower()) for word in s_words]

    for se in s_words:
        for i,w in enumerate(words):
            if w == se :
                bag[i]= 1

    return np.array(bag)

def look_for_pokemon(l):
    # Pas de pokemon de moins de 2 caractères
    for i in l:
        if len(i)<=2:
            l.remove(i)
    with open("pokemon.txt", "r") as f :
        pokemon = f.read()
    pokemon=pokemon.replace("\n","")
    pokemon=pokemon.replace(" ","")
    pokemon=pokemon.split(",")
    for i in l:
        if i in pokemon:
            retour=i
    return str(retour)

def chat():
    print("Parlez avec le chatbot ! quit pour quitter")

    # On voit si le tag nécessite une réponse

    responses=["bonjour", "au revoir", "cava"]

    while True:
        inp = input("Vous: ")
        if inp.lower()=="quit":
            break
        check_responses=False

        result = model.predict([bag_of_words(inp, words)])[0]
        results_index = np.argmax(result)
        tag = labels[results_index]
        check_responses = tag in responses

        if tag=="au revoir":
            break


        # Open json file
        if result[results_index]>0.65:
            for tg in data["intents"]:
                if tg['tag']== tag :
                    responses = tg['responses']
        else :
            print("\nIl est possible que j'ai mal compris. \n")

        if check_responses:
            print(random.choice(responses))
        elif tag=="caracteristiques":
            try :
                possibilities_pokemon=nltk.word_tokenize(inp.lower())
                pokemon=look_for_pokemon(possibilities_pokemon)
                infos=scrapping.scrap(pokemon)
                print("\nVoici les caracteristiques de base de "+ str(pokemon) + " :")
                print(disp.caracteristiques(infos)+ "\n")
            except:
                print("\nErreur. Veuillez demander autre chose.\n")
        elif tag == "type":
            try :
                possibilities_pokemon=nltk.word_tokenize(inp.lower())
                print(possibilities_pokemon)
                pokemon=look_for_pokemon(possibilities_pokemon)
                print(pokemon)
                infos=scrapping.scrap(pokemon)
                print("\n"+str(pokemon)+" est de type "+ str(infos["type"])+ "\n")
            except :
                print("\nErreur. Veuillez demander autre chose.\n")
        elif tag == "evolution":
            try :
                possibilities_pokemon=nltk.word_tokenize(inp.lower())
                pokemon=look_for_pokemon(possibilities_pokemon)
                infos=scrapping.scrap(pokemon)
                if len(infos['evolution'])>1:
                    print("\nVoici le cycle d'evolutions complet de " + str(pokemon))
                    print(disp.evolutions(infos)+'\n')
                else :
                    print("\n" + str(pokemon) + " n'evolue pas et n'a pas de sous-evolution.\n")
            except:
                print("\nErreur. Veuillez demander autre chose.\n")
        elif tag == "description":
            try :
                possibilities_pokemon=nltk.word_tokenize(inp.lower())
                pokemon=look_for_pokemon(possibilities_pokemon)
                infos=scrapping.scrap(pokemon)
                print("\n"+infos["description"]+"\n")
            except :
                print("\nErreur. Veuillez demander autre chose. \n")
        elif tag == "talent":
            try :
                possibilities_pokemon=nltk.word_tokenize(inp.lower())
                pokemon=look_for_pokemon(possibilities_pokemon)
                infos=scrapping.scrap(pokemon)
                print("\n" + str(pokemon) + " : ")
                print("\n"+infos["talent"]+ "\n")
            except:
                print("Erreur. Veuillez demander autre chose. \n")

        elif tag == "news":
            try :
                news = scrapping.news_scrap()
                print('\nLes dernières news sont : \n')
                print(news)
                print('\n')
            except:
                print("Erreur. Veuillez demander autre chose. \n")


        elif tag == "jeux":
            try :
                infos = scrapping.jeux_pokemon()
                disp.display_jeux(infos)

            except:
                print("Erreur. Veuillez demander autre chose. \n")

        elif tag == "zouk":
            print("\nLa meilleure danse est le zouk bresilien.\n Veuillez contacter Thomas EK au 06 28 17 19 19 pour plus d'informations.\n")

        elif tag == "age":
            print("\nMon age est la valeur de l'attaque de Pikachu.\n")
        else :
            print(tag)
            print(bag_of_words(inp,words))

print("Si vous voulez re-entrainer le reseau, lancez python retrain.py")
chat()
