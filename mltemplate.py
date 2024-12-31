import os
from pathlib import Path
import logging
import sys
import argparse
from time import sleep

delay = 0.5


def get_args():
    parser = argparse.ArgumentParser(description="Process key-value arguments")
    parser.add_argument("--author", type=str, required=True, help="Author Name")
    parser.add_argument("--email", type=str, required=False, help="Author Email ")
    parser.add_argument("--project", type=str, required=True, help="Project Name")
    parser.add_argument("--env", type=float, required=True, help="Python version")
    return parser.parse_args()




list_of_files = [
    ".github/workflows/.gitkeep",
    "config/gonfig.yaml",
    "params.yaml",
    "app.py",
    "main.py",
    "Dockerfile",
    "requirements.txt",
    "setup.py",
    "notebook/trails.ipynb",
    "notebook/eda.ipynb",
    "src/__init__.py",
    "src/components/__init__.py",
    "src/utils.py",
    "src/constants/__init__.py",
    "src/pipeline/__init__.py",
    "src/config/__init__.py",
    "src/config/configuration.py",
    "src/entity/__init__.py",
    "src/providers/__init__.py",
    "src/logging.py",
    "src/exception.py", 
]
def run(project_name ,env, author, author_email=''):
    os.system('cls')
    sys.stdout.write(" This Script is built by github.com/theanmol-raj : \n")
    for filepath in list_of_files:
        filepath = Path(filepath)
        filedir, filename = os.path.split(filepath)

        if filedir != "":
            os.makedirs(filedir, exist_ok=True)

        
        if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
            with open(filepath,'w') as f:
                pass
                sys.stdout.write(f"{filename} created : done\n")
                


        
        else:
            sys.stdout.write(f"{filename} is already exists\n")

    sys.stdout.write("Attempting to Write Setup.py ...\n")

    x= r'"\n"'
    lines = f'from setuptools import find_packages , setup\nfrom typing import List\nHYPHEN_E_DOT = "-e ."\ndef get_requirements(filename : str) -> List[str] :\n\treq = []\n\twith open(filename) as f:\n\t\treq = f.readlines()\n\t\treq = [ _.replace({x},"") for _ in req]\n\t\tif HYPHEN_E_DOT in req:\n\t\t\treq.remove(HYPHEN_E_DOT)\n\treturn req\n\nsetup(\n\tname="{project_name}",\n\tversion="0.0.1",\n\tauthor="{author}",\n\tauthor_email="{author_email}",\n\tpackages=find_packages(),\n\tinstall_requires = get_requirements("requirements.txt")\n)'
    with open('setup.py','w') as f:
        f.write(lines)
        f.close()
    x = r'LOG_FILE = f"{datetime.now().strftime("%m_%d_%Y_%H_%M_%S")}.log"'
    logspath = r"logs_path = os.path.join(os.getcwd(),'logs',LOG_FILE)"
    loger = r"logging.basicConfig( filename=LOG_FILE_PATH,format='[ %(asctime)s ] %(name)s - %(levelname)s - %(message)s',level=logging.INFO,)"
    lines = f'import logging\nimport os\nfrom datetime import datetime\n\n{x}\n{logspath}\nos.makedirs(logs_path,exist_ok=True)\nLOG_FILE_PATH = os.path.join(logs_path,LOG_FILE)\n{loger}'
    with open('src/logging.py','w') as f:
        f.write(lines)
        f.close()
    

    er = r"err_msg = f'Error occured in python script : [{file_name}] line number :[{exc_tb.tb_lineno}] error :[{str(err)}]'"
    lines = f'import sys\ndef error_message_detail(err,err_detail:sys) -> str:\n\t_,_,exc_tb =err_detail.exc_info()\n\tfile_name = exc_tb.tb_frame.f_code.co_filename\n\t{er}\n\treturn err_msg\nclass {project_name.capitalize()}Exception(Exception):\n\tdef __init__(self,error_msg,err_details:sys) -> None:\n\t\tsuper().__init__(error_msg)\n\t\tself.error_message = error_message_detail(error_msg,err_details)\n\tdef __str__(self) -> str:\n\t\treturn self.error_message'
    with open('src/exception.py','w') as f:
        f.write(lines)
        f.close()
    
    
    
    
    sys.stdout.write("Attempting to create an environment ...\n")
    python = env

    

    try:
        os.system(f'conda create -p venv python=={python} -y')
        sys.stdout.write(f"Created an environment venv with python version : {python}\n")
    except Exception as e:
        sys.stdout.write(f"Unable to create environment , try creating it manually: {python}\n")

    


if __name__ == "__main__":
    args = get_args()
    
    run(project_name=args.project ,env=args.env , author=args.author , author_email=args.email)
    sys.stdout.write("This Script is built by github.com/theanmol-raj : \n")
    
