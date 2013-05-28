#!/bin/sh

packages="apache2 mysql-server libapache2-mod-php5 samba"
esc=""
blackf="${esc}[30m"
redf="${esc}[31m"
greenf="${esc}[32m"
yellowf="${esc}[33m"
whitef="${esc}[37m"
boldon="${esc}[1m"
boldoff="${esc}[22m"
reset="${esc}[0m"

report() {
	echo -n "${boldon}$@${reset}"
	sleep .5
	echo -n .
	sleep .5
	echo -n .
	sleep .5 
	echo -n .
}
housekeeping() 
{
	report ${boldon}${greenf} "Updating apt-get and distribution"
	sudo apt-get update > /dev/null
	sudo apt-get -y upgrade > /dev/null
	echo done
}
install_package()
{	
	report "Installing $pkg"
	isPackageInstalled=`dpkg --get-selections|grep $pkg`
	if [ "$isPackageInstalled" = "" ] ; then
		echo "INSTALLING $pkg"
		apt-get -y install $pkg > /dev/null 
	fi
	echo done.
}
finish() 
{
	echo ${boldon}${greenf}"DONE!"${reset}
}

# main loop
housekeeping
for pkg in $packages; do 
	install_package
done
finish
