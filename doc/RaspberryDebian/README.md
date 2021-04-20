# Raspberry_Debian10
This tutorial show how to create a Debian 10 sdcard for the Raspberry board and install it on the target.

## Install linux image

Before you start, don't forget to check the
[SD card requirements](https://www.raspberrypi.org/documentation/installation/sd-cards.md)

Link to the original **Raspberry Installer Software** :

> - Windows : https://downloads.raspberrypi.org/imager/imager_1.6.exe
> - Mac OS : https://downloads.raspberrypi.org/imager/imager_1.6.dmg


![Raspberry Installer Software](doc/Specs_and_Design/images/pi_installer.PNG)

>1. Choose your OS

![Image version](doc/Specs_and_Design/images//version_rasp.png)

>2. Choose your sdcard

![Image version](doc/Specs_and_Design/images/sdcard.png)

>3. Write on the sdcard

![Image version](doc/Specs_and_Design/images/write.png)

Your boot SD card is now ready !

## Setup wifi

> Create a file with the name : **wpa_supplicant.conf** with the following content

```
country=fr
update_config=1
ctrl_interface=/var/run/wpa_supplicant

network={
 scan_ssid=1
 ssid="Name of your box here like : Livebox-C5B6"
 psk="password of your box like : is24F4WrCQmFsQbr2p"
}
```
> Change the **ssid** and **psk** with yours

> Create a file with the name : **ssh** without content and extension

> Once this done, you will have to copy and paste both files into the sdcard you made

![Image version](doc/Specs_and_Design/images/images/boot.png)

> Now place the sdcard on the raspberry and power up the board

![Image version](doc/Specs_and_Design/images/sdcard_place.png)

## SSH connection

Default users and password:

1. debian:temppwd
1. root:root
