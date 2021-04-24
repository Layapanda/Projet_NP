
#!/bin/bash

echo "Start installation"

echo "git clone Henner Zeller matrice LED API"
git clone https://github.com/hzeller/rpi-rgb-led-matrix.git

echo "move files to the needed place"
mv matrice_led.py /home/pi/Projet_NP/rpi-rgb-led-matrix/bindings/python/samples
mv clean_matrice.py /home/pi/Projet_NP/rpi-rgb-led-matrix/bindings/python/samples

echo "Creation venv - v"
sudo pip3 install virtualenv
python3 -m venv Projet_NP-env
source Projet_NP-env/bin/activate

echo "Install tensorflow"
pip3 install tensorflow

echo "Install opencv-python"
pip3 install opencv-python

echo "set matrice LED timezone Europe/Paris"
sudo rm /etc/localtime
sudo ln -s /usr/share/zoneinfo/Europe/Paris /etc/localtime

echo "enable exe"
sudo chmod 777 run.sh

echo "enable nodered at startup"
sudo systemctl enable nodered.service
