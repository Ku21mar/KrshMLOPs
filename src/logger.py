import logging
import os, sys
from datetime import datetime






LOG_FILE = f"{datetime.now().strftime('%m-%d-%Y %H-%M-%S')}.log"

logs_path  =os.path.join(os.getcwd(), 'logs',LOG_FILE)  # "logs" folder will created 
os.makedirs(logs_path ,exist_ok=True)


LOG_FILE_PATH  =os.path.join(logs_path ,LOG_FILE)


logging.basicConfig(
    filename=LOG_FILE_PATH,
    format="[ %(asctime)s ] %(lineno)d %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO,
)



if __name__ =="__main__":
    logging.info("LOgging has strated")

# LOG_DIR = "logs" # Folder / Directory

# LOG_DIR = os.path.join(os.getcwd(), LOG_DIR)

# os.makedirs(LOG_DIR, exist_ok = True)

# #log/2023-10-13:19:35.log

# CURRENT_TIME_STAMP = f"{datetime.now().strftime('%Y-%m-%d %H-%M-%S')}"

# file_name = f"log_{CURRENT_TIME_STAMP}.log" # File

# log_file_path = os.path.join(LOG_DIR, file_name)

# logging.basicConfig(filename = log_file_path,
#                     filemode='w',
#                     format = '%(asctime)s %(levelname)s %(name)s %(message)s',
#                     level = logging.INFO)