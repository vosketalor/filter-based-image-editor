from PIL import Image

def image_base(im1): # Création de l'image de base (positionnée à gauche) (By Baptiste)
    L,H = im1.size
    im2 = Image.new("RGB",(L*2+round(1/100*L),H)) # On créé une image de taille égale à deux fois celle de base + 1/100 de l'image de base pour l'espacement
    for ligne in range(L*2):
        for colonne in range(H):
            im2.putpixel((ligne,colonne),(255,255,255)) # On remplit l'image de blanc pour la barre de séparation
    for ligne in range(L):
        for colonne in range(H):
            p = im1.getpixel((ligne,colonne))
            im2.putpixel((ligne,colonne),(p[0],p[1],p[2])) # On place la première image sur la gauche, les pixels de la version modifiée seront placés à droite, espacés par 1/100 de la taile de l'image initiale
    return(im2)

def negatif(im2, im1): # Filtre négatif (By Baptiste)
    L,H = im1.size
    for ligne in range(L):
        for colonne in range(H):
            p = im1.getpixel((ligne,colonne))
            im2.putpixel((ligne+L+round(1/100*L),colonne),(255-p[0],255-p[1],255-p[2]))
    return(im2)

def miroir_horizontal(im2, im1): # Rotation horizontale (By Baptiste)
    L,H = im1.size
    for ligne in range(L):
        for colonne in range(H):
            p = im1.getpixel((ligne,colonne))
            colonne = H-colonne-1
            im2.putpixel((ligne+L+round(1/100*L),colonne),(p[0],p[1],p[2]))
    return(im2)

def miroir_vertical(im2, im1): # Rotation verticale (By Baptiste)
    L,H = im1.size
    for ligne in range(L):
        for colonne in range(H):
            p = im1.getpixel((ligne,colonne))
            ligne = L-ligne-1
            im2.putpixel((ligne+L+round(1/100*L),colonne),(p[0],p[1],p[2]))
    return(im2)

def noir_et_blanc_seuil(im2, im1): # Filtre noir et blanc (seuil) (By Baptiste)
    L,H = im1.size
    seuil=int(input("Définissez le seuil (70 conseillé): ")) # L'utilisateur définit le seul à partir duquel le pixel devient noir (255 = noir total)
    for ligne in range(L):
        for colonne in range(H):
            p = im1.getpixel((ligne,colonne))
            gris=(p[0]*0.2126+p[1]*0.7152+p[2]*0.0722) # Formule pour respecter la Recommandation UIT-R BT.709-6 (en rapport avec la luminance)
            if (round(gris) >= seuil): # Si la muminosité du pixel est suppérieure ou égale au seuil
                r=255
                v=255
                b=255
            else:
                r=0
                v=0
                b=0
            im2.putpixel((ligne+L+round(1/100*L),colonne),(r,v,b))
    return(im2)

def noir_et_blanc_niveaux(im2, im1): # Filtre noir et blanc (niveaux de gris) (By Baptiste)
    L,H = im1.size
    for ligne in range(L):
        for colonne in range(H):
            p = im1.getpixel((ligne,colonne))
            gris=int(p[0]*0.2126+p[1]*0.7152+p[2]*0.0722) # Formule pour respecter la Recommandation UIT-R BT.709-6 (en rapport avec la luminance)
            im2.putpixel((ligne+L+round(1/100*L),colonne),(gris,gris,gris))
    return(im2)

def infrarouge(im2, im1): # Filtre infrarouge (By Baptiste)
    L,H = im1.size
    intensite=int(input("Définissez l'intensité du filtre (75 conseillé) : "))
    for ligne in range(L):
        for colonne in range(H):
            p=im1.getpixel((ligne,colonne))
            gris=int(p[0]*0.2126+p[1]*0.7152+p[2]*0.0722)
            
            if (255 >= round(gris) >= 128) : # Selon la valeur du gris, on applique une couleur en rapport à sa luminosité
                r=225-intensite
                v=225+intensite
                b=225-intensite
                
            elif (127 >= round(gris) >= 100):
                r=192-intensite
                v=192+intensite
                b=192-intensite
                
            elif (99 >= round(gris) >= 64):
                r=128-intensite
                v=128+intensite
                b=128-intensite
                
            elif (63 >= round(gris) >= 46):
                r=96-intensite
                v=96+intensite
                b=96-intensite
                
            elif (45 >= round(gris) >= 32):
                r=64-intensite
                v=64+intensite
                b=64-intensite
                
            elif (31 >= round(gris) >= 8):
                r=32-intensite
                v=32+intensite
                b=32-intensite
                
            else:
                r=0-intensite
                v=0+intensite
                b=0-intensite
                
            im2.putpixel((ligne+L+round(1/100*L),colonne),(r,v,b)) # On place le pixel sur la partie de droite
    return(im2)

def bruit(im2, im1): # Filtre bruit (aléatoire) (By Baptiste)
    from random import randint
    L,H = im1.size
    seuil=int(input("Définissez le seuil du bruit (90 conseillé) : ")) # L'utilisateur définit les bornes du bruit
    for ligne in range(L):
        for colonne in range(H):
            p = im1.getpixel((ligne,colonne))
            r = p[0]+randint(-seuil,seuil) # On modifie la valeur de r en fonction du nombre aléatoire généré
            v = p[1]+randint(-seuil,seuil) # On modifie la valeur de v en fonction du nombre aléatoire généré
            b = p[2]+randint(-seuil,seuil) # On modifie la valeur de b en fonction du nombre aléatoire généré
            im2.putpixel((ligne+L+round(1/100*L),colonne),(r,v,b))
    return(im2)

def sepia(im2, im1): # Filtre sépia (consiste en une image en niveaux de gris où l'on applique un filtre légèrement orangé) (By Baptiste)
    L,H = im1.size
    for ligne in range(L):
        for colonne in range(H):
            p = im1.getpixel((ligne,colonne))
            gris=int(p[0]*0.2126+p[1]*0.7152+p[2]*0.0722) # Formule pour respecter la Recommandation UIT-R BT.709-6 (en rapport avec la luminance)
            r=gris+70
            v=gris+20
            b=gris
            im2.putpixel((ligne+L+round(1/100*L),colonne),(r,v,b)) # On place le pixel sur la partie de droite
    return(im2)
