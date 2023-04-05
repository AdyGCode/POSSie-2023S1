# Session 09 - 2023-04-05

## Session Time
| Detail | 24 Hr |  12 Hr |
|--------|------:|-------:|
| Start  |  1830 | 6.30PM |
| End    |  2030 | 8.30PM |


## Today's Content

- example code on how to create a executable version of a python program (Pyinstaller-Demo)
- 

## Pyinstaller Demo

- presuming application is int eh `application.py` file
- data read from file is in `dummy.txt`
- cli.py is the command line interface / srun code for application
- requiremetns.txt is from a `pip freeze > requirements.txt` execution
- readme file for data about the app
- license is the softweare license
- help.md is the help file (markdown)

Install the pyinstaller package
```bash
pip install pyinstaller
```

Create a cli.py file

create a setup.py file

run the pyinstaller making a single executable file, cleaning the caches and adding data files.

```bash
pyinstaller --onefile --clean --add-data "data.txt;." cli.py
```


### TO DO list
- revise git
- 


## Useful Items

### Repository of Code and Notes
- See GitHub! [POSSie 2023 S1](https://github.com/AdyGCode/POSSie-2023S1)
- POSSie --> Programming Online Student Support Sessions

### Ady's Diigo Account
- https://diigo.com/user/Ady_Gould

### Git Cheat Sheets and Tutes
- https://gitcheatsheet.org/
- https://www.git-tower.com/learn/cheat-sheets/git/

### MS-DOS Command Prompt Tutes etc
- http://people.uncw.edu/pattersone/121/labs/l1_msdos_primer.pdf
- https://www.lifewire.com/dos-commands-4070427
- https://www.makeuseof.com/tag/a-beginners-guide-to-the-windows-command-line/
- https://www.computerhope.com/issues/chusedos.htm
- 

### PyInstaller
- https://python.plainenglish.io/packaging-data-files-to-pyinstaller-binaries-6ed63aa20538
- https://realpython.com/pyinstaller-python/
- https://stackoverflow.com/questions/41870727/pyinstaller-adding-data-files
- 
