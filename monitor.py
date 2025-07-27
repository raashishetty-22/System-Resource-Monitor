import psutil
import time

while True:
    cpu = psutil.cpu_percent()
    memory = psutil.virtual_memory().percent
    disk = psutil.disk_usage('/').percent
    print(f"CPU: {cpu}% | Memory: {memory}% | Disk: {disk}%")
    time.sleep(2)
