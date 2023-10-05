#!/bin/bash

area="$PWD"
pipchk=$(which pip)

if [ "$UID" = "0" ]; then

    if [ -f "$area/requirements.txt" ]; then

        if [ "$pipchk" = "/usr/bin/pip" ]; then

            echo ""
            echo "python3-pip Binary Found!"
            echo ""

        elif [ "$pipchk" = "pip not found" ]; then

            echo ""
            echo " [!] Missing 'python3-pip' binary!"
            echo ""

            apt install python3 python3-pip -y

            echo ""

        else
            
            echo ""
            echo " [!] Unknown Error Occured!, Check Script For More Information!"
            echo ""
    
            exit 4
    
        fi

        pip install -r $area/requirements.txt

        apt install nmap -y
        apt install nikto -y

        echo ""
        echo "Installed Requirements From 'requirements.txt'"
        echo ""

        exit 1

    else

        echo ""
        echo "Error: Please Ensure 'requirements.txt' Is Accessable In $area"
        echo ""

        exit 2

    fi

else

    echo ""
    echo "Please Run This Script As UID = 0"
    echo ""

    exit 3

fi

exit 999