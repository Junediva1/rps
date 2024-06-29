#! /bin/bash

# Ask would you like to play rock paper scissors
read -p "Would you like to play rock paper scissors? (y/n): " answer

# Check what the user has responded
if [ "$answer" = "yes"]; then
   # if the player want to play, go ahead and execute the Python file
   python 3 rps_game.py
else
    # If the user does not want to play, display message
    echo "That sucks, maybe next time."
fi