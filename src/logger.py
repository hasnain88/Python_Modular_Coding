import logging
import os, sys
from datetime import datetime


LOG_FILE=f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log" # for File Name
LOG_Folder = f"{datetime.now().strftime('%m_%d_%Y_%H_%M')}" # Folder Name
log_path=os.path.join(os.getcwd(),"logs",LOG_Folder) # Define path and Folder and File
os.makedirs(log_path,exist_ok=True) # Create a folder and file

LOG_FILE_PATH = os.path.join(log_path,LOG_FILE)

logging.basicConfig(
    filename=LOG_FILE_PATH,
    format="[ %(asctime)s ] %(lineno)d %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO,
)



