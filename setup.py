from setuptools import find_packages, setup
from typing import List

HYPEN_E_DOT = '-e .'
def get_requirements(file_path:str)->List[str]:
    # this function reads the requirements file and returns a list of requirements
    with open(file_path) as f:
        req =  f.readlines()
        req = [req.replace("\n", "") for req in req]
        if HYPEN_E_DOT in req:
            req.remove(HYPEN_E_DOT)
    return req

setup (
    name='generic-mlops',
    version='0.1.0',
    author='Satyam Gupta',
    author_email='satyamgupta3803@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')
)