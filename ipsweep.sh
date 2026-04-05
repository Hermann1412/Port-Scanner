#!/bin/bash

if [ "$1" == "" ]
then
echo "You forgot an IP address!"
echo "Syntax: ./ipsweep.sh *.*.0" #Can replace with another Ip Address on the *.*.0 exemple = "168.18.0"

else

for ip in `seq 254`; do
ping -c 1 $1.$ip | grep "64 bytes" | cut -d " " -f 4 | tr -d ":" &
done
fi
