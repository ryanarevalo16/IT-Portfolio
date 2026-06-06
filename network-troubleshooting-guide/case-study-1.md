# Case Study 1: Network Connectivity Investigation

## Problem
User reports inconsistent network behavior and inability to resolve domains.

---

## Investigation Steps

### 1. DNS Check
Command:
nslookup google.com

Result:
No expected output observed.

---

### 2. Route Check
Command:
traceroute google.com

Result:
Successful routing through ISP and Google backbone servers.

---

### 3. Network Interface Check
Command:
ifconfig

Result:
Active interface found (en0) with valid IP address assigned.

---

### 4. Network Connections
Command:
netstat

Result:
System shows active network connections and normal activity.

---

## Conclusion
Network connectivity is functional, but DNS resolution may require further troubleshooting depending on environment or configuration.
