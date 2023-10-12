# trier les fichiers d'un repertoire par type
import os
import shutil
from os import path
from pathlib import Path
import argparse


def parseFile(directory):
    """
        this function allows you to group file pdf and word file into a directory dedicated for

        PRE: an string which is a path in the computer file system
        POST: 03 directories created where differents types of files are stored


    """
    extensionsDoc = ('.doc', '.docx', '.pptx', '.txt', '.pdf')
    extensionMedia = ('.png', '.jpeg', '.avi', '.mkv', '.mp4')
    extensionSource = ('.zip', '.exe', '.7z', '.msi')

    docFiles = os.path.join(directory, 'document')
    mediaFiles = os.path.join(directory, 'média')
    sourceFiles = os.path.join(directory, 'source')

    # creation des dossiers
    try:
        os.mkdir(docFiles)
        os.mkdir(mediaFiles)
        os.mkdir(sourceFiles)
    except OSError:
        print('Un repertoire de ce nom existe deja')

    files = os.listdir(directory)
    # on parcours la liste de fichiers
    for file in files:

        # tri en fonction des extensions

        if file.endswith(extensionsDoc):
            # if not path.exists(docFiles):
            src = os.path.join(directory, file)
            dest = os.path.join(docFiles, file)
            shutil.move(src, dest)

        if file.endswith(extensionMedia):
            src = os.path.join(directory, file)
            dest = os.path.join(mediaFiles, file)
            shutil.move(src, dest)

        if file.endswith(extensionSource):
            src = os.path.join(directory, file)
            dest = os.path.join(sourceFiles, file)
            shutil.move(src, dest)


if __name__ == '__main__':
    directory = Path.cwd()
    parseFile(directory)
