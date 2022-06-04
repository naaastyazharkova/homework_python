#!/bin/bash
function up_down_ip {
for ip in 10.82.225.{1..10}
do 
    ping -t 5 -w 2 $ip > /dev/null 2> /dev/null
    if [ $? -eq 0 ]
    then  
        echo "${ip} is up" 
    else
        echo "${ip} is down"
    fi
done }

function ip {
out=$(curl curlmyip.ru 2>&1 | egrep "([0-9]{1,3}\.){3}")
echo "IP: $out" 
}

function pass {
symbols=""
for symbol in {A..Z} {a..z} {0..9} 
do 
    symbols=$symbols$symbol 
done
symbols=$symbols'!@#$%&*()?/\[]{}-+_=<>.,'  
lenght_pass=9  
pwd="" 
RANDOM=256  
for i in `seq 1 $lenght_pass`
do
    pwd=$pwd${symbols:$(expr $RANDOM % ${#symbols}):1}
done
echo "Your password: $pwd"
}

while [ -n "$1" ]
do
case "$1" in
-u) up_down_ip ;;
-i) ip ;;
-p) pass ;;
esac
shift
done