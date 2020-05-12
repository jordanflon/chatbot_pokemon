def caracteristiques(infos):
    retour = "PV :" + str(infos['pv']) +"\n"
    retour += "Attaque : " + str(infos['attaque']) +"\n"
    retour += "Defense : " + str(infos['defense']) +"\n"
    retour += "Attaque Speciale : " + str(infos['attaque spe']) +"\n"
    retour += "Defense Speciale : " + str(infos['defense spe']) +"\n"
    retour += "Vitesse : " + str(infos['vitesse']) +"\n"
    return retour

def type(infos):
    retour = "Type : " + str(infos["type"])
    return retour

def evolutions(infos):
    retour = ""
    for i in range(len(infos["evolution"])):
        retour += "\nStade "+ str(i) +" : " +str(infos["evolution"][i]) 
    return retour

def description(infos):
    return  infos['description']

def talent(infos):
    return infos['talent']


def display_jeux(infos):
    for x in infos:
        print("\nLe jeu Pokemon |", str(x[0]), '| de la',str(x[3]) ,'génération est sortie sur la' , str(x[1]), 'en',str(x[2]) )
