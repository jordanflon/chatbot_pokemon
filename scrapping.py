from selenium import webdriver
import requests
import bs4
import pandas as pd
import json

first_gen = ("""Bulbizarre
Herbizarre
Florizarre
Salamèche
Reptincel
Dracaufeu
Carapuce
Carabaffe
Tortank
Chenipan
Chrysacier
Papilusion
Aspicot
Coconfort
Dardargnan
Roucool
Roucoups
Roucarnage
Rattata
Rattatac
Piafabec
Rapasdepic
Abo
Arbok
Pikachu
Raichu
Sabelette
Sablaireau
Nidoran
Nidorina
Nidoqueen
Nidoran
Nidorino
Nidoking
Mélofée
Mélodelfe
Goupix
Feunard
Rondoudou
Grodoudou
Nosferapti
Nosferalto
Mystherbe
Ortide
Rafflésia
Paras
Parasect
Mimitoss
Aéromite
Taupiqueur
Triopikeur
Miaouss
Persian
Psykokwak
Akwakwak
Férosinge
Colossinge
Caninos
Arcanin
Ptitard
Têtarte
Tartard
Abra
Kadabra
Alakazam
Machoc
Machopeur
Mackogneur
Chétiflor
Boustiflor
Empiflor
Tentacool
Tentacruel
Racaillou
Gravalanch
Grolem
Ponyta
Galopa
Ramoloss
Flagadosse
Magnéti
Magnéton
Canarticho
Doduo
Dodrio
Otaria
Lamantine
Tadmorv
Grotadmorv
Kokiyas
Crustabri
Fantominus
Spectrum
Ectoplasma
Onix
Soporifik
Hypnomade
Krabby
Krabboss
Voltorbe
Électrode
Nœunœuf
Noadkoko
Osselait
Ossatueur
Kicklee
Tygnon
Excelangue
Smogo
Smogogo
Rhinocorne
Rhinoféros
Leveinard
Saquedeneu
Kangourex
Hypotrempe
Hypocéan
Poissirène
Poissoroy
Stari
Staross
M. Mime
Insécateur
Lippoutou
Élektek
Magmar
Scarabrute
Tauros
Magicarpe
Léviator
Lokhlass
Métamorph
Évoli
Aquali
Voltali
Pyroli
Porygon
Amonita
Amonistar
Kabuto
Kabutops
Ptéranote
Ronflex
Artikodin
Électhor
Sulfura
Minidraco
Draco
Dracolosse
Mewtwonote
Mew""")
first_gen = first_gen.split("\n")
#PREPROCESSING POKEMON FIRST GENERATION
def replace_last(source_string, replace_what, replace_with):
    head, _sep, tail = source_string.rpartition(replace_what)
    return head + replace_with + tail
for index, value in enumerate(first_gen):
    if value.endswith(('note ', 'note')):
        first_gen[index] = replace_last(value, 'note', '')
        first_gen[index] = first_gen[index].replace(' ', '')
        first_gen[index] = first_gen[index].lower()
    else:
        first_gen[index] = first_gen[index].replace(' ', '')
        first_gen[index] = first_gen[index].lower()

second_gen = ("""Germignon
Macronium
Méganium
Héricendre
Feurisson
Typhlosion
Kaiminus
Crocrodil
Aligatueur
Fouinette
Fouinar
Hoothoot
Noarfang
Coxy
Coxyclaque
Mimigal
Migalos
Nostenfer
Loupio
Lanturn
Pichu
Mélo
Toudoudou
Togepi
Togetic
Natu
Xatu
Wattouat
Lainergie
Pharampnote
Joliflor
Marill
Azumarill
Simularbre
Tarpaud
Granivol
Floravol
Cotovol
Capumain
Tournegrin
Héliatronc
Yanma
Axoloto
Maraiste
Mentali
Noctali
Cornèbre
Roigada
Feuforêve
Zarbi
Qulbutoké
Girafarig
Pomdepik
Foretress
Insolourdo
Scorplane
Steelix
Snubbull
Granbull
Qwilfish
Cizayoxnote
Caratroc
Scarhinonote
Farfuret
Teddiursa
Ursaring
Limagma
Volcaropod
Marcacrin
Cochignon
Corayon
Corayôme
Rémoraid
Octillery
Cadoizo
Démanta
Airmure
Malosse
Démolossenote
Hyporoi
Phanpy
Donphan
Porygon2
Cerfrousse
Queulorior
Debugant
Kapoera
Lippouti
Élekid
Magby
Écrémeuh
Leuphorie
Raikou
Entei
Suicune
Embrylex
Ymphect
Tyranocifnote
Lugia
Ho-Oh
Celebi
""")
second_gen = second_gen.split("\n")
#PREPROCESSING POKEMON SECOND GENERATION
def replace_last(source_string, replace_what, replace_with):
    head, _sep, tail = source_string.rpartition(replace_what)
    return head + replace_with + tail
