#!/bin/bash -x


if [ -d "hello-world" ]; 
then cd hello-world; git pull
else git clone https://$MYSECRET:x-oauth-basic@github.com/rtphokie/hello-world.git
fi

