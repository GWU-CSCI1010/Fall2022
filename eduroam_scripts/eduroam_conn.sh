#!/bin/bash

username=""
passwd=""
echo "Enter netid username: "
read username


echo "Enter password: "
read -s passwd
echo "Editing /etc/wpa_supplicant/wpa_supplicant.conf ..."
{
sudo ed /etc/wpa_supplicant/wpa_supplicant.conf <<EOF
/identity=*
d
i
identity="${username}@gwu.edu"
.
/password=*
d
i
password="${passwd}"
.
w
q
EOF

} &> /dev/null

sudo wpa_cli -i wlan0 reconfigure

sudo ed /etc/network/interfaces <<EOF
w
q
EOF

echo "Restarting network..."
sudo /etc/init.d/networking stop && sudo /etc/init.d/networking start