for index, value in enumerate(second_gen):
    if value.endswith(('note ', 'note')):
        second_gen[index] = replace_last(value, 'note', '')
        second_gen[index] = second_gen[index].replace(' ', '')
        second_gen[index] = second_gen[index].lower()
    else:
        second_gen[index] = second_gen[index].replace(' ', '')
        second_gen[index] = second_gen[index].lower()


third_gen =("""Arcko
Massko
Jungkonote
Poussifeu
Galifeu
Braségalinote
Gobou
Flobio
Laggronnote
Medhyèna
Grahyèna
Zigzatonnote
Linéonnote
Chenipotte
Armulys
Charmillon
Blindalys
Papinox
Nénupiot
Lombre
Ludicolo
Grainipiot
Pifeuil
Tengalice
Nirondelle
Hélédelle
Goélise
Bekipan
Tarsal
Kirlia
Gardevoirnote
Arakdo
Maskadra
Balignon
Chapignon
Parécool
Vigoroth
Monaflèmit
Ningale
Ninjask
Munja
Chuchmur
Ramboum
Brouhabam
Makuhita
Hariyama
Azurill
Tarinor
Skitty
Delcatty
Ténéfixnote
Mysdibulenote
Galekid
Galegon
Galekingnote
Méditikka
Charminanote
Dynavolt
Élecsprintnote
Posipi
Négapi
Muciole
Lumivole
Rosélia
Gloupti
Avaltout
Carvanha
Sharpedonote
Wailmer
Wailord
Chamallot
Caméruptnote
Chartor
Spoink
Groret
Spinda
Kraknoix
Vibraninf
Libégon
Cacnea
Cacturne
Tylton
Altarianote
Mangriff
Séviper
Séléroc
Solaroc
Barloche
Barbicha
Écrapince
Colhomard
Balbuto
Kaorine
Lilia
Vacilys
Anorith
Armaldo
Barpau
Milobellus
Morphéo
Kecleon
Polichombr
Branettenote
Skelénox
Téraclope
Tropius
Éoko
Absolnote
Okéoké
Stalgamin
Oniglalinote
Obalie
Phogleur
Kaimorse
Coquiperl
Serpang
Rosabyss
Relicanth
Lovdisc
Draby
Drackhaus
Drattaknote
Terhal
Métang
Métalossenote
Regirock
Regice
Registeel
Latiasnote
Latiosnote
Kyogrenote
Groudonnote
Rayquazanote
Jirachi
Deoxys
""")
third_gen = third_gen.split("\n")
#PREPROCESSING POKEMON THIRD GENERATION
def replace_last(source_string, replace_what, replace_with):
    head, _sep, tail = source_string.rpartition(replace_what)
    return head + replace_with + tail
for index, value in enumerate(third_gen):
    if value.endswith(('note ', 'note')):
        third_gen[index] = replace_last(value, 'note', '')
        third_gen[index] = third_gen[index].replace(' ', '')
        third_gen[index] = third_gen[index].lower()
    else:
        third_gen[index] = third_gen[index].replace(' ', '')
        third_gen[index] = third_gen[index].lower()

