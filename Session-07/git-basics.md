# Versions

Basics of Git

## Starting a new project
1. Create the folder for the project (or start the project using the IDE)
2. Change into the project's folder
3. Create a `ReadMe.md` file, add some basic text
4. Create a new file called `.gitignore`, this may be left empty 
5. Intialise Version Control
    - `git init .`
6. Check status of VC
   - `git status`
7. Change "master" to "main" for the primary branch:
    - `git branch -m main`
8. Check the status using `git status`
    - Red indicates the file is not yet staged
9. Add a file called FILENAME into VC
    - `git add FILENAME`
    - eg: `git add ReadMe.md .gitignore` adds both files at once
10. Check status 
   - Green indicated in 'staging area' not committed to VC
11. Commit File to VC
   - `git commit -m "COMMIT MESSAGE"` 


### Altered a file?
1. `git status`
2. `git add FILENAME`
3. `git status`
4. `git commit -m "COMMIT MESSAGE"`


## Useful Tips
- Make "main" the default branch name:
  - `git config --global init.defaultBranch main` 

- Short log view
  - `git log --oneline --graph --decorate`

