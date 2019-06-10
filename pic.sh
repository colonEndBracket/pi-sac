#!/bin/bash
. config.sh

ssh pi@$addr "fswebcam -r 640x480 $imgName.jpg||exit"
sftp pi@$addr <<EOT
get $imgName.jpg
exit
EOT
