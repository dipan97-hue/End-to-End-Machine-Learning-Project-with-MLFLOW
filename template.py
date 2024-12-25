import os
from pathlib import Path
import logging

# Error Messages
logging.basicConfig(level = logging.INFO, format ='[%(asctime)s] %(levelname)s: %(message)s')

projectname = 'ML_Project'

list_of_files =[
    ".github/workflows/.gitkeep",
    f"src/{projectname}/__init__.py",
    f"src/{projectname}/components/__init__.py",
    f"src/{projectname}/utils/__init__.py",
    f"src/{projectname}/utils/common.py",
    f"src/{projectname}/config/__init__.py",
    f"src/{projectname}/config/configuration.py",
    f"src/{projectname}/pipeline/__init__.py",
    f"src/{projectname}/entity/__init__.py",
    f"src/{projectname}/entity/config_entity.py",
    f"src/{projectname}/constants/__init__.py",
    "config/config.yaml",
    "params.yaml",
    "schema.yaml",
    "main.py",
    "app.py",
    "Dockerfile",
    "setup.py",
    "requirements.txt",
    "research/trials.ipynb",
    "templates/index.html"

]

for filepath in list_of_files:
    filepath = Path(filepath)
    filedir, filename = os.path.split(filepath)

    if not os.path.exists(filedir) and filedir!= '':
        os.makedirs(filedir)
        logging.info(f"Directory created: {filedir}")
    
    if not os.path.exists(filepath):
        with open(filepath, 'w') as file:
            pass
        logging.info(f"File created: {filepath}")
    else:
        logging.info(f"File already exists: {filename}")