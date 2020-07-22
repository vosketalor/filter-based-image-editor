from PIL import Image
from data.defs import *
import os as command

print("=================================== FILTREUR ==============================\n\n")
path = input("Quelle est l'adresse de l'image ? ")
im1 = Image.open(path) #"enregistrer" l'image

size = int(command.path.getsize(path)/10**3) #prendre sa taille
print("\n\t\t\t Taille de l'image : ", size, "Ko\n") #prendre la taille de l'image

print("1) Filtre n&b (seuil) \n2) Filtre noir & blanc (niveaux de gris)\n3) Filtre négatif")	#| Sélecteur du filtre
print("4) Rotation verticale \n5) Rotation horizontale \n6) Filtre infrarouge")	                #| By Baptiste
print("7) Filtre bruit \n8) Filtre sepia")					                #|
mode = input("\nQuel filtre voulez-vous importer (écrire le nombre) ? ")		        #|

if mode == '1': # 1 = Noir & Blanc (seuils)
    print("Application du filtre noir et blanc (seuils)...")
    im2=noir_et_blanc_seuil(image_base(im1), im1)
    print("Terminé")

elif mode == '2': # 2 = Noir & Blanc (niveaux de gris)
    print("Application du filtre noir et blanc (niveaux de gris)...")
    im2=noir_et_blanc_niveaux(image_base(im1), im1) # Appeler la fonction (double fonction : tracer image de gauche, pui de droite)
    print("Terminé")
    
elif mode == '3': #filtre == négatif
    print("Application du filtre négatif...")
    im2=negatif(image_base(im1), im1) # Appeler la fonction
    print("Terminé")
    
elif mode == '4': #filtre == rotation verticale
    print("Application de la rotation verticale...")
    im2=miroir_vertical(image_base(im1), im1) # Appeler la fonction
    print("Terminé")
    
elif mode == '5': #filtre == rotation horizontale
    print("Application de la rotation horizontale...")
    im2=miroir_horizontal(image_base(im1), im1) # Appeler la fonction
    print("Terminé")

elif mode == '6': #filtre == filtre "infrarouge"
    print("Application du filtre infrarouge...")
    im2=infrarouge(image_base(im1), im1) # Appeler la fonction
    print("Terminé")

elif mode == '7': #filtre == filtre bruit
    print("Application du filtre bruit...")
    im2=bruit(image_base(im1), im1) # Appeler la fonction
    print("Terminé")

elif mode == '8': #filtre == filtre sepia
    print("Application du filtre sepia...")
    im2=sepia(image_base(im1), im1) # Appeler la fonction
    print("Terminé")

sauvegarder = input("Voulez vous sauvegarder l'image ? (o/n) ") # Sauvegarde ?
if sauvegarder == 'o':
    nom = input("Nom du fichier ? ")
    im2.save(nom+".png", format="png")

im2.show() #montrer l'image
