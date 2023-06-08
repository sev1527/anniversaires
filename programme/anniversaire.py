# -*- coding: utf-8 -*-
from time import strftime, mktime, time
import os
from tkinter import Tk, Toplevel, Button, Label, Frame, Entry, Menu
from tkinter.ttk import Treeview, Progressbar, Scrollbar
from tkinter.messagebox import showinfo, askyesno, showerror
from tkinter.simpledialog import askstring
from math import floor
from csv import reader, writer
import requests as rq
import urllib
import json
import threading
from PIL import Image, ImageTk

PATH = "anniversaire.csv"
ICONE = "anniversaire.ico"

ville = "paris"

saint = {'Aaron': ['01/07'], 'Gabin de Rome': ['19/02'], 'Odilon': ['04/01', '28/10', '01/01'], 'Abdon': ['30/07'], 'Gabriel': ['29/09'], 'Gabriel de l’Addolorata': ['27/02'], 'Abel': ['05/08'], 'Gabrielle': ['29/09'], 'Odrade': ['03/11'], 'Abella': ['05/08'], 'Gaby': ['29/09'], 'Odulphe': ['12/06'], 'Ablebert': ['15/01'], 'Gaël': ['17/12'], 'Abondance': ['01/03', '16/09'], 'Gaëlle': ['17/12'], 'Olave': ['29/07'], 'Gaétan': ['07/08'], 'Olga de Russie': ['11/07'], 'Abraham': ['20/12'], 'Gaétane': ['07/08'], 'Olive': ['05/03', '03/06'], 'Acepsimas': ['22/04', '03/11'], 'Galactoire': ['27/07'], 'Olive de Palerme': ['10/06'], 'Achilée': ['12/05'], 'Gall': ['16/10'], 'Olivette': ['05/03'], 'Achille': ['12/05'], 'Gall de Clermont': ['01/07'], 'Olivia': ['05/03'], 'Ada': ['04/12'], 'Gallican': ['25/06'], 'Olivier': ['12/07'], 'Adalbaud': ['02/02'], 'Galmier': ['27/02'], 'Olivier Levèvre': ['02/09'], 'Adalbert d’Egmont': ['25/06'], 'Gamelbert': ['17/01'], 'Olivier Plunket': ['11/07'], 'Adalsinde': ['03/05', '25/12'], 'Gamulbert': ['17/01'], 'Olle': ['09/10'], 'Gandolphe': ['17/09'], 'Ollégaire': ['06/03'], 'Adaltrude': ['14/11'], 'Gandolphe de Binasco': ['03/04'], 'Olympe': ['12/06'], 'Adélaïde': ['16/12'], 'Garembert': ['31/12'], 'Olympiade': ['17/12'], 'Garibald': ['08/01'], 'Ombeline': ['21/08'], 'Adèle': ['24/12'], 'Gaspard': ['06/01', '28/12'], 'Omer': ['09/09'], 'Adelinde': ['28/08'], 'Onésime': ['16/02'], 'Adeline': ['20/10'], 'Gaspard Bertoni': ['12/06'], 'Onésiphore': ['06/09'], 'Adelphe': ['11/09'], 'Gaston': ['06/02'], 'Onuphre': ['12/06'], 'Adérald': ['20/10'], 'Gatien': ['18/12'], 'Opportune': ['22/04'], 'Adile': ['30/06'], 'Gaucher': ['09/04'], 'Orence': ['01/05'], 'Adjuteur': ['30/04', '01/09'], 'Gaud': ['20/07'], 'Orianne': ['04/10'], 'Gaudence': ['22/01', '12/02', '19/06', '30/08', '11/10'], 'Oricula': ['18/11'], 'Adnette': ['04/12'], 'Orion': ['25/06'], 'Adolphe': ['11/02', '30/06'], 'Oronce': ['22/01'], 'Osanna Andreasi': ['18/06'], 'Adon': ['16/12'], 'Osanne': ['09/09'], 'Adrehilde': ['04/12'], 'Gaudérique': ['16/10'], 'Oscar': ['03/02'], 'Adrien': ['08/09'], 'Gausbert': ['27/05', '10/12'], 'Osith': ['07/10'], 'Adrien de Canterbury': ['09/01'], 'Osmanne': ['09/09'], 'Adrienne': ['08/09'], 'Gautier d’Aulne': ['26/11'], 'Osmond': ['04/12'], 'Adrion': ['17/05'], 'Gautier ou Gauthier': ['09/04'], 'Oswald': ['05/08'], 'Adulphe': ['17/06'], 'Gébétrude': ['07/11'], 'Othon de Bamberg': ['02/07'], 'Adventor': ['20/11'], 'Gebhard': ['27/08'], 'Otmar': ['16/11'], 'Africain': ['10/04'], 'Gédéon': ['10/10'], 'Oudocée': ['02/07'], 'Agape': ['03/04'], 'Gemma Galgani': ['11/04'], 'Ouen': ['24/08'], 'Agapet': ['18/08'], 'Génébaud': ['05/09'], 'Oyend': ['01/01'], 'Agathe de Catane': ['05/02'], 'Général': ['14/09'], 'Pablo': ['29/06'], 'Agathoclie': ['17/09'], 'Généreux': ['17/07'], 'Agathodore': ['02/02', '04/03', '13/04'], 'Genès ou Génèse': ['26/08'], 'Pacien': ['09/03'], 'Geneviève': ['03/01'], 'Pacifique': ['08/06'], 'Gengoul': ['11/05'], 'Pacifique de Cerano': ['08/06'], 'Agathon': ['07/12'], 'Gennard': ['06/04'], 'Pacifique de Lisciano': ['10/07'], 'Agilée': ['15/10'], 'Genou': ['17/01'], 'Pacifique de San Severino': ['24/09'], 'Gens': ['16/05'], 'Paco': ['04/10'], 'Agneflète': ['02/04'], 'Genulfe': ['17/01'], 'Pacôme': ['09/05', '26/11'], 'Agnès de Bohème': ['06/03'], 'Geoffrey': ['08/11'], 'Agnès de Monte Pulciano': ['20/04'], 'Geoffroy': ['08/11', '08/11'], 'Palais': ['07/10'], 'Agnès de Rome': ['21/01'], 'Palémon': ['11/01'], 'Agricol d’Avignon': ['01/09'], 'Georges de Lydda': ['23/04'], 'Pallade': ['10/04'], 'Agricole': ['05/02', '26/02', '17/03', '02/09'], 'Georgette': ['15/02', '23/04'], 'Palmace': ['10/05'], 'Pambon': ['18/07'], 'Georgia': ['15/02'], 'Paméla': ['16/02'], 'Georgine': ['15/02', '23/04'], 'Pammaque': ['30/08'], 'Ahmed': ['21/08'], 'Pamphalon': ['17/05'], 'Aignan': ['17/11'], 'Gérald': ['05/12'], 'Pamphile': ['16/02', '28/04', '01/06', '07/09', '21/09'], 'Aimable': ['18/10'], 'Géraldine': ['05/12'], 'Aimé': ['13/09'], 'Gérard': ['29/05', '05/12'], 'Aimée': ['20/02'], 'Alain de la Roche': ['09/09'], 'Gérard d’Aurillac': ['13/10'], 'Alban': ['22/06'], 'Gérard de Brogne': ['03/10'], 'Panacée': ['01/05'], 'Albane': ['22/06'], 'Gérard de Sauve Majeure': ['05/04'], 'Panchaire': ['22/07'], 'Albe': ['22/06'], 'Gérard Magella': ['16/10'], 'Pancrace': ['03/04', '12/05'], 'Albéric': ['15/11'], 'Gérasime': ['05/03'], 'Albert le Grand': ['15/11'], 'Géraud': ['13/10'], 'Pansophe': ['15/01'], 'Alberta': ['15/11'], 'Gerbaud': ['12/06'], 'Pantagape': ['02/09'], 'Alberte': ['15/11'], 'Gerbold': ['07/12'], 'Pantale': ['12/10'], 'Albertine': ['15/11'], 'Pantaléon': ['27/06', '27/07'], 'Albin d’Anvers': ['01/03'], 'Germain d’Auxerre': ['31/07'], 'Alburge': ['25/12'], 'Germain de Constantinople': ['12/05'], 'Pantène': ['07/07'], 'Alda': ['26/04'], 'Germain de Paris': ['28/05'], 'Panthaléon': ['27/07'], 'Germaine': ['15/06'], 'Paola': ['26/01'], 'Aldegonde': ['30/01'], 'Germaine Cousin': ['19/01', '15/06'], 'Papoul': ['03/11'], 'Alèthe': ['04/04'], 'Papyle': ['13/04'], 'Alette': ['04/04'], 'Géronce': ['09/05'], 'Pâquerette': ['05/10'], 'Alexandra': ['22/04'], 'Géronima': ['30/09'], 'Paquita': ['09/03'], 'Alexandre': ['22/04'], 'Gertrude Comensoli': ['18/02'], 'Paquito': ['04/10'], 'Alexandre 1er, pape': ['03/05'], 'Gertrude de Nivelle': ['17/03'], 'Pardoux': ['06/10'], 'Alexandre, patriarche d’Alexandrie': ['26/02'], 'Gertrude la Grande': ['16/11'], 'Parfait': ['18/04'], 'Alexia': ['09/01'], 'Gervais': ['19/06'], 'Paris': ['05/08'], 'Alexis': ['17/02'], 'Gervaise': ['19/06'], 'Parménas': ['23/01'], 'Gervold': ['04/05'], 'Parmène': ['22/04'], 'Aleyde': ['11/06'], 'Gerwin': ['03/03'], 'Alfred le Grand': ['15/09'], 'Géry': ['11/08'], 'Pascal Baylon': ['17/05'], 'Alfred, moine': ['15/08'], 'Gétule': ['10/06'], 'Pascaline': ['17/05'], 'Alice': ['16/12'], 'Gezelin': ['06/08'], 'Pascalle': ['17/05'], 'Alida': ['26/04'], 'Ghislain': ['10/10'], 'Pasquier': ['10/07'], 'Aline': ['20/10'], 'Ghislaine': ['10/10'], 'Passif': ['13/02'], 'Alix': ['09/01'], 'Gibitrude': ['26/10'], 'Pasteur': ['29/03', '30/03', '26/07', '06/08'], 'Aloïs': ['21/06'], 'Gilbert de Neuffonts': ['07/06'], 'Alor': ['26/10'], 'Gilbert de Sempringham': ['04/02'], 'Aloysius de Gonzague': ['21/06'], 'Gilberte': ['11/08'], 'Alphonse': ['01/08'], 'Gildas': ['29/01'], 'Patère': ['21/02'], 'Alphonse Rodriguez': ['30/10'], 'Gildas le Sage': ['29/01'], 'Paterne': ['10/04', '15/04', '16/04', '21/08', '12/11'], 'Alphonse Marie de Liguori': ['01/08'], 'Gilles': ['01/09'], 'Alphonsine': ['01/08'], 'Gina': ['21/06'], 'Amadour': ['20/08'], 'Ginette': ['03/01'], 'Amaël': ['24/05'], 'Gino': ['21/06'], 'Pathermuthe': ['09/07'], 'Amalberge': ['10/07', '19/11', '21/11'], 'Giraud': ['20/04'], 'Patience': ['01/05'], 'Gisèle': ['07/05'], 'Patient': ['08/01', '11/09'], 'Gladys': ['29/03'], 'Amance': ['04/11'], 'Glaphyre': ['13/01'], 'Patrice': ['17/03'], 'Amand': ['06/02', '26/10'], 'Glastien': ['28/01'], 'Patricia': ['17/03'], 'Glossinde': ['25/07'], 'Patrick d’Irlande': ['17/03'], 'Amand de Bordeaux': ['18/06'], 'Glycère': ['13/05', '20/09'], 'Patrocle': ['21/01', '18/11'], 'Amand de Maastricht': ['10/02'], 'Amandine': ['09/07'], 'Glycérie': ['13/05'], 'Paul': ['25/01'], 'Amateur': ['30/04', '01/05'], 'Godard': ['04/05'], 'Paul apôtre': ['29/06'], 'Godeberte': ['11/04'], 'Paul de la croix': ['19/10'], 'Amaury': ['15/01'], 'Godefroy': ['08/11'], 'Paul Miki': ['06/02'], 'Ambroise de Milan': ['07/12'], 'Godefroy de Péronne': ['15/01'], 'Paul, ermite': ['15/01'], 'Amé': ['13/09'], 'Godeliève': ['06/07'], 'Paula': ['26/01'], 'Amédée de Lausanne': ['27/08'], 'Paule': ['26/01'], 'Amédée IX': ['30/03'], 'Paulette': ['26/01'], 'Amelberge': ['10/07'], 'Gombert': ['21/02', '01/05', '15/07'], 'Paulien': ['14/02'], 'Amélie': ['19/09'], 'Paulin': ['11/01'], 'Ammon': ['20/12'], 'Paulin de Nole': ['22/06'], 'Amor': ['09/08'], 'Gommaire': ['11/10'], 'Pauline': ['26/01', '06/06'], 'Amos': ['31/03'], 'Gondlée': ['29/03'], 'Amour': ['09/08', '17/08', '08/10'], 'Gondrude': ['06/10'], 'Pausicaque': ['13/05'], 'Gondulphe': ['17/06', '16/07', '06/09'], 'Pauside': ['24/03'], 'Pavace': ['24/07'], 'Anaclet': ['26/04'], 'Pavin': ['15/11'], 'Anaïs': ['26/07'], 'Gonthilde': ['08/12'], 'Peggy': ['08/01'], 'Anastase 1er': ['11/10'], 'Gontran': ['28/03'], 'Pélade': ['21/06'], 'Anastasie': ['10/03', '15/04'], 'Gonzague': ['21/06'], 'Pélagie': ['08/10'], 'Gorgon': ['09/09'], 'Pélagie de Jérusalem': ['08/10'], 'Anatole': ['03/02', '03/07'], 'Gorgonie': ['09/12'], 'Pélagie la Pénitente': ['08/10'], 'Gouesnou': ['25/10'], 'Pèlerin': ['01/08'], 'Anatolie': ['23/12'], 'Goulven': ['01/07', '03/07'], 'Pépin de Landen': ['21/02'], 'Andoche': ['24/09'], 'André': ['30/11'], 'Gourloé': ['25/08'], 'Pérégrin': ['13/06'], 'André Avellin': ['10/11'], 'Goustan': ['27/11'], 'Perlette': ['16/10'], 'André Corsini': ['04/02'], 'Grâce': ['21/08'], 'Pernelle': ['31/05'], 'André Kim': ['20/09'], 'Gracieuse': ['21/08'], 'Péroline': ['31/05'], 'Andrée': ['30/11'], 'Graziella': ['21/08'], 'Perpète': ['04/11'], 'Anempodiste': ['02/11'], 'Grégoire 1er, dit le Grand': ['03/09'], 'Perpétue': ['07/03'], 'Angadrême': ['14/10'], 'Grégoire de Nazianze': ['02/01'], 'Perrette': ['31/05'], 'Ange de Jérusalem': ['05/05'], 'Grégoire de Nysse': ['09/03'], 'Angèle': ['24/05'], 'Grégoire le Thaumaturge': ['17/11'], 'Perrine': ['31/05'], 'Angèle de Foligno': ['04/01'], 'Grégoire l’Illuminateur': ['30/09'], 'Persévérande': ['26/06'], 'Angèle de Mérici': ['27/01'], 'Grégoire VII': ['25/05'], 'Pervenche': ['05/10'], 'Angélique': ['27/01'], 'Grégory': ['03/09'], 'Peter': ['29/06'], 'Anges gardiens': ['02/10'], 'Grimaud': ['08/07'], 'Pétronille': ['31/05', '06/06'], 'Anicet': ['17/04'], 'Anita': ['26/07'], 'Pharaïlde': ['04/01'], 'Annabelle': ['26/07'], 'Gudélie': ['29/09'], 'Pharmuthe': ['11/04'], 'Anne': ['26/07', '28/07'], 'Gudelinde': ['28/03'], 'Pharnace': ['24/06'], 'Gudule': ['08/01'], 'Phébade': ['25/04'], 'Annette': ['26/07'], 'Guenaël': ['03/11'], 'Philadelphe': ['10/05', '02/09'], 'Annick': ['26/07'], 'Guennolé': ['03/03'], 'Annie': ['26/07'], 'Guénolé': ['03/03'], 'Philarète': ['06/04'], 'Annonciade': ['25/03'], 'Guérin': ['06/01'], 'Philastre': ['18/07'], 'Annonciation': ['25/03', '07/04'], 'Guerric': ['19/08'], 'Philéas': ['04/02', '26/11'], 'Anouchka': ['26/07'], 'Guewen': ['18/10'], 'Philémon': ['21/03', '22/11', '14/12'], 'Anouck': ['26/07'], 'Guiborate': ['02/05'], 'Anschaire': ['03/02'], 'Guier': ['04/04'], 'Philibert': ['20/08', '22/08'], 'Anségise': ['20/07'], 'Guillaume de Bourges': ['10/01'], 'Anselme de Cantorbéry': ['21/04'], 'Guillaume d’Orange, dit le Grand': ['25/06'], 'Philiberte': ['20/08'], 'Anstrude': ['17/10'], 'Guillemette': ['10/01'], 'Philippe': ['22/10'], 'Anthelme de Chignin': ['26/06'], 'Guingalois': ['03/03'], 'Philippe de Néri': ['26/05'], 'Anthime': ['27/04'], 'Guinoc': ['13/04'], 'Philippe l’apôtre': ['03/05'], 'Antholien': ['06/02'], 'Philomène': ['05/07', '10/08', '13/08', '14/11', '29/11'], 'Anthonin': ['04/05'], 'Gumesinde': ['13/01'], 'Anthony': ['17/01'], 'Gundelinde': ['28/03'], 'Antoine': ['05/07'], 'Gunthilde': ['22/09'], 'Antoine de Padoue': ['13/06'], 'Gurloès': ['25/08'], 'Gustave': ['07/10'], 'Guthiern': ['03/07'], 'Philonide': ['30/08'], 'Antoine le Grand': ['17/01'], 'Guy': ['12/06'], 'Phocas': ['22/09'], 'Antoine Marie Claret': ['24/10'], 'Guyonne': ['12/06'], 'Pia': ['19/01'], 'Antoine Marie Zaccaria': ['05/07'], 'Gwen': ['18/10'], 'Antoinette': ['05/07'], 'Gwénaël': ['03/11'], 'Pie 1er': ['11/07'], 'Antonie de Padoue': ['13/06'], 'Gwénaëlle': ['03/11'], 'Pie V': ['30/04'], 'Antonin': ['02/05', '10/05'], 'Gwendolène': ['18/10'], 'Pie X': ['21/08'], 'Gwendoline': ['14/10'], 'Pience': ['11/10'], 'Apollinaire': ['23/07', '12/09'], 'Gwenn': ['18/10'], 'Pient': ['13/03'], 'Gwénola': ['03/03'], 'Pierre': ['23/02', '01/06'], 'Apolline ou Apollonie': ['09/02'], 'Gwladys': ['29/03'], 'Habence': ['07/06'], 'Pierre Casinius': ['21/12'], 'Apollos': ['25/01'], 'Habib': ['27/03'], 'Pierre Célestin': ['19/05'], 'Appia': ['22/11'], 'Hadéloge': ['02/02'], 'Pierre Chanel': ['28/04'], 'Aproncule': ['22/04', '14/05'], 'Hadouin': ['20/08'], 'Pierre Chrysologue': ['30/07'], 'Hadulphe inconnue Hadulf': ['19/05'], 'Pierre Claver': ['09/09'], 'Aquiline': ['13/06'], 'Hans': ['24/06', '27/12'], 'Pierre d’Alcantara': ['19/10'], 'Arcade': ['12/01'], 'Pierre Damien': ['21/02'], 'Arcadius': ['01/08'], 'Hariulf': ['13/08'], 'Pierre de Luxembourg': ['02/07'], 'Arcady': ['01/08'], 'Harlinde': ['22/03'], 'Pierre de Vérone': ['29/04'], 'Ariane': ['18/09'], 'Harold': ['01/11'], 'Pierre Fourier': ['09/12'], 'Arielle': ['01/10'], 'Harry': ['13/07'], 'Aristarque': ['04/08'], 'Hartmann': ['23/12'], 'Pierre l’apôtre': ['29/06', '18/11'], 'Aristide': ['31/08'], 'Hathumar': ['09/08'], 'Hathumode': ['29/11'], 'Pierre Maubant': ['20/09'], 'Hedwige': ['16/10'], 'Pierre Vitalis': ['02/09'], 'Arlette': ['17/07'], 'Hégésippe': ['07/04'], 'Pierre Es Lien': ['01/08'], 'Armagillus': ['16/08'], 'Heimrad': ['28/06'], 'Pierrette': ['31/05'], 'Armand': ['23/12'], 'Heldrad': ['13/03'], 'Pierrick': ['29/06'], 'Armande': ['23/12'], 'Hélène': ['20/06', '18/08'], 'Pigmène': ['24/03'], 'Armel': ['16/08', '16/08'], 'Pirmin': ['03/11'], 'Héliconide': ['28/05'], 'Placide': ['05/10'], 'Armelle': ['16/08'], 'Héliéna': ['18/08'], 'Plaute': ['29/09'], 'Armentaire': ['30/01'], 'Hélier': ['16/07'], 'Plautilla': ['20/05'], 'Arnaud': ['10/02'], 'Héliménas': ['22/04'], 'Plautille': ['20/05'], 'Arnaud Cantaneo': ['10/02'], 'Héliodore': ['06/05'], 'Pol': ['12/03'], 'Arnold': ['14/08'], 'Héllade d’Auxerre': ['08/05'], 'Polycarpe de Smyrne': ['23/02'], 'Arnoul de Metz': ['18/07'], 'Helmetrude': ['31/05'], 'Polychrone': ['17/02'], 'Helrad': ['13/03'], 'Polyeucte': ['13/02'], 'Arnulphe': ['05/01'], 'Hélyette': ['20/07'], 'Pome': ['27/06'], 'Arsace': ['16/08'], 'Hénédine': ['14/05'], 'Pontique': ['02/06'], 'Arsène le Grand': ['19/07'], 'Porchaire': ['01/06'], 'Arthaud': ['06/10'], 'Henri II de Germanie': ['13/07'], 'Porphyre': ['04/11'], 'Arthur': ['15/11'], 'Henriette': ['13/07'], 'Arzel': ['16/08'], 'Possesseur': ['11/05'], 'Asceline': ['23/08'], 'Héradius': ['17/05'], 'Potamiène': ['28/06'], 'Assomption': ['15/08'], 'Herbern': ['30/10'], 'Potamienne la Jeune': ['07/06'], 'Astrid': ['27/11'], 'Herbert': ['20/03'], 'Potamon': ['18/05'], 'Athanase d’Alexandrie': ['02/05'], 'Hérébald': ['11/06'], 'Potentien': ['31/12'], 'Aubert': ['10/09'], 'Hérénie': ['08/03'], 'Potentienne': ['17/04'], 'Aubierge': ['07/07', '12/09'], 'Héribert': ['16/03'], 'Potentin': ['31/12'], 'Hérifrid': ['23/10'], 'Pothin': ['02/06'], 'Aubin': ['01/03'], 'Herlembaud': ['27/06'], 'Potomène': ['02/06'], 'Aude': ['18/11'], 'Herlinde': ['22/03'], 'Pouange': ['31/01'], 'Audebert': ['09/02'], 'Hermance': ['28/08'], 'Praxède': ['21/07'], 'Audrey': ['23/06'], 'Hermann': ['25/09'], 'Précord': ['01/02'], 'Augusta': ['13/11', '24/11'], 'Hermann le Boîteux': ['25/09'], 'Premiers martyrs de Rome': ['30/06'], 'Hermel': ['03/08'], 'Prépédigne': ['18/02'], 'Auguste': ['29/02'], 'Hermeland': ['25/03'], 'Présence de Marie': ['21/11'], 'Augustin de Cantorbéry': ['27/05'], 'Herménégilde ou Hermenegild': ['13/04'], 'Présentation': ['02/02'], 'Augustin de Nicomédie': ['07/05'], 'Hermès': ['28/08'], 'Présentation de Marie': ['21/11'], 'Augustin d’Hippone': ['28/08'], 'Hermine': ['09/07'], 'Augustine': ['13/11'], 'Hermogène': ['17/04'], 'Primaël': ['15/05'], 'Aunemond': ['28/09'], 'Hérodion': ['08/04'], 'Prime': ['09/06'], 'Aure': ['04/10'], 'Hérumbert': ['09/07'], 'Aurée': ['04/10'], 'Hervé': ['17/06'], 'Primitif': ['16/04', '10/06', '18/07'], 'Aurèle': ['15/10'], 'Hesperius': ['22/06'], 'Aurélie': ['15/10', '02/12'], 'Hésyque d’Antioche': ['18/11'], 'Hidulphe': ['18/04', '11/07'], 'Primitive': ['24/02'], 'Aurélien': ['16/06'], 'Principe': ['16/09'], 'Aurore': ['13/12'], 'Prisca': ['18/01'], 'Ausone': ['22/05', '02/06'], 'Hilaire': ['28/02'], 'Priscilla': ['16/01', '08/07'], 'Hilaire de Poitiers': ['13/01'], 'Auspice': ['08/07', '02/08'], 'Hilarion': ['21/10'], 'Prisque': ['18/01'], 'Hilda': ['17/11'], 'Privat': ['21/08'], 'Austrebert': ['05/06'], 'Prix': ['24/01', '25/01', '26/05'], 'Austreberte': ['10/02'], 'Hildegarde': ['30/04', '17/09'], 'Austregilde': ['09/10'], 'Austremoine': ['01/11'], 'Hildegonde': ['20/04'], 'Probace': ['25/08'], 'Auteur': ['10/08'], 'Hildegrin': ['19/06'], 'Procope': ['08/07'], 'Autonome': ['12/09'], 'Hildelitte': ['24/03'], 'Procule': ['09/07'], 'Auxence': ['14/02', '13/12', '18/12'], 'Hildeman': ['08/12'], 'Projet': ['23/09'], 'Hildemarque': ['20/06'], 'Prosdocime': ['07/11'], 'Hildevert': ['27/05'], 'Prosper': ['25/06', '29/07'], 'Auzias': ['26/09'], 'Hilduard': ['07/09'], 'Avit': ['05/02'], 'Hiltrude': ['27/09'], 'Prosper d’Aquitaine': ['25/06', '07/07'], 'Hippolyte': ['13/08'], 'Axel': ['22/04'], 'Hombeline': ['21/08'], 'Axelle': ['22/04'], 'Protaise': ['19/12'], 'Aymar': ['29/05'], 'Honorat': ['16/01'], 'Prothade': ['10/02'], 'Aymeric': ['04/11'], 'Honorat d’Amiens': ['16/05'], 'Protogène': ['06/05'], 'Babette': ['17/11'], 'Honorat de Toulouse': ['21/12'], 'Protolique': ['14/02'], 'Babine': ['31/03'], 'Honoré': ['16/05'], 'Protus': ['11/09'], 'Baboléin': ['26/06'], 'Honorine': ['27/02'], 'Prudence': ['01/04', '06/04', '28/04', '06/05'], 'Badème': ['10/04'], 'Hortense': ['05/10'], 'Bain': ['20/06'], 'Hospice': ['21/05'], 'Balai': ['12/07'], 'Houardon': ['19/11'], 'Balbine': ['31/03'], 'Hubert': ['03/11'], 'Prudent': ['06/10'], 'Balsamie': ['16/11'], 'Hugoline': ['08/08'], 'Psalmode': ['08/03'], 'Balthazar': ['06/01'], 'Hugues de Grenoble': ['01/04'], 'Publia': ['09/10'], 'Baptiste': ['24/06'], 'Pudentienne': ['19/05'], 'Barbara': ['04/12'], 'Huguette': ['01/04'], 'Pulchérie Auguste': ['10/09'], 'Barbe': ['04/12'], 'Humbert': ['25/03'], 'Pupule': ['28/02'], 'Barberine': ['04/12'], 'Hunégonde': ['25/08'], 'Pusinne': ['23/04'], 'Barnabé l’apôtre': ['11/06'], 'Hyacinthe': ['17/08', '11/09', '23/10'], 'Quadragésime': ['26/10'], 'Barnard': ['23/01'], 'Quartille': ['19/03'], 'Barsimée': ['30/01'], 'Quenburge': ['31/08'], 'Barthélémy, apôtre': ['24/08'], 'Hyacinthe de Mariscotti': ['30/01'], 'Quenin de Vaison': ['15/02'], 'Bartolomé': ['24/08'], 'Hygbald': ['18/09'], 'Quentin': ['31/10'], 'Basile le Grand': ['02/01'], 'Hymetière': ['31/07'], 'Basilisse': ['15/04'], 'Hyppolyte': ['13/08'], 'Quinctile': ['08/03', '19/03'], 'Bastien': ['20/01'], 'Iadine': ['03/02'], 'Bathilde': ['30/01'], 'Ida': ['13/04'], 'Quinctus': ['04/01', '19/03'], 'Bathuse': ['26/03'], 'Idir': ['03/02'], 'Bathylle': ['30/01'], 'Quinide': ['15/02'], 'Baud': ['07/11'], 'Ignace': ['01/02', '31/07'], 'Quinidius': ['15/02'], 'Baudouin': ['17/10'], 'Quintien': ['23/05', '13/11'], 'Baudouin de Boucle': ['17/10'], 'Ignace d’Antioche': ['17/10'], 'Ignace de Constantinople': ['17/10'], 'Quiriaque': ['12/08'], 'Béat': ['19/02', '09/05', '31/07', '25/10'], 'Ignace de Loyola': ['31/07'], 'Quirin': ['04/06'], 'Igor': ['05/06'], 'Quiterie': ['22/07'], 'Ildefonse de Tolède': ['23/01'], 'Rabulas': ['19/02'], 'Ildevert': ['27/05'], 'Rachel': ['15/01'], 'Béate': ['08/03', '29/06'], 'Illuminat': ['11/05'], 'Illuminée': ['29/11'], 'Rachilde': ['23/11'], 'Béatrice d’Ornacieux': ['13/02'], 'Ilpide': ['16/06'], 'Radegonde': ['13/08'], 'Bède le Vénérable': ['25/05'], 'Radulphe': ['21/06'], 'Bénédicte': ['16/03', '06/05'], 'Imaine de Loss': ['29/01'], 'Imelda Lambertini': ['12/05'], 'Ragenfrède inconnue Rainfroye': ['13/08'], 'Bénézet ou Benoît': ['14/04'], 'Imma': ['25/11'], 'Ragenulfe': ['14/07'], 'Bénilde': ['15/06'], 'Immaculée conception': ['08/12'], 'Ragnebert': ['13/06'], 'Benjamin': ['31/03'], 'Impère': ['06/09'], 'Benjamine': ['31/03'], 'Imré': ['04/11'], 'Rainfroye': ['13/08'], 'Benoît': ['21/03'], 'Indalèce': ['15/05'], 'Rainfroye ou Ragenfrède': ['13/08'], 'Benoît de Nurcie': ['21/03'], 'Inès': ['10/09'], 'Raingarde': ['24/06'], 'Benoît de Nursie': ['11/07'], 'Ingaud': ['29/10'], 'Rainier': ['17/06'], 'Benoît Joseph Labre': ['16/04'], 'Ingrid': ['02/09'], 'Benoît ou Bénézet': ['14/04'], 'Injurieux': ['25/05'], 'Raïssa': ['05/09'], 'Bérégise': ['03/10'], 'Innocent': ['19/06'], 'Ralph': ['21/06', '07/07'], 'Bérenger': ['26/05', '02/10'], 'Innocents': ['28/12'], 'Iphigénie': ['21/09'], 'Rambert': ['13/06'], 'Bérengère': ['26/05'], 'Iphigénie de Saint Matthieu': ['09/07'], 'Bérénice': ['04/02'], 'Irais': ['05/09'], 'Randoald': ['21/02'], 'Bernadette': ['18/02'], 'Irène': ['05/04', '20/10'], 'Ranulphe': ['27/05'], 'Bernadette Soubirous': ['16/04'], 'Raoul': ['07/07'], 'Bernard': ['15/06'], 'Irénée de Lyon': ['28/06'], 'Raphaël': ['29/09'], 'Bernard de Clairvaux': ['20/08'], 'Iris': ['04/09'], 'Raphaëlle': ['29/09'], 'Bernard de Menthon': ['28/05', '15/06'], 'Irma': ['09/07', '04/09'], 'Rastragène': ['13/05'], 'Rasyphe': ['23/07'], 'Bernardin': ['20/05'], 'Irmengarde': ['17/07', '04/10'], 'Rathard': ['08/08'], 'Irmine': ['24/12'], 'Ravenger': ['17/11'], 'Berthe': ['04/07'], 'Isaac': ['20/12'], 'Ravenne': ['23/07'], 'Isaac Jogues': ['19/10'], 'Raverène': ['17/11'], 'Bertilie': ['03/01'], 'Isabelle': ['22/02'], 'Raymond de Penyafort': ['07/01'], 'Bertille': ['03/01', '18/09', '06/11'], 'Isaïe': ['09/05'], 'Raymond Nonnat': ['31/08'], 'Isarn': ['24/09'], 'Raymonde': ['07/01'], 'Isidore': ['04/02', '15/05'], 'Raynaud': ['18/08'], 'Bertin': ['05/09'], 'Raynier': ['17/06'], 'Bertrand': ['06/06'], 'Rébecca': ['23/03'], 'Bertrand de Comminges': ['16/10'], 'Isidore de Péluse': ['04/02'], 'Rédempt': ['08/04'], 'Bertrand de Garrigues': ['06/09'], 'Isidore de Séville': ['04/04'], 'Réginald': ['17/09', '07/05'], 'Béryl': ['21/03'], 'Isidore le laboureur': ['10/05'], 'Béton': ['24/02'], 'Ivan': ['24/06'], 'Réginbald': ['13/10'], 'Bettina': ['17/11'], 'Ivanne': ['30/05', '12/12'], 'Régine': ['07/09'], 'Betty': ['17/11'], 'Reginswide': ['15/07'], 'Beuve': ['24/04'], 'J.F. Régis': ['16/06'], 'Régis': ['16/06'], 'Bibiane': ['02/12'], 'Jacinthe': ['30/01'], 'Regnauld': ['17/09'], 'Bienvenue': ['30/10'], 'Jack': ['24/06'], 'Regnault': ['16/09'], 'Jackie': ['08/02'], 'Régnobert': ['01/09'], 'Billy': ['10/01'], 'Jacky': ['03/05'], 'Regula': ['11/09'], 'Birillus': ['21/03'], 'Jacme': ['03/05'], 'Reine': ['01/07', '07/09'], 'Bladulphe': ['02/01'], 'Jacob': ['20/12'], 'Blain': ['10/08'], 'Jacopone': ['25/12'], 'Reinelde': ['16/07'], 'Blaise': ['29/06'], 'Jacqueline': ['08/02'], 'Réjane': ['07/09'], 'Blaise de Sébaste': ['03/02'], 'Jacques': ['01/05'], 'Relinde': ['22/03', '17/08'], 'Blanchard': ['10/03'], 'Jacques Chastan': ['20/09'], 'Blanche': ['05/07', '03/10'], 'Jacques de la Marche': ['28/11'], 'Remacle': ['03/09'], 'Jacques le Majeur': ['25/07'], 'Rembert': ['04/02'], 'Blandine': ['02/06'], 'Jacques le Mineur': ['03/05'], 'Blésille': ['22/01'], 'Jacquette': ['08/02'], 'Rémi ou Rémy': ['13/01', '01/10', '01/11'], 'Blier': ['17/06'], 'Jacquine': ['08/02', '25/07'], 'Bluette': ['05/10'], 'Bogomile': ['10/06'], 'Jacquotte': ['08/02'], 'Rémi de Reims': ['15/01'], 'Bonaventure': ['15/07'], 'Jacut': ['08/02'], 'Rémy de Strasbourg': ['20/03'], 'Boniface': ['14/05', '05/06'], 'James': ['25/07'], 'Renald': ['07/05', '17/09'], 'Janvier': ['19/09'], 'Boniface 1er': ['04/09'], 'Renaud': ['17/09'], 'Boniface de Lausanne': ['19/02'], 'Jaouen': ['02/03'], 'René Goupil': ['19/10'], 'Bonne': ['29/05'], 'Jasmine': ['05/10'], 'Renée': ['19/10'], 'Bonne d’Armagnac': ['03/01'], 'Jean': ['27/12'], 'Renobert': ['24/10'], 'Boris': ['02/05'], 'Jean 1er': ['18/05'], 'Jean Antoine Seguin': ['02/09'], 'Resticula': ['11/08'], 'Botwin': ['28/07'], 'Jean Berchmans': ['13/08'], 'Restitude': ['21/05'], 'Jean Bosco': ['31/01'], 'Restitute': ['27/05'], 'Briac': ['18/12'], 'Jean Capeau': ['02/09'], 'Révocat': ['07/03'], 'Brice': ['13/11'], 'Jean Chrysostome': ['13/09'], 'Reynold': ['07/01'], 'Brieuc': ['01/05'], 'Jean Climaque': ['30/03'], 'Rhuddlad': ['04/09'], 'Brigitte': ['01/02'], 'Jean Damascène': ['27/03', '04/12'], 'Ribert': ['15/09'], 'Brigitte de Suède': ['23/07'], 'Richard de Chichester': ['03/04'], 'Brocard': ['02/09'], 'Jean de Bergame': ['11/07'], 'Richarde': ['18/09'], 'Bruno de Cologne': ['06/10'], 'Jean de Bréboeuf': ['19/10'], 'Richilde': ['23/08'], 'Burienne': ['04/06'], 'Jean de Capistran': ['23/10'], 'Richmir': ['17/01'], 'Busiride': ['21/01'], 'Jean de Damas': ['08/03'], 'Rictrude': ['12/05'], 'Jean de Dieu': ['08/03'], 'Rieul': ['30/03', '03/09'], 'Caïus': ['22/04'], 'Jean de la Croix': ['14/12'], 'Calais': ['01/07'], 'Jean de la Grille': ['01/02'], 'Rigobert de Reims': ['04/01'], 'Calanique': ['17/12'], 'Jean de Matha': ['08/02'], 'Rigomer': ['24/08'], 'Calétric': ['04/09'], 'Jean d’Egypte': ['27/03'], 'Rioc': ['12/02'], 'Calimère': ['31/07'], 'Jean Eudes': ['19/08'], 'Rioch': ['06/02'], 'Calixte 1er': ['14/10'], 'Jean Fisher': ['22/06'], 'Ripsime': ['29/09'], 'Callinique': ['28/01'], 'Jean Gabriel': ['11/09'], 'Rita de Cascia': ['22/05'], 'Calliste': ['14/10'], 'Jean Gualbert': ['12/07'], 'Robert': ['30/04'], 'Camélien': ['28/07'], 'Robert de Reims': ['04/01'], 'Camelle': ['16/09'], 'Jean Léonardi': ['09/10'], 'Camille de Lellis': ['14/07'], 'Jean l’Evangéliste': ['27/12'], 'Roberte': ['30/04'], 'Candide': ['03/10'], 'Jean Népomucène': ['16/05'], 'Robin': ['30/04'], 'Cannera': ['28/01'], 'Jean Porte Latine': ['06/05'], 'Canut, roi du Danemark': ['19/01'], 'Jean Vianey': ['04/08'], 'Roch': ['16/08'], 'Capitoline': ['27/10'], 'Jean Baptiste': ['24/06'], 'Roch Gonzalez de Santa Cruz': ['17/11'], 'Caprais': ['01/06', '20/10'], 'Jean Baptiste de la Salle': ['07/04'], 'Rodane': ['02/06'], 'Jean Joseph de la Croix': ['05/03'], 'Capucine': ['05/10'], 'Jean Marie Vianney ou Viannet': ['04/08'], 'Roderick': ['13/03'], 'Carine': ['07/11'], 'Jeanne': ['08/05'], 'Rodobaldus': ['12/10'], 'Carl': ['04/11'], 'Jeanne d’Arc': ['30/05', '10/05'], 'Rodolphe': ['21/06'], 'Carloman': ['17/08'], 'Rodrigue': ['13/03'], 'Carlos': ['04/11'], 'Jeanne de Chantal': ['12/12'], 'Rogata': ['31/12'], 'Carmen': ['16/07'], 'Jeanne de Valois': ['04/02'], 'Rogatien': ['24/05'], 'Carole': ['17/07'], 'Jeanne Françoise de Chantal': ['12/12'], 'Roger': ['30/12'], 'Caroline': ['17/07'], 'Jeannine': ['30/05'], 'Carpe': ['13/04'], 'Jenny': ['30/05'], 'Roland': ['15/09'], 'Casilde': ['09/04'], 'Jérémie': ['01/05'], 'Casimir': ['04/03'], 'Jéroche': ['02/07'], 'Rolande': ['13/05', '15/09'], 'Cassien': ['05/08'], 'Jérôme': ['30/09'], 'Jérôme Emiliani': ['08/02'], 'Rollande ou Rolende': ['13/05'], 'Catalde': ['10/05'], 'Jéron': ['17/08'], 'Cathel': ['25/11'], 'Jessica': ['04/11'], 'Romain de Condat': ['28/02'], 'Catherine': ['25/11'], 'Jessy': ['04/11'], 'Romain du Mans': ['24/11'], 'Catherine de Bologne': ['09/03'], 'Jim': ['03/05'], 'Romaric': ['08/12', '10/12'], 'Catherine de Sienne': ['29/04'], 'Joachim': ['26/07'], 'Catherine de Suède': ['24/03'], 'Joannice': ['04/11'], 'Romary': ['08/12'], 'Catherine L.': ['25/11'], 'Rombaud': ['24/06'], 'Catherine Labouré': ['28/11'], 'Joavan': ['02/03'], 'Romble': ['01/11'], 'Cécile': ['22/11'], 'Joconde': ['27/07', '25/11'], 'Romedius': ['15/01'], 'Cédric': ['07/01'], 'Roméo': ['25/02'], 'Céleste': ['14/10'], 'Joël': ['13/07'], 'Romphaire': ['26/11'], 'Célestin': ['02/05', '19/05'], 'Joëlle': ['13/07'], 'Romuald': ['07/02', '19/06'], 'Joévin': ['02/03'], 'Célia': ['22/11'], 'Johanne': ['30/05'], 'Romule': ['24/03'], 'Céline': ['21/10'], 'John': ['24/06'], 'Ronald': ['17/09'], 'Johnny': ['27/12'], 'Ronan': ['01/06'], 'Joire': ['29/10'], 'Roparz': ['30/04'], 'Rosalie': ['04/09'], 'Censure': ['10/06'], 'Jordane': ['13/02'], 'Rosaline': ['17/01'], 'Céréal': ['14/09'], 'Joris': ['26/07'], 'Rose de Lima': ['23/08'], 'Céréale': ['28/02'], 'Josaphat': ['12/11'], 'Roseline': ['17/01'], 'Césaire d’Arles': ['26/08'], 'José': ['19/03'], 'Rosemonde': ['30/04'], 'Césaire de Nazianze': ['25/02'], 'Joseph': ['19/03'], 'Rosette': ['23/08'], 'César': ['26/08'], 'Joseph Barsabas': ['20/07'], 'Rosine': ['11/03'], 'César de Bus': ['15/04'], 'Rosita': ['23/08'], 'Césarie': ['12/01', '15/05'], 'Joseph de Calsanz': ['25/08'], 'Rosy': ['23/08'], 'Joseph de Cupertino': ['18/09', '25/11'], 'Rotgang': ['06/03'], 'Césarine': ['12/01'], 'Chaire Pierre Apôtre': ['22/02'], 'Joseph de Cupiterno': ['25/11'], 'Rotrude': ['22/06'], 'Chandeleur': ['02/02'], 'Rozenn': ['23/08'], 'Chantal': ['12/12'], 'Joseph Travailleur': ['01/05'], 'Ruaud': ['22/10'], 'Charité': ['01/08'], 'Joséphine': ['19/03'], 'Rudesinde': ['01/03'], 'Charlemagne': ['28/01'], 'Josette': ['19/03'], 'Rudy': ['21/06'], 'Charles Boromée': ['04/11'], 'Josiane': ['19/03'], 'Ruellin': ['28/02'], 'Charles le bon': ['02/03'], 'Josse de Bretagne': ['13/12'], 'Charles Lwanga': ['03/06'], 'Josselin': ['13/12'], 'Ruf': ['14/11'], 'Charley': ['04/11'], 'Josseline': ['13/12'], 'Ruffin': ['14/06'], 'Charlotte': ['17/07'], 'Josué': ['01/09'], 'Rufin': ['14/06'], 'Cher': ['29/04'], 'Jouin': ['01/06'], 'Rufine': ['10/07'], 'Chéron': ['28/05'], 'Jour de l’an': ['01/01'], 'Rufus': ['14/11'], 'Christel': ['24/07'], 'Jovite': ['15/02'], 'Rupert de Salzbourg': ['27/03'], 'Christelle': ['24/07'], 'Juanita': ['30/04'], 'Rusticule': ['12/08'], 'Christian': ['12/11'], 'Jucicaël': ['17/12'], 'Rustique': ['25/04', '18/08', '09/10', '14/10', '26/10'], 'Christiane': ['24/07', '12/11'], 'Jude': ['28/10'], 'Judicaël': ['17/12'], 'Christin': ['12/11'], 'Judith': ['05/05'], 'Christine de Bolsène': ['24/07'], 'Jules 1er': ['12/04'], 'Christophe': ['25/07', '21/08'], 'Julie': ['08/04', '10/12'], 'Rutilus': ['04/06'], 'Rutule': ['18/02'], 'Chrodegang': ['03/09', '06/03'], 'Julie Billart': ['08/04'], 'Sabas': ['05/12'], 'Julien de Brioude': ['28/08'], 'Sabin': ['11/07', '30/12'], 'Chrysante ou Chrysanthe': ['25/10'], 'Julien de Tolède': ['08/03'], 'Chrysanthe': ['25/10'], 'Julien du Mans': ['27/01'], 'Sabine': ['29/08'], 'Chryseuil': ['07/02'], 'Julien l’hospitalier': ['09/01'], 'Sabinien': ['30/12'], 'Chrysogone': ['24/11'], 'Julien Eym': ['02/08'], 'Sabrina': ['29/08'], 'Cilinia': ['21/10'], 'Julienne': ['12/08'], 'Sacha': ['30/08'], 'Clair': ['01/01', '01/06', '10/10', '04/11'], 'Julienne de Bologne': ['07/02'], 'Julienne de Nicomédie': ['16/02'], 'Sadoc': ['02/06'], 'Juliette d’Ancyre': ['18/05'], 'Saens ou Saëns': ['14/11'], 'Juliette de Césarée': ['30/07'], 'Saffier': ['06/09'], 'Clair de Tours': ['08/11'], 'Salaberge': ['22/09'], 'Clair du Dauphiné': ['02/01'], 'Sallustie': ['14/09'], 'Claire d’Assise': ['11/08'], 'Juste de Lyon': ['14/10'], 'Saloine': ['20/08'], 'Clara': ['11/08'], 'Justin le Philosophe': ['01/06'], 'Salomé': ['29/06', '22/10', '17/11'], 'Clarisse': ['12/08'], 'Justine': ['12/03', '26/09', '30/11'], 'Classique': ['18/02'], 'Claude': ['15/02', '18/02'], 'Salomon 1er': ['25/06'], 'Jutta': ['05/05'], 'Salomon III': ['25/06'], 'Claude du Jura': ['06/06'], 'Juvénal': ['07/05'], 'Salonius': ['28/09'], 'Claude la Colombière': ['15/02'], 'Juvénal de Narni': ['03/05'], 'Salutaris': ['13/07'], 'Claudette': ['15/02'], 'Juvence': ['08/02'], 'Salvatore': ['18/03'], 'Claudie': ['15/02'], 'Juvin': ['03/10'], 'Claudine': ['15/02'], 'Karelle': ['07/11'], 'Salvien': ['22/07'], 'Claudius': ['15/02'], 'Karen': ['07/11'], 'Salvius': ['28/10'], 'Clélia': ['13/07'], 'Karine': ['24/03', '07/11'], 'Samson': ['28/07'], 'Clémence': ['21/03'], 'Samuel': ['20/08'], 'Clément 1er': ['23/11'], 'Katel': ['25/11'], 'Samy': ['20/08'], 'Clémentin': ['14/11'], 'Katia': ['25/11'], 'Sandale': ['03/09'], 'Clémentine': ['23/11'], 'Katy': ['25/11'], 'Sandie': ['02/04'], 'Cléophas': ['25/09'], 'Kelvin': ['03/06'], 'Sandra': ['02/04'], 'Clet': ['26/04'], 'Kelvyn': ['03/06'], 'Sandrine': ['02/04'], 'Clodoald': ['07/09'], 'Ketty': ['25/11'], 'Sara': ['13/07', '09/10'], 'Clotilde': ['03/06', '04/06', '23/06'], 'Kevin': ['03/06'], 'Kineburge': ['06/03'], 'Sardot': ['04/05'], 'Sature': ['07/03', '29/03'], 'Clotsende': ['30/06'], 'Kurt': ['26/11'], 'Cloud': ['07/09'], 'Ladislas': ['27/06', '29/07'], 'Saturnin': ['07/03', '29/11'], 'Clovis': ['25/08'], 'Colette de Corbie': ['06/03'], 'Laetitia': ['18/08'], 'Savin': ['12/07', '11/07'], 'Colin': ['06/12'], 'Lamain': ['23/11'], 'Lamalisse': ['03/03'], 'Scariberge': ['02/10'], 'Colombe de Sens': ['31/12'], 'Lambert': ['17/09'], 'Scholastique': ['10/02'], 'Landelin': ['15/06'], 'Scolastique': ['10/02'], 'Landoald': ['19/03'], 'Sébald': ['19/08'], 'Côme': ['26/09', '27/09'], 'Landrade': ['08/07'], 'Sébastien': ['20/01'], 'Landry': ['10/06'], 'Second': ['09/01'], 'Concorde': ['01/01', '25/02', '02/09'], 'Landulphe': ['18/08'], 'Seconde': ['10/07'], 'Lara': ['26/03'], 'Secondel': ['01/08'], 'Large': ['08/08'], 'Secondille': ['02/03'], 'Concordia': ['13/08'], 'Larissa': ['26/03'], 'Secondine': ['15/01'], 'Conogan': ['15/10'], 'Laudulphe': ['18/08'], 'Secondule': ['07/03'], 'Conon': ['29/05'], 'Laure': ['10/08'], 'Sedna': ['10/03'], 'Conrad de Constance': ['26/11'], 'Laurence': ['10/08'], 'Sédophe': ['05/07'], 'Conrad de Parhzam': ['21/04'], 'Laurent de Brindisi': ['21/07'], 'Ségolène': ['24/07'], 'Conrad de Plaisance': ['19/02'], 'Laurent de Rome': ['10/08'], 'Seine': ['19/09'], 'Constable': ['17/02', '23/09'], 'Laurent Imbert': ['20/09'], 'Selma': ['21/04'], 'Laurent Justinien': ['05/09'], 'Sénateur': ['28/05'], 'Constance': ['08/04', '23/09', '12/12'], 'Laurentine': ['10/08'], 'Laurette': ['10/08'], 'Sennen': ['30/07'], 'Laurie': ['10/08'], 'Sénorine': ['22/04'], 'Constancia': ['19/09'], 'Lazare': ['23/02', '29/07'], 'Septime': ['24/10'], 'Constant': ['23/09'], 'Séraphin du Mont Granario': ['12/10'], 'Constantin 1er le Grand': ['21/05'], 'Léa': ['22/03'], 'Séraphine': ['12/03'], 'Consul': ['07/07'], 'Léandre': ['27/02'], 'Sérapion': ['14/11'], 'Contran': ['28/03'], 'Léger': ['02/10'], 'Serdieu': ['16/09'], 'Conversion de Paul': ['25/01'], 'Léïla': ['22/03'], 'Serdon': ['05/05'], 'Cora': ['18/05'], 'Léna': ['18/08'], 'Serein': ['02/10'], 'Coralie': ['18/05'], 'Lénaïc': ['18/08'], 'Sérène': ['07/05'], 'Cordule': ['22/10'], 'Léobard': ['18/01'], 'Serge': ['07/10'], 'Corentin': ['12/12'], 'Léobon': ['13/10'], 'Sergine': ['07/10'], 'Corentine': ['12/12'], 'Léocadie': ['09/12'], 'Sernin': ['29/11'], 'Corinne': ['18/05'], 'Léodebod': ['08/08'], 'Seroire': ['20/08'], 'Corne': ['26/09'], 'Léon IV': ['17/07'], 'Sérotin': ['31/12'], 'Corneille': ['16/09'], 'Léon le Grand': ['10/11'], 'Sérotina': ['31/12'], 'Cornélie': ['31/03'], 'Léonard': ['06/11'], 'Servais': ['13/05'], 'Léonce de Césarée': ['13/01'], 'Servan': ['01/07'], 'Cosme': ['27/09'], 'Léonce de Tripoli': ['18/06'], 'Servane': ['01/07'], 'Couronne': ['14/05'], 'Léone': ['10/11'], 'Servule': ['23/12'], 'Crémence': ['16/04'], 'Léonide': ['19/04', '22/04'], 'Sessétrude': ['07/05'], 'Crépin': ['25/10', '25/10'], 'Séthride': ['10/01'], 'Léonilde': ['10/11'], 'Seurin': ['23/10'], 'Crescence ou Crescent': ['10/03'], 'Léontine': ['10/11'], 'Sève': ['26/07'], 'Crescent ou Crescence': ['10/03'], 'Léopard': ['30/09'], 'Sever': ['01/02'], 'Crésiphon': ['15/05'], 'Léopold': ['15/11'], 'Crispin': ['25/10'], 'Léothade': ['23/10'], 'Croix': ['03/05', '14/09'], 'Léri': ['30/09'], 'Séverin': ['27/11'], 'Leslie': ['17/11'], 'Séverine': ['27/11'], 'Cumian': ['09/06'], 'Lethard': ['24/02'], 'Sevêtre': ['15/04'], 'Cunégonde': ['03/03'], 'Leu': ['01/09'], 'Sheila': ['22/11'], 'Cunégonde de Pologne': ['24/07'], 'Leubais': ['27/07'], 'Sibille': ['09/10'], 'Cuniald': ['24/09'], 'Leucone': ['01/04'], 'Sibylline': ['19/03'], 'Cunibert': ['12/11'], 'Leudin': ['11/09'], 'Sicaire': ['26/03'], 'Curonote': ['12/09'], 'Leufroy': ['21/06'], 'Sidoine': ['23/08', '14/11'], 'Cyprien': ['16/09'], 'Leutiern': ['17/10'], 'Cyprille': ['05/07'], 'Lézin': ['01/11'], 'Sidonie': ['14/11'], 'Cyran': ['04/12'], 'Lia': ['22/03'], 'Siegfried': ['22/08'], 'Cyrénie': ['01/11'], 'Libence': ['04/01'], 'Siffredus': ['27/11'], 'Cyriaque': ['08/08'], 'Libérateur': ['15/05'], 'Siffrein de Carpentras': ['27/11'], 'Cyrille': ['14/02', '28/10'], 'Libert': ['23/06'], 'Sigebaud': ['26/10'], 'Liboire': ['23/07'], 'Sigebert': ['01/02', '27/09'], 'Cyrille d’Alexandrie': ['27/06'], 'Lidoire': ['13/09'], 'Cyrille de Jérusalem': ['18/03'], 'Lidwine': ['14/04'], 'Sigefroy': ['15/02', '22/08'], 'Cyrus': ['31/01'], 'Lié': ['05/11'], 'Dafrose': ['04/01'], 'Liébaut': ['08/08'], 'Sigfrid': ['15/02', '22/08'], 'Dahlia': ['05/10'], 'Liède': ['01/09'], 'Daisy': ['16/11'], 'Liéfard': ['04/02'], 'Sigisbaud': ['07/07'], 'Damasse 1er': ['11/12'], 'Sigisbert': ['11/07'], 'Damien': ['26/09', '27/09'], 'Liévin': ['12/11'], 'Sigismond': ['01/05'], 'Liévine': ['17/10'], 'Sigolène': ['24/07'], 'Daniel Brottier': ['28/02'], 'Lifard': ['03/06'], 'Sigolin': ['28/10'], 'Daniel le Stylite': ['11/12'], 'Liguaire': ['12/11'], 'Sigrade': ['08/08'], 'Danièle': ['11/12'], 'Lila': ['22/03'], 'Danitza': ['11/12'], 'Lilian': ['04/07'], 'Silvain': ['04/05'], 'Dany': ['11/12'], 'Liliane': ['04/07'], 'Silvère': ['20/06'], 'Daria': ['25/10'], 'Lily': ['17/11'], 'Silvia': ['03/11'], 'Darie': ['25/10'], 'Lin': ['23/09'], 'Siméon': ['05/01', '18/02'], 'Darius': ['19/12'], 'Linda': ['28/08'], 'Dathe': ['03/07'], 'Line': ['20/10'], 'Siméon stylite le Jeune': ['03/09'], 'David': ['29/12'], 'Lioba': ['28/09'], 'Similien': ['16/06'], 'Davy': ['20/09'], 'Lionel': ['10/11'], 'Simon le Cananéen': ['28/10'], 'Déborah': ['21/09'], 'Lisbeth': ['17/11'], 'Simone': ['28/10'], 'Défendant': ['25/09'], 'Lise': ['17/11'], 'Simplice de Bourges': ['16/06'], 'Défunts': ['02/11'], 'Lisette': ['17/11'], 'Sinice': ['01/09'], 'Liutrude': ['22/09'], 'Siran': ['04/12'], 'Delphin': ['24/12'], 'Lizzie': ['17/11'], 'Sirice': ['26/11'], 'Delphine': ['26/09', '26/11'], 'Siridion': ['02/01'], 'Loïc': ['25/08', '01/12'], 'Sirile': ['21/02'], 'Démétrie': ['21/06'], 'Sisinnius': ['29/05'], 'Démétrien': ['06/11'], 'Loïs': ['21/06'], 'Sisoès': ['06/07'], 'Lola': ['15/09'], 'Siviard': ['01/03'], 'Denis': ['09/10'], 'Lolita': ['15/09'], 'Sixte': ['08/04'], 'Denise': ['15/05'], 'Longin': ['15/03'], 'Sixte II': ['06/08'], 'Denys': ['26/12'], 'Lore': ['25/06'], 'Soizic': ['04/10'], 'Lorraine': ['30/05'], 'Solange': ['10/05'], 'Désert': ['26/06'], 'Louis de France': ['25/08'], 'Soledad': ['11/10'], 'Désiré': ['11/02', '18/12', '08/05'], 'Louis de Gonzague': ['21/06'], 'Solenne': ['25/09', '17/10'], 'Louis Marie de Grignon de Montfort': ['28/04'], 'Louise de Marillac': ['15/03'], 'Soline': ['17/10'], 'Désiré de Besançon': ['27/07'], 'Louis François Barret': ['02/09'], 'Sonia': ['18/09'], 'Deusdedit': ['14/07', '10/08', '09/10', '08/11', '10/12'], 'Loup': ['29/07', '01/09'], 'Sophie': ['30/04', '25/05'], 'Sosipatre': ['25/06'], 'Luc l’évangéliste': ['18/10'], 'Sosthène': ['28/11'], 'Lucas': ['18/10'], 'Soter': ['22/04'], 'Dévote': ['27/01'], 'Luce': ['13/12'], 'Sperandea': ['11/09'], 'Diane': ['09/06'], 'Lucette': ['13/12'], 'Stable': ['14/12'], 'Didace': ['13/11'], 'Lucide': ['26/04'], 'Stanislas': ['11/04'], 'Didier': ['23/05'], 'Lucie': ['06/07'], 'Stella': ['11/05'], 'Diego': ['13/11'], 'Lucie de Syracuse': ['13/12'], 'Stéphane': ['26/12'], 'Diémode': ['29/03'], 'Lucien': ['08/01'], 'Stéphanie': ['26/12'], 'Dietrich': ['01/07'], 'Lucienne': ['08/01'], 'Steve': ['26/12'], 'Dieudonné': ['10/08'], 'Lucille': ['16/02'], 'Suitbert': ['01/03'], 'Dimitri': ['26/10', '27/10'], 'Lucrèce': ['15/03', '23/11'], 'Sulpice': ['29/01'], 'Sulpice le Pieux': ['17/01'], 'Diodore': ['01/12'], 'Ludmila': ['16/09'], 'Sulplice': ['29/01'], 'Diomède': ['16/08', '02/09', '11/09'], 'Ludolphe': ['29/03'], 'Suzanne': ['11/08'], 'Ludovic': ['25/08'], 'Suzel': ['11/08'], 'Ludwig': ['25/08'], 'Suzette': ['11/08'], 'Dioscore': ['21/12'], 'Lufthilde': ['22/01', '23/01'], 'Suzon': ['11/08'], 'Dirk': ['01/07'], 'Suzy': ['11/08'], 'Lunaire': ['01/07'], 'Svetlana': ['20/03'], 'Dismas': ['25/03'], 'Lupercule': ['05/03'], 'Sylvain': ['04/05'], 'Lutgarde': ['16/06'], 'Sylvaine': ['04/05'], 'Dizier': ['26/03'], 'Luthard': ['02/05'], 'Sylvère': ['20/06'], 'Dogmaël': ['14/06'], 'Lydiane': ['03/08'], 'Sylvestre': ['31/12'], 'Dolorès': ['15/09'], 'Lydie la Pourpre': ['03/08'], 'Sylvette': ['05/11'], 'Dominanda': ['31/12'], 'Macaire': ['10/04'], 'Sylviane': ['05/11'], 'Dominateur': ['05/11'], 'Macaire le Jeune': ['02/01'], 'Sylvie': ['05/11'], 'Dominin': ['09/10'], 'Maccaille': ['25/04'], 'Symphorien': ['22/08'], 'Dominique': ['06/07'], 'Macrine la Jeune': ['19/07'], 'Symphorose': ['02/07'], 'Macrine l’Ancienne': ['14/01'], 'Tamara': ['01/05'], 'Dominique de Guzman': ['08/08'], 'Macrobe': ['13/09'], 'Tanche': ['10/10'], 'Dominique Savio': ['09/03'], 'Macteflède': ['13/03'], 'Tanguy': ['19/11'], 'Domitien': ['01/07'], 'Madalvé': ['04/10'], 'Tania': ['12/01'], 'Domitille': ['07/05'], 'Maddy': ['22/07'], 'Taraise': ['25/02'], 'Dommin inconnue Domnin': ['21/07'], 'Madelberte': ['07/09'], 'Tarbula': ['22/04'], 'Donald': ['15/07'], 'Madeleine': ['22/07'], 'Tarbule': ['22/04'], 'Donat': ['07/08'], 'TarciceinconnueTarcice': ['15/01'], 'Donatien': ['24/05'], 'Mael': ['13/05'], 'Tarcisius': ['15/08'], 'Dora': ['09/11'], 'Maël': ['24/05'], 'Tarsilla': ['24/12'], 'Doria': ['25/10'], 'Maëlle': ['24/05'], 'Tatiana': ['12/01'], 'Dorine': ['09/11'], 'Maelrub': ['21/04'], 'Tatienne': ['12/01'], 'Doris': ['06/02'], 'Mafalda': ['02/05'], 'Teddy': ['05/01', '28/10', '09/11'], 'Dorothée': ['06/02', '05/06'], 'Mafflée': ['13/03'], 'Magali': ['20/07'], 'Droctovée': ['10/03'], 'Maggy': ['20/07'], 'Telchide': ['10/10'], 'Druon': ['16/04'], 'Magloire': ['24/10'], 'Télesphore': ['05/01'], 'Magnéric': ['25/07'], 'Tenenan': ['16/07'], 'Eadbert': ['06/05'], 'Maidoc': ['23/03'], 'Ténestine': ['24/08'], 'Eanflède': ['24/11'], 'Maieul': ['11/05'], 'Térésa': ['15/10'], 'Earcongatha': ['23/02'], 'Maimbeuf': ['16/10'], 'Tessa': ['17/12'], 'Ébrégésile': ['31/08'], 'Maïté': ['07/06'], 'Tétrade': ['16/02'], 'Edburge': ['13/12'], 'Maixent': ['26/06'], 'Teutérie': ['05/05'], 'Edgar le Pacifique': ['08/07'], 'Majoric': ['06/12'], 'Thaddée': ['28/10'], 'Édilbert': ['24/02'], 'Majorien': ['29/10'], 'Thaïs': ['08/10'], 'Edith de Wilton': ['16/09'], 'Malard': ['15/01'], 'Thamel': ['04/09'], 'Edma': ['20/11'], 'Malo': ['15/11'], 'Thécla': ['20/11'], 'Edmée': ['20/11'], 'Malou': ['04/05'], 'Thècle': ['18/01', '24/09'], 'Edmond': ['20/11'], 'Malrub': ['27/08'], 'Edouard': ['05/01'], 'Edouardine': ['05/01'], 'Malulf': ['04/05'], 'Thémistocle': ['21/12'], 'Edwige': ['16/10'], 'Mamert': ['11/05'], 'Mamertin': ['30/03'], 'Théodore de Tarse': ['19/09'], 'Mamet': ['17/08'], 'Théodore le Studite': ['11/11'], 'Eglantine': ['23/08'], 'Mandrien': ['19/08'], 'Théodore le Tiron': ['09/11'], 'Élaphe': ['19/08'], 'Théodore Trichinas': ['20/04'], 'Eléazar': ['01/08'], 'Manoël': ['25/12'], 'Théodoric': ['01/07'], 'Élénaire': ['02/05'], 'Mansuet': ['19/02'], 'Théodose le cénobiarque': ['11/01'], 'Eléonore': ['25/06'], 'Mansuy': ['03/09'], 'Théodosie': ['02/04'], 'Éléonore': ['28/12'], 'Manuel': ['25/12'], 'Théodule': ['17/02', '12/09'], 'Eleuthère': ['18/04', '09/10'], 'Manvieu': ['28/05'], 'Marc l’évangéliste': ['25/04'], 'Théoneste': ['30/10'], 'Elfi': ['08/12'], 'Marceau': ['16/01'], 'Théonille': ['23/08'], 'Elfleda': ['08/02'], 'Marcel': ['09/04', '01/11'], 'Théophane': ['02/02'], 'Elfried': ['08/12'], 'Théophila': ['28/12'], 'Eliane': ['04/07'], 'Théophile': ['20/12'], 'Elie': ['20/07'], 'Marcel 1er, pape': ['16/01'], 'Théophile d’Adana': ['28/02'], 'Eliette': ['20/07'], 'Marcelin': ['06/04'], 'Théophile d’Antioche': ['13/10'], 'Marceline': ['17/07'], 'Théophile de Césarée': ['05/03'], 'Eline': ['18/08'], 'Marcelle': ['31/01'], 'Théopompe': ['21/05'], 'Elisabeth': ['05/11'], 'Marcellin': ['06/04', '26/04', '01/06', '02/06'], 'Thérèse d’Avilla': ['15/10'], 'Elisabeth de Hongrie': ['17/11'], 'Thérèse de l’Enfant Jésus': ['01/10'], 'Elisabeth de Portugal': ['04/07'], 'Thérèse de Lisieux': ['01/10'], 'Elise': ['17/11'], 'Thetgo': ['09/05'], 'Elisée': ['14/06'], 'Ella': ['01/02'], 'Marcia': ['05/06'], 'Ellénita': ['01/02'], 'Marcien': ['25/08'], 'Thiadilde': ['30/01'], 'Élodie': ['22/10'], 'Marcienne': ['12/07'], 'Thibaud': ['21/05', '01/06', '08/07'], 'Eloi': ['01/12'], 'Marcoul': ['01/05'], 'Eloi d’été': ['29/06'], 'Marguerie Marie Alacoque': ['16/10'], 'Elphège': ['19/04'], 'Marguerite d’Antioche': ['20/07'], 'Thibaud de Provins': ['30/06'], 'Elphège l’ancien': ['12/03'], 'Marguerite de Cortone': ['22/02'], 'Thibaut': ['08/07'], 'Elpide': ['02/09'], 'Marguerite d’Ecosse': ['16/11'], 'Thiébaut': ['08/07'], 'Elpidephore': ['02/11'], 'Maria': ['24/11'], 'Thierry': ['01/07'], 'Elsa': ['17/11'], 'Maria Goretti': ['06/07'], 'Elsy': ['17/11'], 'Mariam': ['15/08'], 'Thomas': ['21/12'], 'Elvire': ['16/07'], 'Marianne': ['09/07'], 'Thomas apôtre': ['03/07'], 'Elzéar de Sabran': ['26/09'], 'Mariannick': ['15/08'], 'Thomas Becket': ['29/12'], 'Marie': ['15/08', '08/09'], 'Thomas d’Aquin': ['28/01'], 'Émébert': ['15/01'], 'Thomas de Villeneuve': ['22/09'], 'Marie Crucifiée de Rose': ['15/12'], 'Thomas More': ['22/06'], 'Émeline': ['27/10'], 'Marie de Cléophas': ['09/04'], 'Thorette': ['01/05'], 'Émérentienne': ['23/01', '21/10'], 'Marie Mère de Dieu': ['01/01'], 'Thraséas': ['05/10'], 'Marielle': ['15/08'], 'Thryphène': ['31/01'], 'Émeric': ['04/11'], 'Marie Madeleine': ['22/07'], 'Tiburce': ['09/09'], 'Émerita': ['22/09'], 'Marie Madeleine de Pazzi': ['25/05'], 'Tigre': ['12/01'], 'Emile': ['22/05'], 'Marie Madeleine Postel': ['16/07'], 'Tilbert': ['07/09'], 'Émilie': ['22/05'], 'Marien': ['06/05'], 'Timothée': ['26/01'], 'Emilie de Rodat': ['19/09'], 'Marie Thérèse': ['07/06'], 'Tino': ['14/02'], 'Emilien': ['12/11'], 'Marietta': ['06/07'], 'Tiphaine': ['06/01'], 'Emilienne': ['05/01'], 'Mariette': ['06/07'], 'Tite': ['26/01'], 'Émilion': ['16/11'], 'Marilyne': ['15/08'], 'Toinon': ['28/02'], 'Emma': ['19/04'], 'Marin': ['04/09'], 'Toribio de Mogrovejo': ['23/03'], 'Emmanuel': ['26/03', '25/12'], 'Marina': ['20/07'], 'Tous': ['01/11'], 'Marinette': ['20/07'], 'Toussaint': ['01/11'], 'Emmanuelle': ['25/12'], 'Marion': ['15/08'], 'Tranquille': ['15/03'], 'Emmélie de Césarée': ['30/05'], 'Marius': ['19/01'], 'Transfiguration': ['06/08'], 'Encratide': ['16/04'], 'Marjolaine': ['15/08'], 'Trémeur': ['07/11'], 'Endée': ['21/03'], 'Marjorie': ['20/07'], 'Trésain': ['07/02'], 'Engelmond': ['21/06'], 'Marlène': ['15/08'], 'Tridoire': ['25/10'], 'Enguéran ou Enguerran': ['25/10'], 'Marole': ['23/04'], 'Triduana': ['08/10'], 'Enguerran ou Enguéran': ['25/10'], 'Mars': ['08/06'], 'Triphille': ['13/06'], 'Énimie': ['05/10'], 'Marthe de Béthanie': ['29/07'], 'Triphine': ['05/07'], 'Ennode': ['17/07'], 'Martial de Limoges': ['30/06'], 'Triphyllius': ['13/06'], 'Énogat': ['13/01'], 'Martin': ['04/07'], 'Trivier': ['16/01'], 'Enrique': ['13/07'], 'Martin 1er': ['13/04'], 'Trojan': ['30/11'], 'Éodald': ['31/12'], 'Martin de Porrès': ['03/11'], 'Tryphon': ['10/11'], 'Éoharn': ['11/02'], 'Martin de Tours': ['11/11'], 'Tryphonie': ['18/10'], 'Épain': ['25/10'], 'Martine': ['30/01'], 'Tual': ['30/11'], 'Ephrem le Syrien': ['09/06'], 'Martinien': ['02/07'], 'Tudal': ['01/12'], 'Martyrius': ['29/05'], 'Tudi': ['09/05'], 'Epiphanie': ['06/01'], 'Marylise': ['15/08'], 'Tudin': ['09/05'], 'Épiphanie': ['06/01'], 'Maryse': ['15/08'], 'Tudy': ['09/05'], 'Erasme': ['02/06'], 'Maryvonne': ['15/08'], 'Erbinet': ['25/05'], 'Materne': ['14/09'], 'Erc': ['31/10'], 'Mathan': ['14/11'], 'Turiau': ['13/07'], 'Ercongote': ['07/07'], 'Mathias': ['24/02'], 'Turibe': ['16/04'], 'Érembert': ['24/10'], 'Mathieu ou Matthieu l’apôtre': ['21/09'], 'Tutwal': ['30/11'], 'Éremberte': ['16/10'], 'Mathilde': ['14/03'], 'Tychique': ['29/04'], 'Erémentienne': ['23/01'], 'Mathurin': ['01/11', '09/11'], 'Ubald Adimari': ['09/04'], 'Érentrude': ['30/06'], 'Ubald Baldassini': ['16/05'], 'Eric': ['18/05'], 'Matthias': ['14/05'], 'Ugolin': ['10/10'], 'Erich': ['18/05'], 'Maud': ['14/03'], 'Uldaric': ['04/07'], 'Erika': ['18/05'], 'Ulfrid': ['18/01'], 'Ermelinde': ['29/10'], 'Ulphace': ['09/09'], 'Ermenburge': ['19/11'], 'Ulphe': ['31/01'], 'Ermengaud': ['03/11'], 'Maur': ['15/01', '08/11'], 'Ulpien': ['03/04'], 'Ermenilda': ['13/02'], 'Ulric': ['04/07'], 'Ernée': ['09/08'], 'Maurice': ['22/09'], 'Ulrich': ['10/07'], 'Ernest': ['07/11'], 'Mauricette': ['22/09'], 'Urbain': ['25/05'], 'Ernestine': ['07/11'], 'Urbain IV': ['19/12'], 'Erwan': ['19/05'], 'Urbain V': ['06/11'], 'Erwin': ['19/05'], 'Maxence': ['26/06'], 'Urbin': ['25/05'], 'Espérance': ['01/08'], 'Maxime': ['14/04'], 'Urcisse': ['13/12'], 'Esso': ['27/12'], 'Maxime de Riez': ['27/11'], 'Esteban': ['26/12'], 'Maxime de Turin': ['25/06'], 'Urielle': ['01/10'], 'Estelle': ['11/05'], 'Maximien Kolbe': ['14/08'], 'Esther': ['01/07'], 'Maximilien': ['14/08'], 'Urpasien': ['13/03'], 'Été': ['21/06'], 'Maximilien de Théveste': ['12/03'], 'Ursanne': ['20/12'], 'Ethelburge': ['05/04', '11/10'], 'Maximin de Trèves': ['29/05'], 'Ursicin': ['20/12'], 'May': ['20/07'], 'Ursmar': ['19/04'], 'Etheldrède': ['23/06'], 'Mayeul': ['11/05'], 'Ursula': ['21/10'], 'Ethelhard': ['12/05'], 'Médard de Noyon': ['08/06'], 'Ursule': ['21/10'], 'Etienne d’Apt': ['07/11'], 'Ursuline': ['07/04'], 'Etienne de Hongrie': ['16/08'], 'Mélaine': ['06/01'], 'Vaast': ['06/02'], 'Etienne de Protomartyr': ['26/12'], 'Melaine de Rennes': ['06/01'], 'Vaclav ou Venceslav': ['28/09'], 'Etoile': ['11/05'], 'Valdrade': ['05/05'], 'Eubert': ['01/02'], 'Mélanie': ['26/01', '26/11'], 'Valentin': ['14/02'], 'Valentine': ['14/02', '25/07'], 'Eudes': ['19/08'], 'Mélanie la jeune': ['07/01', '31/12'], 'Eugène': ['13/07'], 'Valentinien': ['03/11'], 'Eugène 1er': ['02/06'], 'Mélanie l’Ancienne': ['08/06'], 'Valère': ['14/06'], 'Eugénie': ['07/02', '15/10'], 'Melchior': ['06/01'], 'Valérie': ['28/04', '05/06'], 'Mélitène': ['15/09'], 'Eugénie de Cordoue': ['26/03'], 'Mellon': ['22/10'], 'Eulalie de Barcelone': ['12/02'], 'Memmius': ['05/08'], 'Valérien': ['14/04'], 'Eulampie': ['10/10'], 'Mémoire': ['01/06'], 'Valéry': ['01/04'], 'Euloge de Cordoue': ['11/03'], 'Ménalippe': ['02/09'], 'Vallier': ['22/10'], 'Euphémie': ['20/03', '03/09', '16/09'], 'Ménandre': ['01/08'], 'Valtrude': ['09/04'], 'Menou': ['12/07'], 'Vambert': ['26/06'], 'Méraut': ['23/02'], 'Vandon': ['17/04'], 'Euphrase': ['15/05'], 'Mercurial': ['23/05'], 'Vanessa': ['04/02'], 'Euphrasie': ['13/03'], 'Mériadec': ['07/06'], 'Vanina': ['30/05'], 'Euphrosyne': ['01/01', '11/02', '08/11'], 'Mérole': ['18/03'], 'Vassili': ['02/01'], 'Messaline': ['19/01', '23/01'], 'Venance': ['18/05'], 'Euplius': ['12/08'], 'Méthode': ['14/02'], 'Venceslas': ['28/09'], 'Eurielle': ['01/10'], 'Métrobe': ['24/12'], 'Venceslas ou Vanceslas': ['28/09'], 'Eusèbe': ['31/01', '17/08'], 'Métrophane': ['04/06'], 'Venturin de Bergame': ['28/03'], 'Métropole': ['08/10'], 'Véra': ['18/09'], 'Michel l’Archange': ['29/09'], 'Véran de Cavaillon': ['13/11'], 'Eusèbe de Crémone': ['05/03'], 'Michèle': ['29/09'], 'Vérane': ['11/11'], 'Eusèbe de Rome': ['14/08'], 'Micheline': ['29/09'], 'Vérémond': ['13/02', '08/03'], 'Eusèbe de Samosate': ['21/06'], 'Mikaël': ['29/09'], 'Eusèbe de Verceil': ['02/08'], 'Milburge': ['23/02'], 'Vérène': ['01/09'], 'Eusébie': ['16/03'], 'Mildred': ['13/07'], 'Véridienne': ['01/02'], 'Eustache': ['20/09'], 'Mildrède': ['13/07'], 'Verny': ['19/04'], 'Eustadiole': ['08/06'], 'Milène': ['15/08'], 'Véronique': ['13/01', '04/02', '08/03', '12/07'], 'Eustochium': ['28/09'], 'Euthalie': ['27/08'], 'Miloud': ['22/05'], 'Euthyme de Sardes': ['11/03'], 'Miltiade': ['10/12'], 'Eutrope d’Orange': ['27/05'], 'Minase': ['20/01'], 'Véronique Giuliani': ['09/07'], 'Eutropie': ['15/06'], 'Mireille': ['15/08'], 'Vianney': ['04/08'], 'Eutyche': ['23/05'], 'Misael': ['16/12'], 'Victeur': ['01/09'], 'Eva': ['06/09'], 'Mitre': ['13/11'], 'Victoire': ['15/11', '23/12'], 'Évariste': ['14/10', '26/10', '23/12'], 'Modéran': ['22/10'], 'Modérate': ['06/04'], 'Victor': ['21/07'], 'Modeste': ['24/02'], 'Victor 1er': ['28/07'], 'Evelyne': ['06/09', '27/12'], 'Modivène': ['05/07'], 'Victor III': ['16/09'], 'Modoald': ['12/05'], 'Victorien': ['23/03', '16/05', '26/08'], 'Éverilde': ['09/07'], 'Moïse': ['04/09', '25/11'], 'Evrard': ['14/08'], 'Molock': ['25/06'], 'Victorin': ['15/05'], 'Évremond': ['10/06'], 'Monegonde': ['02/07'], 'Victorine': ['15/05'], 'Evrilde': ['09/07'], 'Monique': ['27/08'], 'Victrice': ['07/08'], 'Ewald': ['03/10'], 'Moniteur': ['10/11'], 'Villain': ['07/05'], 'Expédit de Mélitène': ['19/04'], 'Monulphe': ['16/07'], 'Vincent': ['22/01'], 'Exupérance': ['26/04'], 'Morand': ['03/06'], 'Vincent de Paul': ['27/09'], 'Exupère': ['19/11'], 'Morvan': ['22/09'], 'Vincent Ferrier': ['05/04'], 'Exupérie': ['26/07'], 'Moshé': ['04/09'], 'Vincent Pallotti': ['22/01'], 'Ezéchiel': ['10/04'], 'Muguet': ['01/05'], 'Vinciane': ['11/09'], 'Fabien': ['20/01'], 'Muguette': ['01/05'], 'Vindémial': ['28/02', '02/05'], 'Fabienne': ['20/01'], 'Mummole': ['18/11'], 'Fabiola': ['27/12'], 'Muriel': ['15/08'], 'Vindicien': ['11/03'], 'Fabius': ['11/05', '31/07'], 'Myriam': ['15/08'], 'Violaine': ['05/10'], 'Myrtille': ['05/10'], 'Violette': ['05/10'], 'Fabrice': ['22/08'], 'Nabor': ['12/07'], 'Virgile': ['05/03', '10/10', '27/11'], 'Fabricien': ['22/08'], 'Nadège': ['18/09'], 'Faine': ['18/05'], 'Nadette': ['18/02'], 'Famien': ['08/08'], 'Nadia': ['18/09'], 'Virginie': ['07/01'], 'Fanchon': ['09/03'], 'Nadine': ['18/02', '18/09'], 'Viridiana': ['01/02'], 'Fandilas': ['13/06'], 'Viril': ['01/10'], 'Fandile': ['13/06'], 'Nahum': ['01/12'], 'Visitation': ['31/05', '02/07'], 'Fanny': ['26/12'], 'Nancy': ['26/07'], 'Fargeau': ['16/06'], 'Narcisse': ['29/10'], 'Vital': ['02/06'], 'Faron': ['28/10'], 'Natacha': ['26/08'], 'Vital de Milan': ['28/04'], 'Natalène': ['10/11'], 'Vitalien': ['27/01', '16/07'], 'Faustin': ['15/02'], 'Natalie': ['27/07'], 'Faustinien': ['26/02'], 'Nathalie': ['27/07'], 'Vitalina': ['13/08'], 'Fébronie': ['25/06'], 'Nathanaël': ['24/08'], 'Vitalique': ['04/09'], 'Félicie': ['07/03', '08/05'], 'Nathanaëlle': ['24/08'], 'Vivence': ['13/01'], 'Nativité de la Vierge': ['08/09'], 'Viventien': ['04/08'], 'Félicien': ['09/06'], 'Naucrace': ['08/06'], 'Vivian': ['10/03'], 'Félicité': ['07/03', '08/05', '10/07'], 'Nazaire': ['12/01', '12/06', '28/07'], 'Viviane': ['02/12'], 'Vivien': ['10/03', '28/08'], 'Félix': ['12/02', '19/05'], 'Volusien': ['18/01'], 'Nectaire': ['01/08', '13/09', '09/12'], 'Vrain': ['19/10', '13/11'], 'Félix de Cantalice': ['18/05'], 'Félix de Nantes': ['07/07'], 'Vulfétrude': ['23/11'], 'Félix de Nole': ['14/01'], 'Nello': ['25/12'], 'Walburge': ['25/02'], 'Félix de Valois': ['20/11'], 'Nelly': ['18/08', '25/12'], 'Walfrid': ['15/02'], 'Ferdinand d’Aragon': ['27/06'], 'Walfroy': ['15/02'], 'Ferdinand III': ['30/05'], 'Nemèse': ['19/12'], 'Wallabonse': ['07/06'], 'Fernande': ['27/06'], 'Néomisie': ['25/09'], 'Walter': ['09/04'], 'Ferréol': ['16/06'], 'Néon': ['02/12', '28/04', '24/04', '23/08'], 'Wanceslas': ['28/09'], 'Fête du travail': ['01/05'], 'Wandon': ['17/04'], 'Fiacre': ['30/08'], 'Wandrille': ['22/07'], 'Fidèle de Sigmaringen': ['24/04'], 'Wenceslas': ['28/09'], 'Fidelmie': ['11/01'], 'Néon d’Antioche': ['28/09'], 'Wendel': ['22/10'], 'Néophyte': ['20/01', '22/08'], 'Wenefrid': ['03/11'], 'Werner': ['19/04'], 'Firmin': ['25/09'], 'Néopole': ['02/05'], 'Wiborade ou Guiborate': ['02/05'], 'Firmin 1er Damien': ['25/09'], 'Néotère': ['08/09'], 'Wigbert': ['12/04', '13/08'], 'Firmin d’Uzès': ['11/10'], 'Népotien': ['22/10'], 'Flamine': ['02/05'], 'Nérée': ['12/05'], 'Wilfrid': ['24/04', '12/10'], 'Flavie': ['07/05', '05/10'], 'Nestabe': ['08/09'], 'Nestor': ['26/02'], 'Wilfrid le jeune': ['29/04'], 'Flavien': ['22/12'], 'Nicaise': ['14/12', '11/10'], 'Wilfried': ['12/10'], 'Flavien de Constantinople': ['18/02'], 'Wilfriede': ['12/10'], 'Fleur': ['05/10'], 'Nicandre': ['17/06', '04/11'], 'Wilgeforte': ['20/07'], 'Floberde': ['02/04'], 'William': ['10/01'], 'Flora': ['24/11'], 'Nicandre de Mélitène': ['07/11'], 'Willibald': ['07/07'], 'Flore': ['29/07'], 'Nicandre d’Egypte': ['15/03'], 'Willibert': ['11/09'], 'Florence': ['01/05', '20/06', '01/12'], 'Nicéphore': ['25/02', '01/03', '04/05', '09/02'], 'Willibrord': ['23/02', '07/11'], 'Willigod': ['28/09'], 'Florent': ['23/02', '04/07'], 'Willy': ['10/01'], 'Nicéphore de Constantinople': ['13/03'], 'Wiltrude': ['06/01'], 'Florent de Strasbourg': ['07/11'], 'Nicet': ['05/12'], 'Winebaud': ['06/04'], 'Florent d’Orange': ['16/10'], 'Nicolas 1er le Grand': ['13/11'], 'Winnoc': ['06/11'], 'Florentin': ['24/10'], 'Nicolas de Myre': ['06/12'], 'Wiron': ['08/05'], 'Florian': ['04/05', '14/12'], 'Nicolas de Tolentino': ['10/09'], 'Withburge': ['17/03', '08/07'], 'Nicole': ['06/03', '06/12'], 'Floribert': ['01/11'], 'Wladimir': ['15/07'], 'Floride': ['10/01'], 'Nicoletta': ['06/03', '06/12'], 'Wolfgang': ['31/10'], 'Florine': ['01/05'], 'Wolfrad': ['24/07'], 'Foillan': ['31/10'], 'Nicomède': ['15/09'], 'Wolfred': ['18/01'], 'Fort': ['16/05'], 'Nicostrate': ['21/05'], 'Wulfhad': ['24/07'], 'Fortunat': ['23/04'], 'Nikita': ['31/01'], 'Wulfhilde': ['09/09'], 'Fortuné': ['01/06'], 'Nils': ['06/12'], 'Wulfran': ['20/03'], 'Foulque': ['26/10'], 'Nina': ['14/01'], 'Wulfron': ['20/03'], 'Fourier': ['09/12'], 'Ninon': ['15/12'], 'Wulftrude': ['09/09'], 'Foy': ['06/10'], 'Nithard': ['03/02'], 'Wulsin': ['08/01'], 'Frambaud': ['16/08'], 'Wynnebald': ['18/12'], 'France': ['09/03'], 'Noé': ['10/11'], 'Xanthéas': ['10/03'], 'Francelin': ['04/10'], 'Noël': ['25/12'], 'Xanthippe': ['23/09'], 'Franceline': ['09/03'], 'Noëlle': ['25/12'], 'Xavier': ['03/12'], 'Francette': ['09/03'], 'Noémi': ['21/08'], 'Xavière': ['22/12'], 'Francine': ['09/03'], 'Nolwenn': ['06/07'], 'Xénophon': ['26/01'], 'Francis': ['04/10'], 'Nominanda': ['31/12'], 'Yann': ['24/06'], 'Francisque': ['04/10'], 'Nonna': ['05/08'], 'Yannick': ['24/06'], 'Franck': ['04/10'], 'Nora': ['25/06'], 'Ygnace': ['03/02'], 'François d’Assise': ['04/10'], 'Norbert de Xanten': ['06/06'], 'Yoann': ['24/06'], 'François de Borgia': ['10/10'], 'Nostrien': ['14/02'], 'Yolande': ['11/06', '15/06', '24/06'], 'François de Caracciolo': ['04/06'], 'Notburge': ['14/09', '31/10'], 'François de Paule': ['02/04'], 'François de Sales': ['24/01'], 'Yon': ['22/09'], 'Françoise': ['12/12'], 'Notre Dame de l’Avent': ['08/12'], 'Youri': ['23/04'], 'Françoise Romaine': ['09/03'], 'Notre Dame de Lourdes': ['11/02'], 'Ysarn': ['24/09'], 'Françoise Xavière Cabrini': ['22/12'], 'Ysile': ['15/03'], 'François Xavier': ['03/12', '22/12'], 'Notre Dame du Mont Carmel': ['16/07'], 'Yvan': ['24/06'], 'Nouvel An': ['31/12'], 'Yves de Chartres': ['23/05'], 'Frankie': ['04/10'], 'Noyale': ['06/07'], 'Yves de Kermartin': ['19/05'], 'Freddy': ['18/07'], 'Numérien': ['05/07'], 'Yvette': ['13/01'], 'Frédéric': ['27/04', '18/07'], 'Nymphe': ['10/11'], 'Yvon': ['19/05'], 'Océan': ['04/09'], 'Yvonne': ['19/05'], 'Frédérique': ['18/07'], 'Octave': ['20/11'], 'Zacharie': ['05/11'], 'Frida': ['18/07', '08/12'], 'Octavie': ['20/11'], 'Zélie': ['17/10'], 'Octavien': ['22/03', '06/08'], 'Zénaïde': ['11/10'], 'Fridolin': ['06/03'], 'Zénon': ['22/12'], 'Frobert': ['02/01'], 'Octobre': ['02/06'], 'Zéphirin': ['20/12'], 'Frodobert': ['02/01'], 'Oda': ['20/04'], 'Zéphyrin': ['26/08'], 'Fronime': ['10/05'], 'Ode': ['23/10'], 'Zita': ['27/04', '05/07'], 'Front': ['25/10'], 'Odette': ['20/04', '20/04'], 'Fructueux': ['21/01', '16/04'], 'Zoé': ['02/05', '05/07'], 'Odilard': ['14/09'], 'Fructule': ['18/02'], 'Odile': ['13/12', '14/12'], 'Zoel': ['24/05'], 'Frumence': ['27/10'], 'Zotique': ['31/01'], 'Fulbert': ['10/04'], 'Zozime': ['18/12']}