fourth_gen = ("""Tortipouss
Boskara
Torterra
Ouisticram
Chimpenfeu
Simiabraz
Tiplouf
Prinplouf
Pingoléon
Étourmi
Étourvol
Étouraptor
Keunotor
Castorno
Crikzik
Mélokrik
Lixy
Luxio
Luxray
Rozbouton
Roserade
Kranidos
Charkos
Dinoclier
Bastiodon
Cheniti
Cheniselle
Papilord
Apitrini
Apireine
Pachirisu
Mustébouée
Mustéflott
Ceribou
Ceriflor
Sancoki
Tritosor
Capidextre
Baudrive
Grodrive
Laporeille
Lockpinnote
Magirêve
Corboss
Chaglam
Chaffreux
Korillon
Moufouette
Moufflair
Archéomire
Archéodong
Manzaï
Mime Jr.
Ptiravi
Pijako
Spiritomb
Griknot
Carmache
Carchacroknote
Goinfrex
Riolu
Lucarionote
Hippopotas
Hippodocus
Rapion
Drascore
Cradopaud
Coatox
Vortente
Écayon
Luminéon
Babimanta
Blizzi
Blizzaroinote
Dimoret
Magnézone
Coudlangue
Rhinastoc
Bouldeneu
Élekable
Maganon
Togekiss
Yanmega
Phyllali
Givrali
Scorvol
Mammochon
Porygon-Z
Gallamenote
Tarinorme
Noctunoir
Momartik
Motisma
Créhelf
Créfollet
Créfadet
Dialga
Palkia
Heatran
Regigigas
Giratina
Cresselia
Phione
Manaphy
Darkrai
Shaymin
Arceus
""")
fourth_gen = fourth_gen.split('\n')
#PREPROCESSING POKEMON FOURTH GENERATION
def replace_last(source_string, replace_what, replace_with):
    head, _sep, tail = source_string.rpartition(replace_what)
    return head + replace_with + tail
for index, value in enumerate(fourth_gen):
    if value.endswith(('note ', 'note')):
        fourth_gen[index] = replace_last(value, 'note', '')
        fourth_gen[index] = fourth_gen[index].replace(' ', '')
        fourth_gen[index] = fourth_gen[index].lower()
    else:
        fourth_gen[index] = fourth_gen[index].replace(' ', '')
        fourth_gen[index] = fourth_gen[index].lower()


fifth_gen = ("""Victini
Vipélierre
Lianaja
Majaspic
Gruikui
Grotichon
Roitiflam
Moustillon
Mateloutre
Clamiral
Ratentif
Miradar
Ponchiot
Ponchien
Mastouffe
Chacripan
Léopardus
Feuillajou
Feuiloutan
Flamajou
Flamoutan
Flotajou
Flotoutan
Munna
Mushana
Poichigeon
Colombeau
Déflaisan
Zébibron
Zéblitz
Nodulithe
Géolithe
Gigalithe
Chovsourir
Rhinolove
Rototaupe
Minotaupe
Nanméouïenote
Charpenti
Ouvrifier
Bétochef
Tritonde
Batracné
Crapustule
Judokrak
Karaclée
Larveyette
Couverdure
Manternel
Venipatte
Scobolide
Brutapode
Doudouvet
Farfaduvet
Chlorobule
Fragilady
Bargantua
Mascaïman
Escroco
Crocorible
Darumarond
Darumacho
Maracachi
Crabicoque
Crabaraque
Baggiguane
Baggaïd
Cryptéro
Tutafeh
Tutankafer
Carapagos
Mégapagos
Arkéapti
Aéroptéryx
Miamiasme
Miasmax
Zorua
Zoroark
Chinchidou
Pashmilla
Scrutella
Mesmérella
Sidérella
Nucléos
Méios
Symbios
Couaneton
Lakmécygne
Sorbébé
Sorboul
Sorbouboul
Vivaldaim
Haydaim
Emolga
Carabing
Lançargot
Trompignon
Gaulet
Viskuse
Moyade
Mamanbo
Statitik
Mygavolt
Grindur
Noacier
Tic
Clic
Cliticlic
Anchwatt
Lampéroie
Ohmassacre
Lewsor
Neitram
Funécire
Mélancolux
Lugulabre
Coupenotte
Incisache
Tranchodon
Polarhume
Polagriffe
Hexagel
Escargaume
Limaspeed
Limonde
Kungfouine
Shaofouine
Drakkarmin
Gringolem
Golemastoc
Scalpion
Scalproie
Frison
Furaiglon
Gueriaigle
Vostourno
Vaututrice
Aflamanoir
Fermite
Solochi
Diamat
Trioxhydre
Pyronille
Pyrax
Cobaltium
Terrakium
Viridium
Boréas
Fulguris
Reshiram
Zekrom
Démétéros
Kyurem
Keldeo
Meloetta
Genesect
""")
fifth_gen = fifth_gen.split('\n')
#PREPROCESSING POKEMON FIFTH GENERATION
def replace_last(source_string, replace_what, replace_with):
    head, _sep, tail = source_string.rpartition(replace_what)
    return head + replace_with + tail
