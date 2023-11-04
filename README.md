# this is my end to end project

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

9.




