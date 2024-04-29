#!/bin/bash
# send a post request with some key value pair to urlmpassed as argument
curl -sd "email=hr@holbertonschool.com&subject=I will always be here for PLD" -X POST "$1"
