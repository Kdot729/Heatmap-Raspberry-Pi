#!/bin/bash
Timezone="America/Detroit"
Day_Format="%Y-%m-%d"
Time_Format="%H:%M"
Date=$(TZ=$Timezone date +"$Day_Format")
Time=$(TZ=$Timezone date +"$Time_Format")
Backup_Directory="/backup/$Date/$Time"

mkdir -p $Backup_Directory
/usr/bin/mongodump -u root -p example --authenticationDatabase admin -d coinbase -o $Backup_Directory
echo "Backup $Date-$Time" >> /var/log/cron.log