class Accueil(Tk):
    def __init__(self):
        super().__init__()
        self.attributes("-topmost", True)
        self.title("Anniversaires")
        self.iconbitmap(ICONE)
        
        self.action = False
        
        self.affiche_anniv = Label(self, text="Patientez...")
        self.affiche_anniv.pack()
        self.affiche_meteo = Label(self, text="")
        self.affiche_meteo.pack()
        self.update()
        f = Frame(self)
        f.pack()
        Button(f, text="voir les données", command=self.modifier).pack(side="left")
        self.but_meteo = Button(f, text="...")
        self.but_meteo.pack(side="left")
        Button(f, text="nouveautés", command=self.nouveau).pack(side="left")
        Button(f, text="fermer", command=self.destroy).pack(side="left")
        
        self.actu_affichage()
        self.after(10, self.actu_meteo())
        
        # évènement
        """
        if strftime("%d/%m") in (f"{i}/05" for i in range(17, 20)):
            if askyesno("Année de naissance", "Souhaitez vous entrer les années de naissance de vos contacts suite à la dernière mise à jour ? (format jj/mm/aaaa)\nCe message apparaîtra jusqu'au 19/05."):
                self.modifier()
        """
        
        self.after(20*1000, self.close)
    
    def actu_affichage(self):
        self.actu_contenu()
        
        self.affiche_anniv["text"] = ""
        self.affiche_anniv["font"] = "Arial 10"
        
        aujourdhui = []
        for personne in self.personnes:
            if strftime("%d/%m") == personne[0].split("/")[0:2]: # Anniversaire
                aujourdhui.append(["l'anniversaire", personne[1]+f" (âge : {personne[6]})"])
            if strftime("%d/%m") == personne[2]: # Fête
                aujourdhui.append(["la fête", personne[1]])
        
        if aujourdhui:
            self.action = True
            self.affiche_anniv["text"] = "\n\n"
            self.attributes("-fullscreen", True)
            self.affiche_anniv["font"] = "Arial 80"
            for evenement in aujourdhui:
                self.affiche_anniv["text"] += "C'est {} de {}\n".format(*evenement)
            self.after(1000, self.animation)
        else:
            self.attributes("-fullscreen", False)
            mini = min(list(zip(*self.personnes))[3])
            apres = []
            for personne in self.personnes:
                if personne[3] == mini:
                    if personne[3] == 1:
                        t = "demain"
                    elif personne[3] >= 7:
                        t = "dans"
                        if personne[3]//7 == 1:
                            t += f" {personne[3]//7} semaine"
                        else:
                            t += f" {personne[3]//7} semaines"
                        if personne[3]%7 == 1:
                            t += " et un jour"
                        elif personne[3]%7 != 0:
                            t += f" et {personne[3]%7} jours"
                    else:
                        t = f"dans {personne[3]} jours"
                    if personne[6] != "inconnu":
                        apres.append(f"{personne[1]} fête ses {personne[6]+1} ans {t}")
                    else:
                        apres.append(f"{personne[1]} fête son anniversaire {t}")
            self.affiche_anniv["text"] = "\n".join(apres)
        self.after(1000, self.actu_affichage)
    
    def actu_contenu(self):
        contenu = reader(open(PATH, "r", encoding="utf-8"), delimiter=',')
        contenu = list(contenu)
        
        # Création de la liste avec les différentes personnes
        self.personnes = []
        for ligne in contenu:
            # Obtention du vrai nom
            try:
                pres = ligne[2]
            except IndexError:
                pres = ligne[1]
            
            # Obtention du nombre de jours avant la fête
            try:
                fete = saint[pres]
                for f in fete:
                    try:
                        dfete = mktime((int(strftime("%Y")), int(f.split("/")[1]), int(f.split("/")[0]), 0, 0, 0, 0, 0, -1))
                        nbf = 365-floor((time()-dfete)/60/60/24)
                        nbf %= 365 if int(strftime("%Y")) % 4 else 366
                    except ValueError:
                        nbf = 999
                    except IndexError:
                        nbf = 999
            except KeyError:
                fete = ["inconnu"]
                nbf = 999
            
            # Obtention du nombre de jours avant l'anniversaire
            try:
                danniv = mktime((int(strftime("%Y")), int(ligne[0].split("/")[1]), int(ligne[0].split("/")[0]), 0, 0, 0, 0, 0, -1))
                nb = 365-floor((time()-danniv)/60/60/24)
                nb %= 365 if int(strftime("%Y")) % 4 else 366
            except ValueError:
                nb = 999
            except IndexError:
                nb = 999
            
            try:
                age = ligne[0].split("/")[2]
                age = int(strftime("%Y")) - int(age)
                if danniv > time():
                    age -= 1
            except IndexError:
                age = "inconnu"
            except NameError:
                age = "inconnu"
            except ValueError:
                age = "erreur saisie"
            
            # Ajout à la liste
            # Format : [date anniv, nom, date fête, jours avant anniv, jours avant fête, vrai nom, age]
            self.personnes.append([ligne[0], ligne[1], fete, nb, nbf, pres, age])
        
        per = []
        for p in self.personnes:
            for i in range(len(per)):
                if p[3] < per[i][3]:
                    break
            try:
                if p[3] > per[-1][3]:
                    per.insert(i+1, p)
                else:
                    per.insert(i, p)
            except NameError:
                per.insert(0, p)
            except IndexError:
                per.insert(0, p)
        self.personnes = per
        
        print(f'[{strftime("%H:%M:%S")}] actualisé')
    
    def enregistrer(self):
        file = open(PATH, "w", encoding="utf-8")
        w = writer(file, delimiter=",")
        for p in self.personnes:
            w.writerow([p[0], p[1], p[5]])
        file.close()
        file = open(PATH, "r", encoding="utf-8")
        t = file.readlines()
        file.close()
        file = open(PATH, "w", encoding="utf-8")
        for l in t:
            if l != "\n" and l != "":
                file.write(l)
        file.close()
    
    def actu_meteo(self):
        try:
            sock = urllib.request.urlopen(f"https://prevision-meteo.ch/services/json/{ville}")
            htmlSource = sock.read()
            sock.close()
            self.meteo = json.loads(htmlSource)
            
            self.affiche_meteo["text"] = f"Température à {ville.capitalize()} : {self.meteo['current_condition']['tmp']}°C\nCondition : {self.meteo['current_condition']['condition']}"
            
            self.but_meteo["text"] = "météo"
            self.but_meteo["command"] = self.afficher_meteo
        except urllib.error.URLError:
            self.affiche_meteo["text"] = "Erreur de connection à internet."
            self.but_meteo["text"] = "reconnecter à internet"
            self.but_meteo["command"] = self.actu_meteo
    
    def modifier(self):
        self.action = True
        self.attributes("-topmost", False)
        try:
            self.mod.deiconify()
        except:
            self.mod = Modifier(self)
            self.mod.mainloop()

    def afficher_meteo(self):
        self.action = True
        self.attributes("-topmost", False)
        try:
            self.met.deiconify()
        except:
            self.met = Meteo(self)
            self.met.mainloop()

    def animation(self, nombre=20, etape=True):
        if nombre:
            self.affiche_anniv["fg"] = ("red" if etape else "black")
            self.after(500, lambda: self.animation(nombre-1, not etape))

    def close(self):
        if not self.action:
            self.close2()
    
    def close2(self):
        if self.attributes("-alpha") > 0.01:
            self.attributes("-alpha", self.attributes("-alpha")-0.01)
            self.after(2, self.close2)
        else:
            self.destroy()
    
    def nouveau(self):
        self.action = True
        showinfo("Nouveautés", """Nouveau (le 08/06) :
Autre :
- changement du séparateur du fichier de données""")


