# CSC131-Project

# This is where we will commit our files to!
# Yay!


# How to run myFlaskProject:

# Clone or pull Repo. Make sure your python version is 3.9 (not 3.12 or 3.10 or 3.11).
# Create venv in myFlaskProject:
# $ py -3 -m venv venv
# Then activate venv
# $ . venv/Scripts/activate
# Then install requirements:
# $ pip install -r requirements.txt
# Then run main.py:
# $ py main.py
# If for some reason it says flask_mysqldb is not installed (even though it already should be), do:
# $ pip install flask_mysqldb
# Now that it runs, Ctrl+C to stop main.py from running
# Downlaod XAMMP. I picked the version 8.0.28 / PHP 8.0.28 for Windows
# Install XAMMP. Just keep pressing 'next'. All the default options are good
# Now open XAMMP and start Apache and MySQL. You might need to give permissions to both or one of them. 
# If MySQL can't run because Port 3306 is being used by something else, go to Task Manager, then Services, then search for MySQL80 and stop it
# There's a good chance that you downloaded MySQL separately already which is using that port
# Now it should run
# Now put https:/localhost in your google browser WHILE XAMMP IS RUNNING! Then go tp PhpMyAdmin
# Create a new database called maindb (spelling must be EXACT)
# Then create a table called test with 2 columns
# Name the first column id and the second one phrase
# id will be a INT and phrase will be a TEXT
# Now go press on maindb and you should see the table called test. Click insert which is beside it. 
# Now put in an id (probably start with the number 1) and a phrase. Then press the GO button below it
# Run main.py again:
# $ py main.py
# Then put this in your browser: http://127.0.0.1:5973/phrases
# Now you should see the database being displayed!


