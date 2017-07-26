# hassbian common tasks
## handle homeassitant service
### start homeassistant (homeassistant should start at startup of your pc)
`sudo systemctl start home-assistant@homeassistant.service`
### stop homeassistant
`sudo systemctl stop home-assistant@homeassistant.service`
### restart homeassistant
`sudo systemctl restart home-assistant@homeassistant.service`

## update homeassistant
1. stop home assistant - `sudo systemctl stop home-assistant@homeassistant.service`
2. switch to homeassistant user - `sudo su -s /bin/bash homeassistant`
3. switch into pyton virtal env - `source /srv/homeassistant/bin/activate`
4. update homeassistant - `pip3 install --upgrade homeassistant`
5. switch back to pi user - `exit`
6. restart homeassistant - `sudo systemctl start home-assistant@homeassistant.service`


## check if your config is valid
1. switch to homeassistant user `sudo su -s /bin/bash homeassistant`
2. switch to pyton virtal env - `source /srv/homeassistant/bin/activate`
3. run check script - `hass --script check_config`
4. return to pi user `exit`


## Read the homeassistant logfile
1. switch to homeassistant user `sudo su -s /bin/bash homeassistant`
2. go to homeassistant config folder -  `cd /home/homeassistant/.homeassistant`
3. open the logs - `nano home-assistant.log`
4. go back to pi user - `exit`


## edit the homeassistant config, if you don't use samba
1. switch to homeassistant user ` sudo su -s /bin/bash homeassistant`
2. go to homeassistant config folder -  `cd /home/homeassistant/.homeassistant`
3. open the config and edit - `nano configuration.yaml`
4. go back to pi user - `exit`

## use the OZWCP Web config
1. stop home assistant - `sudo systemctl stop home-assistant@homeassistant.service`
2. change to the OZWCP directory - `cd /srv/homeassistant/src/open-zwave-control-panel/`
3. lanch OZWCP - `sudo ./ozwcp -p 8888`
4. open the control panel in your browser http://IP_OF_YOUR_PI:8888
5. Specify your Z-Wave controller, for example `/dev/ttyACM0` and hit initialize (don't click on the USB button!)
6. hit `CTRL + C` in the command line to shut down the OZWCP
7. start home assistant - `sudo systemctl start home-assistant@homeassistant.service`

* [Hassbian installation on a raspberry pi 3](https://github.com/masterwendu/ki-adi-mundi/blob/master/hassbian/installation.md)
* [HOME](https://github.com/masterwendu/ki-adi-mundi)
