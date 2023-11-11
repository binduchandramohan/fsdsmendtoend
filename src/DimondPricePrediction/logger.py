import logging
import os
from datetime import datetime

# name of the log file with date time
LOG_FILE = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"
#'11_11_2023_13_19_33.log'

# log file path folder  
# '/Users/bindu.chandramohan/Documents/DataScience/FSDS_May2023/fsdm_project_diamond_prediction_notebook/fsdm_projects/notebooks/logs' 
log_path = os.path.join(os.getcwd(),"logs")

# creates logs as a folder
os.makedirs(log_path,exist_ok=True)

# complete log file path with filename
LOG_FILE_PATH = os.path.join(log_path,LOG_FILE)

logging.basicConfig(level=logging.INFO,
                    filename=LOG_FILE_PATH,
                    format="[%(asctime)s]%(lineno)d %(name)s - %(levelname)s - %(message)s"
                    )