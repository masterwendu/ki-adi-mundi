# Homeassistant installation on a Raspberry pi 3
1. Install Hassbian https://home-assistant.io/docs/hassbian/installation/
  * Make sure that you extract `.zip` and flash the `.img` image to the sdCard
  * update software `sudo apt-get update && sudo apt-get upgrade`
  * update homeassistant
  ```
  sudo systemctl stop home-assistant@homeassistant.service
  sudo su -s /bin/bash homeassistant
  source /srv/homeassistant/bin/activate
  pip3 install --upgrade homeassistant
  exit
  sudo systemctl start home-assistant@homeassistant.service
  ```
  * setup wifi and static ip failed. I set a setatic ip for the wifi but it just works when I pug in ethernet. I don't know why :-( (I used first the networking method and afterwards the dhcpcp method)
* shutdown homeassistant `sudo systemctl stop home-assistant@homeassistant.service`
* Install Open Z-Wave and OZWCP `sudo hassbian-config install openzwave`
  * plan 1 hour to install
* Install Samba `sudo hassbian-config install samba`
* install fish shell `sudo apt-get install fish`
* set fish as standard shell `chsh -s /usr/bin/fish `


* [Hassbian common tasks](https://github.com/masterwendu/ki-adi-mundi/blob/master/hassbian/commonTasks.md)
* [HOME](https://github.com/masterwendu/ki-adi-mundi)