class Modifier(Toplevel):
    def __init__(self, master):
        super().__init__(master)
        self.master = master
        
        self.title("Voir")
        
        f = Frame(self)
        f.pack()
        Button(f, text="Rechercher une fête", command=self.cherche_fete).pack(side="left")
        Button(f, text="Modifier", command=self.modifier).pack(side="left")
        Button(f, text="Nouvelle ligne", command=self.l_new, bg="#d7f0cf").pack(side="left")
        Button(f, text="Supprimer ligne", command=self.l_del, bg="#f0cfcf").pack(side="left")
        self.tree_create()
        
    def tree_create(self):
        columns = ('date', 'prénom', 'age', 'saint', 'restant', 'restantf')
        self.tree = Treeview(self, columns=columns, show='headings')
        self.tree.heading('date', text='Date')
        self.tree.heading('prénom', text='Prénom')
        self.tree.heading('age', text='Âge de la personne')
        self.tree.heading('saint', text='Saint')
        self.tree.heading('restant', text='Anniversaire dans')
        self.tree.heading('restantf', text='Fête dans')
        
        self.scroll = Scrollbar(self, orient="vertical", command=self.tree.yview)
        self.scroll.pack(side="right", fill="y")
        self.tree["yscrollcommand"] = self.scroll.set
        
        self.master.actu_contenu()
        for personne in self.master.personnes:
            self.tree.insert('', "end", values=personne[0:2]+[personne[6]]+personne[2:5])
        
        self.tree.pack()
        self.tree.bind("<Double-1>", lambda e: self.modifier())
        self.tree.bind("<Button-3>", self.clic_droit)
    
    def cherche_fete(self):
        prenom = askstring("Prénom", "Entrez un prénom", initialvalue="Prénom")
        try:
            showinfo("Fête", f"La fête de {prenom} est le {' et '.join(saint[prenom])}")
        except KeyError:
            showerror("Fête", f"Prénom {prenom} inconnu de la base de donnée.")
    
    def clic_droit(self, e):
        self.tree.selection_set(self.tree.identify_row(e.y))
        nb = self.tree.index(self.tree.selection()[0])
        m = Menu(self, tearoff=0)
        m.add_command(label="Modifier", command=self.modifier)
        m.add_command(label="Supprimer", command=self.l_del)
        m.add_separator()
        m.add_command(label=f"Prénom : {self.master.personnes[nb][5]}", state="disabled")
        m.tk_popup(e.x_root, e.y_root)
    
    def modifier(self):
        nb = self.tree.index(self.tree.selection()[0])
        Modifieur(self, nb).mainloop()

    def l_del(self):
        nb = self.tree.index(self.tree.selection()[0])
        if askyesno("Confirmation", f"Supprimer {self.master.personnes[nb][1]} ?"):
            del self.master.personnes[nb]
            self.master.enregistrer()
            self.tree.destroy()
            self.scroll.destroy()
            self.tree_create()

    def l_new(self):
        self.master.personnes.append(["xx/xx", "Nouveau", "inconnu", "xxx", "xxx", "Nouveau"])
        self.master.enregistrer()
        self.tree.destroy()
        self.scroll.destroy()
        self.tree_create()

