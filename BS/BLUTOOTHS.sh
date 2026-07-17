#!/data/data/com.termux/files/usr/bin/bash

echo "[*] Bluetooth Scanner"

if ! command -v bluetoothctl >/dev/null 2>&1; then
    echo "[ERROR] Bluetooth tools are not available."
    echo "[INFO] Android/Termux does not provide Bluetooth scanning from Bash."
    exit 1
fi

echo "[*] Starting scan..."
bluetoothctl scan on