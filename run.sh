#!/bin/bash

sudo rm /tmp/nombre.json

sudo touch /tmp/nombre.json
sudo chmod 777 /tmp/nombre.json

sudo python /home/pi/Projet_NP/rpi-rgb-led-matrix/bindings/python/samples/matrice_led.py -t 12 --led-rows=16 --led-slowdown-gpio=4 --led-no-hardware-pulse=false &	

sleep 1 

source /home/pi/Projet_NP/Projet_NP-env/bin/activate
python3 /home/pi/Projet_NP/TFLite_detection_webcam.py --modeldir=/home/pi/Projet_NP/Sample_TFLite_model