class Modifieur(Toplevel):
    def __init__(self, master, nb):
        super().__init__(master)
        self.master = master
        self.nb = nb
        
        t = [["Date de naissance", self.master.master.personnes[nb][0]], ["Nom usuel", self.master.master.personnes[nb][1]], ["Prénom", self.master.master.personnes[nb][5]]]
        self.e = []
        for i, c in zip(t, range(len(t))):
            Label(self, text=i[0]).grid(row=c, column=1)
            self.e.append(Entry(self))
            self.e[-1].insert(0, i[1])
            self.e[-1].grid(row=c, column=2)
        Button(self, text="valider", command=self.valider).grid(row=c+1, column=1)
        Button(self, text="caractères spéciaux", command=self.charmap).grid(row=c+1, column=2)

    def valider(self):
        self.master.master.personnes[self.nb][0] = self.e[0].get()
        self.master.master.personnes[self.nb][1] = self.e[1].get()
        self.master.master.personnes[self.nb][5] = self.e[2].get()
        self.master.master.enregistrer()
        self.master.tree.destroy()
        self.master.scroll.destroy()
        self.master.tree_create()
        self.destroy()
    
    def charmap(self):
        t = threading.Thread(target=os.system, args=["charmap"])
        t.start()


class Meteo(Toplevel):
    def __init__(self, master):
        super().__init__(master)
        self.master = master
        self.master.after(10, self.master.actu_meteo)
        
        self.title("Météo")
        
        self.suppr = Progressbar(self, length=100)
        self.suppr.pack()
        
        self.after(10, self.load)
    
    def load(self):
        self.t = Treeview(self, columns=list(f"{i}h" for i in range(24)))
        self.t.heading("#0", text="Type")
        for i in range(24):
            self.t.heading(f"{i}h", text=f"{i}:00")
            self.t.column(f"{i}h", width=60)
        
        self.last = []
        for j in range(5):
            jour = self.master.meteo[f"fcst_day_{j}"]
            
            self.last.append(Image.open(rq.get(jour["icon"], stream=True).raw))
            self.last[-1] = self.last[-1].resize((20, 20), Image.ANTIALIAS)
            self.last[-1] = ImageTk.PhotoImage(self.last[-1])
            n = {
                True: f"dans {j} jours",
                j==0: "aujourd'hui",
                j==1: "demain",
                j==2: "après-demain",
            }[True]
            self.t.insert("", "end", text=n, image=self.last[-1], iid=j)
            self.t.insert(j, "end", text="température", values=list(f"{jour['hourly_data'][d]['TMP2m']}°C" for d in jour["hourly_data"]))
            self.t.insert(j, "end", text="précipitations", values=list(f"{jour['hourly_data'][d]['APCPsfc']}mm" for d in jour["hourly_data"]))
            self.t.insert(j, "end", text="vitesse du vent", values=list(f"{jour['hourly_data'][d]['WNDSPD10m']} km/h" for d in jour["hourly_data"]))
            self.suppr.step(20)
            self.suppr.update()
        self.suppr.destroy()
        self.t.pack()
        Label(self, text="Source météo : https://prevision-meteo.ch/").pack()
        
        self.adapte(0)
        self.focus_force()
    
    def adapte(self, nb):
        if nb:
            self.t.config(height=self.winfo_height()//21-1)
        else:
            self.t.config(height=self.winfo_height()//21)
        if nb > 20:
            self.keep()
            self.after(20, lambda: self.adapte(0))
            return
        self.after(20, lambda: self.adapte(nb+1))

    def keep(self):
        g0 = self.winfo_geometry()
        g0 = g0.split("+")
        g = list(map(int, g0[0].split("x")+g0[1:3]))
        g[0] = 1643
        self.geometry("{}x{}+{}+{}".format(*g))

Accueil().mainloop()
