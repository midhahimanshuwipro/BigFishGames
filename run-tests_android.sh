#!/bin/bash

echo "Installing dependencies"
chmod 0755 requirements.txt
python3 -m pip install -r requirements.txt

echo "Starting Appium ..."
appium --log-no-colors --log-timestamp  --command-timeout 60  > appium.log 2>&1 &
sleep 10
ps -ef|grep appium

export APPIUM_APPFILE=$PWD/application.apk #App file is at current working folder
#export  APPIUM_APPFILE=/Users/wipro/Downloads/alttrashcat-tests-python-appium-master/application.apk


## Desired capabilities:
#export APPIUM_URL="http://localhost:4723/wd/hub"
export APPIUM_DEVICE="Local Device"

##Headspin Test
export APPIUM_URL="https://dev-us-mia-0.headspin.io:7018/v0/86b1f5e8842f49bbbf920da797f2ad15/wd/hub"




export APPIUM_DEVICE="SM-A215U"
export  UDID_DETAIL="R9AN70CT3BJ"

###

export AUTO_ACCEPT_ALERTS="true"




export APPIUM_PLATFORM="android"
export APPIUM_AUTOMATION="uiautomator2"


## Run the test:
echo "Running tests"

rm -rf screenshots
python3 -m pytest tests/ -s

echo "Tests done"
