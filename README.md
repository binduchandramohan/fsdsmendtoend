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





