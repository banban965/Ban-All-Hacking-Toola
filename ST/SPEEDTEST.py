#!/usr/bin/env python3

import os
import time
import speedtest

os.system("clear")

print("=" * 45)
print("         INTERNET SPEED TEST")
print("=" * 45)

try:
    print("\n[*] Finding best server...")
    st = speedtest.Speedtest()

    st.get_best_server()
    server = st.results.server

    print("\n========== SERVER ==========")
    print(f"Name     : {server['name']}")
    print(f"Sponsor  : {server['sponsor']}")
    print(f"Country  : {server['country']}")
    print(f"Distance : {server['d']:.2f} km")
    print(f"Host     : {server['host']}")
    print("============================\n")

    print("[*] Testing download speed...")
    download = st.download()

    print("[*] Testing upload speed...")
    upload = st.upload()

    ping = st.results.ping

    print("\n" + "=" * 45)
    print(f"Ping      : {ping:.2f} ms")
    print(f"Download  : {download / 1_000_000:.2f} Mbps")
    print(f"Upload    : {upload / 1_000_000:.2f} Mbps")
    print("=" * 45)

except Exception as e:
    print("\n[ERROR]", e)