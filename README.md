# database
A library made by me to make databases!

# Commands
Commands for now

database.declare(file)
So basically this command finds the database you wanna use, it must be in the same folder your .py file is if you're just entering the name
if it's not you need to give the exact directory
database.declare("File.txt")
database.declare("C:/Users/rubicminer/Appdata/Local/File.txt")
Obviously my file is not there, just an example!
Also if you don't have a file, it will make one with the name you give it, itself!

database.read()
it will read the content of the database

database.write(text)
Will write a new thing into your database

database.overwrite(text)
Like database.write(text), just that this time it will overwrite your file

database.clear()
Will clear every data on your database

database.remove()
Will remove the database from your computer

# How to import
to import this file you can put it in the same directory as your .py file is
but this is not certain to work always and you may want to use it in all of your projects
in that case go to:
C:/Users/$username$/AppData/Local/Programs/(Python)/Python$version-subversion$/Lib/
And put it in there!
Also the (Python) is for the fact that you may not have this folder!
After doing all those things
you do:

from database import *
