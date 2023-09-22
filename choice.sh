#!/bin/bash
echo -e " \n\n Choose the Client type that you want to be! \n"
echo -e " \n \t\t\t 1. Subscriber \n \t\t\t 2. Publisher \n\n"
echo -n " Your choice : "
read choice
if [ $choice == 1 ] 
then
    clear
    echo " Successfully subscribed! "
    eval 'python sub.py'
elif [ $choice == 2 ]
then
    clear
    echo -e " Successfully became a Publisher \n"
    python pub.py

else
    clear
    echo -e " Oops! Invalid Choice , please try again: "
    bash choice.sh
fi
exit
