#Installing backend Env.Variablessudo apt install python3.8-venv#Setting up the environmentsudo python3 -m venv env#Activating the envirionmentsudo 
source env/bin/activate
#Install Django packages
echo Installing Django
sudo apt-get update
sudo apt install python3-djangosudo 
cd backend
sudo pip3 install -r requirements.txt 
sudo apt-get update
sudo apt-get -y 
install postgresql
sudo service postgresql start
sudo useradd -d home/mob_app_user mob_app_user

