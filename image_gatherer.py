import os
import shutil


def gather_images(source, destination):
    '''source = "Croissance HUVEC transfectées 29Oct20"
    destination = "Croissance_29_Oct20_gathered"'''

    try:
            os.mkdir(destination)
            print("Directory " , destination ,  " Created ") 
    except FileExistsError:
            print("Directory " , destination ,  " already exists")



    contenu = os.listdir(source + '/')
    jours = []

    for element in contenu : 
        if os.path.isdir(source + '/' + element) : jours.append(element)#les jours ne sont que les dossiers 

    #print(jours)


    for jour in jours :
        source_jour = source + '/' + jour 

        contenuJour = os.listdir(source_jour)#c'est la liste de tout ce qu'il y a dans un dossier jour__
        champs = []
        for contenu in contenuJour: 
                if os.path.isdir(source_jour + '/' + contenu) : champs.append(contenu)
                
                
        for champ in champs :
            source_champ = source_jour + '/' + champ

            contenuChamp = os.listdir(source_champ)
            temps = []

            for contenu in contenuChamp: 
                if os.path.isdir(source_champ + '/' + contenu) : temps.append(contenu)

            #if jour == jours[1] and champ == champs[0] : print(temps)

            for temp in temps : 
                    source_temp = source_champ + '/' + temp
                    #if jour == jours[1] and champ == champs[1] : print(os.listdir(source_temp)[0])
                    try : 
                            image = os.listdir(source_temp)[0]
                            source_image = source_temp + '/' + image
                            #if jour == jours[1] and champ == champs[1] and temp == temps[2] : print(source_image)
                            print(source_image)

                            dest = destination+'/' + jour + '_' + champ + '_' + temp + os.path.splitext(image)[1]
                            shutil.copyfile(source_image,dest)

                    except : print(f"NO IMAGE AT {source_image}")


def runAnalysis(folder):
    !python detect.py --weights best_pokemon_19_01_14h29.pt --img 640 --conf 0.25 --source new_test 