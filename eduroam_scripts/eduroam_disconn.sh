#!/bin/bash

echo "Editing /etc/wpa_supplicant/wpa_supplicant.conf ..."

{
sudo ed /etc/wpa_supplicant/wpa_supplicant.conf <<EOF
/identity="*
d
i
identity="user@gwu.edu"
.
/password="*
d
i
password="YouPasswordHere"
.
w
q
EOF
} &> /dev/null
