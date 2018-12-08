#------------------------------------------------
# Script for prepare and install WS281X Library--
# Pi4IoT - 08.12.2018----------------------------
#------------------------------------------------

echo -e "\n\e[1;31mCheck and installing build-essential:\e[0m"
sudo apt-get install build-essential 

echo -e "\n\e[1;31mCheck and installing python-dev:\e[0m"
sudo apt-get install python-dev 

echo -e "\n\e[1;31mCheck and installing unzip:\e[0m"
sudo apt-get install unzip 

echo -e "\n\e[1;31mCheck and installing wget:\e[0m"
sudo apt-get install wget 

echo -e "\n\e[1;31mCheck and installing scons:\e[0m"
sudo apt-get install scons 

echo -e "\n\e[1;31mCheck and installing swig:\e[0m"
sudo apt-get install swig

echo -e "\n\e[1;31mDonwload rpi_ws281x:\e[0m"
wget https://github.com/jgarff/rpi_ws281x/archive/master.zip 

echo -e "\n\e[1;31mUnzip rpi_ws281x:\e[0m"
unzip master.zip 

echo -e "\n\e[1;31mChange folder to rpi_ws281x:\e[0m"
cd rpi_ws281x-master 

echo -e "\n\e[1;31mRun scons:\e[0m"
sudo scons 

echo -e "\n\e[1;31mChange folder to python:\e[0m"
cd python

echo -e "\n\e[1;31mRun setup:\e[0m"
sudo python setup.py install
