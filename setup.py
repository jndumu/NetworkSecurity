""""
The setup.py file is an essential part of packaging and distributing Python projects. 
It is used by the setuptools (distutils in older Python versions) to define the 
configuration of your project, such as its metadata dependencies, and more 
"""

from setuptools import find_packages, setup
from typing import List

def get_requirements() -> List[str]:
    """"
    This function will returnlist of requirements

    """
    requirement_list:List[str]=[]
    try:
        with open("requirements.txt", "r") as file:
            #Read lines from the file
            lines=file.readlines()
            #Remove empty lines
            for line in lines:
                requirement=line.strip()
                #ignore empty lines and "-e ."
                if requirement and requirement!= "-e .":
                    requirement_list.append(requirement)
    except FileNotFoundError:
        print("No requirements.txt file found")

    return requirement_list

#print(get_requirements())  

setup(
    name="NetworkSecurity",
    version="1.0.0",
    description="Sample Python Package",
    author="Josephine Ndumu",
    author_email="latinue@gmail.com",
    #url="https://github.com/yourusername/sample_package",
    packages=find_packages(),
    install_requires=get_requirements()
)
