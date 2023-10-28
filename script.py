# trier les fichiers d'un repertoire par type
import os
import shutil
from pathlib import Path
from tabulate import tabulate

def parseFile(directory):
    """
        this function allows you to group file pdf, word file and another kind of extension file into a directory dedicated for

        PRE: a string which is a path in the computer file system
        POST: 03 directories created where differents types of files are stored


    """
    extensionsDoc = ('.doc', '.docx', '.pptx', '.txt', '.pdf')
    extensionMedia = ('.png', '.jpeg','jpg', '.avi', '.mkv', '.mp4')
    extensionSource = ('.zip', '.exe', '.7z', '.msi')

    docDirectory = os.path.join(directory, 'document')
    mediaDirectory = os.path.join(directory, 'média')
    sourceDirectory = os.path.join(directory, 'source')

    # creation des dossiers
    try:
        os.mkdir(docDirectory)
        os.mkdir(mediaDirectory)
        os.mkdir(sourceDirectory)
    except OSError:
        print('Un repertoire de ce nom existe deja')

    files = os.listdir(directory)
    # on parcours la liste de fichiers
    for file in files:

        # tri en fonction des extensions

        if file.endswith(extensionsDoc):
            src = os.path.join(directory, file)
            dest = os.path.join(docDirectory, file)
            shutil.move(src, dest)

        if file.endswith(extensionMedia):
            src = os.path.join(directory, file)
            dest = os.path.join(mediaDirectory, file)
            shutil.move(src, dest)

        if file.endswith(extensionSource):
            src = os.path.join(directory, file)
            dest = os.path.join(sourceDirectory, file)
            shutil.move(src, dest)

 # Parcourir le dossier "documents" et compter les différentes extensions

    documentFiles = os.listdir(docDirectory)
    nbrExtension = {}
    for file in documentFiles:
        fileExtension = os.path.splitext(file)[1].lower()
        nbrExtension[fileExtension] = nbrExtension.get(fileExtension, 0) + 1
    #creation du tableau
    tableauDoc = [(extension, nombre) for extension, nombre in nbrExtension.items()]

    # Afficher le nombre de fichiers pour chaque extension différente
    print("Nombre de fichiers avec différentes extensions dans le dossier 'document':")
    headers = ["Extension", "Nombre de fichiers"]

     #affichage du tableau
    print(tabulate(tableauDoc, headers=headers, tablefmt="grid"))

  # Parcourir le dossier "média" et compter les différentes extensions
    mediaFiles = os.listdir(mediaDirectory)
    nbrExtension = {}
    for file in mediaFiles:

        fileExtension = os.path.splitext(file)[1].lower()
        nbrExtension[fileExtension] = nbrExtension.get(fileExtension, 0) + 1
    #creation du tableau
    tableauMedia = [(extension, nombre) for extension, nombre in nbrExtension.items()]


    # Afficher le nombre de fichiers pour chaque extension différente
    print("Nombre de fichiers avec différentes extensions dans le dossier 'média':")
    headers = ["Extension", "Nombre de fichiers"]

    #affichage du tableau
    print(tabulate(tableauMedia, headers=headers, tablefmt="grid"))

# Parcourir le dossier "source" et compter les différentes extensions
    sourceFiles = os.listdir(sourceDirectory)
    nbrExtension = {}
    for file in sourceFiles:
        fileExtension = os.path.splitext(file)[1].lower()
        nbrExtension[fileExtension] = nbrExtension.get(fileExtension, 0) + 1
    #creation du tableau
    tableauSource = [(extension, nombre) for extension, nombre in nbrExtension.items()]

    # Afficher le nombre de fichiers pour chaque extension différente
    print("Nombre de fichiers avec différentes extensions dans le dossier 'source':")
    headers = ["Extension", "Nombre de fichiers"]
    #affichage du tableau
    print(tabulate(tableauSource, headers=headers, tablefmt="grid"))

if __name__ == '__main__':
    directory = Path.cwd()
    parseFile(directory)
