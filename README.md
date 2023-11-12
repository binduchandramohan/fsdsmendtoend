# this is my end to end project

https://drive.google.com/drive/u/0/folders/1GGXkkFgRVOEcvd8qQyypVSxLRgBq8CoK

1. Init the GIT
    Open a New Terninal 
    (base) bindu.chandramohan@bindu-chandramohan-C07PGKWJ26 fsdm_projects command - init git

    to push the code to git we do
    git add filename

    git add . --> all files inside the workspace / folder will go into git

    git commit -m "this is my first commit"
2. create abc.txt 
3. go to github and create a file
    .gitignore - choose template as python
    see line 122 -- we have env names , if we create environment name with such , it will be ignored..

4. create LICENSE file in github
    choose MIT License and save n commit
    needed to deploy , create as open source project etc..

5. run git pull in terminal - it pulls all changes from github into VS
6. init_setup.sh - shell script
    if we do not want to execute each and every command manually from terminal , we create these as shell script - automation..
    This is only for linux , not for windows , but works on mac
    copy paste the text shared..

    to try to execute , keep only 1st 2 lines and exeute from terminal with command -- bash init_setup.sh 

7. we can also execute with all text in  init_setup.sh  
    with command -- bash init_setup.sh  , but this fails as we dnt have requirements.txt

8. sometimes environment is not activated in windows system , so we need   
    to activate it manually in the terminal
    command - source activate ./env


STEPS for PROJECT - Individual Components of a Pipeline

Below are components and are part of Piepline
so Pipeline is a collection of Components

1. Data Ingestion
2. EDA
3. PreProcessing / Feature Engineering
4. Model Building
5. Evaluate the Model

2 Types of Pipeline inside DS Project
    1. Training Pipeline - Train the Model
    2. Testing / Prediction Pipeline - Test the model , Predict the Model

Lets create a project structure based on above..

We will have below files as well..
1. logger file for logging the information
2. exception file 
3. util file
4. setup.py file
5. requirements.txt


Project Structure

Root Directory - We will create 1 folder - .github folder
we use github bcos we would do ci/cd 
- .github folder
    - workflow folder
        - yaml folder -- for writing our script / configurations
            refer https://github.com/scikit-learn/scikit-learn for example

    one more file
    .gitkeep file 
  - Lets say we have development in our local system and created a folder xyz
  If we have pushed this folder  from local to github , this folder wont be visible in github , as we cannot push empty folder within github
  But we can make it visible by creating a .gitkeep file inside that folder
  and then push the changes to github
  Initially we wouldnt know about ci/cd , so we may have to push empty folders probably into github

Notebook folder
    - Research.ipynb - can do EDA etc

src folder
    - Project Name - eg. DiamondPricePrediction
        - components under this
        - component folder
            -  dataingestion.py file
            - preprocessing.py file
            - modeltraining.py file
        - pipeline folder
            - training.py
            - prediction.py
        - exception.py file
        - logger.py file
        - utils.py file

requirements.txt file
setup.py file
REFER template.py to show the above file structures..

template.py
    we have - from pathlib import Path
    this is to generate system compatible path
    for instance we might have forward slash in local , but system would need backward slash while referring to path.. so system generated path..
    This template.py will create all the folders and files needed..
    execute that to understand the same..

we have init.py file on every folder..
    In python we have Folder , Module etc..
    The .py file is called Module..
    Folder + Module = Package

    pandas , numpy , sklearn , tensorflow are all packages..
    we have folder and code is written inside that as .py file as class / functions etc..

    we write 
        tensorflow -- Folder
            -tensorflow.py -- Module
                -mytensor class -- Class 
                - mytens function - function
        Above all together is called PACKAGE
        PACKAGE is FOLDER --> MODULE --> CLASS / FUNCTION    
    from tensorflow.tensorflow import mytensor
    from sklearn.linearmodel import LinearRegression

    In our case we have  , package is .. we have created our own package..
    src
        DiamondPrediction
            components
                class
                function

    
    for pandas , we do pip install pandas
    how python will get to know our package ?
        we need to create __init__.py file .. so this is rule from python side to show our folder as a local or custom package..


ways to install custom package / local package

ensure the path in the terminal is pointing to the current dir where we have the file / package and then do bash init_setup.sh and select this env , Visual Studio asks about the new env created , select that 
else we end up with issues !! , for instance importing the local package keeps failing !!!
else do --> source activate ./env  , after the env is created using --> bash init_setup.sh

1 . pip install .
2. -e . in requirements.txt
3. python setup.py install in setup.py file

1st method..
Delete the env already created
run the init_setup.sh  file..using the command bash init_setup.sh
pip list --> lists all packages available
but not the local package , ours which is DiamondPrediction
for that to be installed run the following command
python setup.py install
then do pip list , it lists DimondPricePrediction as package installed as well..

now we also see on the left 2 more folders
build
DiamondPricePrediction.egg-info and few files inside that
now if we want to give our package - DiamondPricePrediction -  to another person , we will deploy that file to pypy directory and get it with pip install

2nd method - delete build folder , dist folder , DiamondPricePrediction.egg-info folder also..
to uninstall DiamondPricePrediction package ,command -->  pip uninstall DiamondPricePrediction , this will remove the installed package..
check with pip list..

requirements.txt --> add -e . , and again run pip install -r requirements.txt , this will also install the package..
this internally calls setup.py file only..



good practice - we also need to ensure we install other packages while consuming the DiamondPrediction ,so ensure to include all locally installed packages also in setup.py , so anyone who installs our package DiamondPreditction also installs other required packages too


29th Oct 2023

Modular Coding

data_ingestion.py
data_transformation.py
model_trainer.py

1. Create a Class inside each of the .py file

logger.py file - log all changes
    log folder and this will have log files inside , the file can be named with date and time 
exception.py file - we are creating our own custom exception class
utils.py file - helper module , where we write the helper code


exception.py file - to handle all exceptions and return filename ,error number and actual error

data_ingestion.py file
    import required packages , also local package's logger and exception

    dataclasses:config & artifacts
        DataIngestion -- gives raw data as output
        DataTransformation -- gives transformed data as output / data ready for the model - preprocessed object
        ModelTrainer -- gives model as output
        In terms of ML , all the above outputs are called Artifacts , so Artifcacts folder collects all outputs from Components..

    we are collecting all the above outputs as csv in artifacts folder within data_ingestion.py file

training_pipeline.py file
    write code to create object for DataIngestion class inside training_pipeline.py file
    and call the method initiate_data_ingestion , to create the artifact folder and 3 .csv files inside...
    

    '''
    from src.DimondPricePrediction.components.data_ingestion import DataIngestion

    import os
    import sys
    from src.DimondPricePrediction.logger import logging 
    from src.DimondPricePrediction.exception import customexception

    import pandas as pd


    obj=DataIngestion()

    obj.initiate_data_ingestion()
    '''

