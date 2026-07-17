#!/data/data/com.termux/files/usr/bin/bash

echo "[*] Detecting Wi-Fi network..."

OUTPUT=$(ip route 2>&1)
STATUS=$?

if [ $STATUS -ne 0 ]; then
    echo "[ERROR] Permission denied."
    echo "[DETAILS] $OUTPUT"
    exit 1
fi

SUBNET=$(echo "$OUTPUT" | awk '/src/ {print $1; exit}')

if [ -z "$SUBNET" ]; then
    echo "[ERROR] Unable to detect Wi-Fi subnet."
    exit 1
fi

echo "[OK] Network detected: $SUBNET"E : %s\n\n",ip,mac,name
}'