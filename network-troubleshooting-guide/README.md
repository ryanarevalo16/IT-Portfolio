# Network Troubleshooting Guide (macOS)

## Overview
This project documents basic network troubleshooting steps using macOS terminal commands.

The goal is to simulate real IT support diagnostics used in help desk environments.

---

## Tools Used
- ping
- nslookup
- traceroute
- ifconfig
- netstat

---

## Summary of Findings

- DNS lookup (`nslookup`) did not return expected results in this test
- Network routing (`traceroute`) successfully reached external servers
- Local network interface (`ifconfig`) confirmed active Wi-Fi connection (en0)
- Network statistics (`netstat`) showed active system connections

---

## Conclusion
The system is connected to the internet and can reach external networks. However, DNS resolution may require further investigation depending on environment conditions.