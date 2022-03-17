#!/bin/bash

#Update ubuntu instance
sudo apt-get update


#install ngnix
sudo apt-get install nginx -y


#install nodejs ubuntu
sudo apt-get install curl
curl -sL https://deb.nodesource.com/setup_14.x | sudo -E bash -
sudo apt-get install -y nodejs

