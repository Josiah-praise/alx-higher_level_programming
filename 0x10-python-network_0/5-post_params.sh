#!/bin/bash
# send a post request with some key value pair to urlmpassed as argument
curl -sX POST "$1" -d "email=test@gmail.com" -d "subject=I will always be here for PLD"
