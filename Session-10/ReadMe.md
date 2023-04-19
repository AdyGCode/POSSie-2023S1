# Session 10 - 2023-04-19

## Session Time
| Detail | 24 Hr |  12 Hr |
|--------|------:|-------:|
| Start  |  1830 | 6.30PM |
| End    |  2030 | 8.30PM |


## Today's Content

- Introduction to OOP
- Assessment Schedule (request)
- Intro to Mermaid
- PC Support

## Mermaid!

To start a mermaid diagram using:
```text
    ```mermaid
    
    ```
```

Read the Markdown file to see how to draw the flowchart below.

```mermaid
flowchart TD
    A ([Start]) --> B[Help Message]
    B --> D[[Get Target Word]]
    D --> E[[Prompt for Guess]]
    E --> F{Is it Valid?}
    F -- Yes --> G[[Score Guess]]
    F -- No --> H[Invalid Guess Message]
    H --> E
    G --> I{Is Winner?}
    I -- Yes --> J[Show Winning Message]
    I -- No --> K[Tries += 1]
    K --> L{Tries > MAX?}
    L -- Yes -->E
    L -- No --> M[Display Sorry You Lose...]
    J --> C([End])
    M --> C
    
```

## OOP (Using Python)

OOP!

Object-Oriented Programming

- Class - a blueprint
  - properties - what the blueprint contains
  - methods - function - operates on the properties in the class
- instantiation -- aka to create
- Object -- 

- House Plans
  - rooms, walls, bathrooms, etc
  - light switch (on)
- BUILDING
- House

```
my_house = new House()
my_house.build()
my_house.light_switch(my_house.bedroom, on)
```

 


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
