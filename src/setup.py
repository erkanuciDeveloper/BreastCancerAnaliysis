from setuptools import find_packages, setup
from typing import List

#this for external lirabry 
HYPHEN_E_DOT = '-e .'


def get_requirements(file_path: str) -> List[str]:
    '''
    Reads dependencies from a requirements file and returns a list of requirements.
    '''
    requirements = []

    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        # Remove leading and trailing whitespaces and newline characters
        requirements = [req.strip() for req in requirements]
        # Remove the line with '-e .' if present
        requirements = [req for req in requirements if req != HYPHEN_E_DOT]

    return requirements


setup(
    name='BreastCancerAnaliysis',
    version='0.0.1',
    author='Erkan',
    author_email='erkan48592@hotmail.com',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')
)
