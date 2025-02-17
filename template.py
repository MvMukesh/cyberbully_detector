import os
import logging
from pathlib import Path


logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(message)s: ')

package_name = "abusive_language"
list_of_files = [
    ".github/workflows/.gitkeep",
    f"{package_name}/__init__.py",
    f"{package_name}/components/__init__.py",
    f"{package_name}/configuration/__init__.py",
    f"{package_name}/constants/__init__.py",
    f"{package_name}/entity/__init__.py",
    f"{package_name}/exception/__init__.py",
    f"{package_name}/logger/__init__.py",
    f"{package_name}/ml/__init__.py",
    f"{package_name}/pipeline/__init__.py",
    f"data",
    f"research_env",
    f"app.py",
    f"for_testing.py",
    f"requirements.py",
    f"setup.py",
    ]

for filepath in list_of_files:
    filepath = Path(filepath)
    filedir, filename = os.path.split(filepath)
    if filedir != "":
        os.makedirs(filedir, exist_ok=True)
        logging.info(f"Creating directory: {filedir} for file: {filename}")

    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath, "w") as f:
            pass # create an empty file
            logging.info(f"Creating empty file: {filepath}")
    else:
        logging.info(f"{filename} already exists")