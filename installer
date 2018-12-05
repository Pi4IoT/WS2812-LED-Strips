#------------------------------------------------
# Script for prepare and install WS281X Library--
# Pi4IoT - 05.12.2018----------------------------
#------------------------------------------------

printf "\n${yellow}Check and installing build-essential:${normal}\n"
sudo apt-get install build-essential 

printf "\n${yellow}Check and installing python-dev:${normal}\n"
sudo apt-get install python-dev 

printf "\n${yellow}Check and installing unzip:${normal}\n"
sudo apt-get install unzip 

printf "\n${yellow}Check and installing wget:${normal}\n"
sudo apt-get install wget 

printf "\n${yellow}Check and installing scons:${normal}\n"
sudo apt-get install scons 

printf "\n${yellow}Check and installing swig:${normal}\n"
sudo apt-get install swig

printf "\n${yellow}Donwload rpi_ws281x:${normal}\n"
wget https://github.com/jgarff/rpi_ws281x/archive/master.zip 

printf "\n${yellow}Unzip rpi_ws281x:${normal}\n"
unzip master.zip 

printf "\n${yellow}Change folder to rpi_ws281x:${normal}\n"
cd rpi_ws281x-master 

printf "\n${yellow}Run scons:${normal}\n"
sudo scons 

printf "\n${yellow}Change folder to python:${normal}\n"
cd python
 
printf "\n${yellow}Run setup:${normal}\n"
sudo python setup.py install
