# TravelBudgetCalculator
A travel budget calculator using python Django framework with HTML/CSS/Bootstrap/JavaScript/JQuery/Ajax.


<img src="https://github.com/AtaUllahB/TravelBudgetCalculator/blob/master/Screenshots/Loading.png?raw=true">
<img src="https://github.com/AtaUllahB/TravelBudgetCalculator/blob/master/Screenshots/Main_page.png?raw=true">
<img src="https://github.com/AtaUllahB/TravelBudgetCalculator/blob/master/Screenshots/one.png?raw=true">
<img src="https://github.com/AtaUllahB/TravelBudgetCalculator/blob/master/Screenshots/two.png?raw=true">



How to run:
step 1 : 
Create and activate virtual Environment 
here is the link follow it 

https://programwithus.com/learn-to-code/Pip-and-virtualenv-on-Mac/

step 2: 
Install all the packages from requirements.txt file. use below cmd to install all the packages from requirements first save it to any folder go to that folder in terminal and run below command in terminal.

pip install -r requirements.txt

step 3: 
Download xampp-osx-7.3.8-2-installer.dmg from the given link and then install it.

https://sourceforge.net/projects/xampp/files/XAMPP%20Mac%20OS%20X/7.3.8/

step 4 : 
open Xampp and start Mysql Database and Apache server

step 5 : 
Goto browser and write
localhost then go to myphpadmin

step 6 : 
create new database give name demo same in lowercase

step 7 : 
go to the terminal and then go to the project folder and run cmd. 

python manage.py makemigrations 

if no error occur then run 

python manage.py migrate 

again to check if error occur 

python manage.py makemigrations

step 8 : 
after all the things working correctly run 

python manage.py runserver 

then copy the url link from the terminal and paste into the browser 

if you see any formating issue

python manage.py collectstatic
 
then go to the project folder mysite settings.py 

then see DEBUG = False make it True then again run 

python manage.py runserver 

refresh the link 

if the formating is ok go back to the settings.py file and undo the or make DEBUG = False again and then again run 

python manage.py runserver

if you dont get it right from any steps let me know
