# Session 14 - 2023-05-17

## Session Time
| Detail | 24 Hr |  12 Hr |
|--------|------:|-------:|
| Start  |  1830 | 6.30PM |
| End    |  2030 | 8.30PM |

## Music
No music tonight

All music by Scott is Creative Commons 4, Share and Attribution required.

## Today's Content

- all sorts!

## Client Support ICTSAS432

- Helpdesk
  - email online support (preferred) online@screencraft.net.au
  - Paul - conducts (this semester) the practical totally via email
    - paul.williams@nmtafe.wa.edu.au
  - John - conducting the practical via helpdesk system
    - john.robertson@nmtafe.wa.edu.au

- Send email with subject:
  - "Starting the Helpdesk practical"
- Body of email
  - Hi XXXXX, 
  - Could you please start the help desk practical for me.
  - Name:
  - Student Number:


## OOP - Object-Oriented Programming

- Abstraction
- Polymorphism
- Inheritance
- Encapsulation

Abstraction
- obfuscating the inner workings of part of a program
- black box 
- put things in
- get things out
- vehicle is an abstraction of a mode of transport
- 

Inheritance
- Allows you to take traits from another "abstracted item"
- Child inherit traits etc from their parents
- eye colour 
- car inherits the traits of a vehicle (genralised)

Polymorphism
- "unit" can act as one of many different "units"
- Transport - could be car, truck, motorbike, bicycle etc
- 

Encapsulation
- wrapper for data and methods

Class vs Object
- Class blueprint for a "version" of it, aka an instance
- an instance of a class is an Object
- House Plans -- Class
- Built house -- Object

Class - an abstraction of something
- store all the data and methods for "the something"

```python
class Vehicle:
  # all these properties are hidden from the user
  # this is not good python code!
  
  def __init__(self, wheels=None, colour=None):
    self.wheels = wheels
    self.colour = colour
  
  def start(self):
    pass
  
  def set_wheels(self, number=4):
    self.wheels = number
  
      
class Car(Vehicle):
  # inherits wheels, colour, start
  def __init__(self, wheels=None, colour=None):
    super.__init__(wheels,colour)
    
  
bmw = Car()
bmw.set_wheels(4)


```


## Improvements to units

- Found an error?
- something not working (eg link)

Improvements to units - please send to online@screencraft.net.au with subject "(UNIT/CLUSTER Name or number) Improvement" 


## Software for Learning from Microsoft

To access Microsoft Software for your studies, such as Windows 11, 
and so on, you will need to sign up with the Microsoft Software for 
Students portal at https://portal.azure.com/#home 

To gain access you first must sign up/in using your TAFE email.


## Got Questions?
Part of the ScreenCraft Help Desk is a Knowledge Base (also known as Frequently Asked Questions).
We are slowly adding to this, and have recently added a few more pages to help resolve problems you may be having.

The Knowledge Base is found at: 
- [ScreenCraft Knowledge Base](https://help.screencraft.net.au/hc/1990208628)<br>(https://help.screencraft.net.au/hc/1990208628)

Here are some examples of the articles (or FAQs) that are available so far:

- [MS Teams: Channel Notifications - Turning Off](https://help.screencraft.net.au/hc/1990208628/44/ms-teams-channel-notifications-turning-off)<br><small>(https://help.screencraft.net.au/hc/1990208628/44/ms-teams-channel-notifications-turning-off)</small>
- [Finding Collaborate Recordings](https://help.screencraft.net.au/hc/1990208628/11/finding-collaborate-recordings?category_id=12)<br><small>(https://help.screencraft.net.au/hc/1990208628/11/finding-collaborate-recordings?category_id=12)</small>
- [Names of Symbols](https://help.screencraft.net.au/hc/1990208628/30/names-of-symbols?category_id=5)<br><small>(https://help.screencraft.net.au/hc/1990208628/30/names-of-symbols?category_id=5)</small>

If you have a question you think is suitable for the FAQS then send an email to online@screencraft.net.au - even better, how about submitting  an FAQ for us to check and possibly add to the collection (we will credit you).

Ady
<https://teams.microsoft.com/l/message/19:-difYeG9DqvMGzQ0ZL-388_MX_LLRUfMGkRqjlaSJOI1@thread.tacv2/1682491112263?tenantId=218881e8-07ad-4142-87d7-f6b90d17009b&amp;groupId=1ab34fd8-38b3-4f7f-b218-2501ea2cf0c4&amp;parentMessageId=1682491112263&amp;teamName=NMT Student PIN ICT40120&amp;channelName=General&amp;createdTime=1682491112263&amp;allowXTenantAccess=false>


 


## Useful Items

### Repository of Code and Notes
- See GitHub! [POSSie 2023 S1](https://github.com/AdyGCode/POSSie-2023S1)
- POSSie --> Programming Online Student Support Sessions

FOSS - Fully Online Student Support


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
