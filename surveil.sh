#!/bin/bash
source config.sh

transferImage(){
	mv $imgName.jpg $dumpLocation && echo Image Transfered to Desktop
}
transferVideo(){
	mv $vidName.avi $dumpLocation || rm $dumpLocation/$vidName.avi && mv $vidName.avi $dumpLocation && echo Video Transfered to Desktop
}

read -p "(0)Snap or (1)Record?: " choice
case $choice in
	"0") sh pic.sh ; transferImage ;;
	"1") sh vid.sh ; transferVideo ;;
	*) exit;;
esac

exit 0
