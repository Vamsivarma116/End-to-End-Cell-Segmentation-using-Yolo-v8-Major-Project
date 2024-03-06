import os
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(message)s:')

project_name = "cellSegmentation"

list_of_files = [
    ".github/workflows/.gitkeep",
    "data/.gitkeep",
    f"{project_name}/__init__.py",
    f"{project_name}/components/__init__.py",
    f"{project_name}/components/data_ingestion.py",
    f"{project_name}/components/data_validation.py",
    f"{project_name}/components/model_trainer.py",
    f"{project_name}/constant/__init__.py",
    f"{project_name}/constant/training_pipeline/__init__.py",
    f"{project_name}/constant/application.py",
    f"{project_name}/entity/config_entity.py",   # if we Execute this python file then all files will be created
    f"{project_name}/entity/artifacts_entity.py",
    f"{project_name}/exception/__init__.py",
    f"{project_name}/logger/__init__.py",
    f"{project_name}/pipeline/__init__.py",
    f"{project_name}/pipeline/training_pipeline.py",
    f"{project_name}/utils/__init__.py",
    f"{project_name}/utils/main_utils.py",
    "research/trials.ipynb",
    "templates/index.html",
    "app.py",
    "Dockerfile",
    "requirements.txt",
    "setup.py",
    "test.py",
]

for filepath in list_of_files:
    filepath = Path(filepath)   #To identify weather it is windows path or linux path

    filedir, filename = os.path.split(filepath) # Here we can seperate the file folder and file{(f"{project_name}/components/)----(data_validation.py)} 

    if filedir!="":  # Checking waether filedir is Empty or not
        os.makedirs(filedir,exist_ok=True) #If it is not empty it will make a folder using "os.makedirs"
        logging.info(f"Creating directory: {filedir} for the file {filename}") # logging Info {1}

    
    if(not os.path.exists(filename)) or (os.path.getsize(filename) == 0): # If this file size is Zero Then it is empty Then this snippet will replace the file
        with open(filepath, "w") as f:           #|-------------------------------^
            pass
            logging.info(f"Creating empty file: {filename}")

    
    else:
        logging.info(f"{filename} is already created")