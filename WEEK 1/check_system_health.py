import shutil
import psutil

def check_disk_usage(disk):
    du = shutil.disk_usage(disk)
    return du.free/du.total*100 > 20

def check_cpu_usage():
    cu = psutil.cpu_percent(1)
    return cu > 75

if not check_cpu_usage() or not check_disk_usage("/"):
    print("Fail!")
else:
    print("Pass!")