# Number Person Administrator

This document relates to all the tasks that need to be performed by the system administrator in order to build and deploy the NP application.

## Hardware pre-requisites
To install the NP application you'll need:

1. Raspberry Pi 4 **board** 4go or more
2. Raspberry Pi **power brick**
3. Micro SD card **8 GB or more**

## Operating System build & install and connecting the board to Internet
Refer to my other github repository to **build the system image and install it to the micro SD card**:

> [**Raspberry Debian 10**](https://github.com/Layapanda/Projet_NP/tree/main/doc/RaspberryDebian)

Once you have followed this procedure, you should be able to successfully boot the Raspberry board with a fully working and booting base Debian 10 system image.

## Deploy the program files and configuring the system

Follow this procedure to copy all the necessary files to the **Raspberry PI 4** board.

[**Project files package creation procedure**](../../README.md) -> **Mandatory programs** and **Gathering all the programs section**.


Follow the **install_services.sh** procedure to do the following steps:
1. build **venv — Creation of virtual environment**
2. get **c2v and tensorflow** working
3. authorize access for the whole project
4. enable **NodeRED** on boot with systemd.
5. enable **NodeRED** GPIOs access.


## System wiring

Please refer to the [**Wiring Diagram**](../Specs_and_Design/Wiring_NP.pdf) to hook up the LED Matrice and the relay to the Raspberry PI 4 board.