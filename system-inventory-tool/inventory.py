import time
import platform
import socket
import psutil
import csv

boot_time = psutil.boot_time()
uptime_seconds = time.time() - boot_time
uptime_hours = round(uptime_seconds / 3600, 2)

from datetime import datetime

import getpass

user = getpass.getuser()

timestamp = datetime.now().strftime("%Y-%m-%d %H-%M-%S")
filename = "inventory.csv"

hostname = socket.gethostname()

os_name = platform.system()
os_version = platform.version()

cpu_count = psutil.cpu_count()

ram = round(psutil.virtual_memory().total / (1024**3), 2)

disk = psutil.disk_usage('/')
total_disk = round(disk.total / (1024**3), 2)
free_disk = round(disk.free / (1024**3), 2)

ip = socket.gethostbyname(socket.gethostname())
if ip.startswith("127."):
    ip = "Check Network Settings"

report_type = "Endpoint Inventory Report"

data = [
    ["System Uptime (Hours)", uptime_hours],
    ["Logged-in User", user],
    ["Hostname", hostname],
    ["Operating System", os_name],
    ["OS Version", os_version],
    ["CPU Cores", cpu_count],
    ["RAM (GB)", ram],
    ["Total Disk (GB)", total_disk],
    ["Free Disk (GB)", free_disk],
    ["Timestamp", timestamp],
    ["IP Address", ip],
    ["Report Type", report_type]
]

with open(filename, "w", newline = "") as file:
    writer = csv.writer(file)
    writer.writerow(["Property", "Value"])
    writer.writerows(data)

print("System inventory report successfully generated for IT asset tracking.")