for index, value in enumerate(fifth_gen):

    if value.endswith(('note ', 'note')):
        fifth_gen[index] = replace_last(value, 'note', '')
        fifth_gen[index] = fifth_gen[index].replace(' ', '')
        fifth_gen[index] = fifth_gen[index].lower()
    else:
        fifth_gen[index] = fifth_gen[index].replace(' ', '')
        fifth_gen[index] = fifth_gen[index].lower()

sixth_gen = ("""Marisson
Boguérisse
Blindépique
Feunnec
Roussil
Goupelin
Grenousse
Croâporal
Amphinobi
Sapereau
Excavarenne
Passerouge
Braisillon
Flambusard
Lépidonille
Pérégrain
Prismillon
Hélionceau
Némélios
Flabébé
Floette
Florges
Cabriolaine
Chevroum
Pandespiègle
Pandarbare
Couafarel
Psystigri
Mistigrix
Monorpale
Dimoclès
Exagide
Fluvetin
Cocotine
Sucroquin
Cupcanaille
Sepiatop
Sepiatroce
Opermine
Golgopathe
Venalgue
Kravarech
Flingouste
Gamblast
Galvaran
Iguolta
Ptyranidur
Rexillius
Amagara
Dragmara
Nymphali
Brutalibré
Dedenne
Strassie
Mucuscule
Colimucus
Muplodocus
Trousselin
Brocélôme
Desséliande
Pitrouille
Banshitrouye
Grelaçon
Séracrawl
Sonistrelle
Bruyverne
Xerneas
Yveltal
Zygarde
Diancienote
Hoopa
Volcanion
""")
sixth_gen = sixth_gen.split('\n')
#PREPROCESSING POKEMON SIXTH GENERATION
def replace_last(source_string, replace_what, replace_with):
    head, _sep, tail = source_string.rpartition(replace_what)
    return head + replace_with + tail
for index, value in enumerate(sixth_gen):
    if value.endswith(('note ', 'note')):
        sixth_gen[index] = replace_last(value, 'note', '')
        fifth_gen[index] = sixth_gen[index].replace(' ', '')
        sixth_gen[index] = sixth_gen[index].lower()
    else:
        sixth_gen[index] = sixth_gen[index].replace(' ', '')
        sixth_gen[index] = sixth_gen[index].lower()

seventh_gen = ("""Brindibou
Efflèche
Archéduc
Flamiaou
Matoufeu
Félinferno
Otaquin
Otarlette
Oratoria
Picassaut
Piclairon
Bazoucan
Manglouton
Argouste
Larvibule
Chrysapile
Lucanon
Crabagarre
Crabominable
Plumeline
Bombydou
Rubombelle
Rocabot
Lougaroc
Froussardine
Vorastérie
Prédastérie
Tiboudet
Bourrinos
Araqua
Tarenbulle
Mimantis
Floramantis
Spododo
Lampignon
Tritox
Malamandre
Nounourson
Chelours
Croquine
Candine
Sucreine
Guérilande
Gouroutan
Quartermac
Sovkipou
Sarmuraï
Bacabouh
Trépassable
Concombaffe
Silvallié
Météno
Dodoala
Boumata
Togedemaru
Mimiqui
Denticrisse
Draïeul
Sinistrail
Bébécaille
Écaïd
Ékaïser
Tokorico
Tokotoro
Tokopiyon
Tokopisco
Cosmog
Cosmovum
Solgaleo
Lunala
Zéroïd
Mouscoto
Cancrelove
Câblifère
Bamboiselle
Katagami
Engloutyran
Necrozma
Magearna
Marshadow
Vémini
Mandrillon
Ama-Ama
Pierroteknik
Zeraora
Meltan
Melmetal
""")
seventh_gen = seventh_gen.split('\n')
#PREPROCESSING POKEMON SEVENTH GENERATION
def replace_last(source_string, replace_what, replace_with):
    head, _sep, tail = source_string.rpartition(replace_what)
    return head + replace_with + tail
for index, value in enumerate(seventh_gen):
    if value.endswith(('note ', 'note')):
        seventh_gen[index] = replace_last(value, 'note', '')
        fifth_gen[index] = seventh_gen[index].replace(' ', '')
        seventh_gen[index] = seventh_gen[index].lower()
    else:
        seventh_gen[index] = seventh_gen[index].replace(' ', '')
        seventh_gen[index] = seventh_gen[index].lower()


