# Ancestry Share 23
### A tool to automatically request sharing Ancestry Reports with all your 23andme list of genetic relatives
###### By Ruben Seoane


### Overview:
In 2013 I got a 23andme genetic testing kit, and over time, I haven't managed to keep up with the growing list of genetic cousins (over 1200 now).
23andme offers a function called "Share Ancestry Reports", which allows both you and the other person to see each other's ancestry makeup, 
the percentages, and locations of common genetic information within chromosomes, etc. It is very usefull for triangulating your common ancestors
through your genealogical tree.

In short, not checking my profile for months at a time, it was quite a challenge to go an click on every member of this list, 
find whether they are willing to share reports, and send them the invitation. So I decided to automate
this process by using Beautiful Soup and other python libraries. 

### Current stage:
The Python script only requires you to input your username (email) and password, it then opens a Chrome window, logs in with the given credentials, iterates through a CSV file with the URLs of your genetic cousins, checks whether they are willing to share reports and
sends the request. This CSV file has been obtained from previously downloading your genetic relatives file that 23andmeDNA provides,
and exporting the URL list to a second CSV (the script's input). It prints a count of the number of relatives it has checked on the screen.

### To be developed:
- [ ] Improve function on CSV so it works directly on the original file.
- [ ] Create an UI that allows for entering login credentials, submit genetic relatives CSV to script memory (all working within the local
terminal)
- [ ] Show count and job done notification on UI
- [ ] Automatically download relatives CSV to predefined location with a generic file name?
- [ ] Convert script into executable file with all libraries needed, no need for Python and dependencies installation.
- [ ] Execute with minimized window?
- [ ] Create Firefox variant.
- [ ] Transform workflow to asynchronous using Scrapy
