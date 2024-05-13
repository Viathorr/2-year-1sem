# Project theme: Chat

Programming language: Python

External libraries: tkinter for GUI (+ ttkbootstrap extension (https://ttkbootstrap.readthedocs.io/en/latest/)), 
rsa (for encryption (https://stuvel.eu/python-rsa-doc/))

Code style: PEP8

Database: MySQL

GUI elements (approximately):
- 5 windows
- 30 control elements
- 1 listbox
- 34 event handlers

## Lab2(part)

### Design Patterns used:
- ***Mediator*** (Mediator class handles all the communication between GUI components to avoid circular dependencies among classes)
- ***Command*** (Different commands responsible for certain database operations)