eighth_gen = ("""Ouistempo
Badabouin
Gorythmic
Flambino
Lapyro
Pyrobut
Larméléon
Arrozard
Lézargus
Rongourmand
Rongrigou
Minisange
Bleuseille
Corvaillus
Larvadar
Coléodôme
Astronelle
Goupilou
Roublenard
Tournicoton
Blancoton
Moumouton
Moumouflon
Khélocrok
Torgamord
Voltoutou
Fulgudog
Charbi
Wagomine
Monthracite
Verpom
Pomdrapi
Dratatin
Dunaja
Dunaconda
Nigosier
Embrochet
Hastacuda
Toxizap
Salarsen
Grillepattes
Scolocendre
Poulpaf
Krakos
Théffroi
Polthégeist
Bibichut
Chapotus
Sorcilence
Grimalin
Fourbelin
Angoliath
Ixon
Berserkatt
Corayôme
Palarticho
M. Glaquette
Tutétékri
Crèmy
Charmilly
Hexadron
Wattapik
Frissonille
Beldeneige
Dolman
Bekaglaçon
Wimessir
Morpeko
Charibari
Pachyradjah
Galvagon
Galvagla
Hydragon
Hydragla
Duralugon
Fantyrm
Dispareptil
Lanssorien
Zacian
Zamazenta
Éthernatos
Wushours
Shifours
Sylveroy
Zarude
""")
eighth_gen = eighth_gen.split('\n')
#PREPROCESSING POKEMON EUGHTH GENERATION
def replace_last(source_string, replace_what, replace_with):
    head, _sep, tail = source_string.rpartition(replace_what)
    return head + replace_with + tail
for index, value in enumerate(eighth_gen):
    if value.endswith(('note ', 'note')):
        eighth_gen[index] = replace_last(value, 'note', '')
        eighth_gen[index] = eighth_gen[index].replace(' ', '')
        eighth_gen[index] = eighth_gen[index].lower()
    else:
        eighth_gen[index] = eighth_gen[index].replace(' ', '')
        eighth_gen[index] = eighth_gen[index].lower()


#ICI ON CREER UN FICHIER TXT AVEC TOUS LES POKEMONS EXISTANT

liste_pokemon = first_gen + second_gen + third_gen + fourth_gen + fifth_gen + sixth_gen + seventh_gen + eighth_gen

#
# test = open("pokemon.txt","w")
# for i,v in enumerate(liste_pokemon):
#     test.write(str(v))
#     test.write(",\n")
# test.close()



#SCRAPPING DE CARACTERISTIQUE SUR PAGE WEB D UN POKEMON
def pokemon_caracterisque(name):
    liste=[]
    url = "https://www.pokebip.com/pokedex/pokemon"
    url_fin = '/'+str(name)+'/'+str(name)
    url= url+url_fin
    poke = requests.get(url)
    soup_poke = bs4.BeautifulSoup(poke.text, 'html.parser')
    table = soup_poke.find_all("div",{"class":"progress"})
    for i in range(6):
        v = str(table[i].find('strong')).split('<')
        v1= v[1].split('>')
        liste.append(v1[1])
    return(liste)

#SCRAPPING DU TYPE D UN POKEMON SUR UNE PAGE WEB
def pokemon_type(name):
    liste=[]
    url = "https://www.pokebip.com/pokedex/pokemon"
    url_fin = '/'+name+'/'+name
    url= url+url_fin
    poke = requests.get(url)
    soup_poke = bs4.BeautifulSoup(poke.text, 'html.parser')
    table = soup_poke.find_all("table",{"class":"table table-condensed table-responsive table-bordered2 text-center"})
    e = str(table[0].find('p')).split('=')
    e= e[1].split("\"")
    liste.append(e[1])
    return liste

#SCRAPPING DES EVOLUTIONS  SUR PAGE WEB D UN POKEMON
def evolution_pokemon(name):
    url = "https://www.pokebip.com/pokedex/pokemon"
    url_fin = '/'+name+'/'+name
    url= url+url_fin
    poke = requests.get(url)
    soup_poke = bs4.BeautifulSoup(poke.text, 'html.parser')
    table = soup_poke.find_all("div",{"class":"row"})
    e= str(table[6].find_all('a'))
    e = e.split('<')
    liste = []
    for i in e:
        liste.append(i.split('>'))

    liste2=[]
    for e in liste:
        for x in e:
            if x.lower() in liste_pokemon:
                    liste2.append(x.lower())
    liste4=[]
    for i in liste2:
        if i != '':
            liste4.append(i)
    return liste4

