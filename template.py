from pathlib import Path
import os
import logging

# logging string
logging.basicConfig(level=logging.INFO, format='%(asctime)s : %(levelname)s : %(message)s:')

Project = "BlueStock Tasks"

# List of folders to create
folders = [
    f"data/raw",
    f"data/processed",
    f"notebooks",
    f"sql",
    f"dashboard",
    f"reports",
    
]


# Create folders
for folder in folders:
    folder = Path(folder)
    folder.mkdir(parents=True, exist_ok=True)
    logging.info(f"Ensured folder exists: {folder}")

print("Project folder structure created successfully!")