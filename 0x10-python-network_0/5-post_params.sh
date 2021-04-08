#!/bin/bash

#  takes in a URL, sends a POST request to the passed URL, and displays the body of the response
curl -X "POST" "$1" -sd ""subject=I will always be here for PLD&email=hr@holbertonschool.com"
