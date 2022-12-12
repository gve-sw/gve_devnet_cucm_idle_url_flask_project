# gve_devnet_cucm_idle_url_flask_project
flask project example to setup an idle url web service for Cisco CUCM, flask server has two urls to display text only information (/text) or to display an image as a background with some text (/idle). The example image being used it /screensavers/logo.png

## Contacts
* Jorge Banegas

## Solution Components
* CUCM
* 8845

## Installation/Configuration

First, you will need to fill out the information inside the config.py file to include (title and motd is for /text only). City is to where to query the weather from and the rss feed link is to query current events.

```python
title= "Sample Title Text"
motd= "Hello World!"
city = "miami"
rss_feed_link = "https://feeds.simplecast.com/54nAGcIl"
```

Second, edit the image.xml URL tag to include the IP address of the flask server, default is 127.0.0.1

Third include the image you want to use and replace the logo.png file inside the screensavers folder. Refer to the resource link below to verify the resolution on your specific 8800 IP Phone.

Set up a Python virtual environment. Make sure Python 3 is installed in your environment, and if not, you may download Python [here](https://www.python.org/downloads/). Once Python 3 is installed in your environment, you can activate the virtual environment with the instructions found [here](https://docs.python.org/3/tutorial/venv.html).

Install the requirements with `pip3 install -r requirements.txt`

## Usage

To launch flask server, run the command:

    $ python main.py

Now that the flask server is spun up, its time to go through the CUCM setup for configure the idle url. 

# CUCM configuration following this guide (https://www.voipinfo.net/docs/cisco/42573-idle-url.pdf)

Method 1: All Phones

Choose System > Enterprise Parameters so that the change is propagated to all of the phones from the Cisco CallManager Administration page.

In the URL Idle field, enter http://IP_address_of_CallManager/idle or http://IP_address_of_CallManager/text
In the URL Idle Time field, enter any positive value in seconds.

The image appears on the window of the IP phone after the specified seconds, either after
boot up or after it is idle for that long.

Method 2: To the Phone directly

Choose Device > Phone under the Cisco IP Phone configuration so that only this phone displays the graphics from the Cisco CallManager Administrator page

Choose the phone on which you want to put the display.

In the URL Idle field, enter http://IP_address_of_CallManager/idle or http://IP_address_of_CallManager/text

In the Idle Timer field, enter any positive value in seconds.

The image appears on the window of the IP phone after the specified seconds, either after boot up or after it is idle for that long.

# Resource links

https://www.voipinfo.net/docs/cisco/42573-idle-url.pdf

https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cuipph/8800-series/english/adminguide/P881_BK_C136782F_00_cisco-ip-phone-8800_series/P881_BK_C136782F_00_cisco-ip-phone-8811-8841_chapter_01010.html

# Screenshots

Idle URL Example
![/IMAGES/image_example.png](/IMAGES/image_example.png)

![/IMAGES/0image.png](/IMAGES/0image.png)

### LICENSE

Provided under Cisco Sample Code License, for details see [LICENSE](LICENSE.md)

### CODE_OF_CONDUCT

Our code of conduct is available [here](CODE_OF_CONDUCT.md)

### CONTRIBUTING

See our contributing guidelines [here](CONTRIBUTING.md)

#### DISCLAIMER:
<b>Please note:</b> This script is meant for demo purposes only. All tools/ scripts in this repo are released for use "AS IS" without any warranties of any kind, including, but not limited to their installation, use, or performance. Any use of these scripts and tools is at your own risk. There is no guarantee that they have been through thorough testing in a comparable environment and we are not responsible for any damage or data loss incurred with their use.
You are responsible for reviewing and testing any scripts you run thoroughly before use in any non-testing environment.