from setuptools import find_packages,setup
from typing import List
HYPEN_E_DOT='-e .'
def get_requirements(file_path:str)->List[str]:
    '''
    Cette fonction renvoie la liste des exigences en lisant un fichier requirements.txt.
    Elle supprime l'entrée "-e ." s'il existe dans la liste.
    '''
    requirements=[]
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        requirements=[req.replace("\n","") for req in requirements]
        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)
        
    return requirements
setup(
name='mlproject',
version='0.0.1',
author='Aldric',
author_email='aldric07.bahna@gmail.com',
packages=find_packages(),
install_requires=get_requirements("requirements.txt")
)
