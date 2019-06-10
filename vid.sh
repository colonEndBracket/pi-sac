#!/bin/bash
source config.sh

ssh pi@$addr "rm $vidName.avi; avconv -f video4linux2 -r 14 -s 640x480 -i /dev/video0 $vidName.avi; exit"
sftp pi@$addr <<EOT
get $vidName.avi
exit
EOT
