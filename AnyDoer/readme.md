# AnyDoer
### Start your day by checking your Any.Do list
##### By Ruben Seoane

### Overview
I wanted to have an overview of my todo list as I open my computer, and just creating a shortcut was boring ;)
The purpose of this script is to automatically open and log in into your Any.Do account, right when loging in into your pc. 

### Current Stage
The script was converted to a Bat file, and it's running at startup, but closing unexpectedly. It opens Chrome, maximizes the window and logs in correctly to Any.do dashboard

### To do:
- [ ] Fix issue of windows closing
- [ ] Fix the following issue: When the window is opened, if the user makes any interaction with Chrome testing window, the script, stops, perhaps build _try_ function.
- [ ] Change to Firefox browser to avoid opening all Chrome windows.

### Requirements
This script uses Selenium library,
for installation:
```
pip3 install selenium
```
