#/bin/bash

arrayf[0]="#37bd44"
arrayf[1]="#1c5c22"
arrayf[2]="#8df0d5"
arrayb[0]="#d0f52c"
arrayb[1]="#ff1768"
arrayb[2]="#db38ff"
arrayc[0]="32m"
arrayc[1]="31m"
arrayc[2]="36m"

while true;
do
	size=${#arrayf[@]}
	index=$(($RANDOM % $size))
	color=${arrayf[$index]}
	echo -ne "\e]11;$color\e\\"
	size=${#arrayb[@]}
	index=$(($RANDOM % $size))
	color=${arrayb[$index]}
	echo -ne "\e]10;$color\e\\"
	size=${#arrayc[@]}
	index=$(($RANDOM % $size))
	color=${arrayc[$index]}
	export PS1="\e[0;36m[\u@\h \W]\$ \e[m "
	sleep 1
done