#SCRAPPING DE LA DESCRIPTION SUR PAGE WEB D UN POKEMON
def pokemon_desc(name):
    url = "https://www.pokebip.com/pokedex/pokemon"
    url_fin = '/'+name+'/'+name
    url= url+url_fin
    poke = requests.get(url)
    soup_poke = bs4.BeautifulSoup(poke.text, 'html.parser')
    table = soup_poke.find_all("div",{"class":"panel panel-info"})
    e = str(table[-1].find_all("div"))
    e = e.split('>')
    e =e[3].split('<')
    liste = []
    liste.append(e[0])
    return liste

#SCRAPPING D UN TALENT SUR PAGE WEB D UN POKEMON
def poke_talent(name):
    liste = []
    url = "https://www.pokebip.com/pokedex/pokemon"
    url_fin = '/'+name+'/'+name
    url= url+url_fin
    poke = requests.get(url)
    soup_poke = bs4.BeautifulSoup(poke.text, 'html.parser')
    table = soup_poke.find_all("div",{"class":"panel-body"})
    s = str(table[-5]).split('>')
    s =s[1].split('<')[0]
    liste.append(s)
    return liste

#SCRAPPING CREATION D UN DICTIONNAIRE AVEC TOUTES LES INFOS DES PRECEDENTE FONCTIONS  D UN POKEMON
def scrap(name):
    dictionnaire_poke = {

        'pv': pokemon_caracterisque(name)[0],
            'attaque': pokemon_caracterisque(name)[1],
        'defense': pokemon_caracterisque(name)[2],
        'attaque spe': pokemon_caracterisque(name)[3],
        'defense spe': pokemon_caracterisque(name)[4],
            'vitesse': pokemon_caracterisque(name)[5],



         'type':pokemon_type(name)[0],
        'evolution' : evolution_pokemon(name),
        'description': pokemon_desc(name)[0],
        'talent' : poke_talent(name)[0]

    }
    return dictionnaire_poke

#SCRAPPING DES NEWS SUR PAGE WEB DES POKEMONS
def news_scrap():
    url = "https://www.pokekalos.fr"
    poke = requests.get(url)
    soup_poke = bs4.BeautifulSoup(poke.text, 'html.parser')
    table = soup_poke.find_all("div",{"class":"desc-overflow"})
    table = str(table).split('>')
    table = table[1].split('<')
    return table[0]


#SCRAPPING DES JEUX POKEMON SUR UNE PAGE WEB
def jeux_pokemon():
    url='https://fr.wikipedia.org/wiki/Pok%C3%A9mon_(s%C3%A9rie_de_jeux_vid%C3%A9o)'
    page = requests.get(url)
    test = bs4.BeautifulSoup(page.text, "lxml")
    table = test.find_all("tbody")[4]
    e= str(table).split('"')
    liste=  []
    for index , value in enumerate(e):
        if value ==' title=':
            liste.append(e[index+1])
    liste2=[]
    for index , x in enumerate(liste):
        if 'Game Boy' in x or 'Nintendo' in x:
            liste_inter= [liste[index-1], x , liste[index+1]]
            liste2.append(liste_inter)
    liste2[0][0]='Pokemon Vert'
    liste2[4][0]='Pokemon Cristal'
    liste2[6][0]='Pokemon Emeraude'
    liste2[9][0]='Pokemon Platine'



    for index,x in enumerate(liste2):
        x[2]=x[2].split(' ')[0]
        if index in [0,1,2]:
            x.append('Première')
        if index in [3,4]:
            x.append('Deuxième')
        if index in [5,6,7]:
            x.append('Troisième')
        if index in [8,9,10]:
            x.append('Quatrième')
        if index in [11,12]:
            x.append('Cinquième')
        if index in [13,14]:
            x.append('Sixième')
        if index in [15,16,17]:
            x.append('Septième')
        if index in [18]:
            x.append('Huitième')
    s = ''
    for x in liste2:
        s += ("\n"+ str(x[0]) + ' | '+str(x[3]) +' gen | ' + str(x[1])+ ' | '+str(x[2]))
    return(s)
