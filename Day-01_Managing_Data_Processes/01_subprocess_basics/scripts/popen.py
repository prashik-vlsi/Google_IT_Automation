import subprocess
import time

print("Starting process...")

process = subprocess.Popen(["sleep", "5"])

print("Process started!")
print("Python is free to continue working...")

for i in range(5):
    print(f"Python is working: {i + 1}")
    time.sleep(1)

process.wait()

print("Process finished!")