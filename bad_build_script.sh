#!/bin/bash –x

VAULTTOKEN=(curl -s http://127.0.0.1:8200/v1/auth/github/login -d '{ "token": ”YOURVAULTTOKEN" }' |  python -c 'import sys, json; print json.load(sys.stdin)["auth"]["client_token"]')

GITTOKEN=(curl -s -H "X-Vault-Token: $VAULTTOKEN” -X GET http://127.0.0.1:8200/v1/secret/seccon|  python -c 'import sys, json; print json.load(sys.stdin)["data"]["gittoken"]')

if [ -d "hello-world" ]; 
then 
cd hello-world
git pull
else 
git clone https://$GITTOKEN:x-oauth-basic@github.com/rtphokie/hello-world.git
Fi
rm -Rf hello-world
