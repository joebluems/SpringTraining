# SpringTraining

To build this data, the batting stats from the 2014 MLB and Spring seasons were downloaded as csv files. Using a Python program, 
I combined the players by name from the two sets of data (where I pulled the data, there was no linking key). A few things had 
to be done to the names to get them to match. It's all handled in the python program. 

mlb - took the raw regular season data, removed characters from names and wrote out Name, Team, AB, BA

spring - spring training data, with characters (like # and *) removed, wrote out Name, Team, AB, BA

read.py - reads "mlb" and "spring" and creates one line per matching player who meets AB requirements.

I ran the command "./read.py > mlb2014.csv" which created the file that was read into Tableau. 

trends.R - R script which performs linear regression on all data, then by group (team). 
