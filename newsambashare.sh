#!/bin/sh
appendShareText=/etc/samba/smb.conf
shareDirectory="/srv/share/"
shareNameInquiry="What is the name of your new share?"
shareLocation="Enter the name of the directory for the share"
shareCommentInquiry="Describe your new share"
shareGuestInquiry="Allow guest access into this share?"
shareUserNames="Enter the names of the user who will have 
		access to this share (seperate each name with a space)"
sharevalidate="Is this correct?"

housekeeping()
{
        if [ "`whoami`" != "root" ] ; then
                echo "You must be root to perform this task, exiting..."
                exit
        fi
}

get_user_input()
{
	echo $shareNameInquiry
	read shareName
	echo $shareCommentInquiry
	read comment
	echo $shareLocation
	read locationName
	echo $shareGuestInquiry
	read guestOK
	echo $shareUserNames
	read userNames
	echo $sharevalidate
}

validation()
{	
	finishedProduct=
	"[$shareName]
	 comment = $comment
	 path = /srv/samba/$locationName
	 browsable = yes
	 guest ok = $guestOK
	 read only = no
	 valid users = $userNames"
	echo "$finishedProduct"
	read correct
	if [ "$correct" = "yes" ] ; then
	echo "$finishedProduct" >> $appendShareText
	cat $appendShareText
	elif [ "$correct" = "no" ] ; then 
	echo "please try again"	
fi
}

	housekeeping
        get_user_input
	validation